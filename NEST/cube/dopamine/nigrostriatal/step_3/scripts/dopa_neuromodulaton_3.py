# -*- coding: utf-8 -*-

# ToDo add generator to every part
import numpy as np
from time import clock

import nest
from parameters_3 import *

logger = logging.getLogger("dopa")
'''
This is the implementation of experiment of dopamine neuromodulation based on
https://github.com/research-team/NEUCOGAR/blob/master/experiment_description.md#general-neuromodulation
and
test_stdp_dopa
see explanation of neuronal model:

Prefix description:
	ex_  -  excitory
	inh_ - inhibitory
	d_   - Direct
	ind_ - indirect

Neurotools is used for representing and analyzing nonscientific data.
'''

# orientation='portrait', papertype=None, format=None):

nest.ResetKernel()
startbuild = clock()

sd_folder_name += "-text/" if withoutGUI else  "-image/"
if not os.path.exists(sd_folder_name):
    os.mkdir(sd_folder_name)

nest.SetKernelStatus({'overwrite_files': True, 'data_path': sd_folder_name, "local_num_threads": 4, "resolution": 0.1})

# ============
# Creating BS
# ============
parts_dict_log = {}


def f_register(item, name):
    parts_dict_log[item[0]] = name


parts_BG = generate_neurons_BG(nest)
motor_cortex = (get_ids('motivation', parts_BG), get_ids('action'))
f_register(motor_cortex[motivation], 'Motor Cortex[motivation]')
f_register(motor_cortex[action], 'Motor Cortex[action]')
striatum = (get_ids('D1'), get_ids('D2'), get_ids('tan'))
f_register(striatum[tan], 'Striatum[tan]')
f_register(striatum[D1], 'Striatum[D1]')
f_register(striatum[D2], 'Striatum[D2]')
gpe = get_ids('gpe')
f_register(gpe, 'GPe')
gpi = get_ids('gpi')
f_register(gpi, 'GPi')
stn = get_ids('stn')
f_register(stn, 'STN')
snr = get_ids('snr')
f_register(snr, 'SNr')
thalamus = get_ids('thalamus')
f_register(thalamus, 'Thalamus')
snc = get_ids('snc')
f_register(snc, 'SNc')

del (parts_BG, get_ids, generate_neurons_BG)
log_conn = lambda a, b, is_syn_ex=None: logger.debug('%s -> %s (%s)' % (parts_dict_log[a[0]], parts_dict_log[b[0]],
                                                                        'generator' if is_syn_ex is None else 'excitatory' if is_syn_ex else 'inhibitory'))

'''
help method for connection syntax facilitation
'''
def connect(ner_from, ner_to, is_syn_ex=False):
    nest.Connect(ner_from, ner_to, conn_spec=conn_dict,
                 syn_spec=STDP_synapseparams_ex if is_syn_ex else STDP_synapseparams_in)
    log_conn(ner_from, ner_to, is_syn_ex)


logger.debug('Start connection initialisation')
connect(motor_cortex[motivation], striatum[D1], is_syn_ex=True)
connect(motor_cortex[action], striatum[D1], is_syn_ex=True)

connect(motor_cortex[motivation], striatum[D2], is_syn_ex=True)
connect(motor_cortex[action], striatum[D2], is_syn_ex=True)

connect(motor_cortex[motivation], thalamus, is_syn_ex=True)
connect(motor_cortex[action], thalamus, is_syn_ex=True)

connect(motor_cortex[motivation], stn, is_syn_ex=True)
connect(motor_cortex[action], stn, is_syn_ex=True)

connect(striatum[tan], striatum[D1])
connect(striatum[tan], striatum[D2], is_syn_ex=True)
# ! Direct pathway: → Striatum (inhibits) [D1] → "SNr-GPi" complex (less inhibition of thalamus) →
connect(striatum[D1], snr)
connect(striatum[D1], gpi)
connect(striatum[D1], gpe)
connect(striatum[tan], snc)
# ! Indirect pathwat: Striatum (inhibits) [D2] → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) →
connect(striatum[D2], gpe)
connect(gpe, stn)
connect(gpe, striatum[D1])
connect(gpe, striatum[D2])
connect(gpe, gpi)
connect(stn, snr, is_syn_ex=True)
connect(stn, gpi, is_syn_ex=True)
connect(stn, gpe, is_syn_ex=True)
# ! Common path: SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.
connect(gpi, thalamus)
connect(snr, thalamus)
connect(thalamus, motor_cortex[action], is_syn_ex=True)
connect(thalamus, striatum[D1], is_syn_ex=True)
connect(thalamus, striatum[D2], is_syn_ex=True)
connect(thalamus, stn, is_syn_ex=True)

logger.debug('Making neuromodulating connections...')

