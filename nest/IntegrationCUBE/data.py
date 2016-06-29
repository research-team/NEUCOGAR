from property import *
import numpy as np

# TODO = = = = = = = = = =
# TODO NORADRENALINE
# TODO = = = = = = = = = =

LC = (
    {k_name: 'LC[LC_NA_0]'},
    {k_name: 'LC[LC_Ach]'},
    {k_name: 'LC[LC_GABA]'},
    {k_name: 'LC[LC_D1]'},
    {k_name: 'LC[LC_D2]'},
    {k_name: 'LC[LC_NA_1]'}
)
LC_NA_0 = 0
LC_Ach = 1
LC_GABA = 2
LC_D1 = 3
LC_D2 = 4
LC_NA_1 = 5

PGI = (
    {k_name: 'PGI[PGI_GABA]'},
    {k_name: 'PGI[PGI_Glu]'}
)
PGI_GABA = 0
PGI_Glu = 1

BNST = (
    {k_name: 'BNST[BNST_Glu]'},
    {k_name: 'BNST[BNST_GABA]'},
    {k_name: 'BNST[BNST_Ach]'}
)
BNST_Glu = 0
BNST_GABA = 1
BNST_Ach = 2

Amy = (
    {k_name: 'Amy[Amy_Glu]'},
    {k_name: 'Amy[Amy_Ach]'},
    {k_name: 'Amy[Amy_GABA]'}
)
Amy_Glu = 0
Amy_Ach = 1
Amy_GABA = 2

RN = (
    {k_name: 'RN[RN_5HT]'},
    {k_name: 'RN[RN_a1]'},
    {k_name: 'RN[RN_a2]'}
)
RN_5HT = 0
RN_a1 = 1
RN_a2 = 2

Thalamus = ({k_name: 'Thalamus[Thalamus_Glu]'}, )
Thalamus_Glu = 0

PVN = ({k_name: 'PVN[PVN_GABA]'}, )
PVN_GABA = 0

Striatum = ()


LTD = (
    {k_name: 'LTD[LTD_a1]'},
    {k_name: 'LTD[LTD_a2]'},
    {k_name: 'LTD[LTD_Ach]'}
)
LTD_a1 = 0
LTD_a2 = 1
LTD_Ach = 2

PrH = ({k_name: 'PrH[PrH_GABA]'}, )
PrH_GABA = 0


NTS = ()

AcbCore = (
    {k_name: 'AcbCore[AcbCore_Ach]'},
    {k_name: 'AcbCore[AcbCore_GABA_0]'}
)
AcbCore_Ach = 0
AcbCore_GABA_0 = 1

Prefrontalcortex = (
    {k_name: 'Prefrontalcortex[Prefrontalcortex_Glu_1]'},
    {k_name: 'Prefrontalcortex[Prefrontalcortex_Glu_0]'}
)
Prefrontalcortex_Glu_1 = 0
Prefrontalcortex_Glu_0 = 1

Ab = ({k_name: 'Ab[Ab_NA]'}, )
Ab_NA = 0


VTA = (
    {k_name: 'VTA[VTA_DA_0]'},
    {k_name: 'VTA[VTA_a1]'},
    {k_name: 'VTA[VTA_DA_1]'}
)
VTA_DA_0 = 0
VTA_a1 = 1
VTA_DA_1 = 2

Aa = ({k_name: 'Aa[Aa_NA]'}, )
Aa_NA = 0

AcbShell = ({k_name: 'AcbShell[AcbShell_GABA_1]'}, )
AcbShell_GABA_1 = 0

Motorcortex = ({k_name: 'Motorcortex[Motorcortex_Glu]'}, )
Motorcortex_Glu = 0

LC[LC_NA_0][k_NN] = 1750
LC[LC_Ach][k_NN] = 500
LC[LC_GABA][k_NN] = 400
LC[LC_D1][k_NN] = 1000
LC[LC_D2][k_NN] = 1000
LC[LC_NA_1][k_NN] = 1750

PGI[PGI_GABA][k_NN] = 15000
PGI[PGI_Glu][k_NN] = 15000

BNST[BNST_Glu][k_NN] = 12000
BNST[BNST_GABA][k_NN] = 31500
BNST[BNST_Ach][k_NN] = 2200

Amy[Amy_Glu][k_NN] = 30000
Amy[Amy_Ach][k_NN] = 6600
Amy[Amy_GABA][k_NN] = 3600

RN[RN_5HT][k_NN] =5800
RN[RN_a1][k_NN] = 3450
RN[RN_a2][k_NN] = 3450

Thalamus[Thalamus_Glu][k_NN] = 833000

PVN[PVN_GABA][k_NN] = 1000

LTD[LTD_a1][k_NN] = 1000
LTD[LTD_a2][k_NN] = 1000
LTD[LTD_Ach][k_NN] = 1800

PrH[PrH_GABA][k_NN] = 3700

