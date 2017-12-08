from neucogar.namespaces import *
from neucogar.api_kernel import CreateNetwork
from neucogar.SynapseModel import SynapseModel

from .brain_parts import *
from ..dopamine.connectomes import *

# Init synapses
Serotoninergic_ex = SynapseModel("Serotoninergic_ex", nest_model=STDP_SERO_SYNAPSE, params=stdp_sero_ex_params)
Serotoninergic_in = SynapseModel("Serotoninergic_in", nest_model=STDP_SERO_SYNAPSE, params=stdp_sero_in_params)

# Thalamus Glu_0 - VA/VL
# Thalamus Glu_1 - midline nuclei
pfc.nuclei(Glu).connect(drn.nuclei(HT5), synapse=Glutamatergic, weight=10)
pfc.nuclei(GABA).connect(pfc.nuclei(Glu), synapse=GABAergic, weight=-10)

thalamus.nuclei(Glu_1).connect(pfc.nuclei(Glu), synapse=Glutamatergic, weight=10)

vta.nuclei(DA).connect(pfc.nuclei(Glu), synapse=Dopaminergic_ex, weight=10)
vta.nuclei(DA).connect(drn.nuclei(HT5), synapse=Dopaminergic_ex, weight=10)

snc.nuclei(DA).connect(drn.nuclei(HT5), synapse=Dopaminergic_ex, weight=10)

hippocampus.nuclei(Glu).connect(drn.nuclei(HT5), synapse=Glutamatergic, weight=10)
hippocampus.nuclei(GABA).connect(hippocampus.nuclei(Glu), synapse=GABAergic, weight=-10)

amygdala.nuclei(Glu).connect(drn.nuclei(HT5), synapse=Glutamatergic, weight=10)

hypothalamus.nuclei(Glu).connect(hypothalamus.nuclei(GABA), synapse=Glutamatergic, weight=10)
hypothalamus.nuclei(GABA).connect(drn.nuclei(HT5), synapse=GABAergic, weight=-10)

drn.nuclei(GABA).connect(drn.nuclei(HT5), synapse=GABAergic, weight=-10)
drn.nuclei(HT5).connect(hypothalamus.nuclei(GABA), synapse=Serotoninergic_in, weight=-10)
drn.nuclei(HT5).connect(amygdala.nuclei(Glu), synapse=Serotoninergic_in, weight=-10)
drn.nuclei(HT5).connect(hippocampus.nuclei(GABA), synapse=Serotoninergic_ex, weight=10)
drn.nuclei(HT5).connect(pfc.nuclei(GABA), synapse=Serotoninergic_ex, weight=10)
drn.nuclei(HT5).connect(thalamus.nuclei(Glu_1), synapse=Serotoninergic_ex, weight=10)
drn.nuclei(HT5).connect(vta.nuclei(DA), synapse=Serotoninergic_in, weight=-10)

drn.nuclei(HT5).connect(snc.nuclei(DA), synapse=Serotoninergic_in, weight=-10)
drn.nuclei(HT5).connect(nac.nuclei(DA), synapse=Serotoninergic_ex, weight=10)
