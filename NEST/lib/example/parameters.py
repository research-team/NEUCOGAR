from api_globals import *
import random

""" Synapses """
# Synapse weights
w_Glu = 150.
w_GABA = -w_Glu * 2
w_DA_ex = 170.
w_DA_in = -w_DA_ex

# Neuron parameters
iaf_neuronparams = {
                    }     # Time constant of postsynaptic inhibitory currents in ms

stdp_glu_params = {'delay': 1.0,
                   'weight': w_Glu,
                   'alpha': 2.5,
                   'lambda': 0.5}

stdp_gaba_params = {'delay': 1.0,
                    'weight': w_GABA,
                    'alpha': 2.5,
                    'lambda': 0.5,
                    'Wmax': -100.0}

stdp_dopa_ex_params = {'delay': 1.0,
                       'weight': w_DA_ex}

stdp_dopa_in_params = {'delay': 1.0,
                       'weight': w_DA_in}