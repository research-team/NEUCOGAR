# -*- coding: utf-8 -*-

'''
It contains:

    Cortex                           = 100 neurons, iaf_psc_exp glutamatergic
    Striatum                         =  10 neurons, iaf_psc_exp GABAergic
    GPe: globus pallidus external    =  10 neurons, iaf_psc_exp GABAergic
    GPi: globus pallidus internal    =  10 neurons, iaf_psc_exp GABAergic
    STN: subthalamic nucleus         =  10 neurons, iaf_psc_exp glutamatergic
    SNr: substantia nigra reticulata =  10 neurons, iaf_psc_exp GABAergic
    SNc: substantia nigra compacta   =  10 neurons, iaf_psc_exp dopaminergic
    Thalamus                         =  10 neurons, iaf_psc_exp glutamatergic

Prefix description:
    MSN_ - Medium Spiny Neurons
    ex_  -  excitory
    inh_ - inhibitory
    STP_ - Short Term Plasticity
'''

# general settings
T = 300.0
dt = 10.0

# ========
# NEURONS
# ========

# neurons model for every part of BS
cortex_neurons_model = striatum_neurons_model = gpe_neurons_model = gpi_neurons_model = stn_neurons_model = snc_neurons_model = snr_neurons_model = thalamus_neurons_model = 'iaf_psc_exp'

# Count of neurons in every parts of BS
cortex_number_of_neurons = 100
striatum_number_of_neurons = gpe_number_of_neurons = gpi_number_of_neurons = stn_number_of_neurons = snc_number_of_neurons = snr_number_of_neurons = thalamus_number_of_neurons = 10

# for a time the neuron model parameters would be setted as STP inhibitory or excitory
STP_neuronparams = {'tau_m': 30., 'E_L': 0., 'V_th': 15, 'V_reset': 13.5, 'C_m': 30., 'tau_ex': 3.}
STP_ex_neuronparams = dict([{'tau_ref_abs': 3., 'tau_ref_tot': 3.}] + STP_neuronparams.items())
STP_inh_neuronparams = dict([{'tau_ref_abs': 2., 'tau_ref_tot': 2.}] + STP_neuronparams.items())

cortex_neuronparams = stn_neuronparams = thalamus_neuronparams = STP_ex_neuronparams
striatum_neuronparams = gpe_neuronparams = gpi_neuronparams = snr_neuronparams = STP_inh_neuronparams
snc_neuronparams = STP_neuronparams

# =========
# SYNAPSES
# =========

# parameters of synapses
w_ex = 45.
g = 3.83
w_inh = -w_ex * g

g_w_ex = 40.
g_w_inh = -20.

K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_inh = (1.0 - f_ex) * K

nu_ex = 10.0  # 2.
nu_inh = 10.0  # 2.

stdp_dopamine_synapse_weight = 35.
vt_delay = 1.

'''
    ===========
 In SNr neurons according to recent experimental findings [http://www.biomedcentral.com/1471-2202/12/S1/P145#B2]
 has been found short term facilitation in MSN synapses onto SNr neurons from SNc.
'''

# synapses model are same for test facilitation
bs_synapse_model = 'stdp_synapse'
conn_dict = {'rule': 'all_to_all', 'autapses': True, 'multapses': True}
syn_dict_ex = {'model': bs_synapse_model, 'weight': w_ex, 'delay': vt_delay}
syn_dict_inh = {'model': bs_synapse_model, 'weight': w_inh, 'delay': vt_delay}
syn_dict_dop = {'model': 'stdp_dopamine_synapse', 'weight': stdp_dopamine_synapse_weight, 'delay': vt_delay}
# ============
# CONNECTIONS
# ============

'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''

