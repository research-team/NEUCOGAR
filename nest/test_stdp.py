import nest
import nest.raster_plot
import numpy as np
import pylab
from random import randint


Dt = 1.
nsteps = 300
w_0 = 10.

nest.ResetKernel()
# with another types of neurons weight dynamic is static
nrn_pre = nest.Create('parrot_neuron')
nrn_post1 = nest.Create('iaf_psc_delta')
nrn_post2 = nest.Create('pp_psc_delta')

nest.Connect(nrn_pre, nrn_post1 + nrn_post2, syn_spec={'model':'stdp_synapse', 'weight': w_0} )
conn1 = nest.GetConnections(nrn_pre, nrn_post1)
conn2 = nest.GetConnections(nrn_pre, nrn_post2)

sg_pre = nest.Create('spike_generator')
nest.SetStatus( sg_pre, {'spike_times': np.arange(Dt, nsteps*Dt, 10.*Dt)})
nest.Connect( sg_pre, nrn_pre )

mm = nest.Create('multimeter')
nest.SetStatus(mm, {'record_from':['V_m']})
nest.Connect( mm, nrn_post1+nrn_post2 )

sd = nest.Create('spike_detector')
nest.Connect( nrn_pre + nrn_post1 + nrn_post2, sd )

t = []
w1 = []
w2 = []
t.append( 0. )
w1.append( nest.GetStatus(conn1, keys=['weight'])[0][0] )
w2.append( nest.GetStatus(conn2, keys=['weight'])[0][0] )

table = []

for i in xrange(nsteps):
    print "COMPLETED: ", 100.0 * i / nsteps, "%"
    nest.Simulate( Dt )
    # adding new neurons
    newNeurons = nest.Create('pp_psc_delta', randint(1, 20))
    nest.Connect(newNeurons, sd)
    nrn_post2 += newNeurons
    nest.Connect(nrn_pre, newNeurons, syn_spec={'model':'stdp_synapse', 'weight': w_0} )

    # check synapse weights
    for part in nest.GetStatus(nest.GetConnections(nrn_pre, nrn_post1)):
        if part['weight'] > 39:
            table.append("pre[{0}] to post1[{1}] | time {2}ms | > 39".format(part['source'],
                                                                             part['target'], i))
    for part in nest.GetStatus(nest.GetConnections(nrn_pre, nrn_post2)):
        if part['weight'] > 25:
            table.append("pre[{0}] to post2[{1}] | time {2}ms | > 39".format(part['source'],
                                                                             part['target'], i))

    t.append( i*Dt )
    w1.append( nest.GetStatus(conn1, keys=['weight'])[0][0] )
    w2.append( nest.GetStatus(conn2, keys=['weight'])[0][0] )

# show synapse weights
for item in table:
    print item

# plot images
pylab.figure(1)
pylab.plot(t, w1, 'g', label='iaf_psc_delta, '+str(nrn_post1[0]))
pylab.plot(t, w2, 'r', label='pp_psc_delta, '+str(nrn_post2[0]))
pylab.xlabel('time [ms]')
pylab.ylabel('weight [mV]')
pylab.legend(loc='best')
ylims = pylab.ylim()
pylab.ylim(ylims[0]-5, ylims[1]+5)

nest.raster_plot.from_device(sd)
ylims = pylab.ylim()
pylab.ylim(ylims[0]-.5, ylims[1]+.5)
pylab.show()