from api_globals import *
import random

""" Synapses """
# Synapse weights
w_Glu = 3.
w_GABA = -w_Glu * 2
w_ACh = 8.
w_DA_ex = 13.
w_DA_in = -w_DA_ex

# Neuron parameters
iaf_neuronparams = {'E_L': -70.,            # Resting membrane potential in mV
                    'V_th': -50.,           # Spike threshold in mV
                    'V_reset': -67.,        # Reset membrane potential after a spike in mV
                    'C_m': 250.,            # Capacity of the membrane in pF
                    't_ref': 2.,            # Duration of refractory period (V_m = V_reset) in ms
                    'V_m': -60.,            # Membrane potential in mV at start
                    'tau_syn_ex': 1.,       # Time constant of postsynaptic excitatory currents in ms
                    'tau_syn_in': 1.33}     # Time constant of postsynaptic inhibitory currents in ms

stdp_glu_params = {'delay': 1.0,
                   'weight': w_Glu,
                   'alpha': 2.5,
                   'lambda': 0.5}

stdp_gaba_params = {'delay': 1.0,
                    'weight': w_GABA,
                    'alpha': 2.5,
                    'lambda': 0.5,
                    'Wmax': -100.0}

stdp_ach_params = {'delay': 1.0,
                    'weight': w_ACh,
                    'alpha': 2.5,
                    'lambda': 0.5}

stdp_dopa_ex_params = {'delay': 1.0,
                       'weight': w_DA_ex}

stdp_dopa_in_params = {'delay': 1.0,
                       'weight': w_DA_in,
                       'Wmax': -100.0}