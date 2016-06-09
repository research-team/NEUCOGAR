from func import *

# ATTTENTION! Maybe there are some mistakes in neuron parameters!
# Write to alexey.panzer@gmail.com.

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 4,
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
connect(motor[motor_Glu0], striatum[D1], syn_type=Glu, weight_coef=0.005)
connect(motor[motor_Glu0], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)
connect(motor[motor_Glu0], striatum[D2], syn_type=Glu, weight_coef=0.05)
connect(motor[motor_Glu0], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.008)
connect(motor[motor_Glu0], stn[stn_Glu], syn_type=Glu, weight_coef=7)
#connect(motor[motor_Glu1], striatum[D1], syn_type=Glu)
#connect(motor[motor_Glu1], striatum[D2], syn_type=Glu)
#connect(motor[motor_Glu1], thalamus[thalamus_Glu], syn_type=Glu)
#connect(motor[motor_Glu1], stn[stn_Glu], syn_type=Glu)
#connect(motor[motor_Glu1], nac[nac_GABA0])

connect(striatum[tan], striatum[D1])
connect(striatum[tan], striatum[D2], syn_type=Glu)

connect(striatum[D1], snr[snr_GABA], weight_coef=0.00001)
connect(striatum[D1], gpi[gpi_GABA], weight_coef=0.00001)
connect(striatum[D1], gpe[gpe_GABA], weight_coef=0.000005)
connect(striatum[D2], gpe[gpe_GABA], weight_coef=1)

connect(gpe[gpe_GABA], stn[stn_Glu], weight_coef=0.0001)
connect(gpe[gpe_GABA], striatum[D1], weight_coef=0.001)
connect(gpe[gpe_GABA], striatum[D2], weight_coef=0.3)
connect(gpe[gpe_GABA], gpi[gpi_GABA], weight_coef=0.0001)
connect(gpe[gpe_GABA], snr[snr_GABA], weight_coef=0.0001)

connect(stn[stn_Glu], snr[snr_GABA], syn_type=Glu, weight_coef=20)
connect(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu, weight_coef=20)
connect(stn[stn_Glu], gpe[gpe_GABA], syn_type=Glu, weight_coef=0.3)
#connect(stn[stn_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.000001)

connect(gpi[gpi_GABA], thalamus[thalamus_Glu], weight_coef=3)
connect(snr[snr_GABA], thalamus[thalamus_Glu], weight_coef=3)

connect(thalamus[thalamus_Glu], motor[motor_Glu1], syn_type=Glu)
#connect(thalamus[thalamus_Glu], stn[stn_Glu], syn_type=Glu, weight_coef=1) #005
#connect(thalamus[thalamus_Glu], striatum[D1], syn_type=Glu, weight_coef=0.0001)
#connect(thalamus[thalamus_Glu], striatum[D2], syn_type=Glu, weight_coef=0.0001)
#connect(thalamus[thalamus_Glu], striatum[tan], syn_type=Glu, weight_coef=0.0001)
#connect(thalamus[thalamus_Glu], nac[nac_GABA0], syn_type=Glu)
#connect(thalamus[thalamus_Glu], nac[nac_GABA1], syn_type=Glu)
#connect(thalamus[thalamus_Glu], nac[nac_ACh], syn_type=Glu)

# * * * MESOCORTICOLIMBIC PATHWAY * * *
connect(nac[nac_ACh], nac[nac_GABA1], syn_type=ACh)
connect(nac[nac_GABA0], nac[nac_GABA1])
connect(nac[nac_GABA1], vta[vta_GABA2])

connect(vta[vta_GABA0], prefrontal[pfc_Glu0])
connect(vta[vta_GABA0], prefrontal[pfc_Glu1])
connect(vta[vta_GABA0], pptg[pptg_GABA])
connect(vta[vta_GABA1], vta[vta_DA0])
connect(vta[vta_GABA1], vta[vta_DA1])
connect(vta[vta_GABA2], nac[nac_GABA1])

connect(pptg[pptg_GABA], vta[vta_GABA0])
connect(pptg[pptg_GABA], snc[snc_GABA], weight_coef=0.000005)
connect(pptg[pptg_ACh], vta[vta_GABA0], syn_type=ACh)
connect(pptg[pptg_ACh], vta[vta_DA1], syn_type=ACh)
connect(pptg[pptg_Glu], vta[vta_GABA0], syn_type=Glu)
connect(pptg[pptg_Glu], vta[vta_DA1], syn_type=Glu)
connect(pptg[pptg_ACh], striatum[D1], syn_type=ACh, weight_coef=0.3)
connect(pptg[pptg_ACh], snc[snc_GABA], syn_type=ACh, weight_coef=0.000005)
connect(pptg[pptg_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)

# * * * INTEGRATED PATHWAY * * *
connect(prefrontal[pfc_Glu0], vta[vta_DA0], syn_type=Glu)
connect(prefrontal[pfc_Glu0], nac[nac_GABA1], syn_type=Glu)
connect(prefrontal[pfc_Glu1], vta[vta_GABA2], syn_type=Glu)
connect(prefrontal[pfc_Glu1], nac[nac_GABA1], syn_type=Glu)

connect(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_ACh], syn_type=Glu)
connect(amygdala[amygdala_Glu], striatum[D1], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[D2], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[tan], syn_type=Glu, weight_coef=0.3)

if dopamine_flag:
    logger.debug("* * * Making neuromodulating connections...")
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
    connect(vta[vta_DA0], prefrontal[pfc_Glu0], syn_type=DA_ex)
    connect(vta[vta_DA0], prefrontal[pfc_Glu1], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA0], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA1], syn_type=DA_ex)


logger.debug("* * * Creating spike generators...")
if generator_flag:
    connect_generator(motor[motor_Glu0], rate=300, coef_part=1)
    connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
    connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
    connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
    connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)


logger.debug("* * * Attaching spikes detector")
for part in getAllParts():
    connect_detector(part)


logger.debug("* * * Attaching multimeters")
for part in getAllParts():
    connect_multimeter(part)

del generate_neurons, connect, connect_generator, connect_detector, connect_multimeter

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=status_gui)