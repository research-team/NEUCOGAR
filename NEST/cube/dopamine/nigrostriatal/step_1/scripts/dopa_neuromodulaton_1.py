# -*- coding: utf-8 -*-

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
from parameters_1 import *
import os

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

nest.ResetKernel()
if not os.path.exists(sd_folder_name):
    os.mkdir(sd_folder_name)
nest.SetKernelStatus({'overwrite_files': True, 'data_path': sd_folder_name})  # set to True to permit overwriting

# ============
# Creating BS
# ============

# neuron set
nest.SetDefaults('iaf_psc_exp', STP_neuronparams)
nest.SetDefaults('iaf_psc_alpha', STP_neuronparams)
cortex = nest.Create(cortex_neurons_model, NN_cortex)
striatum = nest.Create(striatum_neurons_model, NN_striatum)
gpe = nest.Create(gpe_neurons_model, NN_gpe)
gpi = nest.Create(gpi_neurons_model, NN_gpi)
stn = nest.Create(stn_neurons_model, NN_stn)
snr = nest.Create(snr_neurons_model, NN_snr)
thalamus = nest.Create(thalamus_neurons_model, NN_thalamus)
snc = nest.Create(snc_neurons_model, NN_snc)

nest.SetStatus(cortex, cortex_neuronparams)
nest.SetStatus(striatum, striatum_neuronparams)
nest.SetStatus(gpe, gpe_neuronparams)
nest.SetStatus(gpi, gpi_neuronparams)
nest.SetStatus(stn, stn_neuronparams)
nest.SetStatus(snr, snr_neuronparams)
nest.SetStatus(snc, snc_neuronparams)
nest.SetStatus(thalamus, thalamus_neuronparams)

# synapses model are same for test facilitation
# ToDo test direct indirect parameters
nest.CopyModel(bs_synapse_model, syn_excitory, {"weight": w_ex, "delay": delay_ex, 'Wmax': 70., })
nest.CopyModel(bs_synapse_model, syn_inhibitory, {'weight': w_in, 'delay': delay_inh, 'Wmax': -60., })

# ToDO delete {'distribution': 'uniform', 'low': 1., 'high': 1.9}

nest.Connect(cortex, striatum, conn_spec=conn_dict, syn_spec=syn_excitory)
nest.Connect(striatum, gpe, conn_dict, syn_inhibitory)
nest.Connect(striatum, snr, conn_dict, syn_inhibitory)
nest.Connect(striatum, gpi, conn_dict, syn_inhibitory)
nest.Connect(gpe, stn, conn_dict, syn_inhibitory)
nest.Connect(stn, snr, conn_dict, syn_excitory)
nest.Connect(stn, gpi, conn_dict, syn_excitory)
nest.Connect(gpi, thalamus, conn_dict, syn_inhibitory)
nest.Connect(snr, thalamus, conn_dict, syn_inhibitory)
nest.Connect(thalamus, cortex, conn_dict, syn_excitory)



# ToDo pathway: check if it is working with inhibitory weights
# ! Direct pathway: Cortex (stimulates) → Striatum (inhibits) → "SNr-GPi" complex (less inhibition of thalamus) → Thalamus (stimulates) → Cortex (stimulates) → Muscles, etc.
# ! Indirect pathwat: Cortex (stimulates) → Striatum (inhibits) → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.

# ==================
# Dopamine modulator
# ==================
if vt_flag:
    # Volume transmission: init dopa_model
    vt_ex = nest.Create("volume_transmitter")
    nest.CopyModel("stdp_dopamine_synapse", dopa_model,
                   {"vt": vt_ex[0], "weight": stdp_dopamine_synapse_weight, "delay": vt_delay, 'Wmax': 120.})
    nest.Connect(snc, vt_ex)

else:
    nest.CopyModel(syn_inhibitory, dopa_model)
nest.Connect(snc, striatum, conn_dict, dopa_model)

# =====
# INPUT
# =====
# 1)Spikes generators of the Cortex generate series of spikes that stimulates the Striatum.Dopamine neurons produce dopamine that modulates Striatum.

