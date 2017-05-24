from property import *
import numpy as np
"""
Primal/initial dictionary of parts
It contains:
    -Motor Cortex
    -Striatum
    -GPe:       globus pallidus external
    -GPi:       globus pallidus internal
    -STN:       subthalamic nucleus
    -SNr:       substantia nigra pars reticulata
    -SNc:       substantia nigra pars compacta
    -Thalamus
    -Prefrontal cortex
    -NAc:       Nucleus Accumbens
    -VTA:       Ventral Tegmental Area
    -PPTg:      Pedunculopontine Tegmental nucleus
    -Amygdala
    -lc:        locus coeruleus 
Prefix description:
    -GABA - GABA
    -Glu  - glutamate
    -ACh  - acetylcholine
    -DA   - dopamine
"""


#noradrenaline sources

lc = ({k_name: 'LC [D1]'},
      {k_name: 'LC [D2]'},
	{k_name: 'LC [Ach]'},
	{k_name: 'LC [N1]'},
	{k_name: 'LC [N0]'},
	{k_name: 'LC [GABA]'},
  {k_name: 'LC [5HT]'})
lc_D1, lc_D2, lc_Ach, lc_N1, lc_N0, lc_GABA, lc_5HT = range(7)

nts = ({k_name: 'NTS [A1]'},
       {k_name: 'NTS [A2]'})
nts_a1, nts_a2 = range(2)

#ventral

ldt = ({k_name: 'LDT [A1]'},
       {k_name: 'LDT [A2]'},
       {k_name: 'LDT [Ach]'})
ldt_a1, ldt_a2, ldt_Ach = range(3)


bnst = ({k_name: 'Bed nucleus of the stria terminalis [GABA]'},
	{k_name: 'Bed nucleus of the stria terminalis [Glu]'},
	{k_name: 'Bed nucleus of the stria terminalis [5HT]'},
	{k_name: 'Bed nucleus of the stria terminalis [Ach]'},
	{k_name: 'Bed nucleus of the stria terminalis [NA]'})
bnst_GABA, bnst_Glu, bnst_5HT, bnst_Ach, bnst_NA = range(5)

pvn = ({k_name: 'Paraventicular nucleus'}, )
pvn_n = 0


amygdala = ({k_name: 'Amygdala [Glu]'},
	{k_name: 'Amygdala [Ach]'},
	{k_name: 'Amygdala [5HT]'},
	{k_name: 'Amygdala [GABA]'},
  {k_name: 'Amygdala [NA]'})
amygdala_Glu, amygdala_Ach, amygdala_5HT, amygdala_GABA, amygdala_NA  = range(5)

#dorsal

vta = ({k_name: 'VTA [Da0]'},
       {k_name: 'VTA [Da1]'},
       {k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [GABA2]'},
       {k_name: 'VTA [a1]'})
vta_D0, vta_D1, vta_GABA0, vta_GABA1, vta_GABA2, vta_a1 = range(6)


pgi = ({k_name: 'Nucleus paragigantocellularis lateralis [GABA]'},
	{k_name: 'Nucleus paragigantocellularis lateralis [Glu]'})
pgi_GABA, pgi_Glu = range(2)

rn = ({k_name: 'RN [a1]'},
      {k_name: 'RN [a2]'})
rn_a1, rn_a2 = range(2)



prh = ({k_name: 'Perirhinal cortex [GABA]'},)
prh_GABA = 0

#################################
motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'},
         {k_name: 'Motor cortex [5HT]'},)
motor_Glu0, motor_Glu1, motor_5HT = range(3)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'},
            {k_name: 'Striatum [DA]'},
            {k_name: 'Striatum [5HT]'}
            )
D1, D2, tan, striatum_DA, striatum_5HT = range(5)

gpe = ({k_name: 'GPe [GABA]'}, )
gpe_GABA = 0

gpi = ({k_name: 'GPi [GABA]'}, )
gpi_GABA = 0

stn = ({k_name: 'STN [Glu]'}, )
stn_Glu = 0

snr = ({k_name: 'SNr [GABA]'}, )
snr_GABA = 0

