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
    # connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
    # connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
    # connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
    # connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
    # connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
    # connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)


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