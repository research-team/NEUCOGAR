from func import *

# ATTTENTION! Maybe there are some mistakes in neuron parameters!

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,
                      'local_num_threads': 8,
                      'resolution': 0.1})

generate_neurons(500000)

# Init parameters of our synapse models
DOPA_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
DOPA_synparams_in['vt'] = nest.Create('volume_transmitter')[0]
SERO_synparams_in['vt'] = nest.Create('volume_transmitter')[0]
SERO_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
NORA_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
nest.CopyModel('static_synapse', gen_static_syn, static_syn)
nest.CopyModel('stdp_synapse', glu_synapse, STDP_synparams_Glu)
nest.CopyModel('stdp_synapse', gaba_synapse, STDP_synparams_GABA)
nest.CopyModel('stdp_synapse', ach_synapse, STDP_synparams_ACh)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_in, DOPA_synparams_in)
nest.CopyModel('stdp_serotonin_synapse', sero_synapse_ex, SERO_synparams_ex)
nest.CopyModel('stdp_serotonin_synapse', sero_synapse_in, SERO_synparams_in)
nest.CopyModel('stdp_noradrenaline_synapse', nora_synapse_ex, NORA_synparams_ex)
## - my .50
logger.debug("* * * Start connection initialisation")




####################################################################


# * * * ventral pathway * * *
connect(ldt[ldt_Ach],thalamus[thalamus_Glu], syn_type=ACh, weight_coef=0.005)
connect(ldt[ldt_Ach], bnst[bnst_Ach], syn_type=ACh, weight_coef=0.005)
connect(ldt[ldt_Ach], lc[lc_N0], syn_type=ACh, weight_coef=0.005)
connect(ldt[ldt_Ach], prefrontal[pfc_Glu0], syn_type=ACh, weight_coef=0.005)
connect(thalamus[thalamus_Glu], motor[motor_Glu0], syn_type=Glu, weight_coef=0.005)
connect(thalamus[thalamus_Glu], motor[motor_Glu1], syn_type=Glu, weight_coef=0.005)
connect(thalamus[thalamus_Glu], motor[motor_5HT], syn_type=Glu, weight_coef=0.005)
connect(motor[motor_Glu0], lc[lc_N0], syn_type=Glu, weight_coef=0.005)
connect(motor[motor_Glu1], lc[lc_N0], syn_type=Glu, weight_coef=0.005)

connect(prefrontal[pfc_Glu0], lc[lc_N0], syn_type=Glu, weight_coef=0.005)
connect(prefrontal[pfc_Glu1], bnst[bnst_Glu], syn_type=Glu, weight_coef=0.005)
connect(bnst[bnst_Glu], bnst[bnst_GABA], syn_type=Glu, weight_coef=0.005)
connect(bnst[bnst_Ach], amygdala[amygdala_Ach], syn_type=ACh, weight_coef=0.005)
connect(bnst[bnst_GABA], hypothalamus[hypothalamus_pvn_GABA], syn_type=GABA, weight_coef=0.005)
connect(amygdala[amygdala_Ach], lc[lc_Ach], syn_type=ACh, weight_coef=0.005)
connect(amygdala[amygdala_GABA], bnst[bnst_GABA], syn_type=GABA, weight_coef=0.005)
connect(amygdala[amygdala_Glu], striatum[striatum_D1], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], striatum[striatum_D2], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], striatum[striatum_tan], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], striatum[striatum_5HT], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], striatum[striatum_Ach], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], striatum[striatum_GABA], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], nac[nac_5HT], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], nac[nac_NA], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], nac[nac_Ach], syn_type=Glu, weight_coef=0.005)
connect(amygdala[amygdala_Glu], nac[nac_DA], syn_type=Glu, weight_coef=0.005)
connect(hypothalamus[hypothalamus_pvn_GABA], motor[motor_Glu0], syn_type=GABA, weight_coef=0.005)
connect(hypothalamus[hypothalamus_pvn_GABA], motor[motor_Glu1], syn_type=GABA, weight_coef=0.005)
connect(hypothalamus[hypothalamus_pvn_GABA], motor[motor_5HT], syn_type=GABA, weight_coef=0.005)


