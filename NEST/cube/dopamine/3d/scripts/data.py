from property import *
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
Prefix description:
    -GABA - GABA
    -Glu  - glutamate
    -ACh  - acetylcholine
    -DA   - dopamine
"""


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