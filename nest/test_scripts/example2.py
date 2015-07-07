import nest
import nest.raster_plot
import numpy as np

J_ex = 1.3  # excitatory weight

neuron_params = {'E_L': 0., 'V_th': 30., 'V_reset': 13.5, 'C_m': 0.01}

# Set parameters of neurons and devices
nest.SetDefaults("iaf_psc_exp", neuron_params)

# p_rate = 20000.  # external Poisson rate
# nest.SetDefaults("poisson_generator", {"rate": p_rate})
# noise = nest.Create("poisson_generator")
# Configure synapse models
nest.CopyModel("static_synapse", "excitatory", {"weight": J_ex, "delay": 1.5})


# Create neurons and devices

nodes_ex_1 = nest.Create("iaf_psc_alpha", 10)
nodes_ex_2 = nest.Create("iaf_psc_exp", 10)


# Volume transmission
stdp_dopamine_synapse_weight = 35.
vt_delay = 1.
vt_flag = True
dopa_model = "dopa_model"
if vt_flag:
    # ToDO observe the point of neuromodulation
    vt = nest.Create("volume_transmitter")
    # Turn on volume transmission
    nest.CopyModel("stdp_dopamine_synapse", dopa_model, {"vt": vt[0], "weight": stdp_dopamine_synapse_weight, "delay": vt_delay})
else:
    # Turn off volume transmission
    nest.CopyModel("stdp_synapse", dopa_model, {"weight": stdp_dopamine_synapse_weight, "delay": vt_delay})
nest.Connect(nodes_ex_1, nodes_ex_2, syn_spec=dopa_model)
# nest.Connect(nodes_ex_1, nodes_ex_2)


nest.SetDefaults("spike_detector", {"withtime": True, "withgid": True})
spikedetector = nest.Create("spike_detector")

ex_spikes_times = np.array([1., 10., 50.])
sg_ex = nest.Create('spike_generator', params={'spike_times': ex_spikes_times})
# nest.Connect(noise,nodes_ex,model="excitatory")
nest.SetDefaults("static_synapse", { 'weight': 1.})
nest.Connect(sg_ex, nodes_ex_1,model= "static_synapse")

nest.Connect(nodes_ex_2, spikedetector)
# nest.RandomConvergentConnect(nodes_ex, nodes_ex, 1000, model="excitatory")


# Simulate for 100. ms
nest.Simulate(100.)

# Plot results
nest.raster_plot.from_device(spikedetector, hist=True)
nest.raster_plot.show()