#inside LC
connect(lc[lc_Ach], lc[lc_GABA], syn_type=ACh, weight_coef=0.005)
connect(lc[lc_Ach], lc[lc_N0], syn_type=ACh, weight_coef=0.005)
connect(lc[lc_Ach], lc[lc_N1], syn_type=ACh, weight_coef=0.005)
connect(lc[lc_D1], lc[lc_N0], syn_type=DA_ex, weight_coef=0.005)
connect(lc[lc_D2], lc[lc_N1], syn_type=DA_in, weight_coef=0.005)
connect(lc[lc_GABA], lc[lc_N0], syn_type=GABA, weight_coef=0.005)


#* * * dorsal pathway * * *

connect(pgi[pgi_Glu], lc[lc_N0], syn_type=Glu, weight_coef=0.005)
connect(pgi[pgi_Glu], lc[lc_N1], syn_type=Glu, weight_coef=0.005)
connect(pgi[pgi_GABA], lc[lc_GABA], syn_type=GABA, weight_coef=0.005)
connect(prh[prh_GABA], lc[lc_GABA], syn_type=GABA, weight_coef=0.005)
connect(striatum[striatum_tan], lc[lc_GABA], syn_type=GABA, weight_coef=0.005)
connect(vta[vta_DA0], lc[lc_D1], syn_type=DA_ex, weight_coef=0.005)
connect(vta[vta_DA0], lc[lc_D2], syn_type=DA_in, weight_coef=0.005)
connect(vta[vta_DA1], striatum[striatum_tan], syn_type=DA_ex, weight_coef=0.005)
connect(vta[vta_DA1], striatum[striatum_GABA], syn_type=DA_ex, weight_coef=0.005)

wse = 0.001
wsi = 0.5


#
# * * * NIGROSTRIATAL PATHWAY* * *
connect(motor[motor_Glu0], striatum[striatum_D1], syn_type=Glu, weight_coef=0.005)
connect(motor[motor_Glu0], snc[snc_DA], syn_type=Glu, weight_coef=0.005)
connect(motor[motor_Glu0], striatum[striatum_D2], syn_type=Glu, weight_coef=0.05)
connect(motor[motor_Glu0], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.003) #0.0008
connect(motor[motor_Glu0], prefrontal[pfc_5HT], syn_type=Glu, weight_coef=0.003) ######not in the diagram
connect(motor[motor_Glu0], motor[motor_5HT], syn_type=Glu, weight_coef=0.003) ######not in the diagram
connect(motor[motor_Glu0], stn[stn_Glu], syn_type=Glu, weight_coef=7)
connect(motor[motor_Glu1], striatum[striatum_D1], syn_type=Glu)
connect(motor[motor_Glu1], striatum[striatum_D2], syn_type=Glu)
connect(motor[motor_Glu0], thalamus[thalamus_Glu], syn_type=Glu)
connect(motor[motor_Glu1], stn[stn_Glu], syn_type=Glu)
connect(motor[motor_Glu1], nac[nac_GABA0], syn_type=GABA)

connect(striatum[striatum_tan], striatum[striatum_D1], syn_type=GABA)
connect(striatum[striatum_tan], striatum[striatum_D2], syn_type=Glu)

connect(striatum[striatum_D1], snr[snr_GABA], syn_type=GABA, weight_coef=0.001)
connect(striatum[striatum_D1], gpi[gpi_GABA], syn_type=GABA, weight_coef=0.001)
connect(striatum[striatum_D1], gpe[gpe_GABA], syn_type=GABA, weight_coef=0.005)
connect(striatum[striatum_D2], gpe[gpe_GABA], syn_type=GABA, weight_coef=1)

