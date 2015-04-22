# -*- coding: utf-8 -*-
__author__ = 'max'

# math and randomise package
import numpy as np
# neuron packages
# visualise spikes
# from NeuroTools import signals, io
# import matplotlib
# Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')
import nest.raster_plot
# local project parameters
from parameters_0 import *
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
nest.CopyModel(bs_synapse_model, syn_excitory ,    {"weight": w_ex, "delay": delay_ex})
nest.CopyModel(bs_synapse_model, syn_inhibitory, {'weight': w_inh, 'delay': delay_inh})

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
# Volume transmission: init dopa_model
vt = nest.Create("volume_transmitter")
# Turn on volume transmission
nest.CopyModel("stdp_dopamine_synapse", dopa_model,
               {"vt": vt[0]})  #, "weight": stdp_dopamine_synapse_weight, "delay": vt_delay})
nest.Connect(snc, striatum, conn_dict, dopa_model)



# ToDo pathway: check if it is working with inhibitory weights
# ! Direct pathway: Cortex (stimulates) → Striatum (inhibits) → "SNr-GPi" complex (less inhibition of thalamus) → Thalamus (stimulates) → Cortex (stimulates) → Muscles, etc.
# ! Indirect pathwat: Cortex (stimulates) → Striatum (inhibits) → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.


# =====
# INPUT
# =====
# 1)Spikes generators of the Cortex generate series of spikes that stimulates the Striatum.Dopamine neurons produce dopamine that modulates Striatum.

# ===============
# Spike Generator
# ===============
ex_spikes_times = np.array([10.0, 30.0, 45.0])  #[10.0, 20.0, 50.0])
snc_spikes_times = np.array([20.0, 40.0, 55.0])  #[15.0, 25.0, 55.0])
sg_ex = nest.Create('spike_generator', params={'spike_times': ex_spikes_times})
sg_snc = nest.Create('spike_generator', params={'spike_times': snc_spikes_times})

# generator's influence parameter
device_static_synapse = "excitatory_static"
nest.CopyModel("static_synapse", device_static_synapse, {"weight": 3.})

# Input #1 : 1) Cortex excitory
nest.Connect(sg_ex, cortex)
# Input #2 : 2) Dopamine neurons produce dopamine that modulates Striatum.
if vt_flag: nest.Connect(sg_snc, snc, syn_spec=device_static_synapse)

# =====
# OUTPUT
# =====
# SPIKEDETECTOR
spikedetector = nest.Create("spike_detector",
                            params={"label": "spikes", "withtime": True, "withgid": True, "to_file": True})
# Spike detector connects to thalamus neurons
nest.Connect(thalamus, spikedetector)
logger.debug("spike detecor is attached to cortex: %d", (NN_cortex))
# nest.PrintNetwork()

nest.Simulate(T)

# =====
# Draw
# =====
nest.raster_plot.from_device(spikedetector, hist=True)
nest.raster_plot.show()

# new type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
