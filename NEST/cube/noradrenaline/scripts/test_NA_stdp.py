import nest
import numpy
import pylab as plt
import nest.raster_plot
import nest.voltage_trace


def createFig(title, num):
    figure = fig.add_subplot(num)
    figure.set_title(title)
    figure.set_ylabel("")
    return figure


def plotSpikes(device):
    events = nest.GetStatus(device)[0]['events']
    times = events['times']
    plt.plot(times, [-56 for _ in times], ".", color='r')


def plotVoltage(device):
    events = nest.GetStatus(device)[0]['events']
    times = events['times']
    volt = events['V_m']
    plt.plot(times, volt)


if __name__ == '__main__':
    # Parameters
    simTime = 150.

    # Kernel
    nest.ResetKernel()
    nest.SetKernelStatus({'print_time': True})

    # Create neurons
    neurons = nest.Create("iaf_psc_alpha", 3, params=dict(
        I_e= 0.0,           # Constant input current in pA. (R=1)
        E_L=-72.,           # Resting membrane potential in mV
        V_th=-55.,          # Spike threshold in mV
        V_reset=-80.,       # Reset membrane potential after a spike in mV
        C_m=25.,            # Capacity of the membrane in pF
        t_ref=2.,           # Duration of refractory period (V_m = V_reset) in ms
        V_m=-72.,           # Membrane potential in mV at start
        tau_syn_ex=1.,      # Time constant of postsynaptic excitatory currents in ms
        tau_syn_in=1.33,    # Time constant of postsynaptic inhibitory currents in ms
        V_min= -85.0,       # Absolute lower value for the membrane potential.
    ))
    pre_neuron= (neurons[0],)
    post_neuron = (neurons[1],)
    NA_neuron = (neurons[2],)

    # Create multimeters
    multimeters = nest.Create("multimeter", 3, params={"interval": 0.1,
                                        "record_from": ["V_m"], "to_file": False})
    m_pre = (multimeters[0],)
    m_post = (multimeters[1],)
    m_NA = (multimeters[2],)

    # Create detectors
    detectors = nest.Create('spike_detector', 3, params={
                  'withtime': True,
                  'to_memory': True,
                  'scientific': True})
    d_pre = (detectors[0],)
    d_post = (detectors[1],)
    d_NA = (detectors[2],)

    # Create generators
    gen_pre = nest.Create("poisson_generator", 1, dict(rate=2700.))
    gen_NA = nest.Create("poisson_generator", 1, dict(rate=2700.))

    # Init synapses and VT
    vt = nest.Create('volume_transmitter')
    nest.SetDefaults('stdp_noradrenaline_synapse', dict(vt=vt[0]))
    nest.SetDefaults('static_synapse', {'weight': 500.})

    # Connect neruons
    nest.Connect(NA_neuron, vt, model="static_synapse")
    nest.Connect(pre_neuron, post_neuron, syn_spec = dict(model='stdp_noradrenaline_synapse',
                                                      weight=500.))
    # Connect generators
    nest.Connect(gen_pre, pre_neuron, syn_spec={'weight': 1000.0})
    nest.Connect(gen_NA, NA_neuron, syn_spec={'weight': 550.0})

    # Connect multimeters
    nest.Connect(m_pre, pre_neuron)
    nest.Connect(m_post, post_neuron)
    nest.Connect(m_NA, NA_neuron)

    # Connect detectors
    nest.Connect(pre_neuron, d_pre)
    nest.Connect(post_neuron, d_post)
    nest.Connect(NA_neuron, d_NA)

    # Simulate with t steps and save WEIGTH result to dict
    x, y = [], []
    for t in xrange(0, int(simTime)):
        nest.Simulate(1.0)
        x.append(t)
        y.append(nest.GetStatus(nest.GetConnections(pre_neuron, post_neuron), keys='weight')[0])

    # Plot figure
    fig = plt.figure()
    #====== PRE=======
    a=createFig('PRE', 322)
    plotSpikes(d_pre)
    plotVoltage(m_pre)
    #=========POST===========
    a=createFig('POST', 324)
    plotSpikes(d_post)
    plotVoltage(m_post)
    #=========NA===========
    a=createFig('NA', 326)
    plotSpikes(d_NA)
    plotVoltage(m_NA)
    #========WEIGHT=========
    a=createFig('Weight', 121)
    plt.plot(x, y)
    plt.show()