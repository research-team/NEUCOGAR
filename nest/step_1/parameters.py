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

k_ids = 'ids'
k_name = 'name'
# functions just for easy settings readability
def generate_neurons_BG(nest):
    STP_neuronparams = {'E_L': -70., 'V_th': -50., 'V_reset': -70., 'C_m': 1., 't_ref': 2., 'V_m': -70.,
                        'tau_syn_ex': 1.,
                        'tau_syn_in': 1.13, 'tau_m': 20.}
    # 'tau_m': {'distribution': 'uniform', 'low': 15., 'high': 25.}}
    # neuron set
    nest.SetDefaults('iaf_psc_exp', STP_neuronparams)
    # k - prefix means key
    k_NN = 'NN'
    k_model = 'model'
    k_params = 'neuroparam'
    # ===================
    # BASAL GANGLIA PARTS
    # ===================
    cortex = {k_name: 'cortex'}
    striatum = ({k_name: 'D1'}, {k_name: 'D2'}, {k_name: 'tan'})
    gpe = {k_name: 'gpe'}
    gpi = {k_name: 'gpi'}
    stn = {k_name: 'stn'}
    snr = {k_name: 'snr'}
    thalamus = {k_name: 'thalamus'}
    iter_BG_parts_no_dopa = (cortex, gpe, gpi, stn, snr, thalamus) + striatum
    snc = {k_name: 'snc'}
    # ========
    # NEURONS
    # ========
    for bg_part in iter_BG_parts_no_dopa: bg_part[k_model] = 'iaf_psc_exp'
    # with dopamine
    snc[k_model] = 'iaf_psc_alpha'
    # Count of neurons in every parts of BGs
    # table for neuron number: https://docs.google.com/spreadsheets/d/1cAm5uosBoKaaPyC1mvb527nYkVcW2YsAA2ECiCDASzg/edit?usp=sharing
    # cortex[k_NN] = 110
    # striatum[D1][k_NN] = 20
    # striatum[D2][k_NN] = 20
    # striatum[tan][k_NN] = 25
    # gpe[k_NN] = 10
    # gpi[k_NN] = 10
    # stn[k_NN] = 10
    # snc[k_NN] = 10
    # snr[k_NN] = 10
    # thalamus[k_NN] = 40
    striatum_NN = 6900
    cortex[k_NN] = 30000
    striatum[D1][k_NN] = int(striatum_NN * 0.425)
    striatum[D2][k_NN] = int(striatum_NN * 0.425)
    striatum[tan][k_NN] = int(striatum_NN * 0.05)
    gpe[k_NN] = 4600
    gpi[k_NN] = 320
    stn[k_NN] = 1360
    snc[k_NN] = 720
    snr[k_NN] = 2630
    thalamus[k_NN] = 249000
    # assign neuron params to every part of BG
    iter_all_parts = iter_BG_parts_no_dopa + (snc,)
    for bg_part in iter_all_parts: bg_part[k_params] = STP_neuronparams

    for bg_part in iter_all_parts: bg_part[k_ids] = nest.Create(bg_part[k_model], bg_part[k_NN])
    for bg_part in iter_all_parts: nest.SetStatus(bg_part[k_ids], bg_part[k_params])
    return iter_all_parts


def get_ids(name, iter_BG=None):
    if iter_BG is not None: get_ids.iter_BG = iter_BG
    for part_BG in get_ids.iter_BG:
        if part_BG[k_name] == name:
            return part_BG[k_ids]
    raise KeyError

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

tau_plus = 20.

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

# =======
# DEVICES
# =======
mm_param = {"to_memory": False, "to_file": True, "label": "neuron_1", 'withtime': True, 'interval': 0.1,
            'record_from': ['V_m'], 'withgid': True}
detector_param = {"label": "spikes", "withtime": True, "withgid": True, "to_file": True,"to_memory":False}
axis = [0, T, -72, -48]

'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''

# =========
# FUNCTIONS
# =========
f_name_gen = lambda name: sd_folder_name + name + ('_yes' if vt_flag else '_no') + '_dopa_generator_' + \
                          ('noise.png' if pg_flag else 'static.png')
