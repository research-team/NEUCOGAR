# -*- coding: utf-8 -*-

'''
It contains:

    Cortex                           =  neurons, iaf_psc_exp glutamatergic
    Striatum                         =  neurons, iaf_psc_exp GABAergic
    GPe: globus pallidus external    =  neurons, iaf_psc_exp GABAergic
    GPi: globus pallidus internal    =  neurons, iaf_psc_exp GABAergic
    STN: subthalamic nucleus         =  neurons, iaf_psc_exp glutamatergic
    SNr: substantia nigra reticulata =  neurons, iaf_psc_exp GABAergic
    SNc: substantia nigra compacta   =  neurons, iaf_psc_exp dopaminergic
    Thalamus                         =  neurons, iaf_psc_exp glutamatergic

Prefix description:
    MSN_ - Medium Spiny Neurons
    ex_  -  excitory
    inh_ - inhibitory
    STP_ - Short Term Plasticity
'''
# Configure logger
import logging
from property import *

FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# general settings
T = 1000.
dt = 10.

# ========
# NEURONS
# ========

# neurons model without neuromodulation
cortex_neurons_model = striatum_neurons_model = gpe_neurons_model = gpi_neurons_model = stn_neurons_model = snr_neurons_model = thalamus_neurons_model = tan_neuron_model = tan_neurons_model= 'iaf_psc_exp'
# with dopamine
snc_neurons_model = 'iaf_psc_alpha'  # ToDo iaf_psc_alpha    understand the purpose of alpha for neuromodulation
# Count of neurons in every parts of BS
# table for neuron number: https://docs.google.com/spreadsheets/d/1cAm5uosBoKaaPyC1mvb527nYkVcW2YsAA2ECiCDASzg/edit?usp=sharing
NN_cortex = 110

NN_tan = 25
NN_striatum = {D1: 20, D2: 20}
NN_gpe = NN_gpi = NN_stn = NN_snc = 10
NN_snr = 10
NN_thalamus = 40

# for a time the neuron model parameters would be setted as STP inhibitory or excitory
STP_neuronparams = {'E_L': -70., 'V_th': -50., 'V_reset': -70., 'C_m': 1., 't_ref': 2., 'V_m': -70., 'tau_syn_ex': 1., 'tau_syn_in': 1.13, 'tau_m':20.}
# 'tau_m': {'distribution': 'uniform', 'low': 15., 'high': 25.}}
# ToDO define appropriate params

cortex_neuronparams = stn_neuronparams = thalamus_neuronparams = tan_neuronparams = \
    striatum_neuronparams = gpe_neuronparams = gpi_neuronparams = snr_neuronparams = snc_neuronparams = STP_neuronparams

# =========
# SYNAPSES
# =========

# Glutamate
w_ex = 45.  # excitatory weights
g = 3.83
# GABA
w_in = -w_ex * g  # inhibitory weight

g_w_ex = 45.
g_w_in = -20.

# poisson generator
K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_in = (1.0 - f_ex) * K

nu_ex = 10.0
nu_in = 10.0

# Volume transmission
stdp_dopamine_synapse_w_ex = 45.
stdp_dopamine_synapse_w_in = -20.
# generator delay
delay = 1.

vt_delay = 1.
delay_ex = 0.8  # {'distribution': 'uniform', 'low': 0.8, 'high': 1.5}
delay_inh = 1.4  # {'distribution': 'uniform', 'low': 1., 'high': 1.9}
'''
    ===========
 In SNr neurons according to recent experimental findings [http://www.biomedcentral.com/1471-2202/12/S1/P145#B2]
 has been found short term facilitation in MSN synapses onto SNr neurons from SNc.
'''


# ============
# CONNECTIONS
# ============
conn_dict = {'rule': 'all_to_all', 'multapses': True}
# synapses model are same for test facilitation


'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''

