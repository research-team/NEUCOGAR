# -*- coding: utf-8 -*-
__author__ = 'max'

import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np
import nest
import nest.raster_plot
import nest.voltage_trace
import pylab as pl

from parameters import *

'''
This is the implementation of experiment of dopamine neuromodulation based on
https://github.com/research-team/NEUCOGAR/blob/master/experiment_description.md#general-neuromodulation
and
test_stdp_dopa
see explanation of neuronal model:
http://www.nest-initiative.org/Network_burst_generation_by_short-term_plasticity

Prefix description:
	ex_  -  excitory
	inh_ - inhibitory
	d_   - Direct 
	ind_ - indirect

'''

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True})  # set to True to permit overwriting

ex_spikes_times = np.array([10.0, 20.0, 50.0])
in_spikes_times = np.array([15.0, 25.0, 55.0])
# Create spike generators and detectors
sg_ex = nest.Create('spike_generator', params={'spike_times': ex_spikes_times})
sg_in = nest.Create('spike_generator', params={'spike_times': in_spikes_times})

sd = nest.Create("spike_detector")
nest.SetStatus(sd, {"label": "spikes", "withtime": True, "withgid": True, "to_file": True})
# ! ===========
#! Creating BS
#! ===========
# neuron set
cortex = nest.Create(cortex_neurons_model, cortex_number_of_neurons)
striatum = nest.Create(striatum_neurons_model, striatum_number_of_neurons)
gpe = nest.Create(gpe_neurons_model, gpe_number_of_neurons)
gpi = nest.Create(gpi_neurons_model, gpi_number_of_neurons)
stn = nest.Create(stn_neurons_model, stn_number_of_neurons)
snr = nest.Create(snr_neurons_model, snr_number_of_neurons)
snc = nest.Create(snc_neurons_model, snc_number_of_neurons)
thalamus = nest.Create(thalamus_neurons_model, thalamus_number_of_neurons)

nest.SetStatus(cortex, cortex_neuronparams)
nest.SetStatus(striatum, striatum_neuronparams)
nest.SetStatus(gpe, gpe_neuronparams)
nest.SetStatus(gpi, gpi_neuronparams)
nest.SetStatus(stn, stn_neuronparams)
nest.SetStatus(snr, snr_neuronparams)
nest.SetStatus(snc, snc_neuronparams)
nest.SetStatus(thalamus, thalamus_neuronparams)

# synapses model are same for test facilitation
# ToDo: moqup the connections and write the code
conn_cortex_striatum = nest.Connect(cortex, striatum, conn_dict, syn_dict_ex)
conn_striatum_gpe = nest.Connect(striatum, gpe, conn_dict, syn_dict_inh)
conn_striatum_snr = nest.Connect(striatum, snr, conn_dict, syn_dict_inh)
conn_gpe_stn = nest.Connect(gpe, stn, conn_dict, syn_dict_inh)
conn_stn_snr = nest.Connect(stn, snr, conn_dict, syn_dict_ex)
conn_stn_gpi = nest.Connect(stn, gpi, conn_dict, syn_dict_ex)
conn_gpi_thalamus = nest.Connect(gpi, thalamus, conn_dict, syn_dict_inh)
conn_snr_thalamus = nest.Connect(snr, thalamus, conn_dict, syn_dict_inh)
conn_thalamus_cortex = nest.Connect(thalamus, cortex, conn_dict, syn_dict_dop)

# neuromodulation :ToDo
conn_snc_striatum = nest.Connect(snc, striatum, conn_dict, )

# ToDo: refactor: create dictionary of connections instead of separated variables with prefix conn_

# ToDo insert spike detector

#! Direct pathway: Cortex (stimulates) → Striatum (inhibits) → "SNr-GPi" complex (less inhibition of thalamus) → Thalamus (stimulates) → Cortex (stimulates) → Muscles, etc.


#! Indirect pathwat: Cortex (stimulates) → Striatum (inhibits) → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.



# =====
# INPUT
# =====
# 1)Spikes generators of the Cortex generate series of spikes that stimulates the Striatum.Dopamine neurons produce dopamine that modulates Striatum.
# 2) Dopamine neurons produce dopamine that modulates Striatum.

#ToDo: input


# ToDo: insert snc as input with neuromodulation
# Volume transmission
vt = nest.Create("volume_transmitter")
nest.CopyModel("stdp_dopamine_synapse", "dopa",
               {"vt": vt[0], "weight": stdp_dopamine_synapse_weight, "delay": vt_delay})