connect(gpe[gpe_GABA], stn[stn_Glu], syn_type=GABA, weight_coef=0.0001)
connect(gpe[gpe_GABA], striatum[striatum_D1], syn_type=GABA, weight_coef=0.001)
connect(gpe[gpe_GABA], striatum[striatum_D2], syn_type=GABA, weight_coef=0.3)
connect(gpe[gpe_GABA], gpi[gpi_GABA], syn_type=GABA, weight_coef=0.0001)
connect(gpe[gpe_GABA], snr[snr_GABA], syn_type=GABA, weight_coef=0.0001)

connect(stn[stn_Glu], snr[snr_GABA], syn_type=Glu, weight_coef=0.2)
connect(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu, weight_coef=0.2)
connect(stn[stn_Glu], gpe[gpe_GABA], syn_type=Glu, weight_coef=0.3)
connect(stn[stn_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.01)

connect(gpi[gpi_GABA], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=1) # weight_coef=3)
connect(snr[snr_GABA], thalamus[thalamus_Glu], syn_type=GABA, weight_coef=1) # weight_coef=3)

connect(thalamus[thalamus_Glu], motor[motor_Glu1], syn_type=Glu)
connect(thalamus[thalamus_Glu], stn[stn_Glu], syn_type=Glu, weight_coef=1) #005
connect(thalamus[thalamus_Glu], striatum[striatum_D1], syn_type=Glu, weight_coef=0.001)
connect(thalamus[thalamus_Glu], striatum[striatum_D2], syn_type=Glu, weight_coef=0.001)
connect(thalamus[thalamus_Glu], striatum[striatum_tan], syn_type=Glu, weight_coef=0.001)
connect(thalamus[thalamus_Glu], striatum[striatum_Ach], syn_type=Glu, weight_coef=0.001)
connect(thalamus[thalamus_Glu], striatum[striatum_GABA], syn_type=Glu, weight_coef=0.001)
connect(thalamus[thalamus_Glu], striatum[striatum_5HT], syn_type=Glu, weight_coef=0.001)
connect(thalamus[thalamus_Glu], nac[nac_GABA0], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_GABA1], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_Ach], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_DA], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_5HT], syn_type=Glu)
connect(thalamus[thalamus_Glu], nac[nac_NA], syn_type=Glu)

# * * * INTEGRATED PATHWAY * * *
connect(prefrontal[pfc_Glu0], vta[vta_DA0], syn_type=Glu)
connect(prefrontal[pfc_Glu0], nac[nac_GABA1], syn_type=Glu)
connect(prefrontal[pfc_Glu1], vta[vta_GABA2], syn_type=Glu)
connect(prefrontal[pfc_Glu1], nac[nac_GABA1], syn_type=Glu)

connect(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_Ach], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_DA], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_5HT], syn_type=Glu)
connect(amygdala[amygdala_Glu], nac[nac_NA], syn_type=Glu)
connect(amygdala[amygdala_Glu], striatum[striatum_D1], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[striatum_D2], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[striatum_tan], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[striatum_Ach], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[striatum_5HT], syn_type=Glu, weight_coef=0.3)
connect(amygdala[amygdala_Glu], striatum[striatum_GABA], syn_type=Glu, weight_coef=0.3)


   

# * * * MESOCORTICOLIMBIC PATHWAY * * *
connect(nac[nac_Ach], nac[nac_GABA1], syn_type=ACh)
connect(nac[nac_GABA0], nac[nac_GABA1],syn_type=GABA,)
connect(nac[nac_GABA1], vta[vta_GABA2],syn_type=GABA,)

connect(vta[vta_GABA0], prefrontal[pfc_Glu0],syn_type=GABA,)
connect(vta[vta_GABA0], pptg[pptg_GABA],syn_type=GABA,)
connect(vta[vta_GABA1], vta[vta_DA0],syn_type=GABA,)
connect(vta[vta_GABA1], vta[vta_DA1],syn_type=GABA,)
connect(vta[vta_GABA2], nac[nac_GABA1],syn_type=GABA,)

