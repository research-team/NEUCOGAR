from api_initialisation import *
from api_connections import *
from api_diagrams import *

from build_structure import *
from parameters import *
from data import *

SetKernelStatus(local_num_threads=4,
                data_path='txt')

InitNeuronModel(IAF_PSC_ALPHA, pyramidal_no_dopa, iaf_neuronparams)
InitNeuronModel(IAF_PSC_EXP, pyramidal_with_dopa, iaf_neuronparams)

InitSynapseModel(Glu, STDP_MODEL, stdp_glu_params)
InitSynapseModel(GABA, STDP_MODEL, stdp_gaba_params)
InitSynapseModel(ACh, STDP_MODEL, stdp_ach_params)
InitSynapseModel(DA_ex, STDP_DOPA_MODEL, stdp_dopa_ex_params, vt=True)
InitSynapseModel(DA_in, STDP_DOPA_MODEL, stdp_dopa_in_params, vt=True)

GenerateStructure(5000)

Connect(motor[motor_Glu0], striatum[D1], neurotransmitter=Glu, conc_coef=0.005)
Connect(motor[motor_Glu0], snc[snc_DA], neurotransmitter=Glu, conc_coef=0.000005)
Connect(motor[motor_Glu0], striatum[D2], neurotransmitter=Glu, conc_coef=0.05)
Connect(motor[motor_Glu0], thalamus[thalamus_Glu], neurotransmitter=Glu, conc_coef=0.008)
Connect(motor[motor_Glu0], stn[stn_Glu], neurotransmitter=Glu, conc_coef=7)
Connect(motor[motor_Glu1], striatum[D1], neurotransmitter=Glu)
Connect(motor[motor_Glu1], striatum[D2], neurotransmitter=Glu)
Connect(motor[motor_Glu1], thalamus[thalamus_Glu], neurotransmitter=Glu)
Connect(motor[motor_Glu1], stn[stn_Glu], neurotransmitter=Glu)
Connect(motor[motor_Glu1], nac[nac_GABA0])

Connect(striatum[tan], striatum[D1])
Connect(striatum[tan], striatum[D2], neurotransmitter=Glu)

Connect(striatum[D1], snr[snr_GABA], conc_coef=0.00005)
Connect(striatum[D1], gpi[gpi_GABA], conc_coef=0.00005)
Connect(striatum[D1], gpe[gpe_GABA], conc_coef=0.000005)
Connect(striatum[D2], gpe[gpe_GABA], conc_coef=1)

Connect(gpe[gpe_GABA], stn[stn_Glu], conc_coef=0.0001)
Connect(gpe[gpe_GABA], striatum[D1], conc_coef=0.001)
Connect(gpe[gpe_GABA], striatum[D2], conc_coef=0.3)
Connect(gpe[gpe_GABA], gpi[gpi_GABA], conc_coef=0.0001)
Connect(gpe[gpe_GABA], snr[snr_GABA], conc_coef=0.0001)

Connect(stn[stn_Glu], snr[snr_GABA], neurotransmitter=Glu, conc_coef=20)
Connect(stn[stn_Glu], gpi[gpi_GABA], neurotransmitter=Glu, conc_coef=20)
Connect(stn[stn_Glu], gpe[gpe_GABA], neurotransmitter=Glu, conc_coef=0.3)
Connect(stn[stn_Glu], snc[snc_DA], neurotransmitter=Glu, conc_coef=0.000005)

Connect(gpi[gpi_GABA], thalamus[thalamus_Glu], conc_coef=3)
Connect(snr[snr_GABA], thalamus[thalamus_Glu], conc_coef=3)

Connect(thalamus[thalamus_Glu], motor[motor_Glu1], neurotransmitter=Glu)
Connect(thalamus[thalamus_Glu], stn[stn_Glu], neurotransmitter=Glu, conc_coef=1) #005
Connect(thalamus[thalamus_Glu], striatum[D1], neurotransmitter=Glu, conc_coef=0.005)
Connect(thalamus[thalamus_Glu], striatum[D2], neurotransmitter=Glu, conc_coef=0.005)
Connect(thalamus[thalamus_Glu], striatum[tan], neurotransmitter=Glu, conc_coef=0.005)
Connect(thalamus[thalamus_Glu], nac[nac_GABA0], neurotransmitter=Glu)
Connect(thalamus[thalamus_Glu], nac[nac_GABA1], neurotransmitter=Glu)
Connect(thalamus[thalamus_Glu], nac[nac_ACh], neurotransmitter=Glu)

# * * * MESOCORTICOLIMBIC * * *
Connect(nac[nac_ACh], nac[nac_GABA1], neurotransmitter=ACh)
Connect(nac[nac_GABA0], nac[nac_GABA1])
Connect(nac[nac_GABA1], vta[vta_GABA2])

