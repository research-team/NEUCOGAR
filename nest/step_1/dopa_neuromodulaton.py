# -*- coding: utf-8 -*-
__author__ = 'max'

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
from parameters import *
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

tan = nest.Create(tan_neurons_model, NN_tan)
striatum = {D1: nest.Create(striatum_neurons_model, NN_striatum[D1]),
            D2: nest.Create(striatum_neurons_model, NN_striatum[D2])}
gpe = nest.Create(gpe_neurons_model, NN_gpe)
gpi = nest.Create(gpi_neurons_model, NN_gpi)
stn = nest.Create(stn_neurons_model, NN_stn)
snr = nest.Create(snr_neurons_model, NN_snr)
thalamus = nest.Create(thalamus_neurons_model, NN_thalamus)
snc = nest.Create(snc_neurons_model, NN_snc)

nest.SetStatus(tan, tan_neuronparams)
nest.SetStatus(cortex, cortex_neuronparams)
(nest.SetStatus(striatum_part, striatum_neuronparams) for striatum_part in striatum.values())
nest.SetStatus(gpe, gpe_neuronparams)
nest.SetStatus(gpi, gpi_neuronparams)
nest.SetStatus(stn, stn_neuronparams)
nest.SetStatus(snr, snr_neuronparams)
nest.SetStatus(snc, snc_neuronparams)
nest.SetStatus(thalamus, thalamus_neuronparams)

# synapses model are same for test facilitation
# ToDo test direct indirect parameters
nest.CopyModel(bs_synapse_model, syn_excitory, {"weight": w_ex, "delay": delay_ex, "tau_plus": 20.0})
nest.CopyModel(bs_synapse_model, syn_inhibitory, {'weight': w_in, 'delay': delay_inh, "tau_plus": 20.0})

nest.Connect(cortex, striatum[D1], conn_spec=conn_dict, syn_spec=syn_excitory)
nest.Connect(cortex, striatum[D2], conn_spec=conn_dict, syn_spec=syn_excitory)
nest.Connect(tan, striatum[D1], conn_spec=conn_dict, syn_spec=syn_inhibitory)
nest.Connect(tan, striatum[D2], conn_spec=conn_dict, syn_spec=syn_excitory)
# ! Direct pathway: → Striatum (inhibits) [D1] → "SNr-GPi" complex (less inhibition of thalamus) →
nest.Connect(striatum[D1], snr, conn_dict, syn_inhibitory)
nest.Connect(striatum[D1], gpe, conn_dict, syn_inhibitory)
# ! Indirect pathwat: Striatum (inhibits) [D2] → GPe (less inhibition of STN) → STN (stimulates) → "SNr-GPi" complex (inhibits) →
nest.Connect(striatum[D2], gpe, conn_dict, syn_inhibitory)
nest.Connect(gpe, stn, conn_dict, syn_inhibitory)
nest.Connect(stn, snr, conn_dict, syn_excitory)
nest.Connect(stn, gpi, conn_dict, syn_excitory)
# ! Common path: SNr-GPi" complex (inhibits) → Thalamus (is stimulating less) → Cortex (is stimulating less) → Muscles, etc.
nest.Connect(gpi, thalamus, conn_dict, syn_inhibitory)
nest.Connect(snr, thalamus, conn_dict, syn_inhibitory)
nest.Connect(thalamus, cortex, conn_dict, syn_excitory)
# Volume transmission: init dopa_model
vt = nest.Create("volume_transmitter")
# Turn on volume transmission

# ==================
# Dopamine modulator
# ==================
nest.CopyModel("static_synapse", device_static_synapse,{'delay': delay})

if vt_flag:
    nest.CopyModel("stdp_dopamine_synapse", dopa_model_ex, {"vt": vt[0], "weight": stdp_dopamine_synapse_w_ex, "delay": vt_delay})
    nest.CopyModel("stdp_dopamine_synapse", dopa_model_in, {"vt": vt[0], "weight": stdp_dopamine_synapse_w_in, "delay": vt_delay})
else:
    nest.CopyModel("static_synapse", dopa_model_ex, {"weight": stdp_dopamine_synapse_w_ex, "delay": vt_delay})
    nest.CopyModel("static_synapse", dopa_model_in, {"weight": stdp_dopamine_synapse_w_in, "delay": vt_delay})
