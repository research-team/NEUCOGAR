# -*- coding: utf-8 -*-

# ToDo add generator to every part

# math and randomise package
import numpy as np
# neuron packages
# visualise spikes
# from NeuroTools import signals, io
# import matplotlib
# Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')
import nest.raster_plot
import nest.voltage_trace
# local project parameters
from parameters_2 import *
import os
from time import clock

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

if not os.path.exists(sd_folder_name):
    os.mkdir(sd_folder_name)
nest.SetKernelStatus({'overwrite_files': True, 'data_path': sd_folder_name, "local_num_threads": 1, "resolution": 0.1})

# ============
# Creating BS
# ============
parts_dict_log = {}


def f_register(item, name):
    parts_dict_log[item[0]] = name


parts_BG = generate_neurons_BG(nest)
cortex = get_ids('motor_cortex', parts_BG)
f_register(cortex, 'Motor Cortex')
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
log_conn = lambda a, b=None, is_syn_ex=None: logger.debug(
    '%s -> %s (%s)' % (
    parts_dict_log[a[0]] if b is not None else '', parts_dict_log[b[0]] if b is not None else parts_dict_log[a[0]],
    'generator' if is_syn_ex is None else 'excitatory' if is_syn_ex else 'inhibitory'))


def connect(ner_from, ner_to, is_syn_ex=False, conn_dict_loc=None):
    nest.Connect(ner_from, ner_to, conn_spec=conn_dict if conn_dict_loc is None else conn_dict_loc,
                 syn_spec=STDP_synapseparams_ex if is_syn_ex else STDP_synapseparams_in)
    log_conn(ner_from, ner_to, is_syn_ex)


logger.debug('Start connection initialisation')
connect(cortex, striatum[D1], is_syn_ex=True, )  # conn_dict_loc={'rule': 'fixed_outdegree', 'outdegree': 40})
connect(cortex, striatum[D2], is_syn_ex=True, )  # conn_dict_loc={'rule': 'fixed_outdegree', 'outdegree': 80})
connect(cortex, striatum[tan], is_syn_ex=True)
connect(striatum[tan], striatum[D1])
connect(striatum[tan], striatum[D2], is_syn_ex=True)
# ! Direct pathway: → Striatum (inhibits) [D1] → "SNr-GPi" complex (less inhibition of thalamus) →
connect(striatum[D1], snr)
connect(striatum[D1], gpi)
# ! Indirect pathwat: Striatum (inhibits) [D2] → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) →
connect(striatum[D2], gpe)
connect(gpe, stn)
connect(stn, snr, is_syn_ex=True)
connect(stn, gpi, is_syn_ex=True)
# ! Common path: SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.
connect(gpi, thalamus)
connect(snr, thalamus)
connect(thalamus, cortex, is_syn_ex=True, )  # conn_dict_loc={'rule': 'fixed_outdegree', 'outdegree': 30})
del (connect)
# ==================
# Dopamine modulator
# ==================
if vt_flag:
    # Volume transmission: init dopa_model
    vt_ex = nest.Create("volume_transmitter")
    vt_in = nest.Create("volume_transmitter")
    DOPA_synparams_ex['vt'] = vt_ex[0]
    DOPA_synparams_in['vt'] = vt_in[0]
    nest.Connect(snc, vt_ex)
    nest.Connect(snc, vt_in)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)

    nest.Connect(snc, striatum[tan], conn_dict, syn_spec=dopa_model_in)
    log_conn(snc, striatum[tan], dopa_model_in)
    nest.Connect(snc, striatum[D1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc, striatum[D1], dopa_model_ex)
    nest.Connect(snc, striatum[D2], conn_dict, syn_spec=dopa_model_in)
    log_conn(snc, striatum[D2], dopa_model_in)

# ===============
# Spike Generator
# ===============
if pg_flag:
    f_pg_start = lambda start_time=1., isFast=False, krate=None: nest.Create("poisson_generator", 1,
                                                                             {
                                                                                 "rate": krate if krate is not None else K_fast if isFast else K_slow,
                                                                                 'start': start_time})
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex, 'delay': pg_delay})
    nest.Connect(f_pg_start(isFast=True), striatum[tan], syn_spec=gen_static_syn)
    log_conn(striatum[tan], is_syn_ex=None)
    nest.Connect(f_pg_start(6.), cortex, syn_spec=gen_static_syn, )
    log_conn(cortex, is_syn_ex=None)
    nest.Connect(f_pg_start(6.), gpe, syn_spec=gen_static_syn)
    log_conn(gpe, is_syn_ex=None)
    nest.Connect(f_pg_start(), stn, syn_spec=gen_static_syn)
    log_conn(stn, is_syn_ex=None)
    nest.Connect(f_pg_start(5., ), thalamus, syn_spec=gen_static_syn)
    log_conn(thalamus, is_syn_ex=None)
    if vt_flag:
        nest.Connect(nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 400., 'stop': 600.}), snc,
                     syn_spec=gen_static_syn)
        logger.debug('Generator is connected to %s' % parts_dict_log[snc[0]])
    del (f_pg_start)
