from func import *

# ATTTENTION! Maybe there are some mistakes in neuron parameters!
# Write to alexey.panzer@gmail.com.

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 1,
                      'resolution': 0.1})

generate_neurons(3000)

# Init parameters of our synapse models
DOPA_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
DOPA_synparams_in['vt'] = nest.Create('volume_transmitter')[0]
nest.CopyModel('static_synapse', gen_static_syn, static_syn)
nest.CopyModel('stdp_synapse', glu_synapse, STDP_synparams_Glu)
nest.CopyModel('stdp_synapse', gaba_synapse, STDP_synparams_GABA)
nest.CopyModel('stdp_synapse', ach_synapse, STDP_synparams_ACh)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_in, DOPA_synparams_in)


logger.debug("* * * Start connection initialisation")
# * * * NIGROSTRIATAL PATHWAY* * *
add_connection(motor[motor_Glu0], striatum[D1], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu0], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)
add_connection(motor[motor_Glu0], striatum[D2], syn_type=Glu, weight_coef=0.05)
add_connection(motor[motor_Glu0], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.008)
add_connection(motor[motor_Glu0], stn[stn_Glu], syn_type=Glu, weight_coef=7)
add_connection(motor[motor_Glu1], striatum[D1], syn_type=Glu)
add_connection(motor[motor_Glu1], striatum[D2], syn_type=Glu)
add_connection(motor[motor_Glu1], thalamus[thalamus_Glu], syn_type=Glu)
add_connection(motor[motor_Glu1], stn[stn_Glu], syn_type=Glu)
add_connection(motor[motor_Glu1], nac[nac_GABA0])

add_connection(striatum[tan], striatum[D1])
add_connection(striatum[tan], striatum[D2], syn_type=Glu)

add_connection(striatum[D1], snr[snr_GABA], weight_coef=0.00001)
add_connection(striatum[D1], gpi[gpi_GABA], weight_coef=0.00001)
add_connection(striatum[D1], gpe[gpe_GABA], weight_coef=0.000005)
add_connection(striatum[D2], gpe[gpe_GABA], weight_coef=1)

add_connection(gpe[gpe_GABA], stn[stn_Glu], weight_coef=0.0001)
add_connection(gpe[gpe_GABA], striatum[D1], weight_coef=0.001)
add_connection(gpe[gpe_GABA], striatum[D2], weight_coef=0.3)
add_connection(snc[snc_DA], gpe[gpe_GABA], weight_coef=0.3, syn_type=DA_ex)
add_connection(amygdala[amygdala_Glu], gpe[gpe_GABA], weight_coef=0.3, syn_type=Glu)
add_connection(gpe[gpe_GABA], amygdala[amygdala_Glu], weight_coef=0.1, syn_type=Glu)
add_connection(gpe[gpe_GABA], snc[snc_DA], weight_coef=0.2, syn_type=GABA)
add_connection(gpe[gpe_GABA], snr[snr_GABA], weight_coef=0.0001)

add_connection(stn[stn_Glu], snr[snr_GABA], syn_type=Glu, weight_coef=20)
add_connection(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu, weight_coef=20)
add_connection(stn[stn_Glu], gpe[gpe_GABA], syn_type=Glu, weight_coef=0.3)
#add_connection(stn[stn_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.000001)

add_connection(gpi[gpi_GABA], thalamus[thalamus_Glu], weight_coef=3)
add_connection(snr[snr_GABA], thalamus[thalamus_Glu], weight_coef=3)

add_connection(thalamus[thalamus_Glu], motor[motor_Glu1], syn_type=Glu)
#add_connection(thalamus[thalamus_Glu], stn[stn_Glu], syn_type=Glu, weight_coef=1) #005
#add_connection(thalamus[thalamus_Glu], striatum[D1], syn_type=Glu, weight_coef=0.0001)
#add_connection(thalamus[thalamus_Glu], striatum[D2], syn_type=Glu, weight_coef=0.0001)
#add_connection(thalamus[thalamus_Glu], striatum[tan], syn_type=Glu, weight_coef=0.0001)
#add_connection(thalamus[thalamus_Glu], nac[nac_GABA0], syn_type=Glu)
#add_connection(thalamus[thalamus_Glu], nac[nac_GABA1], syn_type=Glu)
#add_connection(thalamus[thalamus_Glu], nac[nac_ACh], syn_type=Glu)

