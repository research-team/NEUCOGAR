# -*- coding: utf-8 -*-

# ToDo add generator to every part

# math and randomise package
import numpy as np
import pylab as pl
# neuron packages
# visualise spikes
# from NeuroTools import signals, io
# import matplotlib
# Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')
import nest.raster_plot
import nest.voltage_trace
# local project parameters
from parameters import *
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
nest.SetKernelStatus({'overwrite_files': True, 'data_path': sd_folder_name, "local_num_threads": 1, "resolution": dt})

# ============
# Creating BS
# ============
parts_BG = generate_neurons_BG(nest)
cortex = get_ids('motor_cortex', parts_BG)
striatum = (get_ids('D1'), get_ids('D2'), get_ids('tan'))
gpe = get_ids('gpe')
gpi = get_ids('gpi')
stn = get_ids('stn')
snr = get_ids('snr')
thalamus = get_ids('thalamus')
snc = get_ids('snc')
del (parts_BG, get_ids, generate_neurons_BG)

connect = lambda ner_from, ner_to, is_syn_ex=False: nest.Connect(ner_from, ner_to, conn_spec=conn_dict,
                                                                 syn_spec=STDP_synapseparams_ex if is_syn_ex else STDP_synapseparams_in)
connect(cortex, striatum[D1], is_syn_ex=True)
connect(cortex, striatum[D2], is_syn_ex=True)
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
connect(thalamus, cortex, is_syn_ex=True)
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
else:
    dopa_model_ex = STDP_synapseparams_ex
    dopa_model_in = STDP_synapseparams_in

nest.Connect(snc, striatum[D1], conn_dict, syn_spec=dopa_model_ex)
nest.Connect(snc, striatum[D2], conn_dict, syn_spec=dopa_model_in)

# ===============
# Spike Generator
# ===============
if pg_flag:
    pg_fast = nest.Create("poisson_generator", 1, {"rate": K_fast, 'start': 1., 'stop': 100.})  # ToDo find out nu_ex
    pg_slow = nest.Create("poisson_generator", 1, {"rate": K_slow, 'start': 1., 'stop': 100.})
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex, 'delay': pg_delay})
    nest.Connect(pg_fast, striatum[tan], syn_spec=gen_static_syn)
    nest.Connect(pg_slow, cortex, syn_spec=gen_static_syn)
    nest.Connect(pg_slow, gpe, syn_spec=gen_static_syn)
    nest.Connect(pg_fast, stn, syn_spec=gen_static_syn)
    # nest.Connect(pg_fast, snr, syn_spec=gen_static_syn)
    nest.Connect(pg_slow, thalamus, syn_spec=gen_static_syn)
    # neuromodulation
    # nest.Connect(nest.Create("poisson_generator", 1, {"rate": 150.}), snc, syn_spec=gen_static_syn)
    if vt_flag:
        nest.Connect(nest.Create("poisson_generator", 1, {"rate": 300.}), snc, syn_spec=gen_static_syn)
    else:
        nest.Connect(nest.Create("poisson_generator", 1, {"rate": 100.}), snc, syn_spec=gen_static_syn)
else:
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex})
    spikes_times = np.arange(1, T, 20.)
    f_spike_times = lambda dt: np.array([t + dt for t in spikes_times])
    f_gen_connect = lambda part, dt=0, rang=None: nest.Connect(nest.Create('spike_generator', params={
        'spike_times': (f_spike_times(dt) if rang is None else rang)}), part, syn_spec=gen_static_syn)

    f_gen_connect(cortex)
    f_gen_connect(stn)
    f_gen_connect(striatum[tan], rang=np.arange(1, T, 30.))
    f_gen_connect(gpe)
    f_gen_connect(snr)
    f_gen_connect(thalamus, )  #rang=np.arange(1., T,)
    if vt_flag:
        f_gen_connect(snc, rang=np.arange(1., 200., 20.))
        f_gen_connect(snc, rang=np.arange(200., 300., 10.))
        f_gen_connect(snc, rang=np.arange(300., T, 20.))
    else:
        f_gen_connect(snc, )
    del (f_gen_connect, f_spike_times)
# =============
# SPIKEDETECTOR
# =============
spikedetector = nest.Create("spike_detector", params=detector_param)
nest.Connect(thalamus[:N_rec], spikedetector)
logger.debug("spike detecor is attached to cortex: tracing %d neurons" % N_rec)
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
nest.Simulate(T)

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

nest.raster_plot.from_device(spikedetector, hist=True)
pl.savefig(f_name_gen('spikes', is_image=True), format='png')
nest.raster_plot.show()
pl.close()

# another type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
