import nest
import nest.voltage_trace
import nest.raster_plot
import pylab as pl

nest.ResetKernel()

nest.SetKernelStatus({'local_num_threads': 4,
                      'resolution': 0.01})

lol = {'C_m': 1.5}
nest.SetDefaults("hh_psc_alpha", lol)
neuron = nest.Create("hh_psc_alpha")

noise = nest.Create("poisson_generator")
nest.SetStatus(noise, {'start': 10., 'stop': 40., 'rate': 1000.})

mm = nest.Create("multimeter")
det = nest.Create("spike_detector")

nest.SetStatus(mm, {"withgid": True, "withtime": True, 'record_from': ['V_m', 'Act_m', 'Inact_n', 'Act_h'], 'interval' :0.1})
nest.Connect(noise, neuron, syn_spec={'weight': 90.0})
nest.Connect(mm, neuron)

nest.Connect(neuron, det)

# m = Na
# n = K
# Conductance in nS / cm^2
g_Na = nest.GetDefaults("hh_psc_alpha")['g_Na']
E_Na = nest.GetDefaults("hh_psc_alpha")['E_Na']
g_K = nest.GetDefaults("hh_psc_alpha")['g_K']
E_K = nest.GetDefaults("hh_psc_alpha")['E_K']

nest.Simulate(70.)

events = nest.GetStatus(mm)[0]['events']
t = events['times']

pl.subplot(221)
nest.voltage_trace.from_device(mm)
pl.plot(t, events['V_m'], 'b')
pl.plot(nest.GetStatus(det)[0]['events']['times'], nest.GetStatus(det)[0]['events']['senders'], marker='.', color='r')

pl.subplot(222)
pl.plot(t, events['Act_m'], 'r', t, events['Inact_n'], 'g' )
#pl.plot(t, [ event *  g_Na for event in events['Act_m'] ], t, [ event * g_K for event in events['Inact_n'] ])
#pl.plot(t, [ -event for event in events['Act_m'] ], t, [ event - 0.3 for event in events['Inact_n'] ])
pl.legend( ('Na', 'K') )
pl.title("Ion channels")
pl.ylabel("Channel activation")
pl.xlabel("Time (ms)")

I_Na_list = []
I_K_list = []
# Chloride
# I_L = g_L * (V_m - E_L)
# http://humanphysiology.tuars.com/program/section1/1ch4/s1ch4_49.htm
for i in range( len(events['V_m']) ):

    m = events['Act_m'][i]
    h = events['Act_h'][i]
    n = events['Inact_n'][i]
    V_m = events['V_m'][i]


    I_Na_list.append( m**3 * h * g_Na * (V_m - E_Na) )
    I_K_list.append( n**4 * g_K * (V_m - E_K) )
    print 'm={} | h={} | n={} | V_m={} | I_Na={} | I_K={}'.format(m, h, n, V_m, I_Na_list[i], I_K_list[i])

pl.subplot(223)
pl.plot(t, I_Na_list, 'r')
pl.legend( ('Na', 'K') )
pl.title("Ion channels")
pl.ylabel("nA ")
pl.xlabel("Time (ms)")

pl.subplot(224)
pl.plot(t, I_K_list, 'g', t, I_Na_list, 'r')
pl.legend( ('Na', 'K') )
pl.title("Ion channels")
pl.ylabel("nA ")
pl.xlabel("Time (ms)")

pl.show()
pl.close()