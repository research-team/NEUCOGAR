import nest
import pylab
import matplotlib.pyplot as plt
import nest.voltage_trace
import numpy

nest.ResetKernel()

w_recep = {'AMPA': 18.}
neuron = nest.Create('ht_neuron')

p_gens = nest.Create('spike_generator', params={'spike_times': numpy.array(3.0)})
mm = nest.Create('multimeter',
                 params={'interval': 0.1,
                         'record_from': ['V_m']})

receptors = nest.GetDefaults('ht_neuron')['receptor_types']

for pg, (rec_name, rec_wgt) in zip(p_gens, w_recep.items()):
    nest.Connect([pg], neuron, syn_spec={'receptor_type': receptors[rec_name],
                                      'weight': rec_wgt})

#nest.Connect(p_gens, neuron)
nest.Connect(mm, neuron)


nest.Simulate(20.)

events = nest.GetStatus(mm)[0]['events']
time = events['times']

pylab.subplot(111)
pylab.title('ht_neuron')
pylab.plot(time, events['V_m'])
pylab.ylabel('Membrane potential [mV]')
pylab.draw()

nest.voltage_trace.show()
nest.ResetKernel()