connect(pptg[pptg_GABA], vta[vta_GABA0],syn_type=GABA,)
connect(pptg[pptg_GABA], snc[snc_GABA], syn_type=GABA,weight_coef=0.005)
connect(pptg[pptg_ACh], vta[vta_GABA0], syn_type=ACh)
connect(pptg[pptg_ACh], vta[vta_DA1], syn_type=ACh)
connect(pptg[pptg_Glu], vta[vta_GABA0], syn_type=Glu)
connect(pptg[pptg_Glu], vta[vta_DA1], syn_type=Glu)
connect(pptg[pptg_ACh], striatum[striatum_D1], syn_type=ACh, weight_coef=0.3)
connect(pptg[pptg_ACh], snc[snc_GABA], syn_type=ACh, weight_coef=0.005)
connect(pptg[pptg_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.005)

if noradrenaline_flag:

    logger.debug("* * * Making neuromodulating connections...")


    #vt_ex = nest.Create('volume_transmitter')
    #vt_in = nest.Create('volume_transmitter')
    #NORA_synparams_ex['vt'] = vt_ex[0]
    #NORA_synparams_in['vt'] = vt_in[0]

    connect(nts[nts_a1], lc[lc_N0], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a1], bnst[bnst_Glu], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], lc[lc_N1], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], striatum[striatum_tan], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], striatum[striatum_GABA], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], amygdala[amygdala_Glu], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], amygdala[amygdala_Ach], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], amygdala[amygdala_GABA], syn_type=NA_ex, weight_coef=0.005)
    connect(nts[nts_a2], bnst[bnst_Glu], syn_type=NA_ex, weight_coef=0.005)

    connect(lc[lc_N0], motor[motor_Glu0], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N0], motor[motor_Glu1], syn_type=NA_ex, weight_coef=0.005)

    connect(lc[lc_N0], prefrontal[pfc_Glu1], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N0], vta[vta_a1], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N0], ldt[ldt_a1], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N0], ldt[ldt_a2], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N1], striatum[striatum_tan], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N1], striatum[striatum_GABA], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N1], rn[rn_a1], syn_type=NA_ex, weight_coef=0.005)
    connect(lc[lc_N1], rn[rn_a2], syn_type=NA_ex, weight_coef=0.005)
    connect(rn[rn_a1], rn[rn_dr], syn_type=NA_ex, weight_coef=0.005)
    connect(rn[rn_a2], rn[rn_mnr], syn_type=NA_ex, weight_coef=0.005)
    connect(rn[rn_a2], rn[rn_rpa], syn_type=NA_ex, weight_coef=0.005)
    connect(rn[rn_a2], rn[rn_rmg], syn_type=NA_ex, weight_coef=0.005)

    #connect(vta[vta_a1], vta[vta_DA1], syn_type=NA_in, weight_coef=0.005)

