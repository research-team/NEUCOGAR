from property import *
import nest
import numpy.random as random
# Neuron parameters
iaf_neuronparams = {'E_L': -70.,            # Resting membrane potential in mV
                    'V_th': -50.,           # Spike threshold in mV
                    'V_reset': -67.,        # Reset membrane potential after a spike in mV
                    'C_m': 2.,              # Capacity of the membrane in pF
                    't_ref': 2.,            # Duration of refractory period (V_m = V_reset) in ms
                    'V_m': -60.,            # Membrane potential in mV at start
                    'tau_syn_ex': 1.,       # Time constant of postsynaptic excitatory currents in ms
                    'tau_syn_in': 1.33}     # Time constant of postsynaptic inhibitory currents in ms

# Synapse common parameters
STDP_synapseparams = {
    'alpha': random.normal(0.5, 5.0),       # Asymmetry parameter (scales depressing increments as alpha*lambda)
    'lambda': 0.5                           # Step size
}

# Glutamate synapse
STDP_synparams_Glu = dict({'delay': random.uniform(low=1.0, high=1.3),  # Distribution of delay values for connections
                           'weight': w_Glu,                             # Weight (power) of synapse
                           'Wmax': 20.}, **STDP_synapseparams)          # Maximum allowed weight
# GABA synapse
STDP_synparams_GABA = dict({'delay': random.uniform(low=1.0, high=1.3),
                            'weight': w_GABA,
                            'Wmax': -20.}, **STDP_synapseparams)

# Dictionary of synapses with keys and their parameters
synapses = {GABA:  (gaba_synapse,    w_GABA ),
            Glu:   (glu_synapse,     w_Glu  )
}

# Parameters for generator
static_syn = {
    'weight': w_Glu * 5,
    'delay': pg_delay
}


detector_param = {'label': 'spikes',
                  'withtime': True,
                  'withgid': True,
                  'to_file': False,
                  'to_memory': True,
                  'scientific': True}