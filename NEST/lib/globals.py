import nest

# Neurotransmitter key
Glu = 0
GABA = 1
ACh = 2
DA_ex = 3
DA_in = 4
SERO_ex = 5
SERO_in = 6
NA = 7

# Available keys for dicts
k_NN = 'NN'
k_IDs = 'IDs'
k_name = 'Name'
k_model = 'Model'

""" Brain parts """
brain = {}

"""Synapse models"""
# Storage dict {NTransmitter : (model, basic_weight)}
neurotransmitters = {}
# Keys for synapse models
model = 0
basic_weight = 1

neuron_models = {}

""" Common information """
synapse_number = 0
neuron_number = 0

startsimulate = 0           # begin of simulation
endsimulate = 0             # end of simulation

startbuild = 0
endbuild = 0

""" Graphics """
# Image quality
dpi_n = 120


""" Simulation """
# T - simulation time | dt - simulation pause step
T = 1000.
dt = 10.

current_path = '.'

""" Devices """
# Neurons number for spike detector
N_detect = 100

# Neurons number for multimeter
N_volt = 3

# Generator delay
pg_delay = 5.


""" Synapses """
# Synapse weights
w_Glu = 30.
w_GABA = -w_Glu * 2
w_DA_ex = 130.

# Minimal number of neurons
NN_minimal = 10

synapse_number_limitation = {}
max_synapses = 1000
min_synapses = 10


# Synapse models
glu_synapse      = 'glu_synapse'
gaba_synapse     = 'gaba_synapse'
ach_synapse      = 'ach_synapse'
dopa_synapse_ex  = 'dopa_synapse_ex'
dopa_synapse_in  = 'dopa_synapse_in'


gen_static_syn   = 'noise_conn'