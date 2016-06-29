import nest
import pylab
import matplotlib.pyplot as plt
import nest.raster_plot
import numpy

'''
V_m - membrane potential
spike_duration - duration of re-polarizing potassium current
Tau_m - membrane time constant applying to all currents but repolarizing K-current
(see [1 p 1677])
Tau_spike - membrane time constant applying to repolarizing K-current
'''

nest.ResetKernel()

w_recep = {'AMPA': 500., 'NMDA': 50.}
neuron = nest.Create('ht_neuron', params={'V_m': -70.,'spike_duration': 1.5, 'Tau_m': 1.0, 'Tau_spike': 1.0})

p_gens = nest.Create('spike_generator', params={'spike_times': numpy.array([15.0])})
mm = nest.Create('multimeter', params={'interval': 0.1, 'record_from': ['V_m']})

receptors = nest.GetDefaults('ht_neuron')['receptor_types']

sd = nest.Create("spike_detector")

for pg, (rec_name, rec_wgt) in zip(p_gens, w_recep.items()):
    nest.Connect([pg], neuron, syn_spec={'receptor_type': receptors[rec_name],
                                      'weight': rec_wgt})

nest.Connect(mm, neuron)
nest.Connect(neuron, sd)

nest.Simulate(50.)

events = nest.GetStatus(mm)[0]['events']
time = events['times']

pylab.subplot(111)
pylab.title('ht_neuron')
pylab.plot(time, events['V_m'])
pylab.ylabel('Membrane potential [mV]')
pylab.draw()

nest.raster_plot.from_device(sd)
nest.raster_plot.show()
nest.ResetKernel()
