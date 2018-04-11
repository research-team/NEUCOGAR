
from neucogar.namespaces import *
from neucogar.api_kernel import CreateNetwork
from neucogar.SynapseModel import SynapseModel

import neucogar.api_kernel as kern

from .brain_parts import *

# Init synapses
Glutamatergic = SynapseModel("Glutamatergic", nest_model=STDP_SYNAPSE, params=stdp_glu_params)
GABAergic = SynapseModel("GABAergic", nest_model=STDP_SYNAPSE, params=stdp_gaba_params)
Dopaminergic_ex = SynapseModel("Dopaminergic_ex", nest_model=STDP_DOPA_SYNAPSE, params=stdp_dopa_ex_params)
Dopaminergic_in = SynapseModel("Dopaminergic_in", nest_model=STDP_DOPA_SYNAPSE, params=stdp_dopa_in_params)

NA_ex = SynapseModel("NA_ex", nest_model=STDP_NORA_SYNAPSE, params=stdp_dopa_ex_params)

# Set connectomes
for index in sensory_cortex.getColumnsIndexes():
	sensory_cortex.columns(index).layers(L6).nuclei(Glu).connect(striatum.nuclei(GABA_D1), synapse=Glutamatergic, synMax= 1300, weight=10) # 1 < X < 2 s1000-w20 -500		12
	sensory_cortex.columns(index).layers(L6).nuclei(Glu).connect(striatum.nuclei(GABA_D2), synapse=Glutamatergic, synMax= 1500, weight=20) # 1 < X < 2 s1000-w10 w12 15 17 s800 900 -500	23
	sensory_cortex.columns(index).layers(L6).nuclei(Glu).connect(stn.nuclei(Glu), synapse=Glutamatergic, synMax= 900, weight=2) # ? < X < 0.3		s10000-w0.3 s1000-w11 7 4 1 0.3 s800 w0.2 2
	sensory_cortex.columns(index).layers(L6).nuclei(Glu).connect(thalamus.nuclei(Glu_0), synapse=Glutamatergic, synMax=1300, weight=29.5)	# 2 < X < 3	s500-w17 good 18 21 23 26 s600 w29 30 28.5 // s1300 w26		28.5 26 27 GOOD 28 STDP !=0; 28

for index in sensory_cortex.getColumnsIndexes():
	thalamus.nuclei(Glu_0).connect(motor_cortex.columns(index).layers(L4).nuclei(Glu), synapse=Glutamatergic, weight= 1)	# ? < X < 1 1 0.8

striatum.nuclei(GABA_D1).connect(snr.nuclei(GABA), synapse=GABAergic, weight= -0.00005) # -0.0005 < X < ?
striatum.nuclei(GABA_D1).connect(gpi.nuclei(GABA), synapse=GABAergic, weight= -0.00005) # -0.0005 < X < ?
striatum.nuclei(GABA_D2).connect(gpe.nuclei(GABA), synapse=GABAergic, weight= -2.5) # -0.0005 < X < ?	0.3 0.001 0.005 0.1 1 3 4 x10 4.5

gpe.nuclei(GABA).connect(stn.nuclei(Glu), synapse=GABAergic, weight= -5) # 0.5 < X < ?		1 3 7 10 12 8

stn.nuclei(Glu).connect(snr.nuclei(GABA), synapse=Glutamatergic, weight= 1) # 0.5 < X < 2	2
stn.nuclei(Glu).connect(gpi.nuclei(GABA), synapse=Glutamatergic, weight= 1) # 0.5 < X < 2	2

gpi.nuclei(GABA).connect(thalamus.nuclei(Glu_0), synapse=GABAergic, weight= -0.7) # 2 < X < ?	0.2 2 5 10 13 16 18 25 29 32 37 10
snr.nuclei(GABA).connect(thalamus.nuclei(Glu_0), synapse=GABAergic, weight= -0.7) # 2 < X < ?	0.2 2 5 10 13 16 18 25 29 32 37 10

