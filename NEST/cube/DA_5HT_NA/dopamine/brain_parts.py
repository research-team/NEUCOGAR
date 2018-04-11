from neucogar.namespaces import *
from neucogar.Nucleus import Nucleus
from neucogar.api_kernel import CreateNetwork

from .parameters import *

from neucogar.ColumnsClassess.MotorCortexColumns import MotorCortexColumns

sensory_cortex = MotorCortexColumns(height=2, width=2) #3 3
motor_cortex = MotorCortexColumns(height=7, width=7) # 2.2
pfc = MotorCortexColumns(height=2, width=1)

thalamus = Nucleus("Thalamus")
thalamus.addSubNucleus(Glu_0, params=nrn_parameters, number=833333)   # ToDo ???
thalamus.addSubNucleus(Glu_1, params=nrn_parameters, number=60000)   # ToDo ???

striatum = Nucleus("Striatum")
striatum.addSubNucleus(GABA_D1, params=nrn_parameters, number=1062500)
striatum.addSubNucleus(GABA_D2, params=nrn_parameters, number=1062500)
#striatum.addSubNucleus(DA, params=nrn_parameters, number=1062500) # ToDo ???

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

nac = Nucleus("NAc")
nac.addSubNucleus(DA, params=nrn_parameters, number=20000)

CreateNetwork(500000)

