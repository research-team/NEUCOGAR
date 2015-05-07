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
nest.SetKernelStatus({'overwrite_files': True, 'data_path': sd_folder_name, 'data_prefix': f_name_gen(''),
                      "local_num_threads": 2, "resolution": dt})

# ============
# Creating BS
# ============
parts_BG = generate_neurons_BG(nest)
cortex = get_ids('cortex', parts_BG)
striatum = (get_ids('D1'), get_ids('D2'), get_ids('tan'))
gpe = get_ids('gpe')
gpi = get_ids('gpi')
stn = get_ids('stn')
snr = get_ids('snr')
thalamus = get_ids('thalamus')
snc = get_ids('snc')
del (parts_BG, get_ids, generate_neurons_BG)

# synapses model are same for test facilitation
nest.CopyModel(bg_synapse_model, syn_excitory,
               {"weight": w_ex, "delay": delay_ex, "tau_plus": tau_plus, "Wmax": wmax})
nest.CopyModel(bg_synapse_model, syn_inhibitory,
               {'weight': w_in, 'delay': delay_inh, "tau_plus": tau_plus, "Wmax": wmax})

connect = lambda ner_from, ner_to, is_syn_ex=False: nest.Connect(ner_from, ner_to, conn_spec=conn_dict,
                                                                 syn_spec=syn_excitory if is_syn_ex else syn_inhibitory)
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
    vt_inh = nest.Create("volume_transmitter")
    nest.CopyModel("static_synapse", device_static_synapse, {'delay': delay})
    nest.CopyModel("stdp_dopamine_synapse", dopa_model_ex,
                   {"vt": vt_ex[0], "weight": stdp_dopamine_synapse_w_ex, "delay": vt_delay})
    nest.CopyModel("stdp_dopamine_synapse", dopa_model_in,
                   {"vt": vt_inh[0], "weight": stdp_dopamine_synapse_w_in, "delay": vt_delay})
    # nest.Connect(snc, vt_ex, syn_spec=device_static_synapse)
    # nest.Connect(snc, vt_inh, syn_spec=device_static_synapse)

    # placed in if clause for simple imitatingreinforcment learning
    nest.Connect(snc, striatum[tan], conn_dict, dopa_model_in)
else:
    nest.CopyModel(bg_synapse_model, dopa_model_ex)
    nest.CopyModel(bg_synapse_model, dopa_model_in)

nest.Connect(snc, striatum[D1], conn_dict, dopa_model_ex)
nest.Connect(snc, striatum[D2], conn_dict, dopa_model_in)

# ===============
# Spike Generator
# ===============
if pg_flag:
    pg_ex = nest.Create("poisson_generator", 1, {"rate": K_ex * nu_ex})  # ToDo find out nu_ex
    pg_in = nest.Create("poisson_generator", 1, {"rate": K_in * nu_in, 'start': 1., 'stop': 200.})
    # nest.SetStatus(pg_in, {"rate": K_in * nu_in})
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex, 'delay': delay})
    # nest.Connect(pg_in, ..., syn_spec={'weight': w_in, 'delay': delay})
    nest.Connect(pg_ex, striatum[tan], syn_spec=gen_static_syn)
    nest.Connect(pg_in, cortex, syn_spec=gen_static_syn)
    nest.Connect(pg_in, gpe, syn_spec=gen_static_syn)
    nest.Connect(pg_ex, stn, syn_spec=gen_static_syn)
    nest.Connect(pg_in, snr, syn_spec=gen_static_syn)
    nest.Connect(pg_ex, thalamus, syn_spec=gen_static_syn)
    # neuromodulation
    if vt_flag:
        nest.Connect(nest.Create("poisson_generator", 1, {"rate": 10000.}), snc, syn_spec=gen_static_syn)
    else:
        nest.Connect(nest.Create("poisson_generator", 1, {"rate": 800.}), snc, syn_spec=gen_static_syn)
else:
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex})
    spikes_times = np.arange(1, 100., 30.)
    f_spike_times = lambda dt: np.array([t + dt for t in spikes_times])
    f_gen_connect = lambda part, dt=0, rang=None: nest.Connect(nest.Create('spike_generator', params={
        'spike_times': (f_spike_times(dt) if rang is None else rang)}), part, syn_spec=gen_static_syn)

    f_gen_connect(cortex)
    f_gen_connect(stn)
    f_gen_connect(striatum[tan], rang=np.arange(1, T, 10.))
    f_gen_connect(gpe)
    f_gen_connect(snr)
    f_gen_connect(thalamus)
    if vt_flag:
        f_gen_connect(snc, rang=np.arange(1, T, 10.))
    else:
        f_gen_connect(snc, )
    del (f_gen_connect, f_spike_times)
# =============
# SPIKEDETECTOR
# =============
spikedetector = nest.Create("spike_detector", params=detector_param)
nest.Connect(thalamus[:N_rec], spikedetector)
logger.debug("spike detecor is attached to cortex")
# nest.PrintNetwork()
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
nest.raster_plot.from_device(spikedetector, hist=True)
pl.savefig(f_name_gen('spikes', is_image=True, with_folder=True), format='png')
nest.raster_plot.show()
pl.close()

nest.voltage_trace.from_device(mm1)
pl.axis(axis)
pl.savefig(f_name_gen('thalamus', True, True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

nest.voltage_trace.from_device(mm2)
pl.axis(axis)
pl.savefig(f_name_gen('snc', True, True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

# another type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
