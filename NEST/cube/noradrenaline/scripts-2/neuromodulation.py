# TODO check num_threads before testing / 8 for Cisco Server
# TODO ATTTENTION! Maybe there are some mistakes in neuron parameters! Write to alexey.panzer@gmail.com.

from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True, 'local_num_threads': number_of_threads, 'resolution': 0.1})

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
###########################dopa#########################
DOPA_synparams_ex['vt'] = nest.Create('volume_transmitter')[0]
DOPA_synparams_in['vt'] = nest.Create('volume_transmitter')[0]
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_synapse_in, DOPA_synparams_in)
###########################dopa#########################

logger.debug("* * * Start connection initialisation")

# * * * ventral pathway * * *
add_connection(ldt[ldt_Ach], thalamus[thalamus_Glu], syn_type=ACh, weight_coef=0.005)
add_connection(ldt[ldt_Ach], bnst[bnst_Ach], syn_type=ACh, weight_coef=0.005)
add_connection(ldt[ldt_Ach], nts[nts_a1], syn_type=ACh, weight_coef=0.005)
add_connection(ldt[ldt_Ach], prefrontal[pfc_Glu], syn_type=ACh, weight_coef=5)
add_connection(thalamus[thalamus_Glu], motor[motor_Glu0], syn_type=Glu, weight_coef=0.005)
add_connection(thalamus[thalamus_Glu], motor[motor_Glu1], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu0], nts[nts_a1], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu1], nts[nts_a2], syn_type=Glu, weight_coef=0.005)

add_connection(prefrontal[pfc_Glu], lc[lc_N0], syn_type=Glu, weight_coef=0.005)
add_connection(prefrontal[pfc_Glu], bnst[bnst_Glu], syn_type=Glu, weight_coef=5)
add_connection(bnst[bnst_Glu], bnst[bnst_GABA], syn_type=Glu, weight_coef=5)
add_connection(bnst[bnst_Ach], amygdala[amygdala_Ach], syn_type=ACh, weight_coef=0.005)
add_connection(bnst[bnst_GABA], pvn[pvn_n], syn_type=GABA, weight_coef=0.5)
add_connection(amygdala[amygdala_Ach], lc[lc_Ach], syn_type=ACh, weight_coef=0.005)
add_connection(amygdala[amygdala_GABA], bnst[bnst_GABA], syn_type=GABA, weight_coef=0.005)
add_connection(amygdala[amygdala_Glu], striatum[D1], syn_type=Glu, weight_coef=0.005)
add_connection(amygdala[amygdala_Glu], striatum[D2], syn_type=Glu, weight_coef=0.005)
add_connection(amygdala[amygdala_Glu], striatum[tan], syn_type=Glu, weight_coef=0.005)
add_connection(pvn[pvn_n], motor[motor_Glu0], syn_type=GABA, weight_coef=0.005)
add_connection(pvn[pvn_n], motor[motor_Glu1], syn_type=GABA, weight_coef=0.005)

# inside LC
add_connection(lc[lc_Ach], lc[lc_GABA], syn_type=ACh, weight_coef=0.005)
add_connection(lc[lc_Ach], lc[lc_N0], syn_type=ACh, weight_coef=0.005)
add_connection(lc[lc_Ach], lc[lc_N1], syn_type=ACh, weight_coef=0.005)
add_connection(lc[lc_D1], lc[lc_N0], syn_type=DA_ex, weight_coef=0.005)
add_connection(lc[lc_D2], lc[lc_N1], syn_type=DA_in, weight_coef=0.005)
add_connection(lc[lc_GABA], lc[lc_N0], syn_type=GABA, weight_coef=0.005)

# * * * dorsal pathway * * *

add_connection(pgi[pgi_Glu], lc[lc_N0], syn_type=Glu, weight_coef=0.005)
add_connection(pgi[pgi_Glu], lc[lc_N1], syn_type=Glu, weight_coef=0.005)
add_connection(pgi[pgi_GABA], lc[lc_GABA], syn_type=GABA, weight_coef=0.005)
add_connection(prh[prh_GABA], lc[lc_GABA], syn_type=GABA, weight_coef=0.005)
add_connection(striatum[tan], lc[lc_GABA], syn_type=GABA, weight_coef=0.005)
add_connection(vta[vta_D0], lc[lc_D1], syn_type=DA_ex, weight_coef=0.05)
add_connection(vta[vta_D0], prefrontal[pfc_Glu], syn_type=DA_ex, weight_coef=0.05)
add_connection(vta[vta_D0], lc[lc_D2], syn_type=DA_in, weight_coef=0.05)
add_connection(vta[vta_D1], striatum[tan], syn_type=DA_ex, weight_coef=0.05)

