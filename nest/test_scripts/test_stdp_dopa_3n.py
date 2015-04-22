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
import pylab as pl

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

vt_flag = True
pg_flag = True

neuron_model = "iaf_psc_alpha"
#neuron_model = "iaf_psc_delta"
# neuron_model = "iaf_psc_exp"
#neuron_model = "iaf_cond_exp"
# neuron_model = "iaf_cond_alpha"
#neuron_model = "aeif_cond_alpha"
#neuron_model = "mat2_psc_exp"
#neuron_model = "hh_psc_alpha"
#neuron_model = "hh_cond_exp_traub"
dopa_neuron_model = "iaf_psc_alpha"

stdp_dopamine_synapse_weight = 35.

pg_ex = nest.Create("poisson_generator")
nest.SetStatus(pg_ex, {"rate": K_ex * nu_ex})

pg_in = nest.Create("poisson_generator")
nest.SetStatus(pg_in, {"rate": K_in * nu_in})

# Create spike generators and connect
sg_ex = nest.Create('spike_generator', params={'spike_times': np.array([10.0, 20.0, 50.0])})
sg_in = nest.Create('spike_generator', params={'spike_times': np.array([15.0, 25.0, 55.0])})

sd = nest.Create("spike_detector")
nest.SetStatus(sd, {"label": "spikes", "withtime": True, "withgid": True, "to_file": True})

mm = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m']})

neuron1 = nest.Create(neuron_model)
neuron2 = nest.Create(neuron_model)
dopa_neuron = nest.Create(dopa_neuron_model)

if neuron_model=="iaf_psc_alpha":
    nest.SetStatus(neuron1, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
    nest.SetStatus(neuron2, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
if neuron_model=="iaf_psc_delta":
    nest.SetStatus(neuron1, {"tau_minus": 20.0})
    nest.SetStatus(neuron2, {"tau_minus": 20.0})
if neuron_model=="iaf_psc_exp":
    nest.SetStatus(neuron1, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
    nest.SetStatus(neuron2, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})

vt = nest.Create("volume_transmitter")

if pg_flag:
    nest.Connect(pg_ex, neuron1, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, neuron2, syn_spec={'weight': w_ex, 'delay': delay})
    nest.Connect(pg_ex, dopa_neuron, syn_spec={'weight': w_ex, 'delay': delay})

    nest.Connect(pg_in, neuron1, syn_spec={'weight': w_in, 'delay': delay})
    nest.Connect(pg_in, neuron2, syn_spec={'weight': w_in, 'delay': delay})
    nest.Connect(pg_in, dopa_neuron, syn_spec={'weight': w_in, 'delay': delay})
else:
    # Simplify to get proper generations
    nest.Connect(sg_ex, neuron1, syn_spec={'weight': g_w_ex})
    nest.Connect(sg_ex, neuron2, syn_spec={'weight': g_w_ex})
    nest.Connect(sg_ex, dopa_neuron, syn_spec={'weight': g_w_ex})

    nest.Connect(sg_in, neuron1, syn_spec={'weight': g_w_in})
    nest.Connect(sg_in, neuron2, syn_spec={'weight': g_w_in})
    nest.Connect(sg_in, dopa_neuron, syn_spec={'weight': g_w_in})


nest.Connect(neuron1, sd)
nest.Connect(mm, neuron1)
#nest.Connect(neuron2, sd)
#nest.Connect(dopa_neuron, sd)

# Volume transmission
if vt_flag:
    # Turn on volume transmission
    nest.CopyModel("stdp_dopamine_synapse", "dopa", {"vt": vt[0], "weight": stdp_dopamine_synapse_weight, "delay": delay})
else:
    # Turn off volume transmission
    nest.CopyModel("static_synapse", "dopa", {"weight": stdp_dopamine_synapse_weight, "delay": delay})

nest.CopyModel("static_synapse", "static", {"delay": delay})

nest.Connect(dopa_neuron, vt, model="static")
nest.Connect(neuron1, neuron2, model="dopa")

if nest.GetStatus(neuron2)[0]['local']:
    filename = 'weight_dopa.gdf'
    fname = open(filename, 'w')
else:
    raise

weight_list = []
weight = None
for t in np.arange(0, T + dt, dt):
    if nest.GetStatus(neuron2)[0]['local']:
        weight = nest.GetStatus(nest.FindConnections(neuron1, synapse_model="dopa"))[0]['weight']
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

plot_weights(weight_list, "Neurons currents of 3 neurons " + neuron_model)

# obtain and display data
events = nest.GetStatus(mm)[0]['events']
t = events['times']

pl.subplot(111)
pl.plot(t, events['V_m'])
pl.ylabel('Membrane potential [mV]')

nest.raster_plot.from_device(sd)
nest.raster_plot.show()
