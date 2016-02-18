# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there are some mistakes in neuron parameters! Write to @alexpanzer in Trello.

from func import *

'''
This is the implementation of experiment of dopamine neuromodulation based on
https://github.com/research-team/NEUCOGAR/blob/master/IntegratedCircuits.png
Neurotools is used for representing and analyzing nonscientific data.
'''
nest.ResetKernel()

startbuild = datetime.datetime.now()
logger = logging.getLogger('neuromodulation')
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

# ==============
# Creating parts
# ==============
parts = generate_neurons(nest)
motor_cortex = (get_ids('motivation', parts), get_ids('action'))
f_register(motor_cortex[motivation], 'Motor[motivation]')
f_register(motor_cortex[action], 'Motor[action]')

prefrontal_cortex = (get_ids('pfc_Glu0'), get_ids('pfc_Glu1'))
f_register(prefrontal_cortex[pfc_Glu0], 'Prefrontal[Glu0]')
f_register(prefrontal_cortex[pfc_Glu1], 'Prefrontal[Glu1]')

striatum = (get_ids('D1'), get_ids('D2'), get_ids('tan'))
f_register(striatum[tan], 'Striatum[tan]')
f_register(striatum[D1], 'Striatum[D1]')
f_register(striatum[D2], 'Striatum[D2]')

gpe = (get_ids('gpe_GABA'), )
f_register(gpe[gpe_GABA], 'GPe[GABA]')

gpi = (get_ids('gpi_GABA'), )
f_register(gpi[gpi_GABA], 'GPi[GABA]')

stn = (get_ids('stn_Glu'), )
f_register(stn[stn_Glu], 'STN[Glu]')

snr = (get_ids('snr_GABA'), )
f_register(snr[snr_GABA], 'SNr[GABA]')

thalamus = (get_ids('thalamus_Glu'), )
f_register(thalamus[thalamus_Glu], 'Thalamus[Glu]')

snc = (get_ids('snc_GABA'), get_ids('snc_DA'))
f_register(snc[snc_GABA], 'SNc[GABA]')
f_register(snc[snc_DA], 'SNc[DA]')

nac = (get_ids('nac_ACh'), get_ids('nac_GABA0'), get_ids('nac_GABA1'))
f_register(nac[nac_ACh], 'NAc[ACh]')
f_register(nac[nac_GABA0], 'NAc[GABA0]')
f_register(nac[nac_GABA1], 'NAc[GABA1]')

vta = (get_ids('vta_GABA0'), get_ids('vta_DA0'), get_ids('vta_GABA1'), get_ids('vta_DA1'), get_ids('vta_GABA2'))
f_register(vta[vta_GABA0], 'VTA[GABA0]')
f_register(vta[vta_DA0], 'VTA[DA0]')
f_register(vta[vta_GABA1], 'VTA[GABA1]')
f_register(vta[vta_DA1], 'VTA[DA1]')
f_register(vta[vta_GABA2], 'VTA[GABA2]')

tpp = (get_ids('tpp_GABA'), get_ids('tpp_ACh'), get_ids('tpp_Glu'))
f_register(tpp[tpp_GABA], 'TPP[GABA]')
f_register(tpp[tpp_ACh], 'TPP[ACh]')
f_register(tpp[tpp_Glu], 'TPP[Glu]')

amygdala = (get_ids('amygdala_Glu'), )
f_register(amygdala[amygdala_Glu], 'Amygdala[Glu]')


# =========================
# Connection Initialisation
# =========================
logger.debug("* * * Start connection initialisation")

# * * * NIGROSTRIATAL * * *
#connect(motor_cortex[motivation], striatum[D1], syn_type=Glu, weight_coef=0.005)
#connect(motor_cortex[motivation], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)
connect(motor_cortex[motivation], striatum[D2], syn_type=Glu, weight_coef=0.05)
connect(motor_cortex[motivation], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.008)
connect(motor_cortex[motivation], stn[stn_Glu], syn_type=Glu, weight_coef=7)
#connect(motor_cortex[action], striatum[D1], syn_type=Glu)
#connect(motor_cortex[action], striatum[D2], syn_type=Glu)
#connect(motor_cortex[action], thalamus[thalamus_Glu], syn_type=Glu)
#connect(motor_cortex[action], stn[stn_Glu], syn_type=Glu)
#connect(motor_cortex[action], nac[nac_GABA0])

