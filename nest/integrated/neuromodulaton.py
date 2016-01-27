# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there ara some mistakes in neuron parameters! Write to @alexpanzer in Trello.

from func import *
'''
This is the implementation of experiment of dopamine neuromodulation based on
https://github.com/research-team/NEUCOGAR/blob/master/IntegratedCircuits.png
Neurotools is used for representing and analyzing nonscientific data.
'''
nest.ResetKernel()
startbuild = clock()
logger = logging.getLogger("neuromodulation")
nest.SetKernelStatus({'overwrite_files': True,  "local_num_threads": 4, "resolution": 0.1}) #'data_path':sd_folder_name

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
logger.debug('Start connection initialisation')

# * * * NIGROSTRIATAL * * *
connect(motor_cortex[motivation], striatum[D1], syn_type=Glu)
connect(motor_cortex[motivation], snc[snc_DA], syn_type=Glu)
connect(motor_cortex[motivation], striatum[D2], syn_type=Glu)
connect(motor_cortex[motivation], thalamus[thalamus_Glu], syn_type=Glu)
connect(motor_cortex[motivation], stn[stn_Glu], syn_type=Glu)
connect(motor_cortex[action], striatum[D1], syn_type=Glu)
connect(motor_cortex[action], striatum[D2], syn_type=Glu)
connect(motor_cortex[action], thalamus[thalamus_Glu], syn_type=Glu)
connect(motor_cortex[action], stn[stn_Glu], syn_type=Glu)
connect(motor_cortex[action], nac[nac_GABA0])

connect(striatum[tan], striatum[D1], syn_type=ACh)
connect(striatum[tan], striatum[D2], syn_type=ACh)
connect(striatum[D1], snr[snr_GABA])
connect(striatum[D1], gpi[gpi_GABA])
connect(striatum[D1], gpe[gpe_GABA])
connect(striatum[D2], gpe[gpe_GABA])

connect(gpe[gpe_GABA], stn[stn_Glu])
connect(gpe[gpe_GABA], striatum[D1])
connect(gpe[gpe_GABA], striatum[D2])
connect(gpe[gpe_GABA], gpi[gpi_GABA])
connect(gpe[gpe_GABA], snr[snr_GABA])

connect(stn[stn_Glu], snr[snr_GABA], syn_type=Glu)
connect(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu)
connect(stn[stn_Glu], gpe[gpe_GABA], syn_type=Glu)
connect(stn[stn_Glu], amygdala[amygdala_Glu], syn_type=Glu)
connect(stn[stn_Glu], snc[snc_DA], syn_type=Glu)

connect(gpi[gpi_GABA], thalamus[thalamus_Glu])
connect(snr[snr_GABA], thalamus[thalamus_Glu])

connect(thalamus[thalamus_Glu], motor_cortex[action], syn_type=Glu)
connect(thalamus[thalamus_Glu], stn[stn_Glu], syn_type=Glu)
connect(thalamus[thalamus_Glu], striatum[D1], syn_type=Glu)
connect(thalamus[thalamus_Glu], striatum[D2], syn_type=Glu)
connect(thalamus[thalamus_Glu], striatum[tan], syn_type=Glu)
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
connect(tpp[tpp_GABA], snc[snc_GABA])
connect(tpp[tpp_ACh], vta[vta_GABA0], syn_type=ACh)
connect(tpp[tpp_ACh], vta[vta_DA1], syn_type=ACh)
connect(tpp[tpp_Glu], vta[vta_GABA0], syn_type=Glu)
connect(tpp[tpp_Glu], vta[vta_DA1], syn_type=Glu)
connect(tpp[tpp_ACh], striatum[D1], syn_type=ACh)
connect(tpp[tpp_ACh], snc[snc_GABA], syn_type=ACh)
connect(tpp[tpp_Glu], snc[snc_DA], syn_type=Glu)

# * * * INTEGRATED * * *
connect(prefrontal_cortex[pfc_Glu0], vta[vta_DA0], syn_type=Glu)
connect(prefrontal_cortex[pfc_Glu0], nac[nac_GABA1], syn_type=Glu)
connect(prefrontal_cortex[pfc_Glu1], vta[vta_GABA2], syn_type=Glu)
connect(prefrontal_cortex[pfc_Glu1], nac[nac_GABA1], syn_type=Glu)

connect(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_ACh], syn_type=Glu)
connect(amygdala[amygdala_Glu], striatum[D1], syn_type=Glu)
connect(amygdala[amygdala_Glu], striatum[D2], syn_type=Glu)
connect(amygdala[amygdala_Glu], striatum[tan], syn_type=Glu)


# ==================
# Dopamine modulator
# ==================
logger.debug('Making neuromodulating connections...')

