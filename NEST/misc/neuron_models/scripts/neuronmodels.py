import nest
import pylab
import numpy
import nest.raster_plot
import nest.voltage_trace

nest.ResetKernel()

path = "../results/"
dpi_n = 120
check = 'V_m'

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
    nest.SetDefaults('hh_cond_exp_traub', {
        'C_m': 134.0,
        't_ref': 2.,
        'V_m': -70.0,
        'E_L': -70.0,
        'E_K': -77.0,
        'g_Na': 12000.0,
        'g_K': 3600.0,
        'g_L': 30.0,
        'tau_syn_ex': 0.2,
        'tau_syn_in': 2.0
    })

    print(model)
    neuron = nest.Create(model)

    multimeter = nest.Create('multimeter', params=dict(withtime=True, interval=0.1, record_from=[check]))
    s_detector = nest.Create('spike_detector', params=dict(label=model, withgid=True, to_memory=True))
    s_generator = nest.Create("spike_generator", params=dict(spike_times=[20.,60.], spike_weights=[500., 300.]))

    nest.Connect(multimeter, neuron)
    nest.Connect(neuron, s_detector)
    nest.Connect(s_generator, neuron)

    nest.Simulate(100.)

    pylab.figure()
    pylab.subplot(111)
    spikes = nest.GetStatus(s_detector)[0]['events']['times']
    pylab.plot(spikes, [-70. for _ in spikes], ".", color='r')

    events = nest.GetStatus(multimeter)[0]['events']
    pylab.plot(events['times'], events[check], color='b')
    pylab.title(model)
    pylab.xlabel("Time (ms)")
    pylab.ylabel(check)
    pylab.draw()
    pylab.savefig(path + model + ".png", dpi=dpi_n, format='png')
    pylab.close()

    nest.ResetKernel()
