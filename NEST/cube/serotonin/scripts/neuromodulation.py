from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()

generate_neurons(10000)

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