if serotonin_flag:
        # * * * AFFERENT PROJECTIONS * *
    connect(vta[vta_5HT], rn[rn_dr], syn_type=SERO_ex, weight_coef=wse)
    connect(septum[septum_5HT], rn[rn_dr], syn_type=SERO_ex, weight_coef=wse)
    connect(septum[septum_5HT], rn[rn_mnr], syn_type=SERO_ex, weight_coef=wse)
    connect(prefrontal[pfc_5HT], rn[rn_dr], syn_type=SERO_ex, weight_coef=wse)
    connect(prefrontal[pfc_5HT], rn[rn_mnr], syn_type=SERO_ex, weight_coef=wse)
    connect(hypothalamus[hypothalamus_5HT], rn[rn_rmg], syn_type=SERO_ex, weight_coef=wse)
    connect(hypothalamus[hypothalamus_5HT], rn[rn_rpa], syn_type=SERO_ex, weight_coef=wse)
    connect(periaqueductal_gray[periaqueductal_gray_5HT], rn[rn_rmg], syn_type=SERO_ex, weight_coef=wse)
    connect(periaqueductal_gray[periaqueductal_gray_5HT], rn[rn_rpa], syn_type=SERO_ex, weight_coef=wse)
    connect(bnst[bnst_5HT], rn[rn_rpa], syn_type=SERO_ex, weight_coef=wse)
    connect(amygdala[amygdala_5HT], rn[rn_rpa], syn_type=SERO_ex, weight_coef=wse)
    connect(amygdala[amygdala_5HT], rn[rn_rmg], syn_type=SERO_ex, weight_coef=wse)
    connect(hippocampus[hippocampus_5HT], rn[rn_dr], syn_type=SERO_ex, weight_coef=wse)

    # * * * EFFERENT PROJECTIONS * * *
    connect(rn[rn_dr], striatum[striatum_5HT], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], striatum[striatum_D2], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], striatum[striatum_GABA], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], striatum[striatum_Ach], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], nac[nac_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], nac[nac_GABA0], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], nac[nac_GABA1], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], nac[nac_Ach], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], nac[nac_DA], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], snr[snr_GABA], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], septum[septum_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=wsi) #? tune weights
    connect(rn[rn_dr], thalamus[thalamus_Glu], syn_type=SERO_in, weight_coef=wsi) #? tune weights
    connect(rn[rn_dr], lateral_cortex[lateral_cortex_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], entorhinal_cortex[entorhinal_cortex_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], prefrontal[pfc_5HT], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], prefrontal[pfc_Glu0], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], prefrontal[pfc_Glu1], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], prefrontal[pfc_DA], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], prefrontal[pfc_NA], syn_type=SERO_in, weight_coef=wsi) #!!!
    connect(rn[rn_dr], lateral_tegmental_area[lateral_tegmental_area_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], lc[lc_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], lc[lc_N0], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], bnst[bnst_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], bnst[bnst_Glu], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], bnst[bnst_GABA], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], bnst[bnst_Ach], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], hippocampus[hippocampus_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], amygdala[amygdala_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], amygdala[amygdala_Glu], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], amygdala[amygdala_GABA], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_dr], amygdala[amygdala_Ach], syn_type=SERO_in, weight_coef=wsi)

    connect(rn[rn_mnr], vta[vta_5HT], syn_type=SERO_in, weight_coef=wsi) #!!! 0.005
    connect(rn[rn_mnr], vta[vta_a1], syn_type=SERO_in, weight_coef=wsi) #!!! 0.005
    connect(rn[rn_mnr], vta[vta_DA1], syn_type=SERO_in, weight_coef=wsi) #!!! 0.005
    connect(rn[rn_mnr], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=wsi) #?
    connect(rn[rn_mnr], thalamus[thalamus_Glu], syn_type=SERO_in, weight_coef=wsi) #? tune weights 0.005
    connect(rn[rn_mnr], prefrontal[pfc_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], prefrontal[pfc_Glu0], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], prefrontal[pfc_Glu1], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], motor[motor_Glu0], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], motor[motor_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], insular_cortex[insular_cortex_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], medial_cortex[medial_cortex_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], neocortex[neocortex_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], hypothalamus[hypothalamus_5HT], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], hypothalamus[hypothalamus_pvn_GABA], syn_type=SERO_in, weight_coef=wsi)
    connect(rn[rn_mnr], hippocampus[hippocampus_5HT], syn_type=SERO_in, weight_coef=wsi)

    # * * * THALAMOCORTICAL PATHWAY * * *
    connect(thalamus[thalamus_5HT], prefrontal[pfc_5HT], syn_type=SERO_in, weight_coef=wse)
    connect(thalamus[thalamus_5HT], motor[motor_5HT], syn_type=SERO_ex, weight_coef=wse)
    connect(thalamus[thalamus_5HT], motor[motor_Glu0], syn_type=SERO_ex, weight_coef=wse)
    connect(prefrontal[pfc_5HT], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=wsi) # main was 0.005
    connect(motor[motor_5HT], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=wsi) # main was 0.005

