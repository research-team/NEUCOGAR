# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there are some mistakes in neuron parameters! Write to alexey.panzer@gmail.com.

from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': number_of_threads, 'resolution': 0.1})

generate_neurons(NN)

# Init parameters of our synapse models
NORA_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
NORA_synparams_in['vt'] = nest.Create('volume_transmitter')[0]
nest.CopyModel('static_synapse', gen_static_syn, static_syn)
nest.CopyModel('stdp_synapse', glu_synapse, STDP_synparams_Glu)
nest.CopyModel('stdp_synapse', gaba_synapse, STDP_synparams_GABA)
nest.CopyModel('stdp_synapse', ach_synapse, STDP_synparams_ACh)
nest.CopyModel('stdp_noradrenaline_synapse', nora_synapse_ex, NORA_synparams_ex)
nest.CopyModel('stdp_noradrenaline_synapse', nora_synapse_in, NORA_synparams_in)


logger.debug("* * * Start connection initialisation")

add_connection(motor[motor_cortex], lc[locus_coeruleus], syn_type=Glu, weight_coef=0.005)

add_connection(pf[prefrontal_cortex], lc[locus_coeruleus], syn_type=Glu, weight_coef=0.005)
add_connection(pf[prefrontal_cortex], bnst[bed_nucleus_of_the_stria_terminalis], syn_type=Glu, weight_coef=0.005)



add_connection(pgi[nucleus_paragigantocellularis_lateralis], lc[locus_coeruleus])
add_connection(pgi[nucleus_paragigantocellularis_lateralis], lc[locus_coeruleus], syn_type=Glu, weight_coef=0.005)

add_connection(prh[perirhinal_cortex], lc[locus_coeruleus])

add_connection(ldt[laterodorsal_tegmentum], lc[locus_coeruleus], syn_type=Glu, weight_coef=0.005)
add_connection(ldt[laterodorsal_tegmentum], bnst[bed_nucleus_of_the_stria_terminalis], syn_type=Glu, weight_coef=0.005)

if noradrenaline_flag:
    #TODO
    logger.debug("* * * Making neuromodulating connections...")

    vt_ex = nest.Create('volume_transmitter')
    vt_in = nest.Create('volume_transmitter')
    NORA_synparams_ex['vt'] = vt_ex[0]
    NORA_synparams_in['vt'] = vt_in[0]

    add_connection(nts[nts_a1], lc[locus_coeruleus], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], lc[locus_coeruleus], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], lc[locus_coeruleus], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], striatum[striatumR], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], bnst[bed_nucleus_of_the_stria_terminalis], syn_type=NA_ex, weight_coef=0.005)

    add_connection(lc[locus_coeruleus], pf[prefrontal_cortex], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], motor[motor_cortex], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], vta[vta_a1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], rn[rn_a1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], rn[rn_a2], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], ldt[LDT_a1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], ldt[LDT_a2], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[locus_coeruleus], striatum[striatumR], syn_type=NA_ex, weight_coef=0.005)

    add_connection(vta[ventral_tegmental_area], lc[lc_D1], syn_type=NA_in, weight_coef=0.005)
    add_connection(vta[ventral_tegmental_area], lc[lc_D2], syn_type=NA_in, weight_coef=0.005)
    '''
    # Connect the volume transmitter to the parts
    vt_ex = nest.Create('volume_transmitter')
    vt_in = nest.Create('volume_transmitter')
    NORA_synparams_ex['vt'] = vt_ex[0]
    NORA_synparams_in['vt'] = vt_in[0]
    nest.CopyModel('stdp_dopamine_synapse', nora_model_ex, NORA_synparams_ex)
    nest.CopyModel('stdp_dopamine_synapse', nora_model_in, NORA_synparams_in)
    nest.Connect(snc[snc_DA][k_IDs], vt_ex)
    nest.Connect(snc[snc_DA][k_IDs], vt_in)
    nest.Connect(vta[vta_DA0][k_IDs], vt_ex)
    nest.Connect(vta[vta_DA1][k_IDs], vt_ex)
    # NIGROSTRIATAL
    connect(snc[snc_DA], striatum[D1], syn_type=NR_ex)
    connect(snc[snc_DA], gpe[gpe_GABA], syn_type=NR_ex)
    connect(snc[snc_DA], stn[stn_Glu], syn_type=NR_ex)
    connect(snc[snc_DA], nac[nac_GABA0], syn_type=NR_ex)
    connect(snc[snc_DA], nac[nac_GABA1], syn_type=NR_ex)
    connect(snc[snc_DA], striatum[D2], syn_type=DA_in)
    connect(snc[snc_DA], striatum[tan], syn_type=DA_in)
    # MESOCORTICOLIMBIC
    connect(vta[vta_DA0], striatum[D1], syn_type=NR_ex)
    connect(vta[vta_DA0], striatum[D2], syn_type=DA_in)
    connect(vta[vta_DA0], prefrontal[pfc_Glu0], syn_type=NR_ex)
    connect(vta[vta_DA0], prefrontal[pfc_Glu1], syn_type=NR_ex)
    connect(vta[vta_DA1], nac[nac_GABA0], syn_type=NR_ex)
    connect(vta[vta_DA1], nac[nac_GABA1], syn_type=NR_ex)
'''



logger.debug("* * * Creating connectivity")
connect_all()


logger.debug("* * * Creating spike generators...")
#if generator_flag:
'''
    connect_generator(motor[motor_Glu0], rate=300, coef_part=1)
    connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
    connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
    connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
    connect_generator(vta[vta_DA0], 400., 600., rate=250, coef_part=1)
'''

logger.debug("* * * Attaching spikes detector")
for part in get_all_parts():
    connect_detector(part)

"""
connect_detector(lc[locus_coeruleus])
connect_detector(motor[motor_cortex])

connect_detector(gpe[gpe_GABA])
connect_detector(stn[stn_Glu])
connect_detector(snc[snc_DA])
connect_detector(thalamus[thalamus_Glu])
connect_detector(striatum[tan])
connect_detector(striatum[D1])
connect_detector(striatum[D2])
connect_detector(motor[motor_Glu1])
connect_detector(motor[motor_Glu0])
connect_detector(prefrontal[pfc_Glu0])
connect_detector(vta[vta_DA0])
connect_detector(vta[vta_DA1])
connect_detector(snc[snc_DA])
"""

logger.debug("* * * Attaching multimeters")
for part in get_all_parts():
    connect_multimeter(part)

"""
connect_multimeter(lc[locus_coeruleus])
connect_multimeter(motor[motor_cortex])

connect_multimeter(gpe[gpe_GABA])
connect_multimeter(stn[stn_Glu])
connect_multimeter(snc[snc_DA])
connect_multimeter(thalamus[thalamus_Glu])
connect_multimeter(striatum[tan])
connect_multimeter(striatum[D1])
connect_multimeter(striatum[D2])
connect_multimeter(motor[motor_Glu1])
connect_multimeter(motor[motor_Glu0])
connect_multimeter(prefrontal[pfc_Glu0])
connect_multimeter(vta[vta_DA0])
connect_multimeter(vta[vta_DA1])
connect_multimeter(snc[snc_DA])
"""

del generate_neurons, add_connection, connect_generator, connect_detector, connect_multimeter

endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(create_images)
#save(GUI=statusGUI)
