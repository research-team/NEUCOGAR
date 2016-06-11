from property import *

motor = ({k_name: 'FrontalCortex [Glu0]'},
         {k_name: 'Cortex [Glu1]'})
FrontalCortex, Cortex = range(2)

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

vta = ({k_name: 'VTA [DA0]'}, )
vta_DA0 = 0

if test_flag:
    # TEST NUMBER
    motor[FrontalCortex][k_NN] = 60
    motor[Cortex][k_NN] = 150
    striatum[D1][k_NN] = 30
    striatum[D2][k_NN] = 30
    striatum[tan][k_NN] = 8
    gpe[gpe_GABA][k_NN] = 30
    gpi[gpi_GABA][k_NN] = 10
    stn[stn_Glu][k_NN] = 15
    snc[snc_GABA][k_NN] = 40
    snc[snc_DA][k_NN] = 100
    snr[snr_GABA][k_NN] = 21
    thalamus[thalamus_Glu][k_NN] = 90
    vta[vta_DA0][k_NN] = 20
else:
    # REAL NUMBER
    cerebral_cortex_NN = 29000000
    motor[FrontalCortex][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
    motor[Cortex][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
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
    vta[vta_DA0][k_NN] = 20000