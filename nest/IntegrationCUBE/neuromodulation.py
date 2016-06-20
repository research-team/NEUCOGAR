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
NORA_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
SERO_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
SERO_synparams_in['vt'] = nest.Create('volume_transmitter')[0]

nest.CopyModel('static_synapse', gen_static_syn, static_syn)
nest.CopyModel('stdp_synapse', glu_synapse, STDP_synparams_Glu)
nest.CopyModel('stdp_synapse', gaba_synapse, STDP_synparams_GABA)
nest.CopyModel('stdp_synapse', ach_synapse, STDP_synparams_ACh)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_in, DOPA_synparams_in)
nest.CopyModel('stdp_dopamine_synapse', nora_synapse_ex, NORA_synparams_ex)

nest.CopyModel('stdp_serotonine_synapse', sero_synapse_ex, SERO_synparams_ex)
nest.CopyModel('stdp_serotonine_synapse', sero_synapse_in, SERO_synparams_in)



# = = = = = = = = = = = = = = = = = = =
# N  O  R  A  D  R  E  N  A  L  I  N  E
# = = = = = = = = = = = = = = = = = = =


logger.debug("* * * Start connection initialisation")
# connect(LC[LC_NA_0], Prefrontalcortex[Prefrontalcortex_Glu_1], syn_type=NA_ex, weight_coef=1.0)
connect(LC[LC_NA_0], Prefrontalcortex[Prefrontalcortex_Glu_0], syn_type=NA_ex, weight_coef=1.)
# connect(LC[LC_NA_0], Prefrontalcortex[Prefrontalcortex_Glu_1], syn_type=NA_ex, weight_coef=1.0)
# connect(LC[LC_NA_0], Motorcortex[Motorcortex_Glu], syn_type=NA_ex, weight_coef=1.0)
# connect(LC[LC_NA_0], VTA[VTA_a1], syn_type=NA_ex, weight_coef=1.0)
# connect(LC[LC_NA_0], LTD[LTD_a1], syn_type=NA_ex, weight_coef=1.0)
# connect(LC[LC_NA_0], LTD[LTD_a2], syn_type=NA_ex, weight_coef=1.0)
# connect(LC[LC_Ach], LC[LC_NA_0], syn_type=ACh, weight_coef=1.0)
# connect(LC[LC_Ach], LC[LC_GABA], syn_type=ACh, weight_coef=1.0)
# connect(LC[LC_Ach], LC[LC_NA_1], syn_type=ACh, weight_coef=1.0)
# connect(LC[LC_GABA], LC[LC_NA_0], syn_type=GABA, weight_coef=1.0)
# connect(LC[LC_D1], LC[LC_NA_0], syn_type=DA_ex, weight_coef=1.0)
# #inhibitory???
# connect(LC[LC_D2], LC[LC_NA_1], syn_type=DA_in, weight_coef=1.0)
# connect(LC[LC_NA_1], RN[RN_a2], syn_type=NA_ex, weight_coef=1.0)
# connect(LC[LC_NA_1], RN[RN_a1], syn_type=NA_ex, weight_coef=1.0)
# # JS
# connect(LC[LC_NA_1], AcbShell[AcbShell_GABA_1], syn_type=NA_ex, weight_coef=1.0)
# #
#
# connect(PGI[PGI_GABA], LC[LC_GABA], syn_type=GABA, weight_coef=1.0)
# connect(PGI[PGI_Glu], LC[LC_NA_0], syn_type=Glu, weight_coef=1.0)
# connect(PGI[PGI_Glu], LC[LC_NA_1], syn_type=Glu, weight_coef=1.0)
#
connect(BNST[BNST_Glu], BNST[BNST_GABA], syn_type=Glu, weight_coef=10)
connect(BNST[BNST_GABA], PVN[PVN_GABA], syn_type=GABA, weight_coef=1.0)
# connect(BNST[BNST_Ach], Amy[Amy_Ach], syn_type=ACh, weight_coef=1.0)
#
# connect(Amy[Amy_Glu], AcbShell[AcbShell_GABA_1], syn_type=Glu, weight_coef=1.0)
# connect(Amy[Amy_Glu], AcbCore[AcbCore_Ach], syn_type=Glu, weight_coef=1.0)
# connect(Amy[Amy_Glu], AcbCore[AcbCore_GABA_0], syn_type=Glu, weight_coef=1.0)
# connect(Amy[Amy_Ach], LC[LC_NA_0], syn_type=ACh, weight_coef=1.0)
# connect(Amy[Amy_Ach], LC[LC_Ach], syn_type=ACh, weight_coef=1.0)
# connect(Amy[Amy_Ach], LC[LC_GABA], syn_type=ACh, weight_coef=1.0)
# connect(Amy[Amy_Ach], LC[LC_D1], syn_type=ACh, weight_coef=1.0)
# connect(Amy[Amy_Ach], LC[LC_D2], syn_type=ACh, weight_coef=1.0)
# connect(Amy[Amy_Ach], LC[LC_NA_1], syn_type=ACh, weight_coef=1.0)
# connect(Amy[Amy_GABA], BNST[BNST_GABA], syn_type=GABA, weight_coef=1.0)
#
# connect(RN[RN_5HT], LC[LC_NA_0], syn_type=SERO_in, weight_coef=1.0)
# connect(RN[RN_a1], RN[RN_5HT], syn_type=NA_ex, weight_coef=1.0)
# connect(RN[RN_a2], RN[RN_5HT], syn_type=NA_ex, weight_coef=1.0)
#
# connect(Thalamus[Thalamus_Glu], Motorcortex[Motorcortex_Glu], syn_type=Glu, weight_coef=1.0)
#
connect(PVN[PVN_GABA], Motorcortex[Motorcortex_Glu], syn_type=GABA, weight_coef=1.0)
#
# connect(LTD[LTD_Ach], BNST[BNST_Ach], syn_type=ACh, weight_coef=1.0)
# connect(LTD[LTD_Ach], LC[LC_NA_0], syn_type=ACh, weight_coef=1.0)
# connect(LTD[LTD_Ach], Thalamus[Thalamus_Glu], syn_type=ACh, weight_coef=1.0)
# connect(LTD[LTD_Ach], Prefrontalcortex[Prefrontalcortex_Glu_1], syn_type=ACh, weight_coef=1.0)
# connect(LTD[LTD_Ach], Prefrontalcortex[Prefrontalcortex_Glu_0], syn_type=ACh, weight_coef=1.000000000)
#
# connect(PrH[PrH_GABA], LC[LC_GABA], syn_type=GABA, weight_coef=1.000000000)
#
# connect(Prefrontalcortex[Prefrontalcortex_Glu_1], LC[LC_NA_0], syn_type=Glu, weight_coef=1.000000000)
connect(Prefrontalcortex[Prefrontalcortex_Glu_0], BNST[BNST_Glu], syn_type=Glu, weight_coef=1.)
#
# connect(VTA[VTA_DA_0], LC[LC_D1], syn_type=DA_ex, weight_coef=1.000000000)
# #inhibitory????
# connect(VTA[VTA_DA_0], LC[LC_D2], syn_type=DA_in, weight_coef=1.000000000)
# connect(VTA[VTA_DA_0], Prefrontalcortex[Prefrontalcortex_Glu_1], syn_type=DA_ex, weight_coef=1.000000000)
# connect(VTA[VTA_DA_0], Prefrontalcortex[Prefrontalcortex_Glu_0], syn_type=DA_ex, weight_coef=1.000000000)
# #JS
# connect(VTA[VTA_DA_1], AcbShell[AcbShell_GABA_1], syn_type=DA_ex, weight_coef=1.000000000)
# #JS
# connect(VTA[VTA_a1], VTA[VTA_DA_1], syn_type=NA_ex, weight_coef=1.000000000)
#
# connect(Aa[Aa_NA], LC[LC_NA_0], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Aa[Aa_NA], LC[LC_Ach], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Aa[Aa_NA], LC[LC_GABA], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Aa[Aa_NA], LC[LC_D1], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Aa[Aa_NA], LC[LC_D2], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Aa[Aa_NA], LC[LC_NA_1], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Aa[Aa_NA], BNST[BNST_Glu], syn_type=NA_ex, weight_coef=10.000000000)
#
# #JS
# connect(Ab[Ab_NA], LC[LC_NA_0], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], LC[LC_Ach], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], LC[LC_GABA], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], LC[LC_D1], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], LC[LC_D2], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], LC[LC_NA_1], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], AcbShell[AcbShell_GABA_1], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], Amy[Amy_Ach], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], Amy[Amy_Glu], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], Amy[Amy_GABA], syn_type=NA_ex, weight_coef=1.000000000)
# connect(Ab[Ab_NA], BNST[BNST_Glu], syn_type=NA_ex, weight_coef=1.000000000)
#

