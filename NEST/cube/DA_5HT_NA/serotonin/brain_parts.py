from neucogar.namespaces import *
from neucogar.Nucleus import Nucleus
from neucogar.api_kernel import CreateNetwork

from .parameters import *

hippocampus = Nucleus("Hippocampus")
hippocampus.addSubNucleus(Glu, params=nrn_parameters, number=5000) # ToDo Check
hippocampus.addSubNucleus(GABA, params=nrn_parameters, number=1000) # ToDo Check

amygdala = Nucleus("Amygdala")
amygdala.addSubNucleus(Glu, params=nrn_parameters, number=3000) # ToDo not real

hypothalamus = Nucleus("Hypothalamus")
hypothalamus.addSubNucleus(Glu, params=nrn_parameters, number=1000) # ToDo not real
hypothalamus.addSubNucleus(GABA, params=nrn_parameters, number=1000) # ToDo not real

drn = Nucleus("Raphe nucleus")
drn.addSubNucleus(HT5, params=nrn_parameters, number=15000)
drn.addSubNucleus(GABA, params=nrn_parameters, number=1000) # ToDo not real

locus_coeruleus = Nucleus("Locus coeruleus")
locus_coeruleus.addSubNucleus(NA, params=nrn_parameters, number=1500)

CreateNetwork(28000)

