# -*- coding: utf-8 -*-
'''
It contains:
    Prefrontal Cortex                       = 800 neurons, iaf_psc_exp (100 for each + 800 cortex)
    NAc: Nucleus Accumbens                  = 300  neurons, iaf_psc_exp (100 for each)
    VTA: Ventral Tegmental Area             = 500  neurons, iaf_psc_exp (100 for each)
    TPP: Tegmental Pedunculopontine nucleus = 300  neurons, iaf_psc_exp (100 for each)

    glutamatergic
    GABAergic
    dopaminergic
    acetylholinergic
'''
import logging
from property import *
from matplotlib import collections
from matplotlib.colors import colorConverter
import pylab as pl
import os

FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# general settings
T = 1000.
dt = 10.

# neurons number for spike detector
N_rec = 100
k_ids = 'ids'
k_name = 'name'

"""Set up parameters of brain parts (VTA, NAc...).
If you need new brain part just write name = {k_name: 'name'} and add to all_part variable (dict{'name': neurons_list}).
"""
def generate_neurons_MP(nest):
    logger = logging.getLogger("parameters")
    iaf_neuronparams = {'E_L': -70., 'V_th': -50., 'V_reset': -67., 'C_m': 2., 't_ref': 2., 'V_m': -60.,
                        'tau_syn_ex': 1.,
                        'tau_syn_in': 1.33}
    # k - prefix means key
    k_NN = 'NN'
    k_model = 'model'
    k_coef = 'coefficient'

    # ===================
    # MESOLIMBIC PATHWAY PARTS
    # ===================
    prefrontal_cortex = ({k_name: 'Cortex'}, {k_name: 'Glu0'}, {k_name: 'Glu1'})
    nac = ({k_name: 'Ach'}, {k_name: 'GABA0'}, {k_name: 'GABA1'})
    vta = ({k_name: 'GABA0'}, {k_name: 'DA0'}, {k_name: 'GABA1'}, {k_name: 'DA1'}, {k_name: 'GABA2'})
    tpp = ({k_name: 'GABA'}, {k_name: 'Ach'}, {k_name: 'Glu'})
    parts_no_dopa = prefrontal_cortex + nac + tpp + (vta[vta_GABA0], vta[vta_GABA1], vta[vta_GABA2])
    parts_with_dopa = (vta[vta_DA0], vta[vta_DA1])

    # ========
    # NEURONS
    # ========
    # without dopamine
    for mp_part in parts_no_dopa:
        mp_part[k_model] = 'iaf_psc_exp'
    # with dopamine
    for mp_part in parts_with_dopa:
        mp_part[k_model] = 'iaf_psc_alpha'
    all_parts = parts_no_dopa + parts_with_dopa

    if test_flag:
        # ===========
        # TEST NUMBER
        # ===========
        prefrontal_cortex[cortex][k_NN] = 3600
        prefrontal_cortex[cortex_Glu0][k_NN] = 30
        prefrontal_cortex[cortex_Glu1][k_NN] = 30
        nac[nac_Ach][k_NN] = 15
        nac[nac_GABA0][k_NN] = 142
        nac[nac_GABA1][k_NN] = 142
        vta[vta_GABA0][k_NN] = 70
        vta[vta_DA0][k_NN] = 200
        vta[vta_GABA1][k_NN] = 70
        vta[vta_DA1][k_NN] = 200
        vta[vta_GABA2][k_NN] = 70
        tpp[tpp_GABA][k_NN] = 20
        tpp[tpp_Ach][k_NN] = 14
        tpp[tpp_Glu][k_NN] = 23
    else:
        # ===========
        # REAL NUMBER
        # ===========
        # ToDo check and add real number
        prefrontal_cortex[cortex][k_NN] = 360000
        prefrontal_cortex[cortex_Glu0][k_NN] = 3000
        prefrontal_cortex[cortex_Glu1][k_NN] = 3000
        nac[nac_Ach][k_NN] = 1500
        nac[nac_GABA0][k_NN] = 14250
        nac[nac_GABA1][k_NN] = 14250
        vta[vta_GABA0][k_NN] = 7000
        vta[vta_DA0][k_NN] = 20000
        vta[vta_GABA1][k_NN] = 7000
        vta[vta_DA1][k_NN] = 20000
        vta[vta_GABA2][k_NN] = 7000
        tpp[tpp_GABA][k_NN] = 2000
        tpp[tpp_Ach][k_NN] = 1400
        tpp[tpp_Glu][k_NN] = 2300

        # =================
        # COEFFICIENT COUNT
        # =================
        # possible different coefficients
        # k = 0.12 # 55524 neurons
        k = 0.12
        prefrontal_cortex[cortex][k_coef] = k
        prefrontal_cortex[cortex_Glu0][k_coef] = k
        prefrontal_cortex[cortex_Glu1][k_coef] = k
        nac[nac_Ach][k_coef] = k
        nac[nac_GABA0][k_coef] = k
        nac[nac_GABA1][k_coef] = k
        vta[vta_GABA0][k_coef] = k
        vta[vta_DA0][k_coef] = k
        vta[vta_GABA1][k_coef] = k
        vta[vta_DA1][k_coef] = k
        vta[vta_GABA2][k_coef] = k
        tpp[tpp_GABA][k_coef] = k
        tpp[tpp_Ach][k_coef] = k
        tpp[tpp_Glu][k_coef] = k
        for part in all_parts: part[k_NN] = int(part[k_NN] * part[k_coef])

    logger.debug('Initialised: %d neurons' % sum(item[k_NN] for item in all_parts))
    # assign neuron params to every part of MP
    nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    for mp_part in all_parts:
        mp_part[k_ids] = nest.Create(mp_part[k_model], mp_part[k_NN])

    return all_parts