nest.Connect(snc, vt, model=device_static_synapse)

nest.Connect(snc, striatum[D1], conn_dict, dopa_model_ex)
nest.Connect(snc, striatum[D2], conn_dict, dopa_model_in)
nest.Connect(snc, tan, conn_dict, dopa_model_in)
# ===============
# Spike Generator
# ===============
if pg_flag:
    pg_ex = nest.Create("poisson_generator")
    nest.SetStatus(pg_ex, {"rate": K_ex * nu_ex})
    # pg_in = nest.Create("poisson_generator")
    # nest.SetStatus(pg_in, {"rate": K_in * nu_in})
    # nest.Connect(pg_in, ..., syn_spec={'weight': w_in, 'delay': delay})
    nest.Connect(pg_ex, tan, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, cortex, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, gpe, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, stn, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, snr, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, thalamus, syn_spec={'weight': w_ex,})
    nest.Connect(pg_ex, snc, syn_spec={'weight': w_ex, 'delay': delay})



else:
    spikes_times = np.arange(10, 100, 20.)
    f_spike_times = lambda sp_t, dt : np.array([t + dt for t in sp_t])
    snc_spikes_times = f_spike_times(spikes_times, 10)
    sg_cortex = nest.Create('spike_generator', params={'spike_times': spikes_times})
    sg_snc = nest.Create('spike_generator', params={'spike_times': snc_spikes_times})
    # Input #1 : 1) Cortex excitory
    dt = 5; ddt = 5
    nest.Connect(nest.Create('spike_generator', params={'spike_times': f_spike_times(spikes_times, -dt )}), tan, syn_spec={'weight': w_ex})
    nest.Connect(sg_cortex, cortex)

    nest.Connect(nest.Create('spike_generator', params={'spike_times': f_spike_times(spikes_times, dt )}), gpe,
                 syn_spec={'weight': g_w_ex})
    dt+=ddt
    nest.Connect(nest.Create('spike_generator', params={'spike_times': f_spike_times(spikes_times, dt)}), stn,
                 syn_spec={'weight': g_w_ex})
    dt+=ddt
    nest.Connect(nest.Create('spike_generator', params={'spike_times': f_spike_times(spikes_times, dt)}), snr,
                 syn_spec={'weight': g_w_ex})
    dt+=ddt
    nest.Connect(nest.Create('spike_generator', params={'spike_times': f_spike_times(spikes_times, dt)}), thalamus,
                 syn_spec={'weight': g_w_ex})
    nest.Connect(sg_snc, snc, syn_spec={'weight': g_w_ex})
# =============
# SPIKEDETECTOR
# =============
spikedetector = nest.Create("spike_detector",
                            params={"label": "spikes", "withtime": True, "withgid": True, "to_file": True})
nest.Connect(thalamus, spikedetector)
logger.debug("spike detecor is attached to cortex: %d", (NN_cortex))
# nest.PrintNetwork()
# ============
# MULTIMETER
# ============
mm = nest.Create('multimeter', params = {'withtime': True, 'withgid': True, 'interval': 0.1, 'record_from': ['V_m']})
nest.Connect(mm , (thalamus[0],))
mm2 = nest.Create('multimeter', params = {'withtime': True, 'withgid': True, 'interval': 0.1, 'record_from': ['V_m']})
# nest.Connect(mm2 , (thalamus[len(thalamus)-2],))
nest.Connect(mm2 , (snc[0],))

nest.Simulate(T)

# =====
# Draw
# =====
nest.raster_plot.from_device(spikedetector, hist=True)
nest.raster_plot.show()

nest.voltage_trace.from_device(mm)
nest.voltage_trace.show()

nest.voltage_trace.from_device(mm2)
nest.voltage_trace.show()

# another type of visual representation
# setattr(io,'HAVE_TABLEIO', False)
# data_file = signals.NestFile(sd_folder_name + sd_filename, with_time=True)
# # dims - dimension, it is 1 because there is no topology in connection.
# spikes = signals.load_spikelist(data_file, dims=1, id_list=list(cortex))
# spikes.raster_plot()  # read help spikes.raster_plot
# spikes.mean_rates()
