from neucogar.api_initialisation import *
from neucogar.api_connections import *
from neucogar.api_diagrams import *

# Drop all early threads/settings/parameters

# Set new settings
SetKernelStatus(local_num_threads=4,
                data_path='txt',
                resolution=0.1)

# Get all data variables
from .data import *

# Generate neurons
CreateNeurons(5000)

# Set connectomes of neurons
Connect(motor_cortex[Glu_0], striatum[GABA_D1], synapse=Glutamatergic, weight=0.1)
Connect(motor_cortex[Glu_0], striatum[GABA_D2], synapse=Glutamatergic, weight=0.1)
Connect(motor_cortex[Glu_0], thalamus[Glu], synapse=Glutamatergic, weight=0.08)
Connect(motor_cortex[Glu_0], stn[Glu], synapse=Glutamatergic, weight=1)

Connect(striatum[GABA_D1], snr[GABA], synapse=GABAergic, weight=-0.01)
Connect(striatum[GABA_D1], gpi[GABA], synapse=GABAergic, weight=-0.01)

Connect(striatum[GABA_D2], gpe[GABA], synapse=GABAergic, weight=-0.01)

Connect(gpe[GABA], stn[Glu], synapse=GABAergic, weight=-0.1)

Connect(stn[Glu], snr[GABA], synapse=Glutamatergic, weight=1)
Connect(stn[Glu], gpi[GABA], synapse=Glutamatergic, weight=1)
Connect(stn[Glu], gpe[GABA], synapse=Glutamatergic, weight=0.3)

Connect(gpi[GABA], thalamus[Glu], synapse=GABAergic, weight=-3)
Connect(snr[GABA], thalamus[Glu], synapse=GABAergic, weight=-3)

Connect(thalamus[Glu], motor_cortex[Glu_1], synapse=Glutamatergic, weight=1)

Connect(snc[DA], striatum[GABA_D1], synapse=Dopaminergic_ex, weight=1)
Connect(vta[DA], striatum[GABA_D1], synapse=Dopaminergic_ex, weight=1)
Connect(snc[DA], striatum[GABA_D2], synapse=Dopaminergic_in, weight=-1)
Connect(vta[DA], striatum[GABA_D2], synapse=Dopaminergic_in, weight=-1)

# Connect spikegenerator
ConnectPoissonGenerator(motor_cortex[Glu_0], rate=300, conn_percent=50, weight=100)
ConnectPoissonGenerator(snc[DA], start=400., stop=600., rate=350, conn_percent=100, weight=10)
ConnectPoissonGenerator(vta[DA], start=400., stop=600., rate=350, conn_percent=100, weight=10)

# Connect spikedetectors
ConnectDetector(motor_cortex[Glu_0],)

# Connect multimeters
ConnectMultimeter(motor_cortex[Glu_0], )

# Start the simulataion
Simulate(100.)

BuildSpikeDiagrams()
#BuildVoltageDiagrams()
