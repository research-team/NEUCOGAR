from keys import *
from simulation_params import *
import nest
import numpy.random as random
# Neuron parameters
hh_neuronparams = {'E_L': -70.,          # Resting membrane potential in mV
                   'V_T': -63.,          # Voltage offset that controls dynamics.
                                         # -63mV results in a threshold around -50mV.
                   'C_m': 2.,            # Capacity of the membrane in pF 1
                   't_ref': 2.,          # Duration of refractory period (V_m = V_reset) in ms
                   'tau_syn_ex': 5.,       # Time constant of postsynaptic excitatory currents in ms
                   'tau_syn_in': 10.      # Time constant of postsynaptic inhibitory currents in ms
                   }

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
# Acetylcholine synapse
STDP_synparams_ACh = dict({'delay': random.uniform(low=1.0, high=1.3),
                           'weight': w_ACh,
                           'Wmax': 20.}, **STDP_synapseparams)

# Noradrenaline excitatory synapse
NORA_synparams_ex = dict({'delay': 1.,
                          'weight': w_NA_ex,
                          'Wmax': 100.})
# Noradrenaline inhibitory synapse
NORA_synparams_in = dict({'delay': 1.,
                          'weight': w_NA_in,
                          'Wmax': -100.})

# Dopamine excitatory synapse
DOPA_synparams_ex = dict({'delay': 1.,
                          'weight': w_DA_ex,
                          'Wmax': 100.})
# Dopamine inhibitory synapse
DOPA_synparams_in = dict({'delay': 1.,
                          'weight': w_DA_in,
                          'Wmax': -100.})


# Serotonin excitatory synapse
SERO_synparams_ex = dict({'delay': 1.,
                          'weight': w_SERO_ex,
                          'Wmax': 100.})
# Serotonin inhibitory synapse
SERO_synparams_in = dict({'delay': 1.,
                          'weight': w_SERO_in,
                          'Wmax': -100.})


# Dictionary of synapses with keys and their parameters
synapses = {GABA:  (gaba_synapse,    w_GABA ),
            Glu:   (glu_synapse,     w_Glu  ),
            ACh:   (ach_synapse,     w_ACh  ),
            NA_ex: (nora_synapse_ex, w_NA_ex),
            NA_in: (nora_synapse_in, w_NA_in),
	    DA_ex: (dopa_synapse_ex, w_DA_ex),
            DA_in: (dopa_synapse_in, w_DA_in),
	    SERO_ex: (sero_synapse_ex, w_SERO_ex),
            SERO_in: (sero_synapse_in, w_SERO_in),

}

# Parameters for generator
static_syn = {
    'weight': w_Glu * 5,
    'delay': pg_delay
}

# Device parameters
multimeter_param = {'to_memory': True,
                    'to_file': False,
                    'withtime': True,
                    'interval': 0.1,
                    'record_from': ['V_m'],
                    'withgid': True}

detector_param = {'label': 'spikes',
                  'withtime': True,
                  'withgid': True,
                  'to_file': False,
                  'to_memory': True,
                  'scientific': True}