if noradrenaline_flag:
    logger.debug("* * * Making neuromodulating connections...")

    vt_ex = nest.Create('volume_transmitter')
    vt_in = nest.Create('volume_transmitter')
    NORA_synparams_ex['vt'] = vt_ex[0]
    NORA_synparams_in['vt'] = vt_in[0]

    add_connection(nts[nts_a1], lc[lc_N0], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a1], bnst[bnst_Glu], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], lc[lc_N1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], striatum[tan], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], amygdala[amygdala_Glu], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], amygdala[amygdala_Ach], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], amygdala[amygdala_GABA], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a2], bnst[bnst_Glu], syn_type=NA_ex, weight_coef=0.005)
    add_connection(nts[nts_a1], pvn[pvn_n], syn_type=NA_ex, weight_coef=2)
    add_connection(nts[nts_a2], pvn[pvn_n], syn_type=NA_ex, weight_coef=2)

    add_connection(lc[lc_N0], motor[motor_Glu0], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N0], motor[motor_Glu1], syn_type=NA_ex, weight_coef=0.005)

    add_connection(lc[lc_N0], prefrontal[pfc_Glu], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N0], vta[vta_a1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N0], ldt[ldt_a1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N0], ldt[ldt_a2], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N1], striatum[tan], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N1], rn[rn_a1], syn_type=NA_ex, weight_coef=0.005)
    add_connection(lc[lc_N1], rn[rn_a2], syn_type=NA_ex, weight_coef=0.005)

    add_connection(vta[vta_a1], vta[vta_D0], syn_type=NA_in, weight_coef=0.05)
    add_connection(vta[vta_a1], vta[vta_D1], syn_type=NA_in, weight_coef=0.05)

"""
# * * * NIGROSTRIATAL PATHWAY* * *
add_connection(motor[motor_Glu0], striatum[D1], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu0], snc[snc_DA], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu0], striatum[D2], syn_type=Glu, weight_coef=0.05)
add_connection(motor[motor_Glu0], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.008)
add_connection(motor[motor_Glu0], stn[stn_Glu], syn_type=Glu, weight_coef=7)
add_connection(motor[motor_Glu1], striatum[D1], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu1], striatum[D2], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu1], thalamus[thalamus_Glu], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu1], stn[stn_Glu], syn_type=Glu, weight_coef=0.005)
add_connection(motor[motor_Glu1], nac[nac_GABA0], syn_type=GABA, weight_coef=0.005)
#add_connection(striatum[tan], striatum[D1], syn_type=GABA, weight_coef=0.005)
#add_connection(striatum[tan], striatum[D2], syn_type=Glu, weight_coef=0.005)
add_connection(striatum[D1], snr[snr_GABA],syn_type=GABA, weight_coef=0.001)
add_connection(striatum[D1], gpi[gpi_GABA],syn_type=GABA, weight_coef=0.001)
add_connection(striatum[D1], gpe[gpe_GABA],syn_type=GABA, weight_coef=0.005)
add_connection(striatum[D2], gpe[gpe_GABA],syn_type=GABA, weight_coef=1)
add_connection(gpe[gpe_GABA], stn[stn_Glu],syn_type=GABA, weight_coef=0.001)
#add_connection(gpe[gpe_GABA], striatum[D1],syn_type=GABA, weight_coef=0.001)
#add_connection(gpe[gpe_GABA], striatum[D2],syn_type=GABA, weight_coef=0.3)
add_connection(snc[snc_DA], gpe[gpe_GABA], weight_coef=0.3, syn_type=DA_ex)
add_connection(amygdala[amygdala_Glu], gpe[gpe_GABA], syn_type=Glu, weight_coef=0.3)
add_connection(gpe[gpe_GABA], amygdala[amygdala_Glu], syn_type=GABA, weight_coef=0.1)
add_connection(gpe[gpe_GABA], snc[snc_DA], weight_coef=0.2, syn_type=GABA)
add_connection(gpe[gpe_GABA], snr[snr_GABA], syn_type=GABA,weight_coef=0.001)
add_connection(stn[stn_Glu], snr[snr_GABA], syn_type=Glu, weight_coef=20)
add_connection(stn[stn_Glu], gpi[gpi_GABA], syn_type=Glu, weight_coef=20)
add_connection(stn[stn_Glu], gpe[gpe_GABA], syn_type=Glu, weight_coef=0.3)
add_connection(stn[stn_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.01)
add_connection(gpi[gpi_GABA], thalamus[thalamus_Glu], syn_type=GABA,weight_coef=3)
add_connection(snr[snr_GABA], thalamus[thalamus_Glu], syn_type=GABA,weight_coef=3)
add_connection(thalamus[thalamus_Glu], motor[motor_Glu1], syn_type=Glu)
add_connection(thalamus[thalamus_Glu], stn[stn_Glu], syn_type=Glu, weight_coef=1) #005
add_connection(thalamus[thalamus_Glu], striatum[D1], syn_type=Glu, weight_coef=0.001)
add_connection(thalamus[thalamus_Glu], striatum[D2], syn_type=Glu, weight_coef=0.001)
add_connection(thalamus[thalamus_Glu], striatum[tan], syn_type=Glu, weight_coef=0.001)
add_connection(thalamus[thalamus_Glu], nac[nac_GABA0], syn_type=Glu)
add_connection(thalamus[thalamus_Glu], nac[nac_GABA1], syn_type=Glu)
add_connection(thalamus[thalamus_Glu], nac[nac_ACh], syn_type=Glu)
"""

