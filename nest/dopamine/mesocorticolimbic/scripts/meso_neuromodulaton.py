# -*- coding: utf-8 -*-
# ToDo add generator's to every part!!!
# TODO check num_threads (line 28) before testing / 8 for Cisco Server

# math and randomise package
import numpy as np
# visualise spikes
import nest.raster_plot
import nest.voltage_trace
# local project parameters
from parameters import *
from time import clock
import os

'''
This is the implementation of experiment of mesocorticolimbic pathway based on
https://https://github.com/research-team/NEUCOGAR/blob/master/mesolimbic_dopamine_pathway.png

!!!Neurotools is used for representing and analyzing nonscientific data!!!
'''

logger = logging.getLogger("dopamine")
nest.ResetKernel()
startbuild = clock()

if not os.path.exists(sd_folder_name):
    os.mkdir(sd_folder_name)
nest.SetKernelStatus({'overwrite_files': True, 'data_path': sd_folder_name, "local_num_threads": 4, "resolution": 0.1})

# ============
# Creating parts
# ============
parts_dict_log = {}


def f_register(item, name):
    parts_dict_log[item[0]] = name

parts_MP = generate_neurons_MP(nest)

prefrontal_cortex = (get_ids('Cortex', parts_MP), get_ids('Glu0'), get_ids('Glu1'))
f_register(prefrontal_cortex[cortex], 'Prefrontal Cortex[Cortex]')
f_register(prefrontal_cortex[cortex_Glu0], 'Prefrontal Cortex[Glu0]')
f_register(prefrontal_cortex[cortex_Glu1], 'Prefrontal Cortex[Glu1]')

nac = (get_ids('Ach'), get_ids('GABA0'), get_ids('GABA1'))
f_register(nac[nac_Ach], 'NAc[Ach]')
f_register(nac[nac_GABA0], 'NAc[GABA0]')
f_register(nac[nac_GABA1], 'NAc[GABA1]')

vta = (get_ids('GABA0'), get_ids('DA0'), get_ids('GABA1'), get_ids('DA1'), get_ids('GABA2'))
f_register(vta[vta_GABA0], 'VTA[GABA0]')
f_register(vta[vta_DA0], 'VTA[DA0]')
f_register(vta[vta_GABA1], 'VTA[GABA1]')
f_register(vta[vta_DA1], 'VTA[DA1]')
f_register(vta[vta_GABA2], 'VTA[GABA2]')

tpp = (get_ids('GABA'), get_ids('Ach'), get_ids('Glu'))
f_register(tpp[tpp_GABA], 'VTA[GABA]')
f_register(tpp[tpp_Ach], 'VTA[DA1]')
f_register(tpp[tpp_Glu], 'VTA[GABA2]')

del (parts_MP, get_ids, generate_neurons_MP)
log_conn = lambda a, b, is_syn_ex=None:\
    logger.debug('%s -> %s (%s)' % (parts_dict_log[a[0]], parts_dict_log[b[0]],
                 'generator' if is_syn_ex is None else 'excitatory' if is_syn_ex else 'inhibitory'))


"""Help method for connection syntax facilitation"""
def connect(ner_from, ner_to, is_syn_ex=False):
    nest.Connect(ner_from, ner_to, conn_spec=conn_dict,
                 syn_spec=STDP_synapseparams_ex if is_syn_ex else STDP_synapseparams_in)
    log_conn(ner_from, ner_to, is_syn_ex)

logger.debug('Start connection initialisation')

connect(prefrontal_cortex[cortex], prefrontal_cortex[cortex_Glu0], is_syn_ex=True)
connect(prefrontal_cortex[cortex], prefrontal_cortex[cortex_Glu1], is_syn_ex=True)
connect(prefrontal_cortex[cortex_Glu0], vta[vta_DA0], is_syn_ex=True)
connect(prefrontal_cortex[cortex_Glu1], nac[nac_GABA1], is_syn_ex=True)
connect(prefrontal_cortex[cortex_Glu1], vta[vta_GABA2], is_syn_ex=True)

connect(nac[nac_Ach], nac[nac_GABA1], is_syn_ex=True)
connect(nac[nac_GABA0], nac[nac_GABA1])
connect(nac[nac_GABA1], vta[vta_GABA2])

connect(vta[vta_GABA0], prefrontal_cortex[cortex])
connect(vta[vta_GABA0], tpp[tpp_GABA])
# vta[vta_DA0] -> prefrontl_cortex[cortex] (DOPAMIN)
connect(vta[vta_GABA1], vta[vta_DA0])
connect(vta[vta_GABA1], vta[vta_DA1])
# vta[vta_DA0] -> nac[nac_GABA1] (DOPAMIN)
connect(vta[vta_GABA2], nac[nac_GABA1])

connect(tpp[tpp_GABA], vta[vta_GABA0])
connect(tpp[tpp_Ach], vta[vta_GABA0], is_syn_ex=True)
connect(tpp[tpp_Ach], vta[vta_DA1], is_syn_ex=True)
connect(tpp[tpp_Glu], vta[vta_GABA0], is_syn_ex=True)
connect(tpp[tpp_Glu], vta[vta_DA1], is_syn_ex=True)

logger.debug('Making neuromodulating connections...')

