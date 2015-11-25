# -*- coding: utf-8 -*-
# ToDo add generator to every part
# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there ara some mistakes in neuron parameters! Write @alexpanzer in Trello.
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
This is the implementation of experiment of dopamine neuromodulation based on
https://github.com/research-team/NEUCOGAR/blob/master/IntegratedCircuits.png
Prefix description:
	ex_  -  excitory
	inh_ - inhibitory
	d_   - Direct
	ind_ - indirect

Neurotools is used for representing and analyzing nonscientific data.
'''

logger = logging.getLogger("dopamine")
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

#TODO "...ation', parts), " <- why we input this argument into get_ids once
parts = generate_neurons(nest)

motor_cortex = (get_ids('motivation', parts), get_ids('action'))
f_register(motor_cortex[motivation], 'Motor cortex[motivation]')
f_register(motor_cortex[action], 'Motor cortex[action]')

prefrontal_cortex = (get_ids('Glu0'), get_ids('Glu1'))
f_register(prefrontal_cortex[pfc_Glu0], 'Prefrontal cortex[Glu0]')
f_register(prefrontal_cortex[pfc_Glu1], 'Prefrontal cortex[Glu1]')


striatum = (get_ids('D1'), get_ids('D2'), get_ids('tan'))
f_register(striatum[tan], 'Striatum[tan]')
f_register(striatum[D1], 'Striatum[D1]')
f_register(striatum[D2], 'Striatum[D2]')

gpe = (get_ids('Glu'))
f_register(gpe, 'GPe[Glu]')

gpi = get_ids('GABA')
f_register(gpi, 'GPi[GABA]')

stn = get_ids('Glu')
f_register(stn, 'STN[Glu]')

snr = get_ids('GABA')
f_register(snr, 'SNr[GABA]')

thalamus = get_ids('Glu')
f_register(thalamus, 'Thalamus[Glu]')

snc = (get_ids('GABA'), get_ids('DA'))
f_register(snc[snc_GABA], 'SNc[GABA]')
f_register(snc[snc_DA], 'SNc[DA]')

nac = (get_ids('ACh'), get_ids('GABA0'), get_ids('GABA1'))
f_register(nac[nac_ACh], 'NAc[ACh]')
f_register(nac[nac_GABA0], 'NAc[GABA0]')
f_register(nac[nac_GABA1], 'NAc[GABA1]')

vta = (get_ids('GABA0'), get_ids('DA0'), get_ids('GABA1'), get_ids('DA1'), get_ids('GABA2'))
f_register(vta[vta_GABA0], 'VTA[GABA0]')
f_register(vta[vta_DA0], 'VTA[DA0]')
f_register(vta[vta_GABA1], 'VTA[GABA1]')
f_register(vta[vta_DA1], 'VTA[DA1]')
f_register(vta[vta_GABA2], 'VTA[GABA2]')

tpp = (get_ids('GABA'), get_ids('ACh'), get_ids('Glu'))
f_register(tpp[tpp_GABA], 'TPP[GABA]')
f_register(tpp[tpp_ACh], 'TPP[ACh]')
f_register(tpp[tpp_Glu], 'TPP[Glu')

amygdala = get_ids('Glu')
f_register(amygdala, 'Amygdala[Glu]')

del (parts, get_ids, generate_neurons)

log_conn = lambda a, b, syn_type=None: logger.debug('%s -> %s (%s)'
            % (parts_dict_log[a[0]], parts_dict_log[b[0]], 'generator' if syn_type is None else syn_type))

'''Help method for connection syntax facilitation'''
def connect(ner_from, ner_to, syn_type=GABA):
    if syn_type == Glu:
        nest.Connect(ner_from, ner_to, conn_spec=conn_dict, syn_spec=STDP_synparams_Glu)
        log_conn(ner_from, ner_to, "Glu")
    elif syn_type == ACh:
        nest.Connect(ner_from, ner_to, conn_spec=conn_dict, syn_spec=STDP_synparams_ACh)
        log_conn(ner_from, ner_to, "ACh")
    else:
        nest.Connect(ner_from, ner_to, conn_spec=conn_dict, syn_spec=STDP_synparams_GABA)
        log_conn(ner_from, ner_to, "GABA")


logger.debug('Start connection initialisation')
# * * * NIGROSTRIATAL * * *
connect(motor_cortex[motivation], striatum[D1], syn_type = Glu)
connect(motor_cortex[action], striatum[D1], syn_type = Glu)

connect(motor_cortex[motivation], striatum[D2], syn_type = Glu)
connect(motor_cortex[action], striatum[D2], syn_type = Glu)

connect(motor_cortex[motivation], thalamus, syn_type = Glu)
connect(motor_cortex[action], thalamus, syn_type = Glu)

connect(motor_cortex[motivation], stn, syn_type = Glu)
connect(motor_cortex[action], stn, syn_type = Glu)

connect(motor_cortex[action], nac[nac_GABA0])

connect(striatum[tan], striatum[D1], syn_type = ACh)
connect(striatum[tan], striatum[D2], syn_type = ACh)
# connect(motor_cortex[motivation], snc[snc_DA], syn_type = Glu) (when DOPAMINE on)

# ! Direct pathway: Striatum (inhibits) [D1] → "SNr-GPi" complex (less inhibition of thalamus) →
connect(striatum[D1], snr)
connect(striatum[D1], gpi)
connect(striatum[D1], gpe)

# ! Indirect pathway: Striatum (inhibits) [D2] → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) →
connect(striatum[D2], gpe)
connect(gpe, stn)
connect(gpe, striatum[D1])
connect(gpe, striatum[D2])
connect(gpe, gpi)
connect(gpe, snr)
connect(stn, snr, syn_type = Glu)
connect(stn, gpi, syn_type = Glu)
connect(stn, gpe, syn_type = Glu)
connect(stn, amygdala, syn_type = Glu)
# connect(stn, snc, syn_type = Glu) (when DOPAMINE on)

# ! Common path: SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.
connect(gpi, thalamus)
connect(snr, thalamus)
connect(thalamus, motor_cortex[action], syn_type = Glu)
connect(thalamus, stn, syn_type = Glu)
connect(thalamus, striatum[D1], syn_type = Glu)
connect(thalamus, striatum[D2], syn_type = Glu)
connect(thalamus, striatum[tan], syn_type = Glu)
connect(thalamus, nac[nac_GABA0], syn_type = Glu)
connect(thalamus, nac[nac_GABA1], syn_type = Glu)
connect(thalamus, nac[nac_ACh], syn_type = Glu)

# * * * MESOCORTICOLIMBIC * * *
connect(nac[nac_ACh], nac[nac_GABA1], syn_type = ACh)
connect(nac[nac_GABA0], nac[nac_GABA1])
connect(nac[nac_GABA1], vta[vta_GABA2])

connect(vta[vta_GABA0], prefrontal_cortex[pfc_Glu0])
connect(vta[vta_GABA0], prefrontal_cortex[pfc_Glu1])
connect(vta[vta_GABA0], tpp[tpp_GABA])

connect(vta[vta_GABA1], vta[vta_DA0])
connect(vta[vta_GABA1], vta[vta_DA1])
connect(vta[vta_GABA2], nac[nac_GABA1])
# vta[vta_DA0] -> nac[nac_GABA1] (DOPAMIN)
# vta[vta_DA0] -> prefrontl_cortex[pfc_Glu0] (DOPAMIN)
# vta[vta_DA0] -> prefrontl_cortex[pfc_Glu1] (DOPAMIN)

connect(tpp[tpp_GABA], vta[vta_GABA0])
connect(tpp[tpp_GABA], snc[snc_GABA])
connect(tpp[tpp_ACh], vta[vta_GABA0], syn_type = ACh)
connect(tpp[tpp_ACh], vta[vta_DA1], syn_type = ACh)
connect(tpp[tpp_ACh], striatum[D1], syn_type = ACh)
connect(tpp[tpp_ACh], snc[snc_GABA], syn_type = ACh)
connect(tpp[tpp_Glu], vta[vta_GABA0], syn_type = Glu)
connect(tpp[tpp_Glu], vta[vta_DA1], syn_type = Glu)
connect(tpp[tpp_Glu], snc[snc_DA], syn_type = Glu)

# * * * INTEGRATED * * *
connect(prefrontal_cortex[pfc_Glu0], vta[vta_DA0], syn_type = Glu)
connect(prefrontal_cortex[pfc_Glu0], nac[nac_GABA1], syn_type = Glu)
connect(prefrontal_cortex[pfc_Glu1], vta[vta_GABA2], syn_type = Glu)
connect(prefrontal_cortex[pfc_Glu1], nac[nac_GABA1], syn_type = Glu)

connect(amygdala, nac[nac_GABA0], syn_type = Glu)
connect(amygdala, nac[nac_GABA1], syn_type = Glu)
connect(amygdala, nac[nac_ACh], syn_type = Glu)
connect(amygdala, striatum[D1], syn_type = Glu)
connect(amygdala, striatum[D2], syn_type = Glu)
connect(amygdala, striatum[tan], syn_type = Glu)

#TODO add new connections
logger.debug('Making neuromodulating connections...')

# ==================
# Dopamine modulator
# ==================
if dopa_flag:
    # Volume transmission: init dopa_model
    vt_ex = nest.Create("volume_transmitter")
    vt_in = nest.Create("volume_transmitter")
    DOPA_synparams_ex['vt'] = vt_ex[0]
    DOPA_synparams_in['vt'] = vt_in[0]
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)

    # NIGROSTRIATAL
    nest.Connect(snc[snc_DA], vt_ex)
    nest.Connect(snc[snc_DA], vt_in)
    nest.Connect(snc[snc_DA], striatum[D1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc[snc_DA], striatum[D1], dopa_model_ex)
    #nest.Connect(snc[snc_DA], striatum[D2], conn_dict, syn_spec=dopa_model_in) #TODO check from science-source
    #log_conn(snc[snc_DA], striatum[D2], dopa_model_in)
    nest.Connect(snc[snc_DA], striatum[tan], conn_dict, syn_spec=dopa_model_in) #TODO inhibitory???
    log_conn(snc[snc_DA], striatum[tan], dopa_model_in)
    nest.Connect(snc[snc_DA], gpe, conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc[snc_DA], gpe, dopa_model_ex)
    nest.Connect(snc[snc_DA], stn, conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc[snc_DA], stn, dopa_model_ex)
    nest.Connect(snc[snc_DA], nac[nac_GABA0], conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc[snc_DA], nac[nac_GABA0], dopa_model_ex)
    nest.Connect(snc[snc_DA], nac[nac_GABA1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(snc[snc_DA], nac[nac_GABA1], dopa_model_ex)

    connect(motor_cortex[motivation], snc[snc_DA], syn_type = Glu)  # ToDo neuromodulation
    connect(stn, snc[snc_DA], syn_type = Glu)

    # MESOCORTICOLIMBIC
    nest.Connect(vta[vta_DA0], vt_ex)
    nest.Connect(vta[vta_DA1], vt_ex)
    nest.Connect(vta[vta_DA0], striatum[D1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA0], striatum[D1], dopa_model_ex)
    nest.Connect(vta[vta_DA0], striatum[D2], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA0], striatum[D2], dopa_model_ex)
    nest.Connect(vta[vta_DA0], prefrontal_cortex[pfc_Glu0], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA0], prefrontal_cortex[pfc_Glu0], dopa_model_ex)
    nest.Connect(vta[vta_DA0], prefrontal_cortex[pfc_Glu1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA0], prefrontal_cortex[pfc_Glu1], dopa_model_ex)
    nest.Connect(vta[vta_DA1], nac[nac_GABA0], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA1], nac[nac_GABA0], dopa_model_ex)
    nest.Connect(vta[vta_DA1], nac[nac_GABA1], conn_dict, syn_spec=dopa_model_ex)
    log_conn(vta[vta_DA1], nac[nac_GABA1], dopa_model_ex)
del connect

logger.debug('Starting spike generators')

# ===============
# Spike Generator
# ===============
if poison_generator_flag:
    pg_slow = nest.Create("poisson_generator", 1, {"rate": K_slow})
    parts_dict_log[pg_slow[0]] = 'Poisson Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_Glu, 'delay': pg_delay})
    nest.Connect(pg_slow, motor_cortex[action], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[action]) / 4})
    log_conn(pg_slow, motor_cortex[action])
    if dopa_flag:
        # NIGROSTRIATAL (motor_cortex)
        pg_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 400., 'stop': 600.})
        parts_dict_log[pg_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(pg_fast, motor_cortex[motivation], syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[motivation]) / 4})
        log_conn(pg_fast, motor_cortex[motivation])
        # MESOCORTICOLIMBIC (VTA)
        pg_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 400., 'stop': 600.})
        parts_dict_log[pg_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(pg_fast, vta[vta_DA0], syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(vta[vta_DA0]) / 4})
        log_conn(pg_fast, vta[vta_DA0])
        # ADDITIONAL (Amygdala)
        pg_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 400., 'stop': 600.})
        parts_dict_log[pg_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(pg_fast, amygdala, syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(amygdala) / 4})
        log_conn(pg_fast, amygdala)
else:
    sg_slow = nest.Create('spike_generator', params={'spike_times': np.arange(1, T, 20.)})
    parts_dict_log[sg_slow[0]] = 'Periodic Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_Glu})
    nest.Connect(sg_slow, motor_cortex[action], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[action]) / 4})
    log_conn(sg_slow, motor_cortex[action])
    if dopa_flag:
        # NIGROSTRIATAL (motor_cortex)
        sg_fast = nest.Create('spike_generator', params={'spike_times': np.arange(400, 600, 15.)})
        parts_dict_log[sg_fast[0]] = 'Periodic Generator(fast)'
        nest.Connect(sg_fast, motor_cortex[motivation], syn_spec=gen_static_syn, )
        # conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[motivation]) / 4})
        log_conn(sg_fast, motor_cortex[motivation])
        # MESOCORTICOLIMBIC (VTA)
        sg_fast = nest.Create('spike_generator', params={'spike_times': np.arange(400, 600, 15.)})
        parts_dict_log[sg_fast[0]] = 'Periodic Generator(fast)'
        nest.Connect(sg_fast, vta[vta_DA0], syn_spec=gen_static_syn, )
        # conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(vta[vta_DA0]) / 4})
        log_conn(sg_fast, vta[vta_DA0])

# =============
# SPIKEDETECTOR
# =============
logger.debug('Attaching spikes detector')
spikedetector = nest.Create("spike_detector", 4, params=detector_param)

# NIGROSTRIATAL
nest.Connect(thalamus[:N_rec], (spikedetector[0],))
logger.debug("spike detecor is attached to thalamus: tracing %d neurons" % N_rec)
nest.Connect(motor_cortex[action][:N_rec], (spikedetector[1],))
logger.debug("spike detecor is attached to motor cortex: tracing %d neurons" % N_rec)

# MESOCORTICOLIMBIC
nest.Connect(prefrontal_cortex[pfc_Glu0][:N_rec], (spikedetector[2],))
logger.debug("spike detecor is attached to prefrontal cortex Glu0: tracing %d neurons" % N_rec)
nest.Connect(vta[vta_DA0][:N_rec], (spikedetector[3],))
logger.debug("spike detecor is attached to VTA[DA0]: tracing %d neurons" % N_rec)

# ============
# MULTIMETER
# ============
mm_param["label"] = 'thalamus'
mm1 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm1, (thalamus[0],))
logger.debug("%s - %d", mm_param["label"], thalamus[0])
mm_param["label"] = 'snc'
mm2 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm2, (snc[snc_DA][0],))
logger.debug("%s - %d", mm_param["label"], snc[0])

mm_param["label"] = 'prefrontal_cortex'
mm3 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm3, (prefrontal_cortex[pfc_Glu0][0],))
logger.debug("%s - %d", mm_param["label"], prefrontal_cortex[pfc_Glu0][0])
mm_param["label"] = 'vta[DA0]'
mm4 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm4, (vta[vta_DA0][0],))
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
            if nest.GetStatus(snc)[0]['local']:
                # TODO use both DOPA if save_weight_flag will be True
                #weight = nest.GetStatus(nest.GetConnections(vta[vta_DA0], synapse_model=dopa_model_ex))[0]['weight']
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
rate_th = nest.GetStatus(spikedetector, "n_events")[0] / sim_time * 1000.0 / N_rec
rate_vta = nest.GetStatus(spikedetector, "n_events")[3] / sim_time * 1000.0 / N_rec

# logger.info("Number of neurons : {0}".format(len(thalamus)))
# logger.info("Number of synapses: {0}".format(num_synapses))
logger.info("Building time     : %.2f s" % build_time)
logger.info("Simulation time   : %.2f s" % sim_time)
logger.info("Thalamus rate   : %.2f Hz" % rate_th)
logger.info("VTA[DA0] rate   : %.2f Hz" % rate_vta)
logger.info('Dopamine: ' + ('YES' if dopa_flag else 'NO'))
logger.info('Noise: ' + ('YES' if poison_generator_flag else 'NO'))

# =====
# Draw
# =====
if save_weight_flag: plot_weights(weight_list, "Neurons weights progress neuron 1")

nest.voltage_trace.from_device(mm1)
pl.axis(axis)
pl.savefig(f_name_gen('thalamus', True), dpi=dpi_n, format='png')
if disp_flag: nest.voltage_trace.show()
pl.close()

pl.axis(axis)
nest.voltage_trace.from_device(mm2)
pl.axis(axis)
pl.savefig(f_name_gen('snc', True), dpi=dpi_n, format='png')
if disp_flag: nest.voltage_trace.show()
pl.close()

nest.voltage_trace.from_device(mm3)
pl.axis(axis)
pl.savefig(f_name_gen('prefrontal_cortex', True), dpi=dpi_n, format='png')
if disp_flag:
    nest.voltage_trace.show()
pl.close()

pl.axis(axis)
nest.voltage_trace.from_device(mm4)
pl.axis(axis)
pl.savefig(f_name_gen('vta[da0]', True), dpi=dpi_n, format='png')
if disp_flag:
    nest.voltage_trace.show()
pl.close()


nest.raster_plot.from_device((spikedetector[0],), hist=True)
pl.savefig(f_name_gen('spikes_thalamus', is_image=True), format='png')
if disp_flag: nest.raster_plot.show()
pl.close()

nest.raster_plot.from_device((spikedetector[1],), hist=True)
pl.savefig(f_name_gen('spikes_motorcortex', is_image=True), format='png')
if disp_flag: nest.raster_plot.show()
pl.close()

nest.raster_plot.from_device((spikedetector[2],), hist=True)
pl.savefig(f_name_gen('spikes_prefrontal_cortex', is_image=True), format='png')
if disp_flag:
    nest.raster_plot.show()
pl.close()

nest.raster_plot.from_device((spikedetector[3],), hist=True)
pl.savefig(f_name_gen('spikes_vta[da0]', is_image=True), format='png')
if disp_flag:
    nest.raster_plot.show()
pl.close()

# another type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(motor_cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
