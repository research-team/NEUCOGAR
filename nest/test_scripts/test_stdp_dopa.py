# -*- coding: utf-8 -*-
#
# test_stdp_dopa.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

# Begin Documentation
# Name: testsuite::test_stdp_dopa - script to test stdp_dopamine_synapse model implementing dopamine-dependent spike-timing dependent plasticity as defined in [1], based on [2].
# Two neurons, which fire poisson like, are connected by a stdp_dopamine_synapse. Dopamine is release by a third neuron, which also fires poisson like.
#
# author: Wiebke Potjans
# date: October 2010

import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np
import nest
import nest.raster_plot
import nest.voltage_trace


def plot_weights(weights_list, title="Neurons weights progress", y_lim = None):

    # Plot
    # Make a list of colors cycling through the rgbcmyk series.
    colors = [colorConverter.to_rgba(c) for c in ('k', 'r', 'g', 'b', 'c', 'y', 'm')]

    axes = plt.axes()
    ax4 = axes # unpack the axes

    ncurves = 1
    offs = (0.0, 0.0)

    segs = []
    for i in range(ncurves):
        curve = weights_list
        segs.append(curve)

    col = collections.LineCollection(segs, offsets=offs)
    ax4.add_collection(col, autolim=True)
    col.set_color(colors)
    ax4.autoscale_view()
    ax4.set_title(title)
    ax4.set_xlabel('Time ms')
    ax4.set_ylabel('Weight pA')
    if y_lim :
        ax4.set_ylim(0, y_lim)

    plt.show()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True}) # set to True to permit overwriting

delay = 1.     # the delay in ms

w_ex = 45.
g = 3.83
w_in = -w_ex * g

K = 10000
f_ex = 1.
K_ex = f_ex * K
K_in = (1.0 - f_ex) * K

nu_ex = 10.0#2.
nu_in = 10.0#2.

T = 1000.0
dt = 10.0
vt_flag = True

number_of_neurons = 2
neurons1 = []
neurons2 = []

#stdp_dopamine_synapse_weight = 66.3485433
stdp_dopamine_synapse_weight = 35.

# Setup nest: create Poisson generator, spike detector and volume transmitter
pg_ex = nest.Create("poisson_generator")
nest.SetStatus(pg_ex, {"rate": K_ex * nu_ex})

pgs_ex = nest.Create("poisson_generator", number_of_neurons)
nest.SetStatus(pgs_ex, {"rate": K_ex * nu_ex})

pg_in = nest.Create("poisson_generator")
nest.SetStatus(pg_in, {"rate": K_in * nu_in})

pgs_in = nest.Create("poisson_generator", number_of_neurons)
nest.SetStatus(pgs_in, {"rate": K_in * nu_in})


sd = nest.Create("spike_detector")
nest.SetStatus(sd,  {"label": "spikes", "withtime": True, "withgid": True, "to_file": True})

mm = nest.Create('multimeter', params = {'withtime': True, 'withgid': True, 'interval': 0.1, 'record_from': ['V_m', 'a_ex', 'a_in']})

vt = nest.Create("volume_transmitter")

# Neurogenesis
dopa_neuron = nest.Create("iaf_psc_alpha")

neurons1 = nest.Create('iaf_psc_alpha', number_of_neurons)
neurons2 = nest.Create('iaf_psc_alpha', number_of_neurons)
nest.SetStatus(neurons1, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
nest.SetStatus(neurons2, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})

neuron1 = nest.Create("iaf_psc_alpha")
neuron2 = nest.Create("iaf_psc_alpha")
nest.SetStatus(neuron1, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
nest.SetStatus(neuron2, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})


# Connect neurons with poisson generators and spike detectors
nest.Connect(dopa_neuron, sd)

nest.ConvergentConnect(neurons1, sd)
nest.ConvergentConnect(neuron1, mm)

nest.ConvergentConnect(neurons2, sd)
nest.ConvergentConnect(neuron2, mm)

#nest.Connect(neuron1, sd)
#nest.Connect(neuron2, sd)

nest.Connect(pg_ex, neuron1, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_ex, neuron2, syn_spec={'weight': w_ex, 'delay': delay})