# ==================
# Dopamine modulator
# ==================
if dopa_flag:
    # Volume transmission: init dopa_model
    vt_ex = nest.Create("volume_transmitter")
    DOPA_synparams_ex['vt'] = vt_ex[0]
    nest.Connect(vta[vta_DA0], vt_ex)
    nest.Connect(vta[vta_DA1], vt_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)

    nest.Connect(vta[vta_DA0], prefrontal_cortex[cortex], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA0], prefrontal_cortex[cortex], dopa_model_ex)
    nest.Connect(vta[vta_DA1], nac[nac_GABA1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA1], nac[nac_GABA1], dopa_model_ex)
del connect

logger.debug('Starting spike generators')

# ===============
# Spike Generator
# ===============
if poison_generator:
    pg_slow = nest.Create("poisson_generator", 1, {"rate": K_slow})
    parts_dict_log[pg_slow[0]] = 'Poisson Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex, 'delay': pg_delay})
    nest.Connect(pg_slow, prefrontal_cortex[cortex], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(prefrontal_cortex[cortex]) / 4})
    log_conn(pg_slow, prefrontal_cortex[cortex])
    if dopa_flag:
        pg_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 400., 'stop': 600.})
        parts_dict_log[pg_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(pg_fast, vta[vta_DA0], syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(vta[vta_DA0]) / 4})
        log_conn(pg_fast, vta[vta_DA0])
else:
    sg_slow = nest.Create('spike_generator', params={'spike_times': np.arange(1, T, 20.)})
    parts_dict_log[sg_slow[0]] = 'Periodic Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex})
    nest.Connect(sg_slow, prefrontal_cortex[cortex], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(prefrontal_cortex[cortex]) / 4})
    log_conn(sg_slow, prefrontal_cortex[cortex])
    if dopa_flag:
        sg_fast = nest.Create('spike_generator', params={'spike_times': np.arange(400, 600, 15.)})
        parts_dict_log[sg_fast[0]] = 'Periodic Generator(fast)'
        nest.Connect(sg_fast, vta[vta_DA0], syn_spec=gen_static_syn, )
        # conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(vta[vta_DA0]) / 4})
        log_conn(sg_fast, vta[vta_DA0])

# =============
# SPIKEDETECTOR
# =============
logger.debug('Attaching spikes detector')

spikedetector = nest.Create("spike_detector", 2, params=detector_param)
nest.Connect(prefrontal_cortex[cortex][:N_detect], (spikedetector[0],))
logger.debug("spike detecor is attached to prefrontal cortex: tracing %d neurons" % N_detect)
nest.Connect(vta[vta_DA0][:N_detect], (spikedetector[1],))
logger.debug("spike detecor is attached to VTA[DA0]: tracing %d neurons" % N_detect)

# ============
# MULTIMETER
# ============
mm_param["label"] = 'prefrontal cortex'
mm1 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm1, (prefrontal_cortex[cortex][0],))
logger.debug("%s - %d", mm_param["label"], prefrontal_cortex[cortex][0])
mm_param["label"] = 'vta[DA0]'
mm2 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm2, (vta[vta_DA0][0],))
logger.debug("%s - %d", mm_param["label"], vta[vta_DA0][0])

# ==========
# SIMULATING
# ==========
nest.PrintNetwork()
endbuild = clock()
logger.debug("Simulating")
if not dopa_flag:
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
            if nest.GetStatus(vta[vta_DA0])[0]['local']:
                weight = nest.GetStatus(nest.GetConnections(vta[vta_DA0], synapse_model=dopa_model_ex))[0]['weight']
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
rate_th = events_th / sim_time * 1000.0 / N_detect

# logger.info("Number of neurons : {0}".format(len(thalamus)))
# logger.info("Number of synapses: {0}".format(num_synapses))
logger.info("Building time     : %.2f s" % build_time)
logger.info("Simulation time   : %.2f s" % sim_time)
logger.info("Cortex rate   : %.2f Hz" % rate_th)
logger.info('Dopamine: ' + ('YES' if dopa_flag else 'NO'))
logger.info('Noise: ' + ('YES' if poison_generator else 'NO'))

# =====
# Draw
# =====
if save_weight_flag:
    plot_weights(weight_list, "Neurons weights progress neuron 1")

nest.voltage_trace.from_device(mm1)
pl.axis(axis)
pl.savefig(f_name_gen('prefrontal_cortex', True), dpi=dpi_n, format='png')
if disp_flag:
    nest.voltage_trace.show()
pl.close()

pl.axis(axis)
nest.voltage_trace.from_device(mm2)
pl.axis(axis)
pl.savefig(f_name_gen('vta[da0]', True), dpi=dpi_n, format='png')
if disp_flag:
    nest.voltage_trace.show()
pl.close()

nest.raster_plot.from_device((spikedetector[0],), hist=True)
pl.savefig(f_name_gen('spikes_prefrontal_cortex', is_image=True), format='png')
if disp_flag:
    nest.raster_plot.show()
pl.close()

nest.raster_plot.from_device((spikedetector[1],), hist=True)
pl.savefig(f_name_gen('spikes_vta[da0]', is_image=True), format='png')
if disp_flag:
    nest.raster_plot.show()
pl.close()
