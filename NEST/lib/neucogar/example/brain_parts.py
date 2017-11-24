from neucogar.api_kernel import Nucleus
from neucogar.api_kernel import CreateNetwork

from neucogar.namespaces import *
from parameters import *

motor_cortex = Nucleus("Motor cortex")
motor_cortex.addSubNucleus(Glu_0, params=nrn_parameters, number=3866666)
motor_cortex.addSubNucleus(Glu_1, params=nrn_parameters, number=966666)

thalamus = Nucleus("Thalamus")
thalamus.addSubNucleus(Glu, params=nrn_parameters, number=833333)

striatum = Nucleus("Striatum")
striatum.addSubNucleus(GABA_D1, params=nrn_parameters, number=1062500)
striatum.addSubNucleus(GABA_D2, params=nrn_parameters, number=1062500)

gpe = Nucleus("GPe")
gpe.addSubNucleus(GABA, params=nrn_parameters, number=84100)

gpi = Nucleus("GPi")
gpi.addSubNucleus(GABA, params=nrn_parameters, number=12600)

stn = Nucleus("STN")
stn.addSubNucleus(Glu, params=nrn_parameters, number=22700)

snr = Nucleus("SNr")
snr.addSubNucleus(GABA, params=nrn_parameters, number=47200)

snc = Nucleus("SNc")
snc.addSubNucleus(DA, params=nrn_parameters, number=12700)

vta = Nucleus("VTA")
vta.addSubNucleus(DA, params=nrn_parameters, number=20000)


CreateNetwork(10000)