connect(Motorcortex[Motorcortex_Glu], LC[LC_NA_0], syn_type=Glu, weight_coef=0.05)

logger.debug("* * * Creating spike generators...")
if generator_flag:
    #connect_generator(Aa[Aa_NA], startTime=200., stopTime=800., rate=250., coef_part=1)
    connect_generator(Motorcortex[Motorcortex_Glu], rate=250, coef_part=1)






# = = = = = = = = = = = =
# D  O  P  A  M  I  N  E
# = = = = = = = = = = = =


logger.debug("* * * Start connection initialisation")
# * * * NIGROSTRIATAL PATHWAY* * *
connect(motor[motor_Glu0], striatum[D1], syn_type=Glu, weight_coef=0.005)
connect(motor[motor_Glu0], snc[snc_DA], syn_type=Glu, weight_coef=0.000005)
connect(motor[motor_Glu0], striatum[D2], syn_type=Glu, weight_coef=0.05)
connect(motor[motor_Glu0], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.008)
connect(motor[motor_Glu0], stn[stn_Glu], syn_type=Glu, weight_coef=7)
connect(motor[motor_Glu1], striatum[D1], syn_type=Glu)
connect(motor[motor_Glu1], striatum[D2], syn_type=Glu)
connect(motor[motor_Glu1], thalamus[thalamus_Glu], syn_type=Glu)
connect(motor[motor_Glu1], stn[stn_Glu], syn_type=Glu)
connect(motor[motor_Glu1], nac[nac_GABA0])

