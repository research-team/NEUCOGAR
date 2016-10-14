import nest
import pylab
import nest.voltage_trace
import numpy

nest.ResetKernel()

path = "/Users/komarovvitaliy/GitHub/NEUCOGAR/CalculationNM/Results/"
dpi_n = 130

sysParams = ['synaptic_elements',
             'consistent_integration',
             'element_type',
             'local',
             # 'recordables',
             'thread_local_id',
             'thread',
             'frozen',
             'archiver_length',
             'global_id',
             'local_id',
             'available',
             'capacity',
             'instantiations',
             'needs_prelim_update',
             'model',
             'has_connections',
             'type_id',
             'vp',
             'elementsize']

allModels = ['aeif_cond_alpha',
             'aeif_cond_alpha_RK5',
             # 'aeif_cond_alpha_multisynapse', does not accept SpikeEvent
             'aeif_cond_exp',
             'amat2_psc_exp',
             # 'ginzburg_neuron',
             'hh_cond_exp_traub',
             'hh_psc_alpha',
             'hh_psc_alpha_gap',
             # 'ht_neuron',
             'iaf_chs_2007',
             'iaf_chxk_2008',
             'iaf_cond_alpha',
             # 'iaf_cond_alpha_mc',
             'iaf_cond_exp',
             'iaf_cond_exp_sfa_rr',
             'iaf_neuron',
             'iaf_psc_alpha',
             'iaf_psc_alpha_canon',
             # 'iaf_psc_alpha_multisynapse', does not accept SpikeEvent
             'iaf_psc_alpha_presc',
             'iaf_psc_delta',
             'iaf_psc_delta_canon',
             'iaf_psc_exp',
             # 'iaf_psc_exp_multisynapse', does not accept SpikeEvent
             'iaf_psc_exp_ps',
             'iaf_tum_2000',
             'izhikevich',
             'mat2_psc_exp',
             # 'mcculloch_pitts_neuron',
             # 'parrot_neuron',              does not have recordables
             # 'parrot_neuron_ps',           does not have recordables
             # 'pp_pop_psc_delta',           procces hangs on the inh neurons
             'pp_psc_delta']

for model in allModels:
    neuron = nest.Create(model)
    print "\n", model
    multimeter = nest.Create('multimeter', params={'withtime': True, 'interval': 0.1, 'record_from': ['V_m']})
    generator_ex = nest.Create("spike_generator", params={"spike_times": numpy.array([20.0, 50.0, 58.0]),
                                                          "spike_weights": numpy.array([400., 500., 500.])})
    generator_in = nest.Create("spike_generator", params={"spike_times": numpy.array([25.0, 30.0, 55.0]),
                                                          "spike_weights": numpy.array([-400., -500., -500.])})
    nest.Connect(multimeter, neuron)
    nest.Connect(generator_ex, neuron)
    nest.Connect(generator_in, neuron)

    nest.Simulate(100.)

    events = nest.GetStatus(multimeter)[0]['events']
    t = events['times']

    pylab.figure()
    pylab.subplot(111)
    pylab.title(model)
    pylab.plot(t, events['V_m'])
    pylab.ylabel('Membrane potential [mV]')
    pylab.draw()
    pylab.savefig(path + model + ".png", dpi=dpi_n, format='png')
    pylab.close()

    # nest.voltage_trace.from_device(multimeter)
    # nest.voltage_trace.show()
    nest.ResetKernel()

# Test block
'''
neuron = nest.Create('iaf_cond_alpha')
multimeter = nest.Create('multimeter', params = {'withtime': True, 'interval': 0.1, 'record_from':['V_m', 'g_ex', 'g_in']})
generator_ex = nest.Create("spike_generator", params = {"spike_times": numpy.array([20.0, 50.0, 58.0]),
                                                     "spike_weights": numpy.array([400., 500., 500.])})
generator_in = nest.Create("spike_generator", params={"spike_times": numpy.array([25.0, 30.0, 55.0]),
                                                   "spike_weights": numpy.array([-400., -500., -500.])})
nest.Connect(multimeter, neuron)
nest.Connect(generator_ex, neuron)
nest.Connect(generator_in, neuron)

nest.Simulate(100.)

events = nest.GetStatus(multimeter)[0]['events']
t = events['times']

pylab.subplot(211)
pylab.title('iaf_psc_alpha')
pylab.plot(t, events['V_m'])
pylab.ylabel('Membrane potential [mV]')
pylab.draw()
#pylab.savefig(path + "iaf_psc_alpha" + ".png", dpi=dpi_n, format='png')

pylab.subplot(212)
pylab.title('iaf_psc_alpha')
pylab.plot(t, events['g_ex'], t, events['g_in'])
pylab.xlabel("time (ms)")
pylab.ylabel('Synaptic conductance (nS)')
pylab.legend(("g_exc", "g_inh"))
pylab.draw()

#nest.voltage_trace.from_device(multimeter)
nest.voltage_trace.show()
'''

'''
neuron = nest.Create('aeif_cond_alpha')
multimeter = nest.Create('multimeter', params = {'withtime': True, 'interval': 0.1, 'record_from':['V_m', 'g_ex', 'g_in', 'w']})
generator_ex = nest.Create("spike_generator", params = {"spike_times": numpy.array([20.0, 50.0, 58.0]),
                                                     "spike_weights": numpy.array([400., 500., 500.])})
generator_in = nest.Create("spike_generator", params={"spike_times": numpy.array([25.0, 30.0, 55.0]),
                                                   "spike_weights": numpy.array([-400., -500., -500.])})
nest.Connect(multimeter, neuron)
nest.Connect(generator_ex, neuron)
nest.Connect(generator_in, neuron)

nest.Simulate(100.)

events = nest.GetStatus(multimeter)[0]['events']
t = events['times']

pylab.subplot(311)
pylab.title('aeif_cond_alpha')
pylab.plot(t, events['V_m'])
pylab.ylabel('Membrane potential [mV]')
pylab.draw()
#pylab.savefig(path + "iaf_psc_alpha" + ".png", dpi=dpi_n, format='png')

pylab.subplot(312)
pylab.plot(t, events['g_ex'], t, events['g_in'])
pylab.xlabel("time (ms)")
pylab.ylabel('Synaptic conductance (nS)')
pylab.legend(("g_exc", "g_inh"))
pylab.draw()

pylab.subplot(313)
pylab.plot(t, events['w'])
pylab.xlabel("time (ms)")
pylab.ylabel('Spike-adaptation (pA)')
pylab.draw()

nest.voltage_trace.show()
'''