else:
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex})
    spikes_times = np.arange(1, T, 15.)
    f_spike_times = lambda dt: np.array([t + dt for t in spikes_times])
    f_gen_connect = lambda part, dt=0, rang=None: nest.Connect(nest.Create('spike_generator', params={
        'spike_times': (f_spike_times(dt) if rang is None else rang)}), part, syn_spec=gen_static_syn)

    # f_gen_connect(cortex)
    nest.Connect(nest.Create('spike_generator', params={
        'spike_times': np.arange(1, T, 30.)}), cortex, syn_spec=gen_static_syn, )

    f_gen_connect(stn)
    f_gen_connect(striatum[tan], rang=np.arange(1, T, 15.))
    f_gen_connect(gpe, 6., rang=np.arange(1, T, 28.))
    f_gen_connect(thalamus, 3., rang=np.arange(1., T, 20.))
    if vt_flag:
        f_gen_connect(snc, rang=np.arange(400., 600., 6.))
    del (f_gen_connect, f_spike_times)
# =============
# SPIKEDETECTOR
# =============
spikedetector = nest.Create("spike_detector", 2, params=detector_param)
nest.Connect(thalamus[:N_rec], (spikedetector[0],))
logger.debug("spike detecor is attached to thalamus: tracing %d neurons" % N_rec)
nest.Connect(cortex[:N_rec], (spikedetector[1],))
logger.debug("spike detecor is attached to motor cortex: tracing %d neurons" % N_rec)

# ============
# MULTIMETER
# ============

mm_param["label"] = 'thalamus'
mm1 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm1, (thalamus[-1], ))
logger.debug("%s - %d", mm_param["label"], thalamus[-1])

mm_param["label"] = 'snc'
mm2 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm2, (snc[0],))
logger.debug("%s - %d", mm_param["label"], snc[0])

mm_param["label"] = 'motor cortex'
mm3 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm3, (cortex[0],))
logger.debug("%s - %d", mm_param["label"], cortex[0])

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
logger.info("Thalamus rate   : %.2f Hz" % rate_th)
logger.info('Dopamine: ' + ('YES' if vt_flag else 'NO'))
logger.info('Noise: ' + ('YES' if pg_flag else 'NO'))

# =====
# Draw
# =====
if save_weight_flag: plot_weights(weight_list, "Neurons weights progress neuron 1")

nest.voltage_trace.from_device(mm1)
pl.axis(axis)
pl.savefig(f_name_gen('thalamus', True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

pl.axis(axis)
nest.voltage_trace.from_device(mm2)
pl.axis(axis)
pl.savefig(f_name_gen('snc', True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

nest.raster_plot.from_device((spikedetector[0],), hist=True)
# x1, x2, _, _ = pl.axis()
# pl.xlim([10., x2])
pl.savefig(f_name_gen('spikes_thalamus', is_image=True), format='png')
# nest.raster_plot.show()
pl.close()

nest.raster_plot.from_device((spikedetector[1],), hist=True)
pl.savefig(f_name_gen('spikes_motorcortex', is_image=True), format='png')
# nest.raster_plot.show()
pl.close()

# another type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
