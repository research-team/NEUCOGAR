from keys import *
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
    -PVN:	Paraventicular nucleus
    -LC:	Locus Coeruleus
    -NTS:	Nucleus tracti solitari
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
	{k_name: 'LC [GABA]'})
lc_D1, lc_D2, lc_Ach, lc_N1, lc_N0, lc_GABA = range(6)

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
	{k_name: 'Bed nucleus of the stria terminalis [Ach]'})
bnst_GABA, bnst_Glu, bnst_Ach = range(3)

thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0

pvn = ({k_name: 'Paraventicular nucleus'}, )
pvn_n = 0

motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_Glu0, motor_Glu1 = range(2)


amygdala = ({k_name: 'Amygdala [Glu]'},
	{k_name: 'Amygdala [Ach]'},
	{k_name: 'Amygdala [GABA]'})
amygdala_Glu,amygdala_Ach,amygdala_GABA  = range(3)

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

prefrontal = ({k_name: 'Prefrontal cortex [Glu]'}, )
pfc_Glu = 0

rn = ({k_name: 'RN [a1]'},
      {k_name: 'RN [a2]'})
rn_a1, rn_a2 = range(2)


striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'})
D1, D2, tan = range(3)

prh = ({k_name: 'Perirhinal cortex [GABA]'},)
prh_GABA = 0
################################################### dopa

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

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'})
nac_ACh, nac_GABA0, nac_GABA1  = range(3)

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_Glu = range(3)


#nora numbers
"""
lc[lc_D1][k_NN] = 30
lc[lc_D2][k_NN] = 30
lc[lc_N0][k_NN] = 30
lc[lc_N1][k_NN] = 30
lc[lc_Ach][k_NN] = 30
lc[lc_GABA][k_NN] = 30
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
thalamus[thalamus_Glu][k_NN] = 30
amygdala[amygdala_Glu][k_NN] = 30
amygdala[amygdala_GABA][k_NN] = 30
amygdala[amygdala_Ach][k_NN] = 30
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
prefrontal[pfc_Glu][k_NN] = 40
striatum[D1][k_NN] = 30
striatum[D2][k_NN] = 30
striatum[tan][k_NN] = 30
prh[prh_GABA][k_NN] = 30
#dopa numbers
gpe[gpe_GABA][k_NN] = 40
gpi[gpi_GABA][k_NN] = 30
stn[stn_Glu][k_NN] = 20
snc[snc_GABA][k_NN] = 30              #TODO check number of neurons
snc[snc_DA][k_NN] = 30              #TODO check number of neurons
snr[snr_GABA][k_NN] = 40
nac[nac_ACh][k_NN] = 50               #TODO not real!!!
nac[nac_GABA0][k_NN] = 30            #TODO not real!!!
nac[nac_GABA1][k_NN] = 30            #TODO not real!!!
pptg[pptg_GABA][k_NN] = 30
pptg[pptg_ACh][k_NN] = 30
pptg[pptg_Glu][k_NN] = 30
"""


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
prefrontal[pfc_Glu][k_NN] = 400
striatum[D1][k_NN] = 1500
striatum[D2][k_NN] = 1500
striatum[tan][k_NN] = 14250
prh[prh_GABA][k_NN] = 3627

#dopa numbers

gpe[gpe_GABA][k_NN] = 40
gpi[gpi_GABA][k_NN] = 30
stn[stn_Glu][k_NN] = 20
snc[snc_GABA][k_NN] = 30              #TODO check number of neurons
snc[snc_DA][k_NN] = 30              #TODO check number of neurons
snr[snr_GABA][k_NN] = 40
nac[nac_ACh][k_NN] = 50               #TODO not real!!!
nac[nac_GABA0][k_NN] = 30            #TODO not real!!!
nac[nac_GABA1][k_NN] = 30            #TODO not real!!!
pptg[pptg_GABA][k_NN] = 30
pptg[pptg_ACh][k_NN] = 30
pptg[pptg_Glu][k_NN] = 30