"""
# * * * MESOCORTICOLIMBIC PATHWAY * * *
add_connection(nac[nac_ACh], nac[nac_GABA1], syn_type=ACh)
add_connection(nac[nac_GABA0], nac[nac_GABA1],syn_type=GABA,)
add_connection(nac[nac_GABA1], vta[vta_GABA2],syn_type=GABA,)
add_connection(vta[vta_GABA0], prefrontal[pfc_Glu],syn_type=GABA,)
add_connection(vta[vta_GABA0], pptg[pptg_GABA],syn_type=GABA,)
add_connection(vta[vta_GABA1], vta[vta_D0],syn_type=GABA,)
add_connection(vta[vta_GABA1], vta[vta_D1],syn_type=GABA,)
add_connection(vta[vta_GABA2], nac[nac_GABA1],syn_type=GABA,)
add_connection(pptg[pptg_GABA], vta[vta_GABA0],syn_type=GABA,)
add_connection(pptg[pptg_GABA], snc[snc_GABA], syn_type=GABA,weight_coef=0.005)
add_connection(pptg[pptg_ACh], vta[vta_GABA0], syn_type=ACh)
add_connection(pptg[pptg_ACh], vta[vta_D1], syn_type=ACh)
add_connection(pptg[pptg_Glu], vta[vta_GABA0], syn_type=Glu)
add_connection(pptg[pptg_Glu], vta[vta_D1], syn_type=Glu)
add_connection(pptg[pptg_ACh], striatum[D1], syn_type=ACh, weight_coef=0.3)
add_connection(pptg[pptg_ACh], snc[snc_GABA], syn_type=ACh, weight_coef=0.005)
add_connection(pptg[pptg_Glu], snc[snc_DA], syn_type=Glu, weight_coef=0.005)
"""