connect(striatum[tan], striatum[D1])
connect(striatum[tan], striatum[D2], syn_type=Glu)

connect(striatum[D1], snr[snr_GABA], weight_coef=0.00001)
connect(striatum[D1], gpi[gpi_GABA], weight_coef=0.00001)
connect(striatum[D1], gpe[gpe_GABA], weight_coef=0.000005)
connect(striatum[D2], gpe[gpe_GABA], weight_coef=1)

connect(gpe[gpe_GABA], stn[stn_Glu], weight_coef=0.0001)
connect(gpe[gpe_GABA], striatum[D1], weight_coef=0.001)
connect(gpe[gpe_GABA], striatum[D2], weight_coef=0.3)
onnect(snc[snc_DA], gpe[gpe_GABA], weight_coef=0.3, syn_type=DA_ex)
onnect(amygdala[amygdala_Glu], gpe[gpe_GABA], weight_coef=0.3, syn_type=Glu)
onnect(gpe[gpe_GABA], amygdala[amygdala_Glu], weight_coef=0.1, syn_type=Glu)
onnect(gpe[gpe_GABA], snc[snc_DA], weight_coef=0.2, syn_type=GABA)
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
connect_generator(gpe[gpi_GABA], rate=300, coef_part=1)
connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
connect_generator(snc[snc_DA], 200., 400., rate=250, coef_part=1)
#connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)






# = = = = = = = = = = = = = = =
# S  E  R  O  T  O  N  I  N  E
# = = = = = = = = = = = = = = =