snc = ({k_name: 'SNc [GABA]'},
       {k_name: 'SNc [DA]'})
snc_GABA, snc_DA = range(2)

thalamus = ({k_name: 'Thalamus [Glu]'},
            {k_name: 'Thalamus [5HT]'})
thalamus_Glu = 0
thalamus_5HT = 1

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'},
              {k_name: 'Prefrontal cortex [DA]'},
              {k_name: 'Prefrontal cortex [5HT]'},
              {k_name: 'Prefrontal cortex [NA]'}
              )
pfc_Glu0, pfc_Glu1, pfc_DA, pfc_5HT, pfc_NA = range(5)

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'},
       {k_name: 'NAc [DA]'},
       {k_name: 'NAc [5HT]'},
       {k_name: 'NAc [NA]'}
       )
nac_ACh, nac_GABA0, nac_GABA1, nac_DA, nac_5HT, nac_NA = range(6)

vta = ({k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [DA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [DA1]'},
       {k_name: 'VTA [GABA2]'},
       {k_name: 'VTA [DA2]'},
       {k_name: 'VTA [5HT]'},
       {k_name: 'VTA [a1]'}
       )
vta_GABA0, vta_DA0, vta_GABA1, vta_DA1, vta_GABA2, vta_DA2, vta_5HT, vta_a1 = range(8)

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_Glu = range(3)

medial_cortex = ({k_name: 'Medial cortex [5HT]'}, )
medial_cortex_5HT = 0

cerebral_cortex = ({k_name: 'Cerebral cortex [5HT]'}, )
cerebral_cortex_5HT = 0

neocortex = ({k_name: 'Neocortex [5HT]'}, )
neocortex_5HT = 0

lateral_cortex = ({k_name: 'Lateral cortex [5HT]'}, )
lateral_cortex_5HT = 0

entorhinal_cortex = ({k_name: 'Entorhial cortex [5HT]'}, )
entorhinal_cortex_5HT = 0

septum = ({k_name: 'Septum [5HT]'}, )
septum_5HT = 0

pons = ({k_name: 'Pons [5HT]'}, )
pons_5HT = 0

lateral_tegmental_area = ({k_name: 'Lateral tegmental area [5HT]'}, )
lateral_tegmental_area_5HT = 0

#locus_coeruleus = ({k_name: 'Locus coeruleus [DA]'},
#                  {k_name: 'Locus coeruleus [5HT]'},
#                 {k_name: 'Locus coeruleus [NA]'})
#locus_coeruleus_DA, locus_coeruleus_5HT, locus_coeruleus_NA = np.arange(3)


rostral_group = ({k_name: 'Rostral group [A1]'},
                 {k_name: 'Rostral group [A2]'})
rostral_group_A1, rostral_group_A2 = np.arange(2)

dr = ({k_name: 'DR  [5HT]'}, )
dr_5HT = 0

mnr = ({k_name: 'MnR  [5HT]'}, )
mnr_5HT = 0

reticular_formation = ({k_name: 'Reticular formation [5HT]'}, )
reticular_formation_5HT = 0

periaqueductal_gray = ({k_name: 'Periaqueductal gray [5HT]'}, )
periaqueductal_gray_5HT = 0

hippocampus = ({k_name: 'Hippocampus [5HT]'}, )
hippocampus_5HT = 0

hypothalamus = ({k_name: 'Hypothalamus [5HT]'}, )
hypothalamus_5HT = 0

insular_cortex = ({k_name: 'Insular cortex [5HT]'}, )
insular_cortex_5HT = 0


basal_ganglia = ({k_name: 'basal ganglia [5HT]'}, )
basal_ganglia_5HT = 0

rmg = ({k_name: 'rmg [5HT]'}, )
rmg_5HT = 0

rpa = ({k_name: 'rpa [5HT]'}, )
rpa_5HT = 0



cerebral_cortex_NN = 29000
motor[motor_Glu0][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
motor[motor_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
motor[motor_5HT][k_NN] = 10000
striatum_NN = 25000
striatum[D1][k_NN] = int(striatum_NN * 0.425)
striatum[D2][k_NN] = int(striatum_NN * 0.425)
striatum[tan][k_NN] = int(striatum_NN * 0.05)
striatum[striatum_5HT][k_NN] = 1250
gpe[gpe_GABA][k_NN] = 8410
gpi[gpi_GABA][k_NN] = 1260
stn[stn_Glu][k_NN] = 2270
snc[snc_GABA][k_NN] = 3000              #TODO check number of neurons
snc[snc_DA][k_NN] = 1270               #TODO check number of neurons
snr[snr_GABA][k_NN] = 4720

thalamus[thalamus_5HT][k_NN] = 5000
thalamus[thalamus_Glu][k_NN] = int(5000 / 6) #!!!!
prefrontal[pfc_Glu0][k_NN] = 1830
prefrontal[pfc_Glu1][k_NN] = 1830
prefrontal[pfc_DA][k_NN] = 1000
prefrontal[pfc_5HT][k_NN] = 8000
prefrontal[pfc_NA][k_NN] = 8000


nac[nac_ACh][k_NN] = 1500               #TODO not real!!!
nac[nac_GABA0][k_NN] = 14250            #TODO not real!!!
nac[nac_GABA1][k_NN] = 14250            #TODO not real!!!
nac[nac_5HT][k_NN] = 15000
nac[nac_DA][k_NN] = 15000
nac[nac_NA][k_NN] = 1000


vta[vta_GABA0][k_NN] = 7000
vta[vta_DA0][k_NN] = 2000
vta[vta_GABA1][k_NN] = 7000
vta[vta_DA1][k_NN] = 2000
vta[vta_GABA2][k_NN] = 7000
vta[vta_5HT][k_NN] = 3050
vta[vta_DA2][k_NN] = 3050
vta[vta_a1][k_NN] = 2000

pptg[pptg_GABA][k_NN] = 2000
pptg[pptg_ACh][k_NN] = 1400
pptg[pptg_Glu][k_NN] = 2300

amygdala[amygdala_Glu][k_NN] = 3000
amygdala[amygdala_GABA][k_NN] = 1425
amygdala[amygdala_Ach][k_NN] = 6632
amygdala[amygdala_5HT][k_NN] = 3000
amygdala[amygdala_NA][k_NN] = 3000

basal_ganglia[basal_ganglia_5HT][k_NN] = 2593
bnst[bnst_GABA][k_NN] = 1200
bnst[bnst_Glu][k_NN] = 3150
bnst[bnst_Ach][k_NN] = 2200
bnst[bnst_5HT][k_NN] = 500
bnst[bnst_NA][k_NN] = 500
cerebral_cortex[cerebral_cortex_5HT][k_NN] = 1000
dr[dr_5HT][k_NN] = 1800
entorhinal_cortex[entorhinal_cortex_5HT][k_NN] = 6350
hippocampus[hippocampus_5HT][k_NN] = 4260
hypothalamus[hypothalamus_5HT][k_NN] = 1000
insular_cortex[insular_cortex_5HT][k_NN] = 1000

lateral_cortex[lateral_cortex_5HT][k_NN] = 1000
medial_cortex[medial_cortex_5HT][k_NN] = 1000

septum[septum_5HT][k_NN] = 1000

lateral_tegmental_area[lateral_tegmental_area_5HT][k_NN] = 1000
mnr[mnr_5HT][k_NN] = 1100
nac[nac_ACh][k_NN] = 1500               #TODO not real!!!
nac[nac_GABA0][k_NN] = 14250            #TODO not real!!!
nac[nac_GABA1][k_NN] = 14250            #TODO not real!!!
nac[nac_5HT][k_NN] = 1500
nac[nac_DA][k_NN] = 1500
nac[nac_NA][k_NN] = 100
neocortex[neocortex_5HT][k_NN] = 1000
reticular_formation[reticular_formation_5HT][k_NN] = 1000
periaqueductal_gray[periaqueductal_gray_5HT][k_NN] = 1000
prefrontal[pfc_Glu0][k_NN] = 1830
prefrontal[pfc_Glu1][k_NN] = 1830
prefrontal[pfc_DA][k_NN] = 1000
prefrontal[pfc_5HT][k_NN] = 8000
prefrontal[pfc_NA][k_NN] = 8000
pons[pons_5HT][k_NN] = 1000
rmg[rmg_5HT][k_NN] = 1000
rpa[rpa_5HT][k_NN] = 1000
thalamus[thalamus_5HT][k_NN] = 500
thalamus[thalamus_Glu][k_NN] = int(5000 / 6) #!!!!


#noradrenaline sources
lc[lc_D1][k_NN] = 500
lc[lc_D2][k_NN] = 500
lc[lc_Ach][k_NN] = 50
lc[lc_N0][k_NN] = 175
lc[lc_N1][k_NN] = 175
lc[lc_GABA][k_NN] = 400
lc[lc_5HT][k_NN] = 500

nts[nts_a1][k_NN] = 350
nts[nts_a2][k_NN] = 130

#ventral
ldt[ldt_Ach][k_NN] = 181
ldt[ldt_a1][k_NN] = 180
ldt[ldt_a2][k_NN] = 180
pgi[pgi_GABA][k_NN] = 1500
pgi[pgi_Glu][k_NN] = 1500
pvn[pvn_n][k_NN] = 100
rn[rn_a1][k_NN] = 290
rn[rn_a2][k_NN] = 290
prh[prh_GABA][k_NN] = 362

pvn[pvn_n][k_NN] = 100

#################################
cerebral_cortex_NN = 29000
motor[motor_Glu0][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
motor[motor_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
motor[motor_5HT][k_NN] = 1000

striatum_NN = 2500
striatum[D1][k_NN] = int(striatum_NN * 0.425)
striatum[D2][k_NN] = int(striatum_NN * 0.425)
striatum[tan][k_NN] = int(striatum_NN * 0.05)
striatum[striatum_DA][k_NN] = 12500
striatum[striatum_5HT][k_NN] = 12500


"""
#noradrenaline sources

lc = ({k_name: 'LC [D1]'},
      {k_name: 'LC [D2]'},
	{k_name: 'LC [Ach]'},
	{k_name: 'LC [N1]'},
	{k_name: 'LC [N0]'},
	{k_name: 'LC [GABA]'},
  {k_name: 'LC [5HT]'})
lc_D1, lc_D2, lc_Ach, lc_N1, lc_N0, lc_GABA, lc_5HT = range(7)

nts = ({k_name: 'NTS [A1]'},
       {k_name: 'NTS [A2]'})
nts_a1, nts_a2 = range(2)

#ventral

ldt = ({k_name: 'LDT [A1]'},
       {k_name: 'LDT [A2]'},
       {k_name: 'LDT [Ach]'})
ldt_a1, ldt_a2, ldt_Ach = range(3)


bnst = ({k_name: 'Bed nucleus of the stria terminalis [GABA]'},
	{k_name: 'Bed nucleus of the stria terminalis [Glu]'},
	{k_name: 'Bed nucleus of the stria terminalis [5HT]'},
	{k_name: 'Bed nucleus of the stria terminalis [Ach]'},
	{k_name: 'Bed nucleus of the stria terminalis [NA]'})
bnst_GABA, bnst_Glu, bnst_5HT, bnst_Ach, bnst_NA = range(5)

pvn = ({k_name: 'Paraventicular nucleus'}, )
pvn_n = 0


amygdala = ({k_name: 'Amygdala [Glu]'},
	{k_name: 'Amygdala [Ach]'},
	{k_name: 'Amygdala [5HT]'},
	{k_name: 'Amygdala [GABA]'},
  {k_name: 'Amygdala [NA]'})
amygdala_Glu, amygdala_Ach, amygdala_5HT, amygdala_GABA, amygdala_NA  = range(5)

#dorsal

vta = ({k_name: 'VTA [Da0]'},
       {k_name: 'VTA [Da1]'},
       {k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [GABA2]'},
       {k_name: 'VTA [a1]'})
vta_D0, vta_D1, vta_GABA0, vta_GABA1, vta_GABA2, vta_a1 = range(6)


pgi = ({k_name: 'Nucleus paragigantocellularis lateralis [GABA]'},
	{k_name: 'Nucleus paragigantocellularis lateralis [Glu]'})
pgi_GABA, pgi_Glu = range(2)

rn = ({k_name: 'RN [a1]'},
      {k_name: 'RN [a2]'})
rn_a1, rn_a2 = range(2)



prh = ({k_name: 'Perirhinal cortex [GABA]'},)
prh_GABA = 0

#################################
motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'},
         {k_name: 'Motor cortex [5HT]'},)
motor_Glu0, motor_Glu1, motor_5HT = range(3)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'},
            {k_name: 'Striatum [DA]'},
            {k_name: 'Striatum [5HT]'}
            )
D1, D2, tan, striatum_DA, striatum_5HT = range(5)

gpe = ({k_name: 'GPe [GABA]'}, )
gpe_GABA = 0

gpi = ({k_name: 'GPi [GABA]'}, )
gpi_GABA = 0

stn = ({k_name: 'STN [Glu]'}, )
stn_Glu = 0

snr = ({k_name: 'SNr [GABA]'}, )
snr_GABA = 0

snc = ({k_name: 'SNc [GABA]'},
       {k_name: 'SNc [DA]'})
snc_GABA, snc_DA = range(2)

thalamus = ({k_name: 'Thalamus [Glu]'},
            {k_name: 'Thalamus [5HT]'})
thalamus_Glu = 0
thalamus_5HT = 1

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'},
              {k_name: 'Prefrontal cortex [DA]'},
              {k_name: 'Prefrontal cortex [5HT]'},
              {k_name: 'Prefrontal cortex [NA]'}
              )
pfc_Glu0, pfc_Glu1, pfc_DA, pfc_5HT, pfc_NA = range(5)

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'},
       {k_name: 'NAc [DA]'},
       {k_name: 'NAc [5HT]'},
       {k_name: 'NAc [NA]'}
       )
nac_ACh, nac_GABA0, nac_GABA1, nac_DA, nac_5HT, nac_NA = range(6)

vta = ({k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [DA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [DA1]'},
       {k_name: 'VTA [GABA2]'},
       {k_name: 'VTA [DA2]'},
       {k_name: 'VTA [5HT]'},
       {k_name: 'VTA [a1]'}
       )
vta_GABA0, vta_DA0, vta_GABA1, vta_DA1, vta_GABA2, vta_DA2, vta_5HT, vta_a1 = range(8)

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_Glu = range(3)

medial_cortex = ({k_name: 'Medial cortex [5HT]'}, )
medial_cortex_5HT = 0

cerebral_cortex = ({k_name: 'Cerebral cortex [5HT]'}, )
cerebral_cortex_5HT = 0

neocortex = ({k_name: 'Neocortex [5HT]'}, )
neocortex_5HT = 0

lateral_cortex = ({k_name: 'Lateral cortex [5HT]'}, )
lateral_cortex_5HT = 0

entorhinal_cortex = ({k_name: 'Entorhial cortex [5HT]'}, )
entorhinal_cortex_5HT = 0

septum = ({k_name: 'Septum [5HT]'}, )
septum_5HT = 0

pons = ({k_name: 'Pons [5HT]'}, )
pons_5HT = 0

lateral_tegmental_area = ({k_name: 'Lateral tegmental area [5HT]'}, )
lateral_tegmental_area_5HT = 0

#locus_coeruleus = ({k_name: 'Locus coeruleus [DA]'},
#                  {k_name: 'Locus coeruleus [5HT]'},
#                 {k_name: 'Locus coeruleus [NA]'})
#locus_coeruleus_DA, locus_coeruleus_5HT, locus_coeruleus_NA = np.arange(3)


dr = ({k_name: 'DR  [5HT]'}, )
dr_5HT = 0

mnr = ({k_name: 'MnR  [5HT]'}, )
mnr_5HT = 0

reticular_formation = ({k_name: 'Reticular formation [5HT]'}, )
reticular_formation_5HT = 0

periaqueductal_gray = ({k_name: 'Periaqueductal gray [5HT]'}, )
periaqueductal_gray_5HT = 0

hippocampus = ({k_name: 'Hippocampus [5HT]'}, )
hippocampus_5HT = 0

hypothalamus = ({k_name: 'Hypothalamus [5HT]'}, )
hypothalamus_5HT = 0

insular_cortex = ({k_name: 'Insular cortex [5HT]'}, )
insular_cortex_5HT = 0


basal_ganglia = ({k_name: 'basal ganglia [5HT]'}, )
basal_ganglia_5HT = 0

rmg = ({k_name: 'rmg [5HT]'}, )
rmg_5HT = 0

rpa = ({k_name: 'rpa [5HT]'}, )
rpa_5HT = 0


cerebral_cortex_NN = 29000000
motor[motor_Glu0][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
motor[motor_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
striatum_NN = 2500000
striatum[D1][k_NN] = int(striatum_NN * 0.425)
striatum[D2][k_NN] = int(striatum_NN * 0.425)
striatum[tan][k_NN] = int(striatum_NN * 0.05)
gpe[gpe_GABA][k_NN] = 84100
gpi[gpi_GABA][k_NN] = 12600
stn[stn_Glu][k_NN] = 22700
snc[snc_GABA][k_NN] = 3000              #TODO check number of neurons
snc[snc_DA][k_NN] = 12700               #TODO check number of neurons
snr[snr_GABA][k_NN] = 47200
thalamus[thalamus_Glu][k_NN] = int(5000000 / 6) #!!!!

prefrontal[pfc_Glu0][k_NN] = 183000
prefrontal[pfc_Glu1][k_NN] = 183000
nac[nac_ACh][k_NN] = 1500               #TODO not real!!!
nac[nac_GABA0][k_NN] = 14250            #TODO not real!!!
nac[nac_GABA1][k_NN] = 14250            #TODO not real!!!
vta[vta_GABA0][k_NN] = 7000
vta[vta_DA0][k_NN] = 20000
vta[vta_GABA1][k_NN] = 7000
vta[vta_DA1][k_NN] = 20000
vta[vta_GABA2][k_NN] = 7000
pptg[pptg_GABA][k_NN] = 2000
pptg[pptg_ACh][k_NN] = 1400
pptg[pptg_Glu][k_NN] = 2300

amygdala[amygdala_Glu][k_NN] = 30000    #TODO not real!!!

# REAL NUMBER
amygdala[amygdala_5HT][k_NN] = 3000
basal_ganglia[basal_ganglia_5HT][k_NN] = 2593900
bnst[bnst_5HT][k_NN] = 1000  # not real
cerebral_cortex[cerebral_cortex_5HT][k_NN] = 2593900
dr[dr_5HT][k_NN] = 5800
entorhinal_cortex[entorhinal_cortex_5HT][k_NN] = 635000
hippocampus[hippocampus_5HT][k_NN] = 4260000
hypothalamus[hypothalamus_5HT][k_NN] = 1000  # not real
insular_cortex[insular_cortex_5HT][k_NN] = 1000  # not real
lateral_cortex[lateral_cortex_5HT][k_NN] = 1000  # not real
lateral_tegmental_area[lateral_tegmental_area_5HT][k_NN] = 1000  # not real
locus_coeruleus[locus_coeruleus_5HT][k_NN] = 500
locus_coeruleus[locus_coeruleus_DA][k_NN] = 500
locus_coeruleus[locus_coeruleus_NA][k_NN] = 500
medial_cortex[medial_cortex_5HT][k_NN] = 1000  # not real
mnr[mnr_5HT][k_NN] = 1100
nac[nac_5HT][k_NN] = 15000
nac[nac_DA][k_NN] = 15000
neocortex[neocortex_5HT][k_NN] = 1000  # not real
periaqueductal_gray[periaqueductal_gray_5HT][k_NN] = 1000  # not real
prefrontal[pfc_5HT][k_NN] = 183000
prefrontal[pfc_DA][k_NN] = 183000
pons[pons_5HT][k_NN] = 1000  # not real
reticular_formation[reticular_formation_5HT][k_NN] = 1000  # not real
rmg[rmg_5HT][k_NN] = 1000
rpa[rpa_5HT][k_NN] = 1000
septum[septum_5HT][k_NN] = 1000  # not real
striatum[striatum_5HT][k_NN] = 1250000
striatum[striatum_DA][k_NN] = 12500000
substantia_nigra[substantia_nigra_5HT][k_NN] = 31450
substantia_nigra[substantia_nigra_DA][k_NN] = 31450
thalamus[thalamus_5HT][k_NN] = 5000000
vta[vta_5HT][k_NN] = 30500
vta[vta_DA2][k_NN] = 30500
#nora numbers
lc[lc_D1][k_NN] = 500
lc[lc_D2][k_NN] = 500
lc[lc_N0][k_NN] = 1750
lc[lc_N1][k_NN] = 1750
lc[lc_Ach][k_NN] = 500
lc[lc_GABA][k_NN] = 400

nts[nts_a1][k_NN] = 3500
nts[nts_a2][k_NN] = 1300

#ventral numbers

ldt[ldt_Ach][k_NN] = 1811
ldt[ldt_a1][k_NN] = 1800
ldt[ldt_a2][k_NN] = 1800
pvn[pvn_n][k_NN] = 1000
motor_cortex_NN = 5000 #actually 5000000
motor[motor_Glu0][k_NN] = motor_cortex_NN * 0.8
motor[motor_Glu1][k_NN] = motor_cortex_NN * 0.2
motor[motor_5HT][k_NN] = motor_cortex_NN * 0.2

bnst[bnst_GABA][k_NN] = 12000
bnst[bnst_Glu][k_NN] = 31500
bnst[bnst_Ach][k_NN] = 2200
thalamus[thalamus_Glu][k_NN] = 1000 #actually 1000000
amygdala[amygdala_Glu][k_NN] = 30000
amygdala[amygdala_GABA][k_NN] = 14250
amygdala[amygdala_Ach][k_NN] = 6632

#dorsal numbers

vta[vta_a1][k_NN] = 20000
vta[vta_GABA0][k_NN] = 20000
vta[vta_D0][k_NN] = 20000
vta[vta_GABA1][k_NN] = 20000
vta[vta_D1][k_NN] = 20000
vta[vta_GABA2][k_NN] = 20000

pgi[pgi_GABA][k_NN] = 15000
pgi[pgi_Glu][k_NN] = 15000

rn[rn_a1][k_NN] = 2900
rn[rn_a2][k_NN] = 2900
prefrontal[pfc_Glu][k_NN] = 40
striatum[D1][k_NN] = 1500
striatum[D2][k_NN] = 1500
striatum[tan][k_NN] = 14250
prh[prh_GABA][k_NN] = 3627


cerebral_cortex_NN = 40
motor[motor_Glu0][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
motor[motor_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
motor[motor_5HT][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
striatum_NN = 30
striatum[D1][k_NN] = int(striatum_NN * 0.425)
striatum[D2][k_NN] = int(striatum_NN * 0.425)
striatum[tan][k_NN] = int(striatum_NN * 0.05)
gpe[gpe_GABA][k_NN] = 84
gpi[gpi_GABA][k_NN] = 12
stn[stn_Glu][k_NN] = 22
snc[snc_GABA][k_NN] = 30              #TODO check number of neurons
snc[snc_DA][k_NN] = 12               #TODO check number of neurons
snr[snr_GABA][k_NN] = 47
thalamus[thalamus_Glu][k_NN] = int(50 / 6) #!!!!

prefrontal[pfc_Glu0][k_NN] = 18
prefrontal[pfc_Glu1][k_NN] = 18
nac[nac_ACh][k_NN] = 15               #TODO not real!!!
nac[nac_GABA0][k_NN] = 14            #TODO not real!!!
nac[nac_GABA1][k_NN] = 14
nac[nac_NA][k_NN] = 14             #TODO not real!!!
vta[vta_GABA0][k_NN] = 70
vta[vta_DA0][k_NN] = 20
vta[vta_GABA1][k_NN] = 70
vta[vta_DA1][k_NN] = 20
vta[vta_GABA2][k_NN] = 70
pptg[pptg_GABA][k_NN] = 20
pptg[pptg_ACh][k_NN] = 14
pptg[pptg_Glu][k_NN] = 23

amygdala[amygdala_Glu][k_NN] = 30    #TODO not real!!!

# REAL NUMBER
amygdala[amygdala_5HT][k_NN] = 30
basal_ganglia[basal_ganglia_5HT][k_NN] = 25
bnst[bnst_5HT][k_NN] = 10  # not real
cerebral_cortex[cerebral_cortex_5HT][k_NN] = 25
dr[dr_5HT][k_NN] = 58
entorhinal_cortex[entorhinal_cortex_5HT][k_NN] = 63
hippocampus[hippocampus_5HT][k_NN] = 42
hypothalamus[hypothalamus_5HT][k_NN] = 10  # not real
insular_cortex[insular_cortex_5HT][k_NN] = 10  # not real
lateral_cortex[lateral_cortex_5HT][k_NN] = 10  # not real
lateral_tegmental_area[lateral_tegmental_area_5HT][k_NN] = 10  # not real
#locus_coeruleus[locus_coeruleus_5HT][k_NN] = 50
#locus_coeruleus[locus_coeruleus_DA][k_NN] = 50
#locus_coeruleus[locus_coeruleus_NA][k_NN] = 50
medial_cortex[medial_cortex_5HT][k_NN] = 10  # not real
mnr[mnr_5HT][k_NN] = 11
nac[nac_5HT][k_NN] = 15
nac[nac_DA][k_NN] = 15
neocortex[neocortex_5HT][k_NN] = 10  # not real
periaqueductal_gray[periaqueductal_gray_5HT][k_NN] = 10  # not real
prefrontal[pfc_5HT][k_NN] = 18
prefrontal[pfc_DA][k_NN] = 18
prefrontal[pfc_NA][k_NN] = 18
pons[pons_5HT][k_NN] = 10  # not real
reticular_formation[reticular_formation_5HT][k_NN] = 10  # not real
rmg[rmg_5HT][k_NN] = 10
rpa[rpa_5HT][k_NN] = 10
septum[septum_5HT][k_NN] = 10  # not real
striatum[striatum_5HT][k_NN] = 12
striatum[striatum_DA][k_NN] = 12
thalamus[thalamus_5HT][k_NN] = 50
vta[vta_5HT][k_NN] = 30
vta[vta_DA2][k_NN] = 30

#nora numbers
lc[lc_D1][k_NN] = 30
lc[lc_D2][k_NN] = 30
lc[lc_N0][k_NN] = 30
lc[lc_N1][k_NN] = 30
lc[lc_Ach][k_NN] = 30
lc[lc_GABA][k_NN] = 30
lc[lc_5HT][k_NN] = 30

nts[nts_a1][k_NN] = 30
nts[nts_a2][k_NN] = 30

#ventral numbers

ldt[ldt_Ach][k_NN] = 30
ldt[ldt_a1][k_NN] = 30
ldt[ldt_a2][k_NN] = 30
pvn[pvn_n][k_NN] = 30
motor[motor_Glu0][k_NN] = 40
motor[motor_Glu1][k_NN] = 40

bnst[bnst_GABA][k_NN] = 30
bnst[bnst_Glu][k_NN] = 30
bnst[bnst_Ach][k_NN] = 30
bnst[bnst_NA][k_NN] = 30
thalamus[thalamus_Glu][k_NN] = 30

amygdala[amygdala_GABA][k_NN] = 30
amygdala[amygdala_Ach][k_NN] = 30
amygdala[amygdala_NA][k_NN] = 30
#dorsal numbers

vta[vta_a1][k_NN] = 30
vta[vta_GABA0][k_NN] = 50
vta[vta_D0][k_NN] = 30
vta[vta_GABA1][k_NN] = 50
vta[vta_D1][k_NN] = 30
vta[vta_GABA2][k_NN] = 50

pgi[pgi_GABA][k_NN] = 30
pgi[pgi_Glu][k_NN] = 30

rn[rn_a1][k_NN] = 30
rn[rn_a2][k_NN] = 30

striatum[D1][k_NN] = 30
striatum[D2][k_NN] = 30
striatum[tan][k_NN] = 30
prh[prh_GABA][k_NN] = 30
"""
