from neucogar.namespaces import *
from neucogar.api_kernel import CreateNetwork
from neucogar.SynapseModel import SynapseModel

from .brain_parts import *
from dopamine.connectomes import *

# Init synapses
Serotoninergic_ex = SynapseModel("Serotoninergic_ex", nest_model=STDP_SERO_SYNAPSE, params=stdp_sero_ex_params)
Serotoninergic_in = SynapseModel("Serotoninergic_in", nest_model=STDP_SERO_SYNAPSE, params=stdp_sero_in_params)

# Glu 0 - VA/VL
# GLu1 - midline nuclei

#pfc.nuclei(Glu).connect(drn.nuclei(HT5), synapse=Glutamatergic, weight=10)
#pfc.nuclei(GABA).connect(pfc.nuclei(Glu), synapse=GABAergic, weight=-10)

###thalamus.nuclei(Glu_1).connect(pfc.columns(0).layers(L4).nuclei(Glu), synapse=Glutamatergic, weight=5)

#vta.nuclei(DA).connect(pfc.columns(0).layers(L4).nuclei(Glu), synapse=Dopaminergic_ex, weight=5)

#vta.nuclei(DA).connect(drn.nuclei(HT5), synapse=Dopaminergic_ex, weight=10)
#snc.nuclei(DA).connect(drn.nuclei(HT5), synapse=Dopaminergic_ex, weight=10)

# !!! locus_coeruleus.nuclei(NA).connect(drn.nuclei(HT5), synapse=NA , weight=1)

locus_coeruleus.nuclei(NA).connect(vta.nuclei(DA), synapse=NA_ex, weight=5)	# 10 4
locus_coeruleus.nuclei(NA).connect(snc.nuclei(DA), synapse=NA_ex, weight=5)	# 10 4

#hippocampus.nuclei(Glu).connect(drn.nuclei(HT5), synapse=Glutamatergic, weight=10)
#hippocampus.nuclei(GABA).connect(hippocampus.nuclei(Glu), synapse=GABAergic, weight=-10)

#amygdala.nuclei(Glu).connect(drn.nuclei(HT5), synapse=Glutamatergic, weight=10)

#hypothalamus.nuclei(Glu).connect(hypothalamus.nuclei(GABA), synapse=Glutamatergic, weight=10)
#hypothalamus.nuclei(GABA).connect(drn.nuclei(HT5), synapse=GABAergic, weight=-10)

#drn.nuclei(GABA).connect(drn.nuclei(HT5), synapse=GABAergic, weight=-10)

drn.nuclei(HT5).connect(hypothalamus.nuclei(GABA), synapse=Serotoninergic_in, weight=-10)
drn.nuclei(HT5).connect(hypothalamus.nuclei(GABA), synapse=GABAergic, weight=-0.5)

drn.nuclei(HT5).connect(amygdala.nuclei(Glu), synapse=Serotoninergic_in, weight=-10)
drn.nuclei(HT5).connect(amygdala.nuclei(Glu), synapse=GABAergic, weight=-0.5)

hypothalamus.nuclei(GABA).ConnectPoissonGenerator(rate=300, conn_percent=70, weight=60) 
amygdala.nuclei(Glu).ConnectPoissonGenerator(rate=300, conn_percent=70, weight=60) 


######drn.nuclei(HT5).connect(hippocampus.nuclei(GABA), synapse=Serotoninergic_ex, weight=10)

drn.nuclei(HT5).connect(thalamus.nuclei(Glu_0), synapse=Serotoninergic_in, weight= -7)	# < 1? 2
drn.nuclei(HT5).connect(thalamus.nuclei(Glu_0), synapse=GABAergic, weight= -0.05)	# 1  2

#######drn.nuclei(HT5).connect(thalamus.nuclei(Glu_1), synapse=Serotoninergic_ex, weight=10)

drn.nuclei(HT5).connect(vta.nuclei(DA), synapse=Serotoninergic_in, weight= -7)	# x5 10 12 25 x50 60
drn.nuclei(HT5).connect(snc.nuclei(DA), synapse=Serotoninergic_in, weight= -7)	# x5 10 12 25 x50 60

drn.nuclei(HT5).connect(vta.nuclei(DA), synapse=GABAergic, weight= -0.07) # x5 10 12 25 x50 60 1 0.3 1
drn.nuclei(HT5).connect(snc.nuclei(DA), synapse=GABAergic, weight= -0.07) # x5 10 12 25 x50 60 1 0.3 1

#drn.nuclei(HT5).ConnectPoissonGenerator(start=1000, stop=1200, rate=860, conn_percent=100, weight=60)
#drn.nuclei(HT5).ConnectPoissonGenerator(start=1450, stop=1650, rate=160, conn_percent=100, weight=60)
#drn.nuclei(HT5).ConnectPoissonGenerator(start=1800, stop=2000, rate=160, conn_percent=100, weight=60)


# 5HT 2
for i in [2750, 3500, 4250, 9500, 10250, 11000, 16250, 17000, 17750]:
	drn.nuclei(HT5).ConnectPoissonGenerator(start=i, stop=i+250, rate=160, conn_percent=100, weight=60)		# 100 r350 560

# 5HT 3
for i in [5000, 5750, 6500, 11750, 12500, 13250, 18500, 19250, 20000]:
        drn.nuclei(HT5).ConnectPoissonGenerator(start=i, stop=i+250, rate=860, conn_percent=100, weight=60)

# NA 2
for i in [1250, 3500, 5750, 8000, 10250, 12500, 14750, 17000, 19250]:
	locus_coeruleus.nuclei(NA).ConnectPoissonGenerator(start=i, stop=i+250, rate=180, conn_percent=100, weight=60)

# NA 3
for i in [2000, 4250, 6500, 8750, 11000, 13250, 15500, 17750, 20000]:
	locus_coeruleus.nuclei(NA).ConnectPoissonGenerator(start=i, stop=i+250, rate=350, conn_percent=100, weight=60)

#+ Striatum?
#drn.nuclei(HT5).connect(nac.nuclei(DA), synapse=Serotoninergic_ex, weight=10)
# !!! drn.nuclei(HT5).connect(drn.nuclei(NA), synapse=Serotoninergic_in, weight=1)

drn.nuclei(HT5).ConnectDetector()
locus_coeruleus.nuclei(NA).ConnectDetector()

#####pfc.columns(1).layers(L4).nuclei(Glu).ConnectDetector()
#####pfc.columns(1).layers(L6).nuclei(Glu).ConnectDetector()

hypothalamus.nuclei(GABA).ConnectDetector()
amygdala.nuclei(Glu).ConnectDetector()
#####hippocampus.nuclei(GABA).ConnectDetector()
#####thalamus.nuclei(Glu_1).ConnectDetector()