snc.nuclei(DA).connect(striatum.nuclei(GABA_D1), synapse=Dopaminergic_ex, weight= 8) # 0.6 < X < ?	5 3 6 10
vta.nuclei(DA).connect(striatum.nuclei(GABA_D1), synapse=Dopaminergic_ex, weight= 8) # 0.6 < X < ?	5 3 6 10

snc.nuclei(DA).connect(striatum.nuclei(GABA_D2), synapse=Dopaminergic_in, weight= -25) # 0.6 < X < ?	7 15 25 50 75
vta.nuclei(DA).connect(striatum.nuclei(GABA_D2), synapse=Dopaminergic_in, weight= -25) # 0.6 < X < ?    7 15 25 50 75

vta.nuclei(DA).connect(striatum.nuclei(GABA_D2), synapse=GABAergic, weight= -5) # 0.6 < X < ? 3
snc.nuclei(DA).connect(striatum.nuclei(GABA_D2), synapse=GABAergic, weight= -5) # 0.6 < X < ? 3



# Connect spikegenerators
sensory_cortex.columns(0).layers(L4).nuclei(Glu).ConnectPoissonGenerator(rate=350, conn_percent=70, weight=40) # 40 < X < 50

"""
snc.nuclei(DA).ConnectPoissonGenerator(start=100, stop=300, rate=420, conn_percent=100, weight=40)	# 70 r350 550 450
vta.nuclei(DA).ConnectPoissonGenerator(start=100, stop=300, rate=420, conn_percent=100, weight=40)	# 70

snc.nuclei(DA).ConnectPoissonGenerator(start=550, stop=750, rate=800, conn_percent=100, weight=40)	# 70 r350 550 450
vta.nuclei(DA).ConnectPoissonGenerator(start=550, stop=750, rate=800, conn_percent=100, weight=40)	# 70


snc.nuclei(DA).ConnectPoissonGenerator(start=1450, stop=1650, rate=420, conn_percent=100, weight=40)      # 70 r350 550 450
vta.nuclei(DA).ConnectPoissonGenerator(start=1450, stop=1650, rate=420, conn_percent=100, weight=40)      # 70

"""

# 2 level
for i in [7250, 8000, 8750, 9500, 10250, 11000, 11750, 12500, 13250]:
	snc.nuclei(DA).ConnectPoissonGenerator(start=i, stop=i+250, rate=420, conn_percent=100, weight=40)	# 70 r350 550 450
	vta.nuclei(DA).ConnectPoissonGenerator(start=i, stop=i+250, rate=420, conn_percent=100, weight=40)	# 70

# 3 level
for i in [14000, 14750, 15500, 16250, 17000, 17750, 18500, 19250, 20000]:
	snc.nuclei(DA).ConnectPoissonGenerator(start=i, stop=i+250, rate=800, conn_percent=100, weight=40)
	vta.nuclei(DA).ConnectPoissonGenerator(start=i, stop=i+250, rate=800, conn_percent=100, weight=40)

gpe.nuclei(GABA).ConnectPoissonGenerator(rate=360, conn_percent=50, weight=40) # %50 w40 r350 320 350 370


# Connect spikedetectors

sensory_cortex.columns(0).layers(L2).nuclei(Glu).ConnectDetector()
sensory_cortex.columns(0).layers(L4).nuclei(Glu).ConnectDetector()
sensory_cortex.columns(0).layers(L5B).nuclei(Glu).ConnectDetector()
sensory_cortex.columns(0).layers(L6).nuclei(Glu).ConnectDetector()

motor_cortex.columns(1).layers(L4).nuclei(Glu).ConnectDetector()
motor_cortex.columns(1).layers(L6).nuclei(Glu).ConnectDetector()

striatum.nuclei(GABA_D1).ConnectDetector()
striatum.nuclei(GABA_D2).ConnectDetector()

thalamus.nuclei(Glu_0).ConnectDetector()

gpi.nuclei(GABA).ConnectDetector()
snr.nuclei(GABA).ConnectDetector()

stn.nuclei(Glu).ConnectDetector()

gpe.nuclei(GABA).ConnectDetector()

vta.nuclei(DA).ConnectDetector()
snc.nuclei(DA).ConnectDetector()
