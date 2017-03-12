import numpy as np
import random
import nest
import nest.voltage_trace as plot
import nest.raster_plot
import matplotlib.pyplot as plt
import pylab as pl

nest.ResetKernel()
nest.SetKernelStatus(
    {'overwrite_files': True })  # set to True to permit overwriting

delay = 1.  # the delay in ms

w_ex = 45.
g = 3.83
w_in = -w_ex * g

K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_in = (1.0 - f_ex) * K

nu_ex = 10.0  # 2.
nu_in = 10.0  # 2.

pg_ex = nest.Create("poisson_generator")
nest.SetStatus(pg_ex, {"rate": K_ex * nu_ex})

pg_in = nest.Create("poisson_generator")
nest.SetStatus(pg_ex, {"rate": K_in * nu_in})

sd = nest.Create("spike_detector")
nest.SetStatus(sd, {
	"label": "spikes",
	"withtime": True,
	"withgid": True,
	"to_file": True,
	})

neuron1 = nest.Create("hh_psc_alpha")
neuron2 = nest.Create("hh_psc_alpha")
nora_neuron = nest.Create("hh_psc_alpha")
nest.SetStatus(neuron1,
	{"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
nest.SetStatus(neuron2,
	{"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})

vt = nest.Create("volume_transmitter")

nest.Connect(pg_ex, neuron1, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_ex, neuron2, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_ex, nora_neuron, syn_spec={'weight': w_ex, 'delay': delay})

nest.Connect(pg_in, neuron1, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_in, neuron2, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_in, nora_neuron, syn_spec={'weight': w_ex, 'delay': delay})

nest.Connect(neuron1, sd)
nest.Connect(neuron2, sd)
nest.Connect(nora_neuron, sd)

nest.CopyModel("stdp_noradrenaline_synapse", "nora",
	{"vt": vt[0], "weight": 35.,"n": .1, "delay": delay})
nest.CopyModel("static_synapse", "static", {"delay": delay})

nest.Connect(nora_neuron, vt, model="static")
nest.Connect(neuron1, neuron2, model="nora")

# Init and connect voltmeter to see membrane potential of serotonin neuron
voltmeter = nest.Create('voltmeter', 1, {'withgid': True})
nest.Connect(voltmeter, nora_neuron)

dt = 10
T = 150
weight = None
time = []
nora_dyn = []
results_folder = ""

if nest.GetStatus(neuron2)[0]['local']:
	sum_time = 0
	for t in range(0, T +dt , dt):
		nest.Simulate(t)
		sum_time+=t
		conns = nest.GetConnections(neuron1, synapse_model="nora")
		n = nest.GetStatus(conns)[0]['n']
		time.append(sum_time)
		nora_dyn.append(n)


	nest.raster_plot.from_device(sd, hist=True, hist_binwidth=100.)
	pl.savefig(results_folder + "spikes_" + str(t) + ".png")
	pl.close()
	plot.from_device(voltmeter, timeunit="s")
	pl.savefig(results_folder + "voltage_" + str(t) + ".png")
	pl.close()

	plt.plot(time, nora_dyn)
	plt.xlabel('Time (ms)')
	plt.title('Noradreline concentration dynamics')
	plt.savefig( results_folder + "nora_dynamic_" + str(t) + ".png")
