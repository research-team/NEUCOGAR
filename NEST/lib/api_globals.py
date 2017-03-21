__author__  = "Alexey Panzer"
__version__ = "1.2"
__tested___ = "22.03.2017"

import nest
import logging

logging.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=logging.INFO)

# Neurotransmitter key
static = 0
Glu = 1
GABA = 2
ACh = 3
DA_ex = 4
DA_in = 5
SERO_ex = 6
SERO_in = 7
NA = 8

# Available keys for dicts
k_NN = 'NN'
k_IDs = 'IDs'
k_name = 'Name'
k_model = 'Model'

""" Brain parts """
brain = {}

"""Synapse models"""
# Storage dict {NTransmitter : (model, basic_weight)}
# Keys for synapse models
model = 0
basic_weight = 1


neuron_models = {}
synapse_models = {}


""" Common information """
synapse_number = 0
neuron_number = 0

startsimulate = 0           # begin of simulation
endsimulate = 0             # end of simulation

startbuild = 0
endbuild = 0


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
min_neurons = 10

synapse_number_limitation = {}
max_synapses = 999999
min_synapses = 10

# Neuron models
IAF_NEURON    = 'iaf_neuron'
IAF_PSC_EXP   = 'iaf_psc_exp'
IAF_PSC_ALPHA = 'iaf_psc_alpha'

# Synapse models
STATIC_MODEL    = 'static_synapse'
STDP_MODEL      = 'stdp_synapse'
STDP_DOPA_MODEL = 'stdp_dopamine_synapse'
STDP_SERO_MODEL = 'stdp_serotonin_synapse'
STDP_NORA_MODEL = 'stdp_noradrenaline_synapse'