# ===============
# Spike Generator
# ===============
gen_static_syn = 'gen_stat'
if pg_flag:
    pg_fast = nest.Create("poisson_generator", 1, {"rate": 190.,})  # ToDo find out nu_ex
    pg_slow = nest.Create("poisson_generator", 1, {"rate": 60., })  # 'start': 1., 'stop': 200.})
    # nest.SetStatus(pg_in, {"rate": K_in * nu_in})
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_ex})
    # nest.Connect(pg_in, ..., syn_spec={'weight': w_in, 'delay': delay})
    nest.Connect(pg_slow, striatum, syn_spec=gen_static_syn)
    nest.Connect(nest.Create("poisson_generator", 1, {"rate": 5.}), cortex, syn_spec=gen_static_syn, conn_spec={'rule': 'fixed_indegree', 'indegree': 2})
    nest.Connect(nest.Create("poisson_generator", 1, {"rate": 30., 'start': 10.}), gpe, syn_spec=gen_static_syn)
    nest.Connect(pg_fast, stn, syn_spec=gen_static_syn)
    nest.Connect(pg_fast, snr, syn_spec=gen_static_syn)
    nest.Connect(nest.Create("poisson_generator", 1, {"rate": 50., 'start' : 10.}), thalamus, syn_spec=gen_static_syn)
    # neuromodulation
    if vt_flag:
        nest.Connect(nest.Create("poisson_generator", 1, {"rate": 500.,'start': 500., 'stop': 600.}), snc, syn_spec=gen_static_syn)
else:
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': 40.})
    spikes_times = np.arange(1, T, 19.)
    f_spike_times = lambda dt: np.array([t + dt for t in spikes_times])
    f_gen_connect = lambda part, dt=0, rang=None: nest.Connect(nest.Create('spike_generator', params={
        'spike_times': (f_spike_times(dt) if rang is None else rang)}), part, syn_spec=gen_static_syn)
    f_gen_connect(thalamus, rang=np.arange(2, T, 21.))
    # f_gen_connect(cortex, rang=np.arange(1, T, 73.))
    nest.Connect(nest.Create('spike_generator', params={'spike_times':np.arange(1, T, 70.)}), cortex, syn_spec=gen_static_syn, conn_spec={'rule': 'fixed_indegree', 'indegree': 10})
    f_gen_connect(stn, )
    f_gen_connect(gpe, 2)
    f_gen_connect(snr, )

    if vt_flag:
        f_gen_connect(snc, rang=np.arange(500., 600., 30.))
        # else:
        # f_gen_connect(snc, rang = np.arange(1, T, 40.))
    del (f_gen_connect, f_spike_times)


# =====
# OUTPUT
# =====
mm_param["label"] = 'thalamus'
mm1 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm1, (thalamus[0],))
logger.debug("%s - %d", mm_param["label"], thalamus[0])
mm_param["label"] = 'snc'
mm2 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm2, (snc[0],))
logger.debug("%s - %d", mm_param["label"], snc[0])

mm3 = nest.Create('multimeter', params=mm_param)
nest.Connect(mm3, (cortex[0],))
logger.debug("%s - %d", mm_param["label"], cortex[0])

# mm_param["label"] = 'thalamus_last'
# mm3 = nest.Create('multimeter', params=mm_param)
# nest.Connect(mm3, (thalamus[-1],))
# logger.debug("%s - %d", mm_param["label"], thalamus[-1])

# SPIKEDETECTOR
spikedetectors = nest.Create("spike_detector", 2, params=detector_param)
# Spike detector connects to thalamus neurons
nest.Connect(thalamus, (spikedetectors[0],))
nest.Connect(cortex, (spikedetectors[1],))

logger.debug("spike detecor is attached to thalamus: %d", (NN_thalamus))
nest.PrintNetwork()

nest.Simulate(T)

# =====
# Draw
# =====
f_name_gen = lambda name, is_image=False, with_folder=False: (sd_folder_name if with_folder else '') + \
                                                             (name + '_' if len(name) > 0 else '') + \
                                                             ('yes' if vt_flag else 'no') + '_dopa_generator_' + \
                                                             ('noise' if pg_flag else 'static') + \
                                                             ('.png' if is_image else '_')



pl.axis(axis)
nest.voltage_trace.from_device(mm1)

pl.savefig(f_name_gen('thalamus', True, True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

nest.voltage_trace.from_device(mm2)
pl.axis(axis)
pl.savefig(f_name_gen('snc', True, True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

nest.voltage_trace.from_device(mm3)
pl.axis(axis)
pl.savefig(f_name_gen('motorcortex', True, True), dpi=dpi_n, format='png')
# nest.voltage_trace.show()
pl.close()

nest.raster_plot.from_device((spikedetectors[0],), hist=True)
pl.savefig(f_name_gen('spikes_thalamus', is_image=True, with_folder=True), format='png')
# nest.raster_plot.show()
pl.close()

nest.raster_plot.from_device((spikedetectors[1],), hist=True)
pl.savefig(f_name_gen('spikes_motorcortex', is_image=True, with_folder=True), format='png')
# nest.raster_plot.show()
pl.close()

# nest.voltage_trace.from_device(mm3)
# pl.axis(axis)
# pl.savefig(f_name_gen('thalamus_lasts', True, True), dpi=dpi_n, format='png')
# # nest.voltage_trace.show()
# pl.close()

# new type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