nest.Connect(pgs_ex, neurons1, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pgs_ex, neurons2, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_ex, dopa_neuron, syn_spec={'weight': w_ex, 'delay': delay})

nest.Connect(pg_in, neuron1, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_in, neuron2, syn_spec={'weight': w_ex, 'delay': delay})

nest.Connect(pgs_in, neurons1, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pgs_in, neurons2, syn_spec={'weight': w_ex, 'delay': delay})
nest.Connect(pg_in, dopa_neuron, syn_spec={'weight': w_in, 'delay': delay})

# Volume transmission
if vt_flag :
    # Turn on volume transmission
    nest.CopyModel("stdp_dopamine_synapse", "dopa", {"vt": vt[0], "weight": stdp_dopamine_synapse_weight, "delay": delay})
else:
    # Turn off volume transmission
    nest.CopyModel("static_synapse", "dopa", {"weight": stdp_dopamine_synapse_weight, "delay": delay})

nest.CopyModel("static_synapse", "static", {"delay": delay})

nest.Connect(dopa_neuron, vt, syn_spec="static")
nest.Connect(neuron1, neuron2, syn_spec="dopa")
nest.Connect(neurons1, neurons2, syn_spec="dopa")

if nest.GetStatus(neuron2)[0]['local']:
    filename = 'weight_dopa.gdf'
    fname = open(filename, 'w')
else:
    raise

# Simulation
weight = None
weight_list = [(0, 1)]
weights_list = [[(0, 1)]]
i = 0
weights_list.append([(0, 1)])
for t in np.arange(0, T + dt, dt):
    if nest.GetStatus(neuron2)[0]['local']:

        weight = nest.GetStatus(nest.GetConnections(neuron1, synapse_model="dopa"))[0]['weight']
        print(weight)
        weight_list.append((t, weight))
        weightstr = str(weight)
        timestr = str(t)
        data = timestr + ' ' + weightstr + '\n'
        fname.write(data)

        nest.Simulate(dt)

if nest.GetStatus(neuron2)[0]['local']:
    print("expected weight at T=1000 ms: 28.6125 pA")
    print("weight at last event: " + str(weight) + " pA")
    fname.close()

nest.raster_plot.from_device(sd)
nest.raster_plot.show()


nest.voltage_trace.from_device(mm)
nest.voltage_trace.show()


plot_weights(weight_list, "Neurons weights progress neuron 1")
plot_weights(weights_list[0], "Neurons weights progress neuron 0")
#plot_weights(weight_list_neurons[number_of_neurons/2], "Neurons weights progress neuron " + str(number_of_neurons/2))
#plot_weights(weight_list_neurons2, "Neurons weights progress neuron " + str(number_of_neurons-1))

print "Simulation of %.0f milliseconds" % T
print "Volume transmission is on = ", vt_flag
print "number of spikes = %.4f " % nest.GetStatus(sd, "n_events")[0]

'''
Simulation of 100000.0000 milliseconds
Volume transmission is on =  False
number of spikes = 12976.0000
'''
'''
Simulation of 100000.0000 milliseconds
Volume transmission is on =  True
number of spikes = 12977.0000
'''

'''
Simulation of 1000000 milliseconds
Volume transmission is on =  False
number of spikes = 130565.0000
'''
'''
Simulation of 1000000 milliseconds
Volume transmission is on =  True
number of spikes = 130557.0000
'''
'''
expected weight at T=1000 ms: 28.6125 pA
weight at last event: 0.0 pA
Simulation of 1000000 milliseconds
Volume transmission is on =  True
number of spikes = 170041.0000

expected weight at T=1000 ms: 28.6125 pA
weight at last event: 35.0 pA
Simulation of 1000000 milliseconds
Volume transmission is on =  False
number of spikes = 170104.0000
'''
'''
Simulation of 1000000 milliseconds
Volume transmission is on =  True
number of spikes = 170432.0000

Simulation of 1000000 milliseconds
Volume transmission is on =  False
number of spikes = 170757.0000
'''
#nest.raster_plot.from_device(sd)
#nest.raster_plot.show()