Connect(vta[vta_GABA0], prefrontal[pfc_Glu0])
Connect(vta[vta_GABA0], prefrontal[pfc_Glu1])
Connect(vta[vta_GABA0], pptg[pptg_GABA])
Connect(vta[vta_GABA1], vta[vta_DA0])
Connect(vta[vta_GABA1], vta[vta_DA1])
Connect(vta[vta_GABA2], nac[nac_GABA1])

Connect(pptg[pptg_GABA], vta[vta_GABA0])
Connect(pptg[pptg_GABA], snc[snc_GABA], conc_coef=0.000005)
Connect(pptg[pptg_ACh], vta[vta_GABA0], neurotransmitter=ACh)
Connect(pptg[pptg_ACh], vta[vta_DA1], neurotransmitter=ACh)
Connect(pptg[pptg_Glu], vta[vta_GABA0], neurotransmitter=Glu)
Connect(pptg[pptg_Glu], vta[vta_DA1], neurotransmitter=Glu)
Connect(pptg[pptg_ACh], striatum[D1], neurotransmitter=ACh, conc_coef=0.3)
Connect(pptg[pptg_ACh], snc[snc_GABA], neurotransmitter=ACh, conc_coef=0.000005)
Connect(pptg[pptg_Glu], snc[snc_DA], neurotransmitter=Glu, conc_coef=0.000005)

# * * * INTEGRATED * * *
Connect(prefrontal[pfc_Glu0], vta[vta_DA0], neurotransmitter=Glu)
Connect(prefrontal[pfc_Glu0], nac[nac_GABA1], neurotransmitter=Glu)
Connect(prefrontal[pfc_Glu1], vta[vta_GABA2], neurotransmitter=Glu)
Connect(prefrontal[pfc_Glu1], nac[nac_GABA1], neurotransmitter=Glu)

Connect(amygdala[amygdala_Glu], nac[nac_GABA0], neurotransmitter=Glu)
Connect(amygdala[amygdala_Glu], nac[nac_GABA1], neurotransmitter=Glu)
Connect(amygdala[amygdala_Glu], nac[nac_ACh], neurotransmitter=Glu)
Connect(amygdala[amygdala_Glu], striatum[D1], neurotransmitter=Glu, conc_coef=0.3)
Connect(amygdala[amygdala_Glu], striatum[D2], neurotransmitter=Glu, conc_coef=0.3)
Connect(amygdala[amygdala_Glu], striatum[tan], neurotransmitter=Glu, conc_coef=0.3)

Connect(snc[snc_DA], striatum[D1], neurotransmitter=DA_ex)
Connect(snc[snc_DA], gpe[gpe_GABA], neurotransmitter=DA_ex)
Connect(snc[snc_DA], stn[stn_Glu], neurotransmitter=DA_ex)
Connect(snc[snc_DA], nac[nac_GABA0], neurotransmitter=DA_ex)
Connect(snc[snc_DA], nac[nac_GABA1], neurotransmitter=DA_ex)
Connect(snc[snc_DA], striatum[D2], neurotransmitter=DA_in)
Connect(snc[snc_DA], striatum[tan], neurotransmitter=DA_in)
Connect(vta[vta_DA0], striatum[D1], neurotransmitter=DA_ex)
Connect(vta[vta_DA0], striatum[D2], neurotransmitter=DA_in)
Connect(vta[vta_DA0], prefrontal[pfc_Glu0], neurotransmitter=DA_ex)
Connect(vta[vta_DA0], prefrontal[pfc_Glu1], neurotransmitter=DA_ex)
Connect(vta[vta_DA1], nac[nac_GABA0], neurotransmitter=DA_ex)
Connect(vta[vta_DA1], nac[nac_GABA1], neurotransmitter=DA_ex)

ConnectPoissonGenerator(motor[motor_Glu0], rate=300, prob=1, weight=w_Glu*5)
ConnectPoissonGenerator(pptg[pptg_GABA], 400., 600., rate=250, prob=1, weight=w_Glu*5)
ConnectPoissonGenerator(pptg[pptg_Glu], 400., 600., rate=250, prob=1, weight=w_Glu*5)
ConnectPoissonGenerator(pptg[pptg_ACh], 400., 600., rate=250, prob=1, weight=w_Glu*5)
ConnectPoissonGenerator(amygdala[amygdala_Glu], 400., 600., rate=250, prob=1, weight=w_Glu*5)
ConnectPoissonGenerator(snc[snc_DA], 400., 600., rate=250, prob=1, weight=w_Glu*5)
ConnectPoissonGenerator(vta[vta_DA0], 400., 600., rate=250, prob=1, weight=w_Glu*5)

for part in glob.all_parts:
    ConnectDetector(part)

for part in glob.all_parts:
    ConnectMultimeter(part)

Simulate()

BuildSpikeDiagrams()
BuildVoltageDiagrams()