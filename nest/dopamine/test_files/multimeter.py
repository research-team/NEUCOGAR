__author__ = 'max'

import nest
import numpy as np
import pylab as pl
import nest.raster_plot

neuron_model = "iaf_psc_alpha"
neuron_model = "iaf_psc_delta"
neuron_model = "iaf_psc_exp"
#neuron_model = "iaf_cond_exp" -
#neuron_model = "iaf_cond_alpha" -
#neuron_model = "aeif_cond_alpha" -
#neuron_model = "mat2_psc_exp"
#neuron_model = "hh_psc_alpha" -
#neuron_model = "hh_cond_exp_traub" -

#spike detector
sd = nest.Create("spike_detector")
nest.SetStatus(sd, {"label": "spikes", "withtime": True, "withgid": True, "to_file": False})

# display recordables for illustration
print neuron_model, ' recordables: ', nest.GetDefaults(neuron_model)['recordables']

# create neuron and multimeter
if neuron_model == "iaf_psc_alpha" or neuron_model == "iaf_psc_exp":
    n = nest.Create(neuron_model, params={'tau_syn_ex': 1.0, 'V_reset': -70.0})
elif neuron_model == "iaf_psc_delta":
    n = nest.Create(neuron_model, params={'V_reset': -70.0})
else:
    n = nest.Create(neuron_model, params={'tau_syn_ex': 1.0})

m = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m']})

if neuron_model=="iaf_psc_alpha" or neuron_model=="iaf_psc_exp":
    m = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m', 'input_currents_ex', 'input_currents_in', "weighted_spikes_in", "weighted_spikes_ex"]})
elif neuron_model == "mat2_psc_exp":
    m = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m', 'V_th']})

# Create spike generators and connect
gex = nest.Create('spike_generator', params={'spike_times': np.array(np.arange(10.0, 25.0, 0.1))})
gin = nest.Create('spike_generator', params={'spike_times': np.array([15.0, 25.0, 55.0])})

nest.Connect(gex, n, syn_spec={'weight':  40.0}) # excitatory
nest.Connect(gin, n, syn_spec={'weight': -20.0}) # inhibitory
nest.Connect(m, n)
nest.Connect(n, sd)

# simulate
nest.Simulate(100)

# obtain and display data
events = nest.GetStatus(m)[0]['events']
t = events['times']

if neuron_model == "iaf_psc_alpha" or neuron_model == "iaf_psc_exp":
    pl.subplot(311)
    pl.plot(t, events['V_m'])
    pl.ylabel('Membrane potential [mV]')

    pl.subplot(312)
    pl.plot(t, events['input_currents_ex'], t, events['input_currents_in'])
    pl.xlabel('Time [ms]')
    pl.ylabel('Currents [pA]')
    pl.legend(('input_currents_ex', 'input_currents_in'))

    pl.subplot(313)
    pl.plot(t, events['weighted_spikes_ex'], t, events['weighted_spikes_in'])
    pl.xlabel('Time [ms]')
    pl.ylabel('Weighted Spikes')
    pl.legend(('weighted_spikes_ex', 'weighted_spikes_in'))

elif neuron_model == "mat2_psc_exp":
    pl.subplot(211)
    pl.plot(t, events['V_m'])
    pl.ylabel('Membrane potential [mV]')

    pl.subplot(212)
    pl.plot(t, events['V_th'])
    pl.xlabel('Time [ms]')
    pl.ylabel('Membrane potential V_th [mV]')

else:
    pl.subplot(111)
    pl.plot(t, events['V_m'])
    pl.ylabel('Membrane potential [mV]')

nest.raster_plot.from_device(sd)
nest.raster_plot.show()