# ==================
# Dopamine modulator
# ==================
if vt_flag:
    connect(motor_cortex[motivation], snc, is_syn_ex=True)  # ToDo neuromodulation
    connect(stn, snc, is_syn_ex=True)


    # Volume transmission: init dopa_model
    vt_ex = nest.Create("volume_transmitter")
    vt_in = nest.Create("volume_transmitter")
    DOPA_synparams_ex['vt'] = vt_ex[0]
    DOPA_synparams_in['vt'] = vt_in[0]
    nest.Connect(snc, vt_ex)
    nest.Connect(snc, vt_in)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)

    nest.Connect(snc, striatum[D1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc, striatum[D1], dopa_model_ex)
    nest.Connect(snc, striatum[D2], conn_dict, syn_spec=dopa_model_in)
    log_conn(snc, striatum[D2], dopa_model_in)
    nest.Connect(snc, striatum[tan], conn_dict, syn_spec=dopa_model_in)
    log_conn(snc, striatum[tan], dopa_model_in)

    nest.Connect(snc, gpe, conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc, gpe, dopa_model_in)
    nest.Connect(snc, stn, conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc, stn, dopa_model_in)
del connect

logger.debug('Starting spike generators')

# ===============
# Spike Generator
# ===============
if pg_flag:
    pg_slow = nest.Create("poisson_generator", 1, {"rate": K_slow})
    parts_dict_log[pg_slow[0]] = 'Poisson Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex, 'delay': pg_delay})
    nest.Connect(pg_slow, motor_cortex[action], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[action]) / 4})
    log_conn(pg_slow, motor_cortex[action])
    if vt_flag:
        pg_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 400., 'stop': 600.})
        parts_dict_log[pg_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(pg_fast, motor_cortex[motivation], syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[motivation]) / 4})
        log_conn(pg_fast, motor_cortex[motivation])
else:
    sg_slow = nest.Create('spike_generator', params={'spike_times': np.arange(1, T, 20.)})
    parts_dict_log[sg_slow[0]] = 'Periodic Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex})

    nest.Connect(sg_slow, motor_cortex[action], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[action]) / 4})
    log_conn(sg_slow, motor_cortex[action])
    if vt_flag:
        sg_fast = nest.Create('spike_generator', params={'spike_times': np.arange(400, 600, 15.)})
        parts_dict_log[sg_fast[0]] = 'Periodic Generator(fast)'
        nest.Connect(sg_fast, motor_cortex[motivation], syn_spec=gen_static_syn, )
        # conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[motivation]) / 4})
        log_conn(sg_fast, motor_cortex[motivation])

logger.debug('Attaching spikes detector')

# =============
# SPIKEDETECTOR
# =============
spikedetector = nest.Create("spike_detector", 2, params=detector_param)
nest.Connect(thalamus[:N_rec], (spikedetector[0],))
logger.debug("spike detecor is attached to thalamus: tracing %d neurons" % N_rec)
nest.Connect(motor_cortex[action][:N_rec], (spikedetector[1],))
logger.debug("spike detecor is attached to motor cortex: tracing %d neurons" % N_rec)
# ============
# MULTIMETER
# ============
mm_param["label"] = 'thalamus'
mm1 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm1, (thalamus[0],))
logger.debug("%s - %d", mm_param["label"], thalamus[0])
mm_param["label"] = 'snc'
mm2 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm2, (snc[0],))
logger.debug("%s - %d", mm_param["label"], snc[0])

# ==========
# SIMULATING
# ==========
nest.PrintNetwork()
endbuild = clock()
logger.debug("Simulating")
if not vt_flag:
    # TYPE_1
    nest.Simulate(T)
else:
    if not save_weight_flag:
        nest.Simulate(T)
    else:
        # TYPE_2
        weight = None
        weight_list = [(0, 1)]
        filename = 'weight_dopa.gdf'
        fname = open(filename, 'w')

        for t in np.arange(0, T + dt, dt):
            if nest.GetStatus(snc)[0]['local']:
                weight = nest.GetStatus(nest.GetConnections(snc, synapse_model=dopa_model_ex))[0]['weight']
                print(weight)
                weight_list.append((t, weight))
                weightstr = str(weight)
                timestr = str(t)
                data = timestr + ' ' + weightstr + '\n'
                fname.write(data)

                nest.Simulate(dt)
        fname.close()
# ===============
# LOG information
# ===============
endsimulate = clock()
build_time = endbuild - startbuild
sim_time = endsimulate - endbuild
events_th = nest.GetStatus(spikedetector, "n_events")[0]
rate_th = events_th / sim_time * 1000.0 / N_rec

# logger.info("Number of neurons : {0}".format(len(thalamus)))
# logger.info("Number of synapses: {0}".format(num_synapses))
logger.info("Building time     : %.2f s" % build_time)
logger.info("Simulation time   : %.2f s" % sim_time)
logger.info("Thalamus rate     : %.2f Hz" % rate_th)
logger.info('Dopamine: ' + ('YES' if vt_flag else 'NO'))
logger.info('Noise: ' + ('YES' if pg_flag else 'NO'))

# =====
# Draw
# =====
if withoutGUI:
    from write_from_sensors import *
    save_voltage(mm1, name="thalamus")
    save_voltage(mm2, name="snc")
    save_spikes((spikedetector[0],), name="thalamus")       #, hist=True)
    save_spikes((spikedetector[1],), name="motor_cortex")   #, hist=True)
else:
    import nest.raster_plot
    import nest.voltage_trace
    import pylab as pl
    pl.axis(axis)
    nest.voltage_trace.from_device(mm1)
    pl.savefig(f_name_gen('thalamus', True), dpi=dpi_n, format='png')
    pl.close()

    pl.axis(axis)
    nest.voltage_trace.from_device(mm2)
    pl.savefig(f_name_gen('snc', True), dpi=dpi_n, format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[0],), hist=True)
    pl.savefig(f_name_gen('spikes_thalamus', is_image=True), format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[1],), hist=True)
    pl.savefig(f_name_gen('spikes_motorcortex', is_image=True), format='png')
    pl.close()