if dopa_flag:
    # Volume transmission: init dopa_model
    #vt_in = nest.Create("volume_transmitter") #TODO inhibitory???
    #DOPA_synparams_in['vt'] = vt_in[0]
    #nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)
    #nest.Connect(snc[snc_DA], striatum[tan], conn_dict, syn_spec=dopa_model_in)
    vt_ex = nest.Create("volume_transmitter")
    DOPA_synparams_ex['vt'] = vt_ex[0]
    nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)

    # NIGROSTRIATAL
    nest.Connect(snc[snc_DA], vt_ex)
    connectDA_ex(snc[snc_DA], striatum[D1])
    connectDA_ex(snc[snc_DA], gpe[gpe_GABA])
    connectDA_ex(snc[snc_DA], stn[stn_Glu])
    connectDA_ex(snc[snc_DA], nac[nac_GABA0])
    connectDA_ex(snc[snc_DA], nac[nac_GABA1])

    # MESOCORTICOLIMBIC
    nest.Connect(vta[vta_DA0], vt_ex)
    nest.Connect(vta[vta_DA1], vt_ex)
    connectDA_ex(vta[vta_DA0], striatum[D1])
    connectDA_ex(vta[vta_DA0], striatum[D2])
    connectDA_ex(vta[vta_DA0], prefrontal_cortex[pfc_Glu0])
    connectDA_ex(vta[vta_DA0], prefrontal_cortex[pfc_Glu1])
    connectDA_ex(vta[vta_DA1], nac[nac_GABA0])
    connectDA_ex(vta[vta_DA1], nac[nac_GABA1])


# ===============
# Spike Generator
# ===============
logger.debug('Creating spike generators...')

if poison_generator_flag:
    connect_spikegenerator('slow', motor_cortex[action], 400., 600.)
    if dopa_flag:
        connect_spikegenerator('fast', motor_cortex[motivation], 400., 600.)
        connect_spikegenerator('fast', prefrontal_cortex[pfc_Glu0], 400., 600.)
        connect_spikegenerator('fast', prefrontal_cortex[pfc_Glu1], 400., 600.)
        connect_spikegenerator('fast', tpp[tpp_GABA], 400., 600.)
        connect_spikegenerator('fast', tpp[tpp_Glu], 400., 600.)
        connect_spikegenerator('fast', tpp[tpp_ACh], 400., 600.)
        connect_spikegenerator('fast', amygdala[amygdala_Glu], 400., 600.)
'''
else:
    sg_slow = nest.Create('spike_generator', params={'spike_times': np.arange(1, T, 20.)})
    parts_dict_log[sg_slow[0]] = 'Periodic Generator(slow)'
    nest.CopyModel("static_synapse", gen_static_syn, {'weight': w_Glu})
    nest.Connect(sg_slow, motor_cortex[action], syn_spec=gen_static_syn,
                 conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[action]) / 4})
    log_conn(sg_slow, motor_cortex[action])
    if dopa_flag:
        # NIGROSTRIATAL (motor_cortex)
        sg_fast = nest.Create('spike_generator', params={'spike_times': np.arange(400, 600, 15.)})
        parts_dict_log[sg_fast[0]] = 'Periodic Generator(fast)'
        nest.Connect(sg_fast, motor_cortex[motivation], syn_spec=gen_static_syn, )
        # conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(motor_cortex[motivation]) / 4})
        log_conn(sg_fast, motor_cortex[motivation])
        # MESOCORTICOLIMBIC (VTA)
        sg_fast = nest.Create('spike_generator', params={'spike_times': np.arange(400, 600, 15.)})
        parts_dict_log[sg_fast[0]] = 'Periodic Generator(fast)'
        nest.Connect(sg_fast, vta[vta_DA0], syn_spec=gen_static_syn, )
        # conn_spec={'rule': 'fixed_outdegree', 'outdegree': len(vta[vta_DA0]) / 4})
        log_conn(sg_fast, vta[vta_DA0])
'''

# =============
# SPIKEDETECTOR
# =============
logger.debug('Attaching spikes detector')

connect_spikedetector(thalamus[thalamus_Glu])
connect_spikedetector(motor_cortex[action])
connect_spikedetector(prefrontal_cortex[pfc_Glu0])
connect_spikedetector(vta[vta_DA0])
connect_spikedetector(vta[vta_DA1])
connect_spikedetector(snc[snc_DA])

# ==========
# MULTIMETER
# ==========
logger.debug('Attaching multimeters')

connect_multimeter(thalamus[thalamus_Glu])
connect_multimeter(snc[snc_DA])
connect_multimeter(prefrontal_cortex[pfc_Glu0])
connect_multimeter(vta[vta_DA0])

endbuild = clock()

del parts, get_ids, generate_neurons, connect, connectDA_ex, \
    connect_spikegenerator, connect_spikedetector, connect_multimeter

# ==========
# SIMULATING
# ==========
logger.debug("Simulating")

start_simulation()

# ==========
# SAVING
# ==========
get_information(startbuild, endbuild)

save_results(GUI=statusGUI)