logger.debug("* * * Start connection initialisation")
# * * * AFFERENT PROJECTIONS * *
connect(basal_ganglia[basal_ganglia_5HT], dr[dr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(basal_ganglia[basal_ganglia_5HT], mnr[mnr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(basal_ganglia[basal_ganglia_5HT], rmg[rmg_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(basal_ganglia[basal_ganglia_5HT], rpa[rpa_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(vta[vta_5HT], dr[dr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(septum[septum_5HT], dr[dr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(septum[septum_5HT], mnr[mnr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(pfc[pfc_5HT], dr[dr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(pfc[pfc_5HT], mnr[mnr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(pons[pons_5HT], mnr[mnr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(hypothalamus[hypothalamus_5HT], rmg[rmg_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(hypothalamus[hypothalamus_5HT], rpa[rpa_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(periaqueductal_gray[periaqueductal_gray_5HT], rmg[rmg_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(periaqueductal_gray[periaqueductal_gray_5HT], rpa[rpa_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(bed_nucleus_of_the_stria_terminalis[bed_nucleus_of_the_stria_terminalis_5HT], rpa[rpa_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(reticular_formation[reticular_formation_5HT], dr[dr_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(reticular_formation[reticular_formation_5HT], rpa[rpa_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(reticular_formation[reticular_formation_5HT], rmg[rmg_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(amygdala[amygdala_5HT], rpa[rpa_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(amygdala[amygdala_5HT], rmg[rmg_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(hippocampus[hippocampus_5HT], dr[dr_5HT], syn_type=SERO_ex, weight_coef=0.005)

# * * * EFFERENT PROJECTIONS * * *
connect(dr[dr_5HT], basal_ganglia[basal_ganglia_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], striatum[striatum_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], nac[nac_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], substantia_nigra[substantia_nigra_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], septum[septum_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], lateral_cortex[lateral_cortex_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], entorhinal_cortex[entorhinal_cortex_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], pfc[pfc_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], lateral_tegmental_area[lateral_tegmental_area_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], locus_coeruleus[locus_coeruleus_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], bed_nucleus_of_the_stria_terminalis[bed_nucleus_of_the_stria_terminalis_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], amygdala[amygdala_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(dr[dr_5HT], hippocampus[hippocampus_5HT], syn_type=SERO_in, weight_coef=0.005)

connect(mnr[mnr_5HT], vta[vta_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], cerebral_cortex[cerebral_cortex_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], insular_cortex[insular_cortex_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], medial_cortex[medial_cortex_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], neocortex[neocortex_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], hypothalamus[hypothalamus_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(mnr[mnr_5HT], hippocampus[hippocampus_5HT], syn_type=SERO_in, weight_coef=0.005)

# * * * THALAMOCORTICAL PATHWAY * * *
connect(thalamus[thalamus_5HT], cerebral_cortex[cerebral_cortex_5HT], syn_type=SERO_ex, weight_coef=0.005)
#connect(cerebral_cortex[cerebral_cortex_5HT], thalamus[thalamus_5HT], syn_type=SERO_in, weight_coef=0.005)
connect(cerebral_cortex[cerebral_cortex_5HT], thalamus[thalamus_5HT], syn_type=SERO_ex, weight_coef=0.005)
connect(cerebral_cortex[cerebral_cortex_5HT], basal_ganglia[basal_ganglia_5HT], syn_type=SERO_ex, weight_coef=0.005)

# * * * DOPAMINE INTERACTION * * *
connect(pfc[pfc_5HT], pfc[pfc_DA], syn_type=SERO_ex, weight_coef=0.005)
connect(pfc[pfc_DA], vta[vta_5HT], syn_type=DOPA_in, weight_coef=0.005)
connect(pfc[pfc_DA], vta[vta_DA], syn_type=DOPA_in, weight_coef=0.005)
#connect(vta[vta_5HT], vta[vta_DA], syn_type=SERO_in, weight_coef=0.005)
connect(vta[vta_5HT], vta[vta_DA], syn_type=SERO_ex, weight_coef=0.005)
connect(vta[vta_DA], pfc[pfc_5HT], syn_type=DOPA_ex, weight_coef=0.005)
connect(vta[vta_DA], pfc[pfc_DA], syn_type=DOPA_ex, weight_coef=0.005)
#connect(vta[vta_DA], striatum[striatum_5HT], syn_type=DOPA_in, weight_coef=0.005)
connect(vta[vta_DA], striatum[striatum_5HT], syn_type=DOPA_ex, weight_coef=0.005)
#connect(vta[vta_DA], striatum[striatum_DA], syn_type=DOPA_in, weight_coef=0.005)
connect(vta[vta_DA], striatum[striatum_DA], syn_type=DOPA_ex, weight_coef=0.005)
#connect(vta[vta_DA], nac[nac_5HT], syn_type=DOPA_in, weight_coef=0.005)
connect(vta[vta_DA], nac[nac_5HT], syn_type=DOPA_ex, weight_coef=0.005)
#connect(vta[vta_DA], nac[nac_DA], syn_type=DOPA_in, weight_coef=0.005)
connect(vta[vta_DA], nac[nac_DA], syn_type=DOPA_ex, weight_coef=0.005)
#connect(striatum[striatum_5HT], striatum[striatum_DA], syn_type=SERO_in, weight_coef=0.005)
connect(striatum[striatum_5HT], striatum[striatum_DA], syn_type=SERO_ex, weight_coef=0.005)
#connect(striatum[striatum_DA],  substantia_nigra[substantia_nigra_5HT], syn_type=DOPA_in, weight_coef=0.005)
connect(striatum[striatum_DA],  substantia_nigra[substantia_nigra_5HT], syn_type=DOPA_ex, weight_coef=0.005)
#connect(striatum[striatum_DA],  substantia_nigra[substantia_nigra_DA], syn_type=DOPA_in, weight_coef=0.005)
connect(striatum[striatum_DA],  substantia_nigra[substantia_nigra_DA], syn_type=DOPA_ex, weight_coef=0.005)
connect(nac[nac_5HT], nac[nac_DA], syn_type=SERO_ex, weight_coef=0.005)
connect(substantia_nigra[substantia_nigra_5HT], substantia_nigra[substantia_nigra_DA], syn_type=SERO_in, weight_coef=0.005)
connect(substantia_nigra[substantia_nigra_DA], striatum[striatum_5HT], syn_type=DOPA_in, weight_coef=0.005)
connect(substantia_nigra[substantia_nigra_DA], striatum[striatum_DA], syn_type=DOPA_in, weight_coef=0.005)
connect(substantia_nigra[substantia_nigra_DA], nac[nac_5HT], syn_type=DOPA_in, weight_coef=0.005)
connect(substantia_nigra[substantia_nigra_DA], nac[nac_DA], syn_type=DOPA_in, weight_coef=0.005)
connect(locus_coeruleus[locus_coeruleus_5HT], locus_coeruleus[locus_coeruleus_DA], syn_type=SERO_ex, weight_coef=0.005)
connect(locus_coeruleus[locus_coeruleus_DA], dr[dr_5HT], syn_type=DOPA_ex, weight_coef=0.005)

# * * * NORADRENALINE INTERACTION * * *
connect(locus_coeruleus[locus_coeruleus_5HT], locus_coeruleus[locus_coeruleus_NA], syn_type=SERO_in, weight_coef=0.005)
connect(locus_coeruleus[locus_coeruleus_NA], rostral_group[rostral_group_A1], syn_type=NORA_ex, weight_coef=0.005)
connect(locus_coeruleus[locus_coeruleus_NA], rostral_group[rostral_group_A2], syn_type=NORA_ex, weight_coef=0.005)
connect(rostral_group[rostral_group_A1], dr[dr_5HT], syn_type=NORA_ex, weight_coef=0.005)
connect(rostral_group[rostral_group_A2], dr[dr_5HT], syn_type=NORA_ex, weight_coef=0.005)
connect(rostral_group[rostral_group_A1], mnr[mnr_5HT], syn_type=NORA_ex, weight_coef=0.005)
connect(rostral_group[rostral_group_A2], mnr[mnr_5HT], syn_type=NORA_ex, weight_coef=0.005)


logger.debug("* * * Creating spike generators...")
if generator_flag:
    connect_generator(thalamus[thalamus_5HT], rate=300, coef_part=1)
    connect_generator(pons[pons_5HT], 400., 600., rate=250, coef_part=1)
    connect_generator(periaqueductal_gray[periaqueductal_gray_5HT], 400., 600., rate=250, coef_part=1)
    connect_generator(reticular_formation[reticular_formation_5HT], 400., 600., rate=250, coef_part=1)




# = = = = = = = = = = = = = = = = = =
# C  O  M  M  O  N   P  A  R  A  M  S
# = = = = = = = = = = = = = = = = = =

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