# * * * MESOCORTICOLIMBIC PATHWAY * * *
add_connection(nac[nac_ACh], nac[nac_GABA1], syn_type=ACh)
add_connection(nac[nac_GABA0], nac[nac_GABA1])
add_connection(nac[nac_GABA1], vta[vta_GABA2])

add_connection(vta[vta_GABA0], prefrontal[pfc_Glu0])
add_connection(vta[vta_GABA0], prefrontal[pfc_Glu1])
add_connection(vta[vta_GABA0], pptg[pptg_GABA])
add_connection(vta[vta_GABA1], vta[vta_DA0])
add_connection(vta[vta_GABA1], vta[vta_DA1])
add_connection(vta[vta_GABA2], nac[nac_GABA1])

add_connection(pptg[pptg_GABA], vta[vta_GABA0])
add_connection(pptg[pptg_GABA], snc[snc_GABA], weight_coef=0.000005)
add_connection(pptg[pptg_ACh], vta[vta_GABA0], syn_type=ACh)
add_connection(pptg[pptg_ACh], vta[vta_DA1], syn_type=ACh)
add_connection(pptg[pptg_Glu], vta[vta_GABA0], syn_type=Glu)
add_connection(pptg[pptg_Glu], vta[vta_DA1], syn_type=Glu)
add_connection(pptg[pptg_ACh], striatum[D1], syn_type=ACh, weight_coef=0.3)
add_connection(pptg[pptg_ACh], snc[snc_GABA], syn_type=ACh, weight_coef=0.000005)
add_connection(pptg[pptg_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)

# * * * INTEGRATED PATHWAY * * *
add_connection(prefrontal[pfc_Glu0], vta[vta_DA0], syn_type=Glu)
add_connection(prefrontal[pfc_Glu0], nac[nac_GABA1], syn_type=Glu)
add_connection(prefrontal[pfc_Glu1], vta[vta_GABA2], syn_type=Glu)
add_connection(prefrontal[pfc_Glu1], nac[nac_GABA1], syn_type=Glu)

add_connection(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], nac[nac_ACh], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], striatum[D1], syn_type=Glu, weight_coef=0.3)
add_connection(amygdala[amygdala_Glu], striatum[D2], syn_type=Glu, weight_coef=0.3)
add_connection(amygdala[amygdala_Glu], striatum[tan], syn_type=Glu, weight_coef=0.3)

if dopamine_flag:
    logger.debug("* * * Making neuromodulating connections...")
    # NIGROSTRIATAL
    add_connection(snc[snc_DA], striatum[D1], syn_type=DA_ex)
    add_connection(snc[snc_DA], gpe[gpe_GABA], syn_type=DA_ex)
    add_connection(snc[snc_DA], stn[stn_Glu], syn_type=DA_ex)
    add_connection(snc[snc_DA], nac[nac_GABA0], syn_type=DA_ex)
    add_connection(snc[snc_DA], nac[nac_GABA1], syn_type=DA_ex)
    add_connection(snc[snc_DA], striatum[D2], syn_type=DA_in)
    add_connection(snc[snc_DA], striatum[tan], syn_type=DA_in)

    # MESOCORTICOLIMBIC
    add_connection(vta[vta_DA0], striatum[D1], syn_type=DA_ex)
    add_connection(vta[vta_DA0], striatum[D2], syn_type=DA_in)
    add_connection(vta[vta_DA0], prefrontal[pfc_Glu0], syn_type=DA_ex)
    add_connection(vta[vta_DA0], prefrontal[pfc_Glu1], syn_type=DA_ex)
    add_connection(vta[vta_DA1], nac[nac_GABA0], syn_type=DA_ex)
    add_connection(vta[vta_DA1], nac[nac_GABA1], syn_type=DA_ex)


logger.debug("* * * Creating connectivity")
connect_all()

logger.debug("* * * Attaching spike generators...")
connect_generator(gpe[gpi_GABA], rate=300, coef_part=1)
connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(snc[snc_DA], 200., 400., rate=250, coef_part=1)
connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)


logger.debug("* * * Attaching spikes detector")
for part in get_all_parts():
    connect_detector(part)

logger.debug("* * * Attaching multimeters")
for part in get_all_parts():
    connect_multimeter(part)

del generate_neurons, add_connection, connect_generator, connect_detector, connect_multimeter

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=gui_enabled)