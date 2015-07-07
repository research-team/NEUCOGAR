# -*- coding: utf-8 -*-

'''
It contains:

    Motor Cortex                           =  neurons, iaf_psc_exp glutamatergic
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
from property_2 import *
import os
from matplotlib import collections
from matplotlib.colors import colorConverter
import pylab as pl

FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# general settings
T = 1000.
dt = 10.

# neurons number for spike detector
N_rec = 100

k_ids = 'ids'
k_name = 'name'
# functions just for easy settings readability
def generate_neurons_BG(nest):
    logger = logging.getLogger("parameters")
    iaf_neuronparams = {'E_L': -70., 'V_th': -50., 'V_reset': -67., 'C_m': 2., 't_ref': 2., 'V_m': -60.,
                        'tau_syn_ex': 1.,
                        'tau_syn_in': 1.33}
    # neuron set
    # k - prefix means key
    k_NN = 'NN'
    k_model = 'model'
    k_coef = 'coefficient'
    # ===================
    # BASAL GANGLIA PARTS
    # ===================
    motor_cortex = {k_name: 'motor_cortex'}
    striatum = ({k_name: 'D1'}, {k_name: 'D2'}, {k_name: 'tan'})
    gpe = {k_name: 'gpe'}
    gpi = {k_name: 'gpi'}
    stn = {k_name: 'stn'}
    snr = {k_name: 'snr'}
    thalamus = {k_name: 'thalamus'}
    iter_BG_parts_no_dopa = (motor_cortex, gpe, gpi, stn, snr, thalamus) + striatum
    snc = {k_name: 'snc'}
    # ========
    # NEURONS
    # ========
    for bg_part in iter_BG_parts_no_dopa: bg_part[k_model] = 'iaf_psc_exp'
    # with dopamine
    snc[k_model] = 'iaf_psc_alpha'
    iter_all_parts = iter_BG_parts_no_dopa + (snc,)
    # Count of neurons in every parts of BGs
    # table for neuron number: https://docs.google.com/spreadsheets/d/1cAm5uosBoKaaPyC1mvb527nYkVcW2YsAA2ECiCDASzg/edit?usp=sharing
    if test_flag:
        # ===========
        # TEST NUMBER
        # ===========
        motor_cortex[k_NN] = 210
        striatum[D1][k_NN] = 30
        striatum[D2][k_NN] = 30
        striatum[tan][k_NN] = 8
        gpe[k_NN] = 30
        gpi[k_NN] = 10
        stn[k_NN] = 15
        snc[k_NN] = 10
        snr[k_NN] = 21
        thalamus[k_NN] = 90
    else:
        # ===========
        # REAL NUMBER
        # ===========
        striatum_NN = 2500000
        motor_cortex[k_NN] = 29000000
        striatum[D1][k_NN] = int(striatum_NN * 0.425)
        striatum[D2][k_NN] = int(striatum_NN * 0.425)
        striatum[tan][k_NN] = int(striatum_NN * 0.05)
        gpe[k_NN] = 84100
        gpi[k_NN] = 12600
        stn[k_NN] = 22700
        snc[k_NN] = 12700
        snr[k_NN] = 47200
        thalamus[k_NN] = 5000000
        # =================
        # COEFFICIENT COUNT
        # =================
        k = 0.001
        motor_cortex[k_coef] = k
        striatum[D1][k_coef] = k
        striatum[D2][k_coef] = k
        striatum[tan][k_coef] = k
        gpe[k_coef] = k
        gpi[k_coef] = k
        stn[k_coef] = k
        snc[k_coef] = k
        snr[k_coef] = k
        thalamus[k_coef] = k
        for part in iter_all_parts: part[k_NN] = int(part[k_NN] * part[k_coef])
    logger.debug('Initialised: %d neurons' % sum(item[k_NN] for item in iter_all_parts))
    # assign neuron params to every part of BG
    nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    for bg_part in iter_all_parts:
        bg_part[k_ids] = nest.Create(bg_part[k_model], bg_part[k_NN])

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
# poisson generator
K = 80
f_part = 0.7
K_fast = f_part * K
K_slow = (1.0 - f_part) * K

# Volume transmission
stdp_dopamine_synapse_w_ex = 85.
stdp_dopamine_synapse_w_in = -stdp_dopamine_synapse_w_ex

# generator delay
pg_delay = 20.

# Glutamate
w_ex = 45.  # excitatory weights
# GABA
k = 1.2
w_in = k * w_ex  # inhibitory weight

STDP_synapseparams = {
    'model': 'stdp_synapse',
    'tau_m': {'distribution': 'uniform', 'low': 15., 'high': 25.},
    'alpha': {'distribution': 'normal_clipped', 'low': 0.5, 'mu': 5.0, 'sigma': 1.0},
    'delay': {'distribution': 'uniform', 'low': 0.8, 'high': 2.5},
    'lambda': 0.5
}
STDP_synapseparams_ex = dict({'delay': {'distribution': 'uniform', 'low': 0.7, 'high': 1.3},
                              'weight': w_ex,
                              'Wmax': 70.
                             }, **STDP_synapseparams)

STDP_synapseparams_in = dict({'delay': {'distribution': 'uniform', 'low': 1., 'high': 1.9},
                              'weight': w_in,
                              'Wmax': -60.
                             }, **STDP_synapseparams)
DOPA_synparams = {"delay": 1.}
DOPA_synparams_ex = dict({"weight": stdp_dopamine_synapse_w_ex, 'Wmax': 100., 'Wmin': 85.}, **DOPA_synparams)
DOPA_synparams_in = dict({"weight": stdp_dopamine_synapse_w_in, 'Wmax': -100., 'Wmin': -85.}, **DOPA_synparams)

'''
===========
 In SNr neurons according to recent experimental findings [http://www.biomedcentral.com/1471-2202/12/S1/P145#B2]
 has been found short term facilitation in MSN synapses onto SNr neurons from SNc.
'''
# ============
# CONNECTIONS
# ============
# conn_dict = {'rule': 'all_to_all', 'multapses': True}
conn_dict = {'rule': 'fixed_outdegree', 'outdegree': 10}
# =========
# FUNCTIONS
# =========
def f_name_gen(name, is_image=False):
    sub_folder = os.path.join(sd_folder_name, 'noise/' if pg_flag else 'static/')
    if not os.path.exists(sub_folder): os.makedirs(sub_folder)

    return sub_folder + \
           (name + '_' if len(name) > 0 else '') + \
           ('yes' if vt_flag else 'no') + '_dopa_generator_' + \
           ('noise' if pg_flag else 'static') + \
           ('.png' if is_image else '_')

def plot_weights(weights_list, title="Neurons weights progress", y_lim = None):

    # Plot
    # Make a list of colors cycling through the rgbcmyk series.
    colors = [colorConverter.to_rgba(c) for c in ('k', 'r', 'g', 'b', 'c', 'y', 'm')]

    axes = pl.axes()
    ax4 = axes # unpack the axes

    ncurves = 1
    offs = (0.0, 0.0)

    segs = []
    for i in range(ncurves):
        curve = weights_list
        segs.append(curve)

    col = collections.LineCollection(segs, offsets=offs)
    ax4.add_collection(col, autolim=True)
    col.set_color(colors)
    ax4.autoscale_view()
    ax4.set_title(title)
    ax4.set_xlabel('Time ms')
    ax4.set_ylabel('Weight pA')
    y_lim = 105.
    if y_lim :
        ax4.set_ylim(-5, y_lim)
    pl.savefig(f_name_gen('dopa-weights', is_image=True), format='png')
    # pl.show()

# =======
# DEVICES
# =======
mm_param = {"to_memory": True, "to_file": False, 'withtime': True, 'interval': 0.1,
            'record_from': ['V_m'], 'withgid': True}
detector_param = {"label": "spikes", "withtime": True, "withgid": True, "to_file": False, "to_memory": True, 'scientific': True}
axis = [0, T, -72, -48]

'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''