"""Help method to get neurons_list from iter_MP{'name': neurons_list}"""
def get_ids(name, iter_MP=None):
    if iter_MP is not None:
        get_ids.iter_MP = iter_MP
    for part_MP in get_ids.iter_MP:
        if part_MP[k_name] == name:
            return part_MP[k_ids]
    raise KeyError

# =========
# SYNAPSES
# =========
# poisson generator
K = 500
f_part = 0.5
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
k = 1.5
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
                              'Wmax': 70.}, **STDP_synapseparams)

STDP_synapseparams_in = dict({'delay': {'distribution': 'uniform', 'low': 1., 'high': 1.9},
                              'weight': w_in,
                              'Wmax': -60.}, **STDP_synapseparams)
DOPA_synparams = {"delay": 1.}
DOPA_synparams_ex = dict({"weight": stdp_dopamine_synapse_w_ex, 'Wmax': 100., 'Wmin': 85.}, **DOPA_synparams)
DOPA_synparams_in = dict({"weight": stdp_dopamine_synapse_w_in, 'Wmax': -100., 'Wmin': -85.}, **DOPA_synparams)

# ============
# CONNECTIONS
# ============
conn_dict = {'rule': 'all_to_all', 'multapses': True} # or another scheme 'fixed_outdegree', 'outdegree': 100

# =========
# USEFUL FUNCTIONS
# =========
"""Generates string full name (subfolders with respect to flags defined in properties) of an image"""
def f_name_gen(name, is_image=False):
    sub_folder = os.path.join(sd_folder_name, 'noise/' if poison_generator else 'static/')
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)

    return sub_folder + \
           (name + '_' if len(name) > 0 else '') + \
           ('yes' if dopa_flag else 'no') + '_dopa_generator_' + \
           ('noise' if poison_generator else 'static') + \
           ('.png' if is_image else '_')


"""If save_weight_flag is True then do plotting of weight change in a synapse"""
def plot_weights(weights_list, title="Neurons weights progress"):
    # Make a list of colors cycling through the rgbcmyk series.
    colors = [colorConverter.to_rgba(c) for c in ('k', 'r', 'g', 'b', 'c', 'y', 'm')]
    axes = pl.axes()
    ax4 = axes  # unpack the axes
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
    if y_lim:
        ax4.set_ylim(-5, y_lim)
    pl.savefig(f_name_gen('dopa-weights', is_image=True), format='png')
    # pl.show()

# =======
# DEVICES
# =======
mm_param = {"to_memory": True, "to_file": False, 'withtime': True, 'interval': 0.1,
            'record_from': ['V_m'], 'withgid': True}
detector_param = {"label": "spikes", "withtime": True, "withgid": True, "to_file": False, "to_memory": True,
                  'scientific': True}
axis = [0, T, -72, -48]
