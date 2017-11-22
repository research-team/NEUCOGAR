from neucogar.SynapseModel import SynapseModel
from neucogar.Nucleus import Nucleus

from neucogar.api_globals import *
from neucogar.api_initialisation import *

from .parameters import *

# = = = = = = = = = = = =
# N E U R O N S  D A T A
# = = = = = = = = = = = =
motor_cortex = NeuronGroup("Motor cortex",
                           Nucleus(Glu_0, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=3866666),  #int(29000000 * 0.8 / 6)
                           Nucleus(Glu_1, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=966666))    #int(29000000 * 0.2 / 6)
striatum = NeuronGroup("Striatum",
                       Nucleus(GABA_D1, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=1062500),  #int(2500000 * 0.425)
                       Nucleus(GABA_D2, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=1062500))     #int(2500000 * 0.425)

gpe = NeuronGroup("GPe",
                  Nucleus(GABA, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=84100))

gpi = NeuronGroup("GPi",
                  Nucleus(GABA, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=12600))

stn = NeuronGroup("STN",
                  Nucleus(Glu, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=22700))

snr = NeuronGroup("SNr",
                  Nucleus(GABA, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=47200))

snc = NeuronGroup("SNc",
                  Nucleus(DA, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=12700))

vta = NeuronGroup("VTA",
                  Nucleus(DA, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=20000))

thalamus = NeuronGroup("Thalamus",
                       Nucleus(Glu, model=HH_COND_EXP_TRAUB, params=nrn_parameters, number=833333)) #int(5000000 / 6)

# = = = = = = = = = = = = =
# S Y N A P S E S  D A T A
# = = = = = = = = = = = = =

Glutamatergic = SynapseModel("Glutamatergic", nest_model=STDP_SYNAPSE, params=stdp_glu_params)
GABAergic = SynapseModel("GABAergic", nest_model=STDP_SYNAPSE, params=stdp_gaba_params)
Dopaminergic_ex = SynapseModel("Dopaminergic_ex", nest_model=STDP_DOPA_SYNAPSE, params=stdp_dopa_ex_params)
Dopaminergic_in = SynapseModel("Dopaminergic_in", nest_model=STDP_DOPA_SYNAPSE, params=stdp_dopa_in_params)

"""
Glutamatergic
GABAergic
Dopaminergic
Serotonergic
Noradrenergic
Acetylcholinergic
"""