import numpy as np
import nest
import nest.voltage_trace as plot

# Reset simulation
nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True}) # set to True to permit overwriting

# Set up simulation time limits
T = 10000.0
dt = 10.0

# Set basic params
delay = 1.     # the delay in ms
w_ex = 45.
g = 3.83
w_in = -w_ex * g
K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_in = (1.0 - f_ex) * K
nu_ex = 10.0#2.
nu_in = 10.0#2.

# Add required "devices"
pg_ex = nest.Create("poisson_generator")
nest.SetStatus(pg_ex, {"rate": K_ex * nu_ex})

pg_in = nest.Create("poisson_generator")
nest.SetStatus(pg_in, {"rate": K_in * nu_in})

sd = nest.Create("spike_detector")

# Add neyrons
neuron1 = nest.Create("iaf_psc_alpha")
neuron2 = nest.Create("iaf_psc_alpha")
sero_neuron = nest.Create("iaf_psc_alpha")
nest.SetStatus(neuron1, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})
nest.SetStatus(neuron2, {"tau_syn_ex": 0.3, "tau_syn_in": 0.3, "tau_minus": 20.0})

vt = nest.Create("volume_transmitter")

# Connect to exit of Poisson generator
nest.Connect(pg_ex, neuron1)
nest.Connect(pg_ex, neuron2)
nest.Connect(pg_ex, sero_neuron)

# Connect to entrance of Poisson generator
nest.Connect(pg_in, neuron1)
nest.Connect(pg_in, neuron2)
nest.Connect(pg_in, sero_neuron)

# Connect to spike detector
nest.Connect(neuron1, sd)
nest.Connect(neuron2, sd)
nest.Connect(sero_neuron, sd)

# Init connections
nest.CopyModel("stdp_serotonine_synapse", "sero", {"vt": vt[0], "weight": 35., "delay": delay})
nest.CopyModel("static_synapse", "static", {"delay": delay})

nest.Connect(sero_neuron, vt, model="static")
nest.Connect(neuron1, neuron2, model="sero")

# Init and connect voltmeter to see membrane potential of serotonin neuron
voltmeter = nest.Create('voltmeter', 1, {'withgid': True})
nest.Connect(voltmeter, sero_neuron)

# Set up output file
if nest.GetStatus(neuron2)[0]['local']:
    filename = 'simulation_results.gdf'
    fname = open(filename, 'w')
else:
    raise

# Tab delimiter in a string
dlm = '\t'
# Next line symbol
nl = '\n';

# Set-up file header: time[ms], connection weight, serotonin concentration, eligibility trace
fname.write('time'+ dlm + 'weight' + dlm + 'n' + dlm + 'c' + nl)

def get_neuron1_prop(property_name):
    return str(nest.GetStatus(nest.FindConnections(neuron1, synapse_model="sero"))[0][property_name])

# Run simualtion
weight = None
for t in np.arange(0, T + dt, dt):
    if nest.GetStatus(neuron2)[0]['local']:
        data = str(t) + dlm + get_neuron1_prop('weight') + dlm + get_neuron1_prop('n') + dlm + get_neuron1_prop('c') + nl
        fname.write(data)
        nest.Simulate(dt)
        print '///////////////////////////////// ' + str(t/T * 100) + ' % completed'

if nest.GetStatus(neuron2)[0]['local']:
    print("weight = " + str(weight) + " pA")
    fname.close()

print("Eligibility trace = " + get_neuron1_prop('c'))
print("Serotonin conc-on = " + get_neuron1_prop('n'))

plot.from_device(voltmeter, timeunit="s")
plot.show()