if dopamine_flag:
    logger.debug("* * * Making neuromodulating connections...")
    # NIGROSTRIATAL
    
    connect(snc[snc_DA], striatum[striatum_D1], syn_type=DA_ex)
    connect(snc[snc_DA], gpe[gpe_GABA], syn_type=DA_ex)
    connect(snc[snc_DA], stn[stn_Glu], syn_type=DA_ex)
    connect(snc[snc_DA], nac[nac_GABA0], syn_type=DA_ex)
    connect(snc[snc_DA], nac[nac_GABA1], syn_type=DA_ex)
    connect(snc[snc_DA], striatum[striatum_D2], syn_type=DA_in)
    connect(snc[snc_DA], striatum[striatum_tan], syn_type=DA_in)

    # MESOCORTICOLIMBIC
    connect(vta[vta_DA0], striatum[striatum_D1], syn_type=DA_ex)
    connect(vta[vta_DA0], striatum[striatum_D2], syn_type=DA_in)
    connect(vta[vta_DA0], prefrontal[pfc_Glu0], syn_type=DA_ex)
    connect(vta[vta_DA0], prefrontal[pfc_Glu1], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA0], syn_type=DA_ex)
    connect(vta[vta_DA1], nac[nac_GABA1], syn_type=DA_ex)

if dopamine_flag and serotonin_flag and noradrenaline_flag:
    # * * * DOPAMINE INTERACTION * * *
    connect(prefrontal[pfc_5HT], prefrontal[pfc_DA], syn_type=SERO_ex, weight_coef=wse)
    connect(prefrontal[pfc_DA], vta[vta_5HT], syn_type=DA_in, weight_coef=0.005)
    connect(prefrontal[pfc_DA], vta[vta_DA1], syn_type=DA_in, weight_coef=0.005)
    #connect(vta[vta_5HT], vta[vta_DA1], syn_type=SERO_in, weight_coef=0.005)
    connect(vta[vta_5HT], vta[vta_DA1], syn_type=SERO_ex, weight_coef=wse)
    connect(vta[vta_DA1], prefrontal[pfc_5HT], syn_type=DA_ex, weight_coef=0.005)
    connect(vta[vta_DA1], prefrontal[pfc_DA], syn_type=DA_ex, weight_coef=0.005)
    #connect(vta[vta_DA1], striatum[striatum_5HT], syn_type=DOPA_in, weight_coef=0.005)
    connect(vta[vta_DA1], striatum[striatum_5HT], syn_type=DA_ex, weight_coef=0.005)
    #connect(vta[vta_DA1], striatum[striatum_DA], syn_type=DOPA_in, weight_coef=0.005)
    connect(vta[vta_DA1], striatum[striatum_D1], syn_type=DA_ex, weight_coef=0.005)
    #connect(vta[vta_DA1], nac[nac_5HT], syn_type=DOPA_in, weight_coef=0.005)
    connect(vta[vta_DA1], nac[nac_5HT], syn_type=DA_ex, weight_coef=0.005)
    #connect(vta[vta_DA1], nac[nac_DA], syn_type=DOPA_in, weight_coef=0.005)
    connect(vta[vta_DA1], nac[nac_DA], syn_type=DA_ex, weight_coef=0.005)
    #connect(striatum[striatum_5HT], striatum[striatum_DA], syn_type=SERO_in, weight_coef=0.005)
    connect(striatum[striatum_5HT], striatum[striatum_D1], syn_type=SERO_ex, weight_coef=wse) #??????????????????????????????????? D1, D2?
    #connect(striatum[striatum_DA],  snr[snr_GABA], syn_type=DOPA_in, weight_coef=0.005)
    connect(striatum[striatum_D1], snr[snr_GABA], syn_type=DA_ex, weight_coef=0.005)
    #connect(striatum[striatum_DA],  snc[snc_DA], syn_type=DOPA_in, weight_coef=0.005)
    connect(striatum[striatum_D1], snc[snc_GABA], syn_type=DA_ex, weight_coef=0.005)
    connect(striatum[striatum_D1], snc[snc_DA], syn_type=DA_ex, weight_coef=0.005)
    connect(nac[nac_5HT], nac[nac_DA], syn_type=SERO_ex, weight_coef=wse)
    connect(snr[snr_GABA], snc[snc_DA], syn_type=SERO_in, weight_coef=wsi)
    connect(snc[snc_GABA], striatum[striatum_5HT], syn_type=DA_in, weight_coef=0.005) #?
    connect(snc[snc_DA], striatum[striatum_5HT], syn_type=DA_in, weight_coef=0.005)
    connect(snc[snc_DA], striatum[striatum_D1], syn_type=DA_in, weight_coef=0.005)
    connect(snc[snc_DA], nac[nac_5HT], syn_type=DA_in, weight_coef=0.005)
    connect(snc[snc_DA], nac[nac_DA], syn_type=DA_in, weight_coef=0.005)
    connect(lc[lc_5HT], lc[lc_D1], syn_type=SERO_ex, weight_coef=0.005)
    connect(lc[lc_D1], rn[rn_dr], syn_type=DA_ex, weight_coef=0.005)

    # * * * NORADRENALINE INTERACTION * * *
    connect(lc[lc_5HT], lc[lc_N0], syn_type=SERO_in, weight_coef=0.005)
    connect(lc[lc_5HT], lc[lc_N1], syn_type=SERO_in, weight_coef=0.005)