connect(striatum[tan], striatum[D1])
connect(striatum[tan], striatum[D2], syn_type=Glu)

connect(striatum[D1], snr[snr_GABA], weight_coef=0.00005)
connect(striatum[D1], gpi[gpi_GABA], weight_coef=0.00005)
#connect(striatum[D1], gpe[gpe_GABA], weight_coef=0.000005)
connect(striatum[D2], gpe[gpe_GABA], weight_coef=1)

connect(gpe[gpe_GABA], stn[stn_Glu], weight_coef=0.0001)
connect(gpe[gpe_GABA], striatum[D1], weight_coef=0.001)
connect(gpe[gpe_GABA], striatum[D2], weight_coef=0.3)
connect(gpe[gpe_GABA], gpi[gpi_GABA], weight_coef=0.0001)
connect(gpe[gpe_GABA], snr[snr_GABA], weight_coef=0.0001)

connect(stn[stn_Glu], snr[snr_GABA], syn_type=Glu, weight_coef=20)
connect(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu, weight_coef=20)
connect(stn[stn_Glu], gpe[gpe_GABA], syn_type=Glu, weight_coef=0.3)
#connect(stn[stn_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)

connect(gpi[gpi_GABA], thalamus[thalamus_Glu], weight_coef=3)
connect(snr[snr_GABA], thalamus[thalamus_Glu], weight_coef=3)

connect(thalamus[thalamus_Glu], motor_cortex[action], syn_type=Glu)
connect(thalamus[thalamus_Glu], stn[stn_Glu], syn_type=Glu, weight_coef=1) #005
connect(thalamus[thalamus_Glu], striatum[D1], syn_type=Glu, weight_coef=0.005)
connect(thalamus[thalamus_Glu], striatum[D2], syn_type=Glu, weight_coef=0.005)
connect(thalamus[thalamus_Glu], striatum[tan], syn_type=Glu, weight_coef=0.005)
connect(thalamus[thalamus_Glu], nac[nac_GABA0], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_GABA1], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_ACh], syn_type=Glu)

# * * * MESOCORTICOLIMBIC * * *
connect(nac[nac_ACh], nac[nac_GABA1], syn_type=ACh)
connect(nac[nac_GABA0], nac[nac_GABA1])
connect(nac[nac_GABA1], vta[vta_GABA2])

connect(vta[vta_GABA0], prefrontal_cortex[pfc_Glu0])
connect(vta[vta_GABA0], prefrontal_cortex[pfc_Glu1])
connect(vta[vta_GABA0], tpp[tpp_GABA])
connect(vta[vta_GABA1], vta[vta_DA0])
connect(vta[vta_GABA1], vta[vta_DA1])
connect(vta[vta_GABA2], nac[nac_GABA1])

connect(tpp[tpp_GABA], vta[vta_GABA0])
#connect(tpp[tpp_GABA], snc[snc_GABA], weight_coef=0.000005)
connect(tpp[tpp_ACh], vta[vta_GABA0], syn_type=ACh)
connect(tpp[tpp_ACh], vta[vta_DA1], syn_type=ACh)
connect(tpp[tpp_Glu], vta[vta_GABA0], syn_type=Glu)
connect(tpp[tpp_Glu], vta[vta_DA1], syn_type=Glu)
connect(tpp[tpp_ACh], striatum[D1], syn_type=ACh, weight_coef=0.3)
#connect(tpp[tpp_ACh], snc[snc_GABA], syn_type=ACh, weight_coef=0.000005)
#connect(tpp[tpp_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)

# * * * INTEGRATED * * *
connect(prefrontal_cortex[pfc_Glu0], vta[vta_DA0], syn_type=Glu)
connect(prefrontal_cortex[pfc_Glu0], nac[nac_GABA1], syn_type=Glu)
connect(prefrontal_cortex[pfc_Glu1], vta[vta_GABA2], syn_type=Glu)
connect(prefrontal_cortex[pfc_Glu1], nac[nac_GABA1], syn_type=Glu)

