from neucogar.namespaces import *
from neucogar.api_kernel import CreateNetwork
from neucogar.SynapseModel import SynapseModel

from brain_parts import *

# Init synapses
Glutamatergic = SynapseModel("Glutamatergic", nest_model=STDP_SYNAPSE, params=stdp_glu_params)
GABAergic = SynapseModel("GABAergic", nest_model=STDP_SYNAPSE, params=stdp_gaba_params)
Dopaminergic_ex = SynapseModel("Dopaminergic_ex", nest_model=STDP_DOPA_SYNAPSE, params=stdp_dopa_ex_params)
Dopaminergic_in = SynapseModel("Dopaminergic_in", nest_model=STDP_DOPA_SYNAPSE, params=stdp_dopa_in_params)


# Set connectomes
motor_cortex.nuclei(Glu_0).connect(striatum.nuclei(GABA_D1), synapse=Glutamatergic, weight=0.1)
motor_cortex.nuclei(Glu_0).connect(striatum.nuclei(GABA_D2), synapse=Glutamatergic, weight=0.1)
motor_cortex.nuclei(Glu_0).connect(striatum.nuclei(GABA_D2), synapse=Glutamatergic, weight=0.08)
motor_cortex.nuclei(Glu_0).connect(stn.nuclei(Glu), synapse=Glutamatergic, weight=1)

thalamus.nuclei(Glu).connect(motor_cortex.nuclei(Glu_1), synapse=Glutamatergic, weight=1)

striatum.nuclei(GABA_D1).connect(snr.nuclei(GABA), synapse=GABAergic, weight=-0.01)
striatum.nuclei(GABA_D1).connect(gpi.nuclei(GABA), synapse=GABAergic, weight=-0.01)
striatum.nuclei(GABA_D2).connect(gpe.nuclei(GABA), synapse=GABAergic, weight=-0.01)

gpe.nuclei(GABA).connect(stn.nuclei(Glu), synapse=GABAergic, weight=-0.01)

stn.nuclei(Glu).connect(snr.nuclei(GABA), synapse=Glutamatergic, weight=1)
stn.nuclei(Glu).connect(gpi.nuclei(GABA), synapse=Glutamatergic, weight=1)
stn.nuclei(Glu).connect(gpe.nuclei(GABA), synapse=Glutamatergic, weight=0.3)

gpi.nuclei(GABA).connect(thalamus.nuclei(Glu), synapse=GABAergic, weight=-3)

snr.nuclei(GABA).connect(thalamus.nuclei(Glu), synapse=GABAergic, weight=-3)

snc.nuclei(DA).connect(striatum.nuclei(GABA_D1), synapse=Dopaminergic_ex, weight=1)
vta.nuclei(DA).connect(striatum.nuclei(GABA_D1), synapse=Dopaminergic_ex, weight=1)
snc.nuclei(DA).connect(striatum.nuclei(GABA_D2), synapse=Dopaminergic_in, weight=-1)
vta.nuclei(DA).connect(striatum.nuclei(GABA_D2), synapse=Dopaminergic_in, weight=-1)

# Connect spikegenerators
motor_cortex.nuclei(Glu_0).ConnectPoissonGenerator(rate=300, conn_percent=50, weight=100)
snc.nuclei(DA).ConnectPoissonGenerator(start=400., stop=600., rate=350, conn_percent=100, weight=10)
vta.nuclei(DA).ConnectPoissonGenerator(start=400., stop=600., rate=350, conn_percent=100, weight=10)

# Connect spikedetectors
motor_cortex.nuclei(Glu_0).ConnectDetector()
striatum.nuclei(GABA_D1).ConnectDetector()
striatum.nuclei(GABA_D2).ConnectDetector()

# Connect multimeters
motor_cortex.nuclei(Glu_0).ConnectMultimeter()
striatum.nuclei(GABA_D2).ConnectMultimeter()
