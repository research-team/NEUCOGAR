from api_initialisation import *
from api_connections import *
from api_diagrams import *

from build_structure import *
from parameters import *
from data import *

SetKernelStatus(local_num_threads=4,
                data_path='txt')

InitNeuronModel(HH_PSC_ALPHA, pyramidal_no_dopa, iaf_neuronparams)

InitSynapseModel(Glu, STDP_MODEL, stdp_glu_params)
InitSynapseModel(GABA, STDP_MODEL, stdp_gaba_params)
InitSynapseModel(DOPA_ex, STDP_DOPA_MODEL, stdp_dopa_ex_params, vt=True)
InitSynapseModel(DOPA_in, STDP_DOPA_MODEL, stdp_dopa_in_params, vt=True)

GenerateStructure(7000)

Connect(motor[motor_Glu0], striatum[D1], neurotransmitter=Glu, weight_coef=0.005)
Connect(motor[motor_Glu0], striatum[D2], neurotransmitter=Glu, weight_coef=0.05)
Connect(motor[motor_Glu0], thalamus[thalamus_Glu], neurotransmitter=Glu, weight_coef=0.08)
Connect(motor[motor_Glu0], stn[stn_Glu], neurotransmitter=Glu, weight_coef=1)

Connect(striatum[D1], snr[snr_GABA], weight_coef=0.01)
Connect(striatum[D1], gpi[gpi_GABA], weight_coef=0.01)

Connect(striatum[D2], gpe[gpe_GABA], weight_coef=0.01)

Connect(gpe[gpe_GABA], stn[stn_Glu], weight_coef=0.1)

Connect(stn[stn_Glu], snr[snr_GABA], neurotransmitter=Glu, weight_coef=1)
Connect(stn[stn_Glu], gpi[gpi_GABA], neurotransmitter=Glu, weight_coef=1)
Connect(stn[stn_Glu], gpe[gpe_GABA], neurotransmitter=Glu, weight_coef=0.3)

Connect(gpi[gpi_GABA], thalamus[thalamus_Glu], weight_coef=3)
Connect(snr[snr_GABA], thalamus[thalamus_Glu], weight_coef=3)

Connect(thalamus[thalamus_Glu], motor[motor_Glu1], neurotransmitter=Glu, weight_coef=1.0)

Connect(snc[snc_DA], striatum[D1], neurotransmitter=DOPA_ex)
Connect(snc[snc_DA], striatum[D2], neurotransmitter=DOPA_in)

Connect(vta[vta_DA], striatum[D1], neurotransmitter=DOPA_ex)
Connect(vta[vta_DA], striatum[D2], neurotransmitter=DOPA_in)


ConnectPoissonGenerator(gpe[gpe_GABA], rate=300, prob=1., weight=w_Glu*5)
ConnectPoissonGenerator(snc[snc_DA], 400., 600., rate=250, prob=1., weight=w_Glu*5)
ConnectPoissonGenerator(vta[vta_DA], 400., 600., rate=300, prob=1., weight=w_Glu*5)


Connect(motor[motor_Glu0], striatum[D1], neurotransmitter=Glu, weight_coef=0.005)

for part in glob.all_parts:
    ConnectDetector(part)

for part in glob.all_parts:
    ConnectMultimeter(part)

Simulate(1000.)

BuildSpikeDiagrams()
BuildVoltageDiagrams()