AcbCore[AcbCore_Ach][k_NN] = 1500
AcbCore[AcbCore_GABA_0][k_NN] = 14250

Prefrontalcortex[Prefrontalcortex_Glu_1][k_NN] = 183000
Prefrontalcortex[Prefrontalcortex_Glu_0][k_NN] = 183000

Ab[Ab_NA][k_NN] = 1300

VTA[VTA_DA_0][k_NN] = 20000
VTA[VTA_a1][k_NN] = 1000
VTA[VTA_DA_1][k_NN] = 20000

Aa[Aa_NA][k_NN] = 3500

AcbShell[AcbShell_GABA_1][k_NN] = 14250

Motorcortex[Motorcortex_Glu][k_NN] = 4833000



# TODO = = = = = = = = = =
# TODO DOPAMINE
# TODO = = = = = = = = = =


motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_Glu0, motor_Glu1 = range(2)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'})
D1, D2, tan = range(3)

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

thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'})
pfc_Glu0, pfc_Glu1 = range(2)

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'})
nac_ACh, nac_GABA0, nac_GABA1  = range(3)

vta = ({k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [DA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [DA1]'},
       {k_name: 'VTA [GABA2]'})
vta_GABA0, vta_DA0, vta_GABA1, vta_DA1, vta_GABA2 = range(5)

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_Glu = range(3)

amygdala = ({k_name: 'Amygdala [Glu]'}, )
amygdala_Glu = 0

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



# TODO = = = = = = = = = =
# TODO SEROTONINE
# TODO = = = = = = = = = =


striatum = ({k_name: 'Striatum [DA]'},
            {k_name: 'Striatum [5HT]'})
striatum_DA, striatum_5HT = np.arange(2)

thalamus = ({k_name: 'Thalamus [5HT]'}, )
thalamus_5HT = 0

pfc = ({k_name: 'Prefrontal cortex [DA]'},
       {k_name: 'Prefrontal cortex [5HT]'})
pfc_DA, pfc_5HT = np.arange(2)

nac = ({k_name: 'NAc [DA]'},
       {k_name: 'NAc [5HT]'})
nac_DA, nac_5HT  = np.arange(2)

vta = ({k_name: 'VTA [DA]'},
       {k_name: 'VTA [5HT]'})
vta_DA, vta_5HT = np.arange(2)

amygdala = ({k_name: 'Amygdala [5HT]'}, )
amygdala_5HT = 0

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

locus_coeruleus = ({k_name: 'Locus coeruleus [DA]'},
                   {k_name: 'Locus coeruleus [5HT]'},
                   {k_name: 'Locus coeruleus [NA]'})
locus_coeruleus_DA, locus_coeruleus_5HT, locus_coeruleus_NA = np.arange(3)

bed_nucleus_of_the_stria_terminalis = ({k_name: 'Bed nucleus of the stria terminalis [5HT]'}, )
bed_nucleus_of_the_stria_terminalis_5HT = 0

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

substantia_nigra = ({k_name: 'Substantia nigra [DA]'},
                    {k_name: 'Substantia nigra [5HT]'})
substantia_nigra_DA, substantia_nigra_5HT = np.arange(2)

insular_cortex = ({k_name: 'Insular cortex [5HT]'}, )
insular_cortex_5HT = 0


basal_ganglia = ({k_name: 'basal ganglia [5HT]'}, )
basal_ganglia_5HT = 0

rmg = ({k_name: 'rmg [5HT]'}, )
rmg_5HT = 0

rpa = ({k_name: 'rpa [5HT]'}, )
rpa_5HT = 0


# REAL NUMBER
amygdala[amygdala_5HT][k_NN] = 3000
basal_ganglia[basal_ganglia_5HT][k_NN] = 2593900
bed_nucleus_of_the_stria_terminalis[bed_nucleus_of_the_stria_terminalis_5HT][k_NN] = 1000  # not real
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
pfc[pfc_5HT][k_NN] = 183000
pfc[pfc_DA][k_NN] = 183000
pons[pons_5HT][k_NN] = 1000  # not real
reticular_formation[reticular_formation_5HT][k_NN] = 1000  # not real
rmg[rmg_5HT][k_NN] = 1000
rpa[rpa_5HT][k_NN] = 1000
rostral_group[rostral_group_A1][k_NN] = 1000  # not real
rostral_group[rostral_group_A2][k_NN] = 1000  # not real
septum[septum_5HT][k_NN] = 1000  # not real
striatum[striatum_5HT][k_NN] = 1250000
striatum[striatum_DA][k_NN] = 12500000
substantia_nigra[substantia_nigra_5HT][k_NN] = 31450
substantia_nigra[substantia_nigra_DA][k_NN] = 31450
thalamus[thalamus_5HT][k_NN] = 5000000
vta[vta_5HT][k_NN] = 30500
vta[vta_DA][k_NN] = 30500