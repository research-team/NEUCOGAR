__author__  = "Alexey Panzer"
__version__ = "2.0.0"
__tested___ = "07.11.2017 NEST 2.12.0 Python 3"

import numpy as numpy
import logging as log
import nest as NEST

log.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=log.INFO)

# Common information
global_syn_number = 0
global_nrn_number = 0

start_build = 0
end_build = 0

current_path = '.'
rec_weight_nrn_num = 5

# Neurons number for spike detector
N_detect = 300

# Neurons number for multimeter
N_volt = 5

default_syn_delay = [1.0, 2.5]

# Generator delay
pg_delay = 5.

min_neurons = 10
max_syn_per_nrn = 10000

# Neuron models
IAF_PSC_EXP = 'iaf_psc_exp'
IAF_PSC_ALPHA = 'iaf_psc_alpha'
HH_PSC_ALPHA = 'hh_psc_alpha'
HH_COND_EXP_TRAUB = 'hh_cond_exp_traub'
IZHIKEVICH = 'izhikevich'

# Synapse models
STATIC_SYNAPSE = 'static_synapse'
STDP_SYNAPSE = 'stdp_synapse'
STDP_DOPA_SYNAPSE = 'stdp_dopamine_synapse'
STDP_SERO_SYNAPSE = 'stdp_serotonin_synapse'
STDP_NORA_SYNAPSE = 'stdp_noradrenaline_synapse'

# Namespaces
Glu = "Glu"
Glu_0 = "Glu_0"
Glu_1 = "Glu_1"
Glu_2 = "Glu_2"
Glu_3 = "Glu_3"

GABA = "GABA"
GABA_0 = "GABA_0"
GABA_1 = "GABA_1"
GABA_2 = "GABA_2"
GABA_3 = "GABA_3"
GABA_D1 = "GABA_D1"
GABA_D2 = "GABA_D2"

DA = "DA"
DA_0 = "DA_0"
DA_1 = "DA_1"
DA_2 = "DA_2"
DA_3 = "DA_3"
DA_ex = "DA_excititory"
DA_in = "DA_inhibitory"

NA = "NA"
NA_0 = "NA_0"
NA_1 = "NA_1"
NA_2 = "NA_2"
NA_3 = "NA_3"

HT5 = "HT5"
HT5_0 = "5-HT_0"
HT5_1 = "5-HT_1"
HT5_2 = "5-HT_2"
HT5_3 = "5-HT_3"
HT5_ex = "5-HT_excitatory"
HT5_in = "5-HT_inhibitory"

ACh = "ACh"
ACh_0 = "ACh_0"
ACh_1 = "ACh_1"
ACh_2 = "ACh_2"
ACh_3 = "ACh_3"


# Memory usage constants
MEM_PER_STATIC_SYNAPSE = NEST.GetDefaults('static_synapse')['sizeof']
MEM_PER_STDP_SYNAPSE = NEST.GetDefaults('stdp_synapse')['sizeof']
#MEM_PER_DOPA_SYNAPSE = NEST.GetDefaults('stdp_dopamine_synapse')['sizeof']
#MEM_PER_SERO_SYNAPSE = NEST.GetDefaults('stdp_serotonin_synapse')['sizeof']
#MEM_PER_NORA_SYNAPSE = NEST.GetDefaults('stdp_noradrenaline_synapse')['sizeof']

syn_mem_usage = 0
nrn_mem_usage = 0
