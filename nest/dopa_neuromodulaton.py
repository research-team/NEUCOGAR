__author__ = 'max'

import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np
import nest
import nest.raster_plot
import nest.voltage_trace
import pylab as pl
'''
This is the implementation of experiment of dopamine neuromodulation based on
https://github.com/research-team/NEUCOGAR/blob/master/experiment_description.md#general-neuromodulation
and
test_stdp_dopa
see explanation of neuronal model:
http://www.nest-initiative.org/Network_burst_generation_by_short-term_plasticity
It contains:

    Cortex
    Striatum
    GPe: globus pallidus external
    GPi: globus pallidus internal
    STN: subthalamic nucleus
    SNc: substantia nigra compacta
    SNr: substantia nigra reticulata

'''

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True})# set to True to permit overwriting

cortex_neurons_model = striatum_neurons_model = gpe_neurons_model = gpi_neurons_model = stn_neurons_model = snc_neurons_model = snr_neurons_model = 'iaf_psc_exp'

cortex_number_of_neurons = 100
striatum_number_of_neurons = gpe_number_of_neurons = gpi_number_of_neurons = stn_number_of_neurons = snc_number_of_neurons = snr_number_of_neurons = 10

ex_spikes_times = np.array([10.0, 20.0, 50.0])
in_spikes_times = np.array([15.0, 25.0, 55.0])

w_ex = 45.
g = 3.83
w_in = -w_ex * g

g_w_ex =  40.
g_w_in = -20.

K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_in = (1.0 - f_ex) * K

nu_ex = 10.0#2.
nu_in = 10.0#2.

T = 300.0
dt = 10.0

stdp_dopamine_synapse_weight = 35.
vt_delay = 1.

# Create spike generators and detectors
sg_ex = nest.Create('spike_generator', params={'spike_times': ex_spikes_times})
sg_in = nest.Create('spike_generator', params={'spike_times': in_spikes_times})

sd = nest.Create("spike_detector")
nest.SetStatus(sd, {"label": "spikes", "withtime": True, "withgid": True, "to_file": True})

# Creating brain
cortex = nest.Create(cortex_neurons_model, cortex_number_of_neurons)
striatum = nest.Create(striatum_neurons_model, striatum_number_of_neurons)
gpe = nest.Create(gpe_neurons_model, gpe_number_of_neurons)
gpi = nest.Create(gpi_neurons_model, gpi_number_of_neurons)
stn = nest.Create(stn_neurons_model, stn_number_of_neurons)
snr = nest.Create(snr_neurons_model, snr_number_of_neurons)
snc = nest.Create(snc_neurons_model, snc_number_of_neurons)

# Volume transmission
vt = nest.Create("volume_transmitter")
nest.CopyModel("stdp_dopamine_synapse", "dopa", {"vt": vt[0], "weight": stdp_dopamine_synapse_weight, "delay": vt_delay})