connect(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_ACh], syn_type=Glu)
connect(amygdala[amygdala_Glu], striatum[D1], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[D2], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[tan], syn_type=Glu, weight_coef=0.3)


# ==================
# Dopamine modulator
# ==================
logger.debug("* * * Making neuromodulating connections...")

if dopa_flag:
    # Volume transmission: init dopa_model
    vt_ex = nest.Create('volume_transmitter')
    vt_in = nest.Create('volume_transmitter')
    DOPA_synparams_ex['vt'] = vt_ex[0]
    DOPA_synparams_in['vt'] = vt_in[0]
    nest.Connect(snc[snc_DA], vt_ex)
    nest.Connect(snc[snc_DA], vt_in)
    nest.Connect(vta[vta_DA0], vt_ex)
    nest.Connect(vta[vta_DA1], vt_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)

    # NIGROSTRIATAL
    connect(snc[snc_DA], striatum[D1], syn_type=DA_ex)
    connect(snc[snc_DA], gpe[gpe_GABA], syn_type=DA_ex)
    connect(snc[snc_DA], stn[stn_Glu], syn_type=DA_ex)
    connect(snc[snc_DA], nac[nac_GABA0], syn_type=DA_ex)
    connect(snc[snc_DA], nac[nac_GABA1], syn_type=DA_ex)
    connect(snc[snc_DA], striatum[D2], syn_type=DA_in)
    connect(snc[snc_DA], striatum[tan], syn_type=DA_in)

    # MESOCORTICOLIMBIC
    connect(vta[vta_DA0], striatum[D1], syn_type=DA_ex)
    connect(vta[vta_DA0], striatum[D2], syn_type=DA_in)
    connect(vta[vta_DA0], prefrontal_cortex[pfc_Glu0], syn_type=DA_ex)
    connect(vta[vta_DA0], prefrontal_cortex[pfc_Glu1], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA0], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA1], syn_type=DA_ex)


# ===============
# Spike Generator
# ===============
logger.debug("* * * Creating spike generators...")
if generator_flag:
    #Generator synapse
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_Glu * 5, 'delay': pg_delay})
    connect_generator(motor_cortex[motivation], rate=300, coef_part=1)
    connect_generator(tpp[tpp_GABA], 400., 600., rate=250, coef_part=1)
    connect_generator(tpp[tpp_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(tpp[tpp_ACh], 400., 600., rate=250, coef_part=1)
    connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
    connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)


# =============
# SPIKEDETECTOR
# =============
logger.debug("* * * Attaching spikes detector")
connect_detector(gpi[gpi_GABA])
connect_detector(snr[snr_GABA])
connect_detector(gpe[gpe_GABA])
connect_detector(stn[stn_Glu])
connect_detector(snc[snc_DA])
connect_detector(thalamus[thalamus_Glu])
connect_detector(striatum[tan])
connect_detector(striatum[D1])
connect_detector(striatum[D2])
connect_detector(motor_cortex[action])
connect_detector(motor_cortex[motivation])
connect_detector(prefrontal_cortex[pfc_Glu0])
connect_detector(vta[vta_DA0])
connect_detector(vta[vta_DA1])
connect_detector(snc[snc_DA])

# ==========
# MULTIMETER
# ==========
logger.debug("* * * Attaching multimeters")
connect_multimeter(gpi[gpi_GABA])
connect_multimeter(snr[snr_GABA])
connect_multimeter(gpe[gpe_GABA])
connect_multimeter(stn[stn_Glu])
connect_multimeter(snc[snc_DA])
connect_multimeter(thalamus[thalamus_Glu])
connect_multimeter(striatum[tan])
connect_multimeter(striatum[D1])
connect_multimeter(striatum[D2])
connect_multimeter(motor_cortex[action])
connect_multimeter(motor_cortex[motivation])
connect_multimeter(prefrontal_cortex[pfc_Glu0])
connect_multimeter(vta[vta_DA0])
connect_multimeter(vta[vta_DA1])
connect_multimeter(snc[snc_DA])

endbuild = datetime.datetime.now()

del parts, get_ids, generate_neurons, connect, connect_generator, connect_detector, connect_multimeter

simulate()
get_log(startbuild, endbuild)
save(GUI=statusGUI)