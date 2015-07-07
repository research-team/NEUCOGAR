__author__ = 'max'

import nest
import numpy as np
import pylab as pl
import nest.raster_plot
import nest.voltage_trace

# display recordables for illustration
print 'iaf_cond_alpha recordables: ', nest.GetDefaults('iaf_psc_exp')['recordables']

# create neuron and multimeter
n_exp = nest.Create('iaf_psc_exp', params={'tau_syn_ex': 1.0, 'V_reset': -70.0})
n_alpha = nest.Create('iaf_psc_alpha', params={'tau_syn_ex': 1.0, 'V_reset': -70.0})
n_delta = nest.Create('iaf_psc_delta')

m = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m']})
m_alpha = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m']})
m_delta = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m']})
sd = nest.Create("spike_detector")
nest.SetStatus(sd, {"label": "spikes", "withtime": True, "withgid": True, "to_file": False})

# Create spike generators and connect
gex = nest.Create('spike_generator', params={'spike_times': np.array([10.0, 20.0, 50.0])})
gin = nest.Create('spike_generator', params={'spike_times': np.array([15.0, 25.0, 55.0])})

nest.Connect(gex, n_exp, syn_spec={'weight': 40.0})  # excitatory
nest.Connect(gin, n_exp, syn_spec={'weight': -20.0})  # inhibitory
nest.Connect(gex, n_alpha, syn_spec={'weight': 40.0})  # excitatory
nest.Connect(gin, n_alpha, syn_spec={'weight': -20.0})  # inhibitory
nest.Connect(gex, n_delta, syn_spec={'weight': 40.0})  # excitatory
nest.Connect(gin, n_delta, syn_spec={'weight': -20.0})  # inhibitory

nest.Connect(m, n_exp)
nest.Connect(n_exp, sd)
nest.Connect(m_alpha, n_alpha)
nest.Connect(m_delta, n_delta)

# simulate
nest.Simulate(100)

# obtain and display data
events = nest.GetStatus(m)[0]['events']
t = events['times']
events_alpha = nest.GetStatus(m_alpha)[0]['events']
t_alpha = events['times']
events_delta = nest.GetStatus(m_delta)[0]['events']
t_delta = events['times']

pl.subplot(311)
pl.plot(t, events['V_m'])
# pl.axis([0, 100, -75, -53])
pl.ylabel('Membrane potential [mV]')

pl.subplot(312)
pl.plot(t_alpha, events_alpha['V_m'])
#pl.axis([0, 100, 0, 45])
pl.ylabel('Membrane potential [mV]')

pl.subplot(313)
pl.plot(t_delta, events_delta['V_m'])
#pl.axis([0, 100, 0, 45])
pl.ylabel('Membrane potential [mV]')

nest.voltage_trace.from_device(m)
nest.voltage_trace.show()

nest.raster_plot.from_device(sd)
nest.raster_plot.show()