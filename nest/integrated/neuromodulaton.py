# -*- coding: utf-8 -*-
# ToDo add generator to every part
# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there ara some mistakes in neuron parameters! Write @alexpanzer in Trello.
from time import clock
# math and randomise package
import numpy as np
# visualise spikes
import nest.raster_plot
import nest.voltage_trace
# local project parameters
from parameters import *

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

'''Help method for creating spikeGenerator'''
def spikeGenerator(typeGenerator, part, startTime, stopTime, weightParam=w_Glu):
    if typeGenerator == 'fast':
        generator_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': startTime, 'stop': stopTime})
        parts_dict_log[generator_fast[0]] = 'Poisson Generator(fast)'
        nest.Connect(generator_fast, part, syn_spec=gen_static_syn,
                     conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(part) / 4})
        log_conn(generator_fast, part)
    else:
        generator_slow = nest.Create("poisson_generator", 1, {"rate": K_slow})
        parts_dict_log[generator_slow[0]] = 'Poisson Generator(slow)'
        nest.CopyModel("static_synapse", gen_static_syn, {'weight': weightParam, 'delay': pg_delay})
        nest.Connect(generator_slow, part, syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(part) / 4})
        log_conn(generator_slow, part)

# ===============
# Spike Generator
# ===============
if poison_generator_flag:
    spikeGenerator('slow', motor_cortex[action], 400., 600.)
    if dopa_flag:
        # NIGROSTRIATAL (motor_cortex)
        spikeGenerator('fast', motor_cortex[motivation], 400., 600.)
        # MESOCORTICOLIMBIC (PFC and PPTg)
        spikeGenerator('fast', prefrontal_cortex[pfc_Glu0], 400., 600.)
        spikeGenerator('fast', prefrontal_cortex[pfc_Glu1], 400., 600.)
        spikeGenerator('fast', tpp[tpp_GABA], 400., 600.)
        spikeGenerator('fast', tpp[tpp_Glu], 400., 600.)
        spikeGenerator('fast', tpp[tpp_ACh], 400., 600.)
        # ADDITIONAL (Amygdala)
        spikeGenerator('fast', amygdala, 400., 600.)
'''
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
'''
# =============
# SPIKEDETECTOR
# =============
#TODO add function to build spikedetectors
logger.debug('Attaching spikes detector')
spikedetector = nest.Create("spike_detector", 6, params=detector_param)

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
nest.Connect(vta[vta_DA1][:N_rec], (spikedetector[4],))
logger.debug("spike detecor is attached to VTA[DA1]: tracing %d neurons" % N_rec)
nest.Connect(snc[snc_DA][:N_rec], (spikedetector[5],))
logger.debug("spike detecor is attached to SNC[DA]: tracing %d neurons" % N_rec)

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
logger.debug("%s - %d", mm_param["label"], snc[snc_DA][0])

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
endbuild = clock()
startsimulate = clock()
nest.PrintNetwork()
logger.debug("Simulating")
MEGA = 10 ** 6

timerFlag = True



times = []
resources = []

'''
import psutil

import time
from threading import Thread

class writeRes(Thread):
    def run(self):
        resources.append(str('%5d MB %7.1f MHz ' % (psutil.virtual_memory()[3] / MEGA, psutil.cpu_times()[0] ) + str(datetime.datetime.now().time())) + '\n')

class timer(Thread):
    def run(self):
        while timerFlag:
            writeRes().start()
            sleep
'''
import datetime
if not dopa_flag:
    # TYPE_1
    nest.Simulate(T)
else:
    if not save_weight_flag:
        nest.Simulate(T)
    else:
        iterA = 0
        begin = 0
        for t in np.arange(0, T + dt, dt):
            nest.Simulate(dt)
            end = clock()
            times.append(str('%.1f %.1f %.1f %4d ' % (begin, end - begin, end, t)) + str(datetime.datetime.now().time()) + '\n')
            iterA+=1
            begin = end
        timerFlag = False

        tRes = open('timeResources.txt', 'w')
        tSim = open('timeSimulation.txt', 'w')
        for item in resources:
            tRes.write(item)
        for item in times:
            tSim.write(item)
        tSim.close()
        tRes.close()

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
logger.info("Thalamus rate     : %.2f Hz" % rate_th)
logger.info("VTA[DA0] rate     : %.2f Hz" % rate_vta)
logger.info('Dopamine: ' + ('YES' if dopa_flag else 'NO'))
logger.info('Noise: ' + ('YES' if poison_generator_flag else 'NO'))

'''
import matplotlib.pyplot as plt
import numpy as np

ev = nest.GetStatus((spikedetector[3],), "events")[0]
ts = ev["times"]
gids = ev["senders"]

hist, bins = np.histogram(gids, bins=len(ts))
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
'''

# =====
# BUILDING DIAGRAM'S
# =====
if withoutGUI:
    from write_from_sensors import *
    save_voltage(mm1, name="thalamus")
    save_voltage(mm2, name="snc[da0]")
    save_voltage(mm3, name="prefrontal_cortex")
    save_voltage(mm4, name="vta[da0]")

    save_spikes((spikedetector[0],), name="thalamus")           #, hist=True)
    save_spikes((spikedetector[1],), name="motor_cortex")       #, hist=True)
    save_spikes((spikedetector[2],), name="prefrontal_cortex")  #, hist=True)
    save_spikes((spikedetector[3],), name="vta[da0]")           #, hist=True)
    save_spikes((spikedetector[4],), name="vta[da1]")           #, hist=True)
    save_spikes((spikedetector[5],), name="snc[da]")            #, hist=True)
else:
    import nest.raster_plot
    import nest.voltage_trace
    import pylab as pl

    nest.voltage_trace.from_device(mm1)
    pl.axis(axis)
    pl.savefig(f_name_gen('thalamus', True), dpi=dpi_n, format='png')
    pl.close()

    pl.axis(axis)
    nest.voltage_trace.from_device(mm2)
    pl.savefig(f_name_gen('snc[da0]', True), dpi=dpi_n, format='png')
    pl.close()

    nest.voltage_trace.from_device(mm3)
    pl.axis(axis)
    pl.savefig(f_name_gen('prefrontal_cortex', True), dpi=dpi_n, format='png')
    pl.close()

    pl.axis(axis)
    nest.voltage_trace.from_device(mm4)
    pl.axis(axis)
    pl.savefig(f_name_gen('vta[da0]', True), dpi=dpi_n, format='png')
    pl.close()


    nest.raster_plot.from_device((spikedetector[0],), hist=True)
    pl.savefig(f_name_gen('spikes_thalamus', is_image=True), format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[1],), hist=True)
    pl.savefig(f_name_gen('spikes_motorcortex', is_image=True), format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[2],), hist=True)
    pl.savefig(f_name_gen('spikes_prefrontal_cortex', is_image=True), format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[3],), hist=True)
    pl.savefig(f_name_gen('spikes_vta[da0]', is_image=True), format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[4],), hist=True)
    pl.savefig(f_name_gen('spikes_vta[da1]', is_image=True), format='png')
    pl.close()

    nest.raster_plot.from_device((spikedetector[5],), hist=True)
    pl.savefig(f_name_gen('spikes_snc[da]', is_image=True), format='png')
    pl.close()