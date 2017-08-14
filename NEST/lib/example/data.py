from api_globals import *


motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_Glu0, motor_Glu1 = range(2)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'})
D1, D2 = range(2)

gpe = ({k_name: 'GPe [GABA]'}, )
gpe_GABA = 0

gpi = ({k_name: 'GPi [GABA]'}, )
gpi_GABA = 0

stn = ({k_name: 'STN [Glu]'}, )
stn_Glu = 0

snr = ({k_name: 'SNr [GABA]'}, )
snr_GABA = 0

snc = ({k_name: 'SNc [DA]'}, )
snc_DA = 0

thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0

vta = ({k_name: 'VTA [DA]'}, )
vta_DA = 0

cerebral_cortex_NN = 29000000
motor[motor_Glu0][k_NN] = int(cerebral_cortex_NN * 0.8 / 6)
motor[motor_Glu1][k_NN] = int(cerebral_cortex_NN * 0.2 / 6)
striatum_NN = 2500000
striatum[D1][k_NN] = int(striatum_NN * 0.425)
striatum[D2][k_NN] = int(striatum_NN * 0.425)
gpe[gpe_GABA][k_NN] = 84100
gpi[gpi_GABA][k_NN] = 12600
stn[stn_Glu][k_NN] = 22700
snc[snc_DA][k_NN] = 12700               #TODO check number of neurons
vta[vta_DA][k_NN] = 20000
snr[snr_GABA][k_NN] = 47200
thalamus[thalamus_Glu][k_NN] = int(5000000 / 6) #!!!!


pyramidal_no_dopa = 'pyramidal1'
pyramidal_with_dopa = 'pyramidal2'