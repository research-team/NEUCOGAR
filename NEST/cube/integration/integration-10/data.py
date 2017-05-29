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
       {k_name: 'LDT [Ach]'},
       {k_name: 'LDT [5HT]'})
ldt_a1, ldt_a2, ldt_Ach, ldt_5HT = range(4)


bnst = ({k_name: 'Bed nucleus of the stria terminalis [GABA]'},
	{k_name: 'Bed nucleus of the stria terminalis [Glu]'},
	{k_name: 'Bed nucleus of the stria terminalis [5HT]'},
	{k_name: 'Bed nucleus of the stria terminalis [Ach]'})
bnst_GABA, bnst_Glu, bnst_5HT, bnst_Ach = range(4)

amygdala = ({k_name: 'Amygdala [Glu]'},
	{k_name: 'Amygdala [Ach]'},
	{k_name: 'Amygdala [5HT]'},
	{k_name: 'Amygdala [GABA]'})
amygdala_Glu, amygdala_Ach, amygdala_5HT, amygdala_GABA  = range(4)

#dorsal

vta = ({k_name: 'VTA [Da0]'},
       {k_name: 'VTA [Da1]'},
       {k_name: 'VTA [5HT]'},
       {k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [GABA2]'},
       {k_name: 'VTA [a1]'})
vta_DA0, vta_DA1, vta_5HT, vta_GABA0, vta_GABA1, vta_GABA2, vta_a1 = range(7)


pgi = ({k_name: 'Nucleus paragigantocellularis lateralis [GABA]'},
	{k_name: 'Nucleus paragigantocellularis lateralis [Glu]'})
pgi_GABA, pgi_Glu = range(2)

rn = ({k_name: 'Raphe nuclei [a1]'},
      {k_name: 'Raphe nuclei [a2]'},
      {k_name: 'Raphe nuclei [rmg]'},
      {k_name: 'Raphe nuclei [rpa]'},
      {k_name: 'Raphe nuclei [dr]'},
      {k_name: 'Raphe nuclei [mnr]'},
)
rn_a1, rn_a2, rn_rmg, rn_rpa, rn_dr, rn_mnr = range(6)

#################################
motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'},
         {k_name: 'Motor cortex [5HT]'},)
motor_Glu0, motor_Glu1, motor_5HT = range(3)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'},
            {k_name: 'Striatum [5HT]'},
            {k_name: 'Striatum [Ach]'},
            {k_name: 'Striatum [GABA]'}
            )
striatum_D1, striatum_D2, striatum_tan, striatum_5HT, striatum_Ach, striatum_GABA = range(6)

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
thalamus_Glu, thalamus_5HT = range(2)

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'},
              {k_name: 'Prefrontal cortex [DA]'},
              {k_name: 'Prefrontal cortex [5HT]'},
              {k_name: 'Prefrontal cortex [NA]'}
              )
pfc_Glu0, pfc_Glu1, pfc_DA, pfc_5HT, pfc_NA = range(5)


#################################### but it's a part of striatum??
nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'},
       {k_name: 'NAc [DA]'},
       {k_name: 'NAc [5HT]'},
       {k_name: 'NAc [NA]'}
       )
nac_Ach, nac_GABA0, nac_GABA1, nac_DA, nac_5HT, nac_NA = range(6)


################################## but it projects SERO to rn_dr?
pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [5HT]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_5HT, pptg_Glu = range(4)

medial_cortex = ({k_name: 'Medial cortex [5HT]'}, )
medial_cortex_5HT = 0

prh = ({k_name: 'Perirhinal cortex [GABA]'},)
prh_GABA = 0

neocortex = ({k_name: 'Neocortex [5HT]'}, )
neocortex_5HT = 0

lateral_cortex = ({k_name: 'Lateral cortex [5HT]'}, )
lateral_cortex_5HT = 0

entorhinal_cortex = ({k_name: 'Entorhial cortex [5HT]'}, )
entorhinal_cortex_5HT = 0

septum = ({k_name: 'Septum [5HT]'}, )
septum_5HT = 0

lateral_tegmental_area = ({k_name: 'Lateral tegmental area [5HT]'}, )
lateral_tegmental_area_5HT = 0

periaqueductal_gray = ({k_name: 'Periaqueductal gray [5HT]'}, )
periaqueductal_gray_5HT = 0

hippocampus = ({k_name: 'Hippocampus [5HT]'}, )
hippocampus_5HT = 0

hypothalamus = ({k_name: 'Hypothalamus [5HT]'},
                {k_name: 'Hypothalmus paraventricular nucleus [GABA]'})
hypothalamus_5HT, hypothalamus_pvn_GABA = range(2)

insular_cortex = ({k_name: 'Insular cortex [5HT]'}, )
insular_cortex_5HT = 0

cerebral_cortex_NN = 29000
motor[motor_Glu0][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
motor[motor_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
motor[motor_5HT][k_NN] = 10000

striatum_NN = 25000
striatum[striatum_D1][k_NN] = int(striatum_NN * 0.425)
striatum[striatum_D2][k_NN] = int(striatum_NN * 0.425)
striatum[striatum_tan][k_NN] = int(striatum_NN * 0.05)
striatum[striatum_5HT][k_NN] = 1250
striatum[striatum_Ach][k_NN] = 1250
striatum[striatum_GABA][k_NN] = 1250

gpe[gpe_GABA][k_NN] = 8410
gpi[gpi_GABA][k_NN] = 1260
stn[stn_Glu][k_NN] = 2270
snc[snc_GABA][k_NN] = 3000              #TODO check number of neurons
snc[snc_DA][k_NN] = 1270               #TODO check number of neurons
snr[snr_GABA][k_NN] = 4720

prefrontal[pfc_Glu0][k_NN] = 1830
prefrontal[pfc_Glu1][k_NN] = 1830
prefrontal[pfc_DA][k_NN] = 1000
prefrontal[pfc_5HT][k_NN] = 8000
prefrontal[pfc_NA][k_NN] = 8000


nac[nac_Ach][k_NN] = 1500               #TODO not real!!!
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
vta[vta_a1][k_NN] = 2000

pptg[pptg_GABA][k_NN] = 2000
pptg[pptg_ACh][k_NN] = 1400
pptg[pptg_5HT][k_NN] = 1400
pptg[pptg_Glu][k_NN] = 2300

amygdala[amygdala_Glu][k_NN] = 3000
amygdala[amygdala_GABA][k_NN] = 1425
amygdala[amygdala_Ach][k_NN] = 6632
amygdala[amygdala_5HT][k_NN] = 3000

bnst[bnst_GABA][k_NN] = 1200
bnst[bnst_Glu][k_NN] = 3150
bnst[bnst_Ach][k_NN] = 2200
bnst[bnst_5HT][k_NN] = 500

entorhinal_cortex[entorhinal_cortex_5HT][k_NN] = 6350
hippocampus[hippocampus_5HT][k_NN] = 4260
hypothalamus[hypothalamus_5HT][k_NN] = 1000
hypothalamus[hypothalamus_pvn_GABA][k_NN] = 1000
insular_cortex[insular_cortex_5HT][k_NN] = 1000

lateral_cortex[lateral_cortex_5HT][k_NN] = 1000
medial_cortex[medial_cortex_5HT][k_NN] = 1000
septum[septum_5HT][k_NN] = 1000
lateral_tegmental_area[lateral_tegmental_area_5HT][k_NN] = 1000
neocortex[neocortex_5HT][k_NN] = 1000
periaqueductal_gray[periaqueductal_gray_5HT][k_NN] = 1000

thalamus[thalamus_5HT][k_NN] = 5000
thalamus[thalamus_Glu][k_NN] = int(5000 / 6) #!!!!


#noradrenaline sources
lc[lc_D1][k_NN] = 500
lc[lc_D2][k_NN] = 500
lc[lc_Ach][k_NN] = 500
lc[lc_N0][k_NN] = 1750
lc[lc_N1][k_NN] = 1750
lc[lc_GABA][k_NN] = 400
lc[lc_5HT][k_NN] = 5000

nts[nts_a1][k_NN] = 3500
nts[nts_a2][k_NN] = 1300

#ventral
ldt[ldt_Ach][k_NN] = 18100
ldt[ldt_a1][k_NN] = 18000
ldt[ldt_a2][k_NN] = 18000
ldt[ldt_5HT][k_NN] = 1000
pgi[pgi_GABA][k_NN] = 15000
pgi[pgi_Glu][k_NN] = 15000


rn[rn_a1][k_NN] = 29000
rn[rn_a2][k_NN] = 29000
rn[rn_rmg][k_NN] = 1000
rn[rn_rpa][k_NN] = 1000
rn[rn_dr][k_NN] = 1800
rn[rn_mnr][k_NN] = 1100
prh[prh_GABA][k_NN] = 36200