logger.debug("* * * Attaching spike generators...")

"""
connect_generator(nts[nts_a1], 400., 600., rate=250, coef_part=1)
connect_generator(nts[nts_a2], 400., 600., rate=250, coef_part=1)
connect_generator(prh[prh_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pgi[pgi_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pgi[pgi_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(ldt[ldt_a1], 400., 600., rate=250, coef_part=1)
connect_generator(ldt[ldt_a2], 400., 600., rate=250, coef_part=1)
connect_generator(ldt[ldt_Ach], 400., 600., rate=250, coef_part=1)
connect_generator(lc[lc_N0], 400., 600., rate=250, coef_part=1)
#connect_generator(lc[lc_N1], 400., 600., rate=250, coef_part=1)

connect_generator(prefrontal[pfc_5HT], 400., 600., rate=250, coef_part=1)
connect_generator(motor[motor_5HT], 400., 600., rate=250, coef_part=1)
connect_generator(rn[rn_dr], 400., 600., rate=250, coef_part=1)
connect_generator(rn[rn_mnr], 400., 600., rate=250, coef_part=1)

connect_generator(motor[motor_Glu0], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)
"""

#################################surprise
"""
connect_generator(nts[nts_a1], 100., 250., rate=250, coef_part=1)
connect_generator(nts[nts_a2], 100., 250., rate=250, coef_part=1)
connect_generator(prh[prh_GABA], 100., 250., rate=250, coef_part=1)
connect_generator(pgi[pgi_GABA], 100., 250., rate=250, coef_part=1)
connect_generator(pgi[pgi_Glu], 100., 250., rate=250, coef_part=1)
connect_generator(ldt[ldt_a1], 100., 250., rate=250, coef_part=1)
connect_generator(ldt[ldt_a2], 100., 250., rate=250, coef_part=1)
connect_generator(ldt[ldt_Ach], 100., 250., rate=250, coef_part=1)
connect_generator(lc[lc_N0], 100., 250., rate=250, coef_part=1)
#connect_generator(lc[lc_N1], 100., 250., rate=250, coef_part=1)

connect_generator(prefrontal[pfc_5HT], 100., 250., rate=250, coef_part=1)
connect_generator(motor[motor_5HT], 100., 250., rate=250, coef_part=1)
connect_generator(rn[rn_dr], 100., 250., rate=250, coef_part=1)
connect_generator(rn[rn_mnr], 100., 250., rate=250, coef_part=1)
"""


############################anger/rage
"""
connect_generator(nts[nts_a1], 400., 600., rate=250, coef_part=1)
connect_generator(nts[nts_a2], 400., 600., rate=250, coef_part=1)
connect_generator(prh[prh_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pgi[pgi_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pgi[pgi_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(ldt[ldt_a1], 400., 600., rate=250, coef_part=1)
connect_generator(ldt[ldt_a2], 400., 600., rate=250, coef_part=1)
connect_generator(ldt[ldt_Ach], 400., 600., rate=250, coef_part=1)
connect_generator(lc[lc_N0], 400., 600., rate=250, coef_part=1)
#connect_generator(lc[lc_N1], 400., 600., rate=250, coef_part=1)

connect_generator(motor[motor_Glu0], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)1)
"""

"""
#####################surprise
connect_generator(nts[nts_a1], 400., 600., rate=100, coef_part=1)
connect_generator(nts[nts_a2], 400., 600., rate=100, coef_part=1)
connect_generator(prh[prh_GABA], 400., 600., rate=100, coef_part=1)
connect_generator(pgi[pgi_GABA], 400., 600., rate=100, coef_part=1)
connect_generator(pgi[pgi_Glu], 400., 600., rate=100, coef_part=1)
connect_generator(ldt[ldt_a1], 400., 600., rate=100, coef_part=1)
connect_generator(ldt[ldt_a2], 400., 600., rate=100, coef_part=1)
connect_generator(ldt[ldt_Ach], 400., 600., rate=100, coef_part=1)
connect_generator(lc[lc_N0], 400., 600., rate=100, coef_part=1)
connect_generator(lc[lc_N1], 400., 600., rate=100, coef_part=1)

connect_generator(cerebral_cortex[cerebral_cortex_5HT], 300., 600., rate=250, coef_part=1)
connect_generator(dr[dr_5HT], 300., 600., rate=250, coef_part=1)
connect_generator(mnr[mnr_5HT], 300., 600., rate=250, coef_part=1)
"""

"""
######################distress/anguish
connect_generator(nts[nts_a1], 400., 600., rate=100, coef_part=1)
connect_generator(nts[nts_a2], 400., 600., rate=100, coef_part=1)
connect_generator(prh[prh_GABA], 400., 600., rate=100, coef_part=1)
connect_generator(pgi[pgi_GABA], 400., 600., rate=100, coef_part=1)
connect_generator(pgi[pgi_Glu], 400., 600., rate=100, coef_part=1)
connect_generator(ldt[ldt_a1], 400., 600., rate=100, coef_part=1)
connect_generator(ldt[ldt_a2], 400., 600., rate=100, coef_part=1)
connect_generator(ldt[ldt_Ach], 400., 600., rate=100, coef_part=1)
connect_generator(lc[lc_N0], 400., 600., rate=100, coef_part=1)
connect_generator(lc[lc_N1], 400., 600., rate=100, coef_part=1)
"""

"""
##############################enjoyment/joy
connect_generator(cerebral_cortex[cerebral_cortex_5HT], 300., 600., rate=250, coef_part=1)
connect_generator(dr[dr_5HT], 300., 600., rate=250, coef_part=1)
connect_generator(mnr[mnr_5HT], 300., 600., rate=250, coef_part=1)

connect_generator(motor[motor_Glu0], 200., 600., rate=300, coef_part=1)
connect_generator(pptg[pptg_GABA], 200., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_Glu], 200., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_ACh], 200., 600., rate=250, coef_part=1)
connect_generator(amygdala[amygdala_Glu], 200., 600., rate=250, coef_part=1)
connect_generator(snc[snc_DA], 200., 600., rate=250, coef_part=1)
connect_generator(vta[vta_DA0], 200., 600., rate=250, coef_part=1)
"""


#########################contempt/disgust
connect_generator(prefrontal[pfc_5HT], 100., 250., rate=250, coef_part=1)
connect_generator(motor[motor_5HT], 100., 250., rate=250, coef_part=1)
connect_generator(rn[rn_dr], 100., 250., rate=250, coef_part=1)
connect_generator(rn[rn_mnr], 100., 250., rate=250, coef_part=1)


################################fear/terror
connect_generator(motor[motor_Glu0], 400., 600., rate=250, coef_part=1)
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