"""
# * * * INTEGRATED PATHWAY * * *
add_connection(prefrontal[pfc_Glu], vta[vta_D0], syn_type=Glu)
add_connection(prefrontal[pfc_Glu], nac[nac_GABA1], syn_type=Glu)
add_connection(prefrontal[pfc_Glu], vta[vta_GABA2], syn_type=Glu)
add_connection(prefrontal[pfc_Glu], nac[nac_GABA1], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], nac[nac_GABA0], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], nac[nac_GABA1], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], nac[nac_ACh], syn_type=Glu)
add_connection(amygdala[amygdala_Glu], striatum[D1], syn_type=Glu, weight_coef=0.3)
add_connection(amygdala[amygdala_Glu], striatum[D2], syn_type=Glu, weight_coef=0.3)
add_connection(amygdala[amygdala_Glu], striatum[tan], syn_type=Glu, weight_coef=0.3)
"""
"""
if dopamine_flag:
    logger.debug("* * * Making neuromodulating connections...")
    # NIGROSTRIATAL

    add_connection(snc[snc_DA], striatum[D1], syn_type=DA_ex)
    add_connection(snc[snc_DA], gpe[gpe_GABA], syn_type=DA_ex)
    add_connection(snc[snc_DA], stn[stn_Glu], syn_type=DA_ex)
    add_connection(snc[snc_DA], nac[nac_GABA0], syn_type=DA_ex)
    add_connection(snc[snc_DA], nac[nac_GABA1], syn_type=DA_ex)
    #add_connection(snc[snc_DA], striatum[D2], syn_type=DA_in)
    #add_connection(snc[snc_DA], striatum[tan], syn_type=DA_in)
    # MESOCORTICOLIMBIC
    add_connection(vta[vta_D0], striatum[D1], syn_type=DA_ex)
    #add_connection(vta[vta_D0], striatum[D2], syn_type=DA_in)
    add_connection(vta[vta_D0], prefrontal[pfc_Glu], syn_type=DA_ex)
    add_connection(vta[vta_D0], prefrontal[pfc_Glu], syn_type=DA_ex)
    add_connection(vta[vta_D1], nac[nac_GABA0], syn_type=DA_ex)
    add_connection(vta[vta_D1], nac[nac_GABA1], syn_type=DA_ex)
"""
###########################dopa#########################


logger.debug("* * * Creating connectivity")
connect_all()

logger.debug("* * * Attaching spike generators...")
if generator_flag:
    connect_generator(nts[nts_a1], 200., 600., rate=100, coef_part=1)
    connect_generator(nts[nts_a2], 200., 600., rate=100, coef_part=1)
    connect_generator(prh[prh_GABA], 200., 600., rate=100, coef_part=1)
    connect_generator(pgi[pgi_GABA], 200., 600., rate=100, coef_part=1)
    connect_generator(pgi[pgi_Glu], 200., 600., rate=100, coef_part=1)
    connect_generator(ldt[ldt_a1], 200., 600., rate=100, coef_part=1)
    connect_generator(ldt[ldt_a2], 200., 600., rate=100, coef_part=1)
    connect_generator(ldt[ldt_Ach], 200., 600., rate=100, coef_part=1)
    #connect_generator(lc[lc_N0], 200., 600., rate=100, coef_part=1)
    #connect_generator(lc[lc_N1], 200., 600., rate=100, coef_part=1)
    # connect_generator(gpe[gpe_GABA], 400., 600., rate=250, coef_part=1)
    # connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
    # connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
    # connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
    # connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
    # connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)
    # connect_generator(vta[vta_D0], 400., 600., rate=250, coef_part=1)
    # connect_generator(motor[motor_Glu0], 400., 600., rate=250, coef_part=1)
#########dopa########
"""
    #connect_generator(gpe[gpi_GABA], rate=250, coef_part=1)
    connect_generator(pptg[pptg_GABA], 400., 600., rate=250, coef_part=1)
    connect_generator(pptg[pptg_Glu], 400., 600., rate=250, coef_part=1)
    connect_generator(pptg[pptg_ACh], 400., 600., rate=250, coef_part=1)
    connect_generator(amygdala[amygdala_Glu], 400., 600., rate=250, coef_part=1)
"""
# connect_generator(snc[snc_DA], 400., 600., rate=250, coef_part=1)




####
"""
# EXPERIMENT
delta = [1.0, 1.5, 0.38, 0.8, 0.33]
k = 100.
for i in xrange(len(delta)):
	connect_generator(lc[locus_coeruleus], k, k + 12., rate=250, coef_part=1,
                      weight=float((delta[i] + 2) * 5))
	connect_generator(nts[nts_a1], k, k + 12., rate=250, coef_part=1,
                      weight=float((delta[i] + 2) * 5))
	connect_generator(nts[nts_a2], k, k + 12., rate=250, coef_part=1,
                      weight=float((delta[i] + 2) * 5))
	k += 100.
"""

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
# save(GUI=statusGUI)

"""
histfile = open("/home/mariya/Desktop/results/hist")
g.save_spikes(spike_detectors,histfile,true)
connfile = open("/home/mariya/Desktop/results/conn")
g.print_connections(connfile)
gdffile = open("/home/mariya/Desktop/results/gdf")
g.print_gdf(gdffile)
"""
