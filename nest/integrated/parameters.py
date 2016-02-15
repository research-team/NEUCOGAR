'''
It contains:
    Motor Cortex
    Striatum
    GPe: globus pallidus external
    GPi: globus pallidus internal
    STN: subthalamic nucleus
    SNr: substantia nigra reticulata
    SNc: substantia nigra compacta
    Thalamus
    Prefrontal cortex
    NAc: Nucleus Accumbens
    VTA: Ventral Tegmental Area
    TPP: Tegmental Pedunculopontine nucleus
    Amy: Amygdala
Prefix description:
    MSN_ - Medium Spiny Neurons
    ex_  -  excitory
    inh_ - inhibitory
    STP_ - Short Term Plasticity
    GABA - GABA
    Glu - glutamate
    ACh - acetylcholine
    DA  - dopamine
'''
import logging
from property import *

FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(filename='param.log', format=FORMAT, level=logging.DEBUG)


# general settings
T = 1000.
dt = 10.

# neurons number for spike detector
N_rec = 100
k_ids = 'ids'
k_name = 'name'

'''
If you need new brain part just write name = {k_name: 'name'} and add to all_part variable (dict{'name': neurons_list}).
'''

def generate_neurons(nest):
    logger = logging.getLogger('parameters')
    iaf_neuronparams = {'E_L': -70.,
                        'V_th': -50.,
                        'V_reset': -67.,
                        'C_m': 2.,
                        't_ref': 2.,
                        'V_m': -60.,
                        'tau_syn_ex': 1.,
                        'tau_syn_in': 1.33}
    # k - prefix means key
    k_NN = 'NN'
    k_model = 'model'

    # NIGROSTRIATAL PATHWAY PARTS
    motor_cortex = ({k_name: 'motivation'}, {k_name: 'action'})
    striatum = ({k_name: 'D1'}, {k_name: 'D2'}, {k_name: 'tan'})
    gpe = ({k_name: 'gpe_GABA'}, )
    gpi = ({k_name: 'gpi_GABA'}, )
    stn = ({k_name: 'stn_Glu'}, )
    snr = ({k_name: 'snr_GABA'}, )
    thalamus = ({k_name: 'thalamus_Glu'}, )
    snc = ({k_name: 'snc_GABA'}, {k_name: 'snc_DA'})

    # MESOCORTICOLIMBIC PATHWAY PARTS
    prefrontal_cortex = ({k_name: 'pfc_Glu0'}, {k_name: 'pfc_Glu1'})
    nac = ({k_name: 'nac_ACh'}, {k_name: 'nac_GABA0'}, {k_name: 'nac_GABA1'})
    vta = ({k_name: 'vta_GABA0'}, {k_name: 'vta_DA0'}, {k_name: 'vta_GABA1'}, {k_name: 'vta_DA1'}, {k_name: 'vta_GABA2'})
    tpp = ({k_name: 'tpp_GABA'}, {k_name: 'tpp_ACh'}, {k_name: 'tpp_Glu'})

    # ADDITIONAL PARTS
    amygdala = ({k_name: 'amygdala_Glu'}, )

    parts_no_dopa = gpe + gpi + stn + snr + amygdala + (vta[vta_GABA0], vta[vta_GABA1], vta[vta_GABA2], snc[snc_GABA]) + \
                    striatum + motor_cortex + prefrontal_cortex + nac + tpp + thalamus

    parts_with_dopa = (vta[vta_DA0], vta[vta_DA1], snc[snc_DA])

    # ========
    # NEURONS
    # ========
    for part in parts_no_dopa:                  # without dopamine
        part[k_model] = 'iaf_psc_exp'
    for part in parts_with_dopa:                # with dopamine
        part[k_model] = 'iaf_psc_alpha'
    all_parts = parts_no_dopa + parts_with_dopa

    if test_flag:
        # ===========
        # TEST NUMBER
        # ===========
        motor_cortex[motivation][k_NN] = 60
        motor_cortex[action][k_NN] = 150
        striatum[D1][k_NN] = 30
        striatum[D2][k_NN] = 30
        striatum[tan][k_NN] = 8
        gpe[gpe_GABA][k_NN] = 30
        gpi[gpi_GABA][k_NN] = 10
        stn[stn_Glu][k_NN] = 15
        snc[snc_GABA][k_NN] = 40
        snc[snc_DA][k_NN] = 100
        snr[snr_GABA][k_NN] = 21
        thalamus[thalamus_Glu][k_NN] = 90

        prefrontal_cortex[pfc_Glu0][k_NN] = 150
        prefrontal_cortex[pfc_Glu1][k_NN] = 150
        nac[nac_ACh][k_NN] = 15
        nac[nac_GABA0][k_NN] = 70
        nac[nac_GABA1][k_NN] = 70
        vta[vta_GABA0][k_NN] = 30
        vta[vta_DA0][k_NN] = 20
        vta[vta_GABA1][k_NN] = 30
        vta[vta_DA1][k_NN] = 20
        vta[vta_GABA2][k_NN] = 30
        tpp[tpp_GABA][k_NN] = 20
        tpp[tpp_ACh][k_NN] = 14
        tpp[tpp_Glu][k_NN] = 23

        amygdala[amygdala_Glu][k_NN] = 40
    else:
        # ===========
        # REAL NUMBER
        # ===========
        cerebral_cortex_NN = 29000000
        motor_cortex[motivation][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
        motor_cortex[action][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
        striatum_NN = 2500000
        striatum[D1][k_NN] = int(striatum_NN * 0.425)
        striatum[D2][k_NN] = int(striatum_NN * 0.425)
        striatum[tan][k_NN] = int(striatum_NN * 0.05)
        gpe[gpe_GABA][k_NN] = 84100
        gpi[gpi_GABA][k_NN] = 12600
        stn[stn_Glu][k_NN] = 22700
        snc[snc_GABA][k_NN] = 3000      #TODO check number of neurons
        snc[snc_DA][k_NN] = 12700       #TODO check number of neurons
        snr[snr_GABA][k_NN] = 47200
        thalamus[thalamus_Glu][k_NN] = int(5000000 / 6) #!!!!

        prefrontal_cortex[pfc_Glu0][k_NN] = 183000
        prefrontal_cortex[pfc_Glu1][k_NN] = 183000
        nac[nac_ACh][k_NN] = 1500       #TODO not real!!!
        nac[nac_GABA0][k_NN] = 14250    #TODO not real!!!
        nac[nac_GABA1][k_NN] = 14250    #TODO not real!!!
        vta[vta_GABA0][k_NN] = 7000
        vta[vta_DA0][k_NN] = 20000
        vta[vta_GABA1][k_NN] = 7000
        vta[vta_DA1][k_NN] = 20000
        vta[vta_GABA2][k_NN] = 7000
        tpp[tpp_GABA][k_NN] = 2000
        tpp[tpp_ACh][k_NN] = 1400
        tpp[tpp_Glu][k_NN] = 2300

        amygdala[amygdala_Glu][k_NN] = 30000          #TODO not real!!!

        # possible different coefficients
        k = 0.0013
        for part in all_parts: part[k_NN] = 10 if int(part[k_NN] * k) < 10 else int(part[k_NN] * k)

    logger.debug('Initialised: %d neurons' % sum(item[k_NN] for item in all_parts))
    # assign neuron params to every part

    nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    for part in all_parts:
        part[k_ids] = nest.Create(part[k_model], part[k_NN])
    return all_parts


# =========
# SYNAPSES
# =========
# poisson generator
K = 500
f_part = 0.5
K_fast = f_part * K
K_slow = (1.0 - f_part) * K

# Volume transmission
w_DA_ex = 13.
w_DA_in = -w_DA_ex

# generator delay
pg_delay = 10.

w_Glu = 3.
w_GABA = -w_Glu * 2
w_ACh = 8.

#FixMe A params from NEST docs, find real numbers
STDP_synapseparams = {
    'model': 'stdp_synapse',
    'tau_m': {'distribution': 'uniform', 'low': 15., 'high': 25.},
    'alpha': {'distribution': 'normal_clipped', 'low': 0.5, 'mu': 5.0, 'sigma': 1.0},
    'delay': {'distribution': 'uniform', 'low': 0.8, 'high': 2.5},
    'lambda': 0.5
}

STDP_synparams_Glu = dict({'delay': {'distribution': 'uniform', 'low': 0.7, 'high': 1.3},
                           'weight': w_Glu,
                           'Wmax': 70.}, **STDP_synapseparams)

STDP_synparams_GABA = dict({'delay': {'distribution': 'uniform', 'low': 1., 'high': 1.9},
                            'weight': w_GABA,
                            'Wmax': -60.}, **STDP_synapseparams)

STDP_synparams_ACh = dict({'delay': {'distribution': 'uniform', 'low': 0.7, 'high': 1.3},
                           'weight': w_ACh,
                           'Wmax': 70.}, **STDP_synapseparams)

DOPA_synparams = {'delay': 1.}
DOPA_synparams_ex = dict({'weight': w_DA_ex,
                          'Wmax': 100.,
                          'Wmin': 85.}, **DOPA_synparams)

DOPA_synparams_in = dict({'weight': w_DA_in,
                          'Wmax': -100.,
                          'Wmin': -85.}, **DOPA_synparams)

types = {GABA: (STDP_synparams_GABA, w_GABA, 'GABA'),
         ACh: (STDP_synparams_ACh, w_ACh, 'Ach'),
         Glu: (STDP_synparams_Glu, w_Glu, 'Glu'),
         DA_ex: (DOPA_synparams_ex, w_DA_ex, 'DA_ex', dopa_model_ex),
         DA_in: (DOPA_synparams_in, w_DA_in, 'DA_in', dopa_model_in)}

'''
===========
 In SNr neurons according to recent experimental findings [http://www.biomedcentral.com/1471-2202/12/S1/P145#B2]
 has been found short term facilitation in MSN synapses onto SNr neurons from SNc.
'''
# ============
# CONNECTIONS
# ============
conn_dict = {'rule': 'all_to_all', 'multapses': True}


# =======
# DEVICES
# =======
mm_param = {'to_memory': True, 'to_file': False, 'withtime': True, 'interval': 0.1,
            'record_from': ['V_m'], 'withgid': True}
detector_param = {'label': 'spikes', 'withtime': True, 'withgid': True, 'to_file': False, 'to_memory': True,
                  'scientific': True}
axis = [0, T, -72, -48]


'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''