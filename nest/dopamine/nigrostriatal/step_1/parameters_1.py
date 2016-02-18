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
# Configure logger
import logging
FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
dpi_n = 120

# general settings
T = 1000.
dt = 10.
sd_folder_name = "spike_detector_data/"
sd_filename = "spikes-172-0.gdf"
#"spike_detector-cortex-0.gdf"
# dopamine modulation flag
vt_flag = True
pg_flag = False
# dopamine model key
dopa_model = "dopa"

# ========
# NEURONS
# ========

# neurons model without neuromodulation
cortex_neurons_model = striatum_neurons_model = gpe_neurons_model = gpi_neurons_model = stn_neurons_model = snr_neurons_model = thalamus_neurons_model = 'iaf_psc_exp'
# with dopamine
snc_neurons_model = 'iaf_psc_alpha'
# Count of neurons in every parts of BS
# table for neuron number: https://docs.google.com/spreadsheets/d/1cAm5uosBoKaaPyC1mvb527nYkVcW2YsAA2ECiCDASzg/edit?usp=sharing
NN_cortex = 100
NN_striatum = NN_gpe = NN_gpi = NN_stn = NN_snc = NN_thalamus = 10
NN_snr = 10

# for a time the neuron model parameters would be setted as STP inhibitory or excitory
# for a time the neuron model parameters would be setted as STP inhibitory or excitory
STP_neuronparams = {'E_L': -70., 'V_th': -50., 'V_reset': -75., 'C_m': 2., 't_ref': 2., 'V_m': -60.,
                        'tau_syn_ex': 1.,
                        'tau_syn_in': 1.33, 'tau_m': 20.,}
# ToDO define appropriate params


STP_ex_neuronparams = {'tau_syn_ex': 0.7}
STP_inh_neuronparams = {'tau_syn_inh': 1.13}

# Excitory neurons
cortex_neuronparams = stn_neuronparams = thalamus_neuronparams = STP_neuronparams
# Inhibitory neurons
striatum_neuronparams = gpe_neuronparams = gpi_neuronparams = snr_neuronparams = STP_neuronparams
# Neuromodulation neurons
snc_neuronparams = STP_neuronparams

# =========
# SYNAPSES
# =========

# parameters of synapses
# Glutamate
w_ex = 30.
# GABA
g = 0.9
w_in = -w_ex * g

# Volume transmission
stdp_dopamine_synapse_weight = 95.

#--------------------------- ToDo what for?
g_w_ex = 40.
g_w_inh = -20.

K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_inh = (1.0 - f_ex) * K

nu_ex = 10.0  # 2.
nu_inh = 10.0  # 2.
#--------------------------

vt_delay = 1.
delay_inh = 1.
delay_ex = 1.

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
bs_synapse_model = 'stdp_synapse'
syn_excitory = "excitatory"
syn_inhibitory = "inhibitory"

mm_param = {"to_memory": True, "to_file": False, 'withtime': True,  'interval': 0.1,
            'record_from': ['V_m'], 'withgid': True}
detector_param = {"label": "spikes", "withtime": True, "withgid": True, "to_file": False, "to_memory": True}
axis = [0, T, -78, -48]

'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''

