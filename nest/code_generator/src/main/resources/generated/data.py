from __future__ import division
import nest
import numpy as np

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

number_of_neuron = 340
DEFAULT = 10 = 10
LC_NA[0]_NN = int(10 / 340 * number_of_neuron)
if LC_NA[0]_NN < DEFAULT : LC_NA[0]_NN = DEFAULT
LC_Ach_NN = int(10 / 340 * number_of_neuron)
if LC_Ach_NN < DEFAULT : LC_Ach_NN = DEFAULT
LC_GABA_NN = int(10 / 340 * number_of_neuron)
if LC_GABA_NN < DEFAULT : LC_GABA_NN = DEFAULT
LC_D1_NN = int(10 / 340 * number_of_neuron)
if LC_D1_NN < DEFAULT : LC_D1_NN = DEFAULT
LC_D2_NN = int(10 / 340 * number_of_neuron)
if LC_D2_NN < DEFAULT : LC_D2_NN = DEFAULT
LC_NA[1]_NN = int(10 / 340 * number_of_neuron)
if LC_NA[1]_NN < DEFAULT : LC_NA[1]_NN = DEFAULT

LC = (
{'Name': 'LC[LC_NA[0]]', 'NN': LC_NA[0]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LC_NA[0]_NN)},
{'Name': 'LC[LC_Ach]', 'NN': LC_Ach_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LC_Ach_NN)},
{'Name': 'LC[LC_GABA]', 'NN': LC_GABA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LC_GABA_NN)},
{'Name': 'LC[LC_D1]', 'NN': LC_D1_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LC_D1_NN)},
{'Name': 'LC[LC_D2]', 'NN': LC_D2_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LC_D2_NN)},
{'Name': 'LC[LC_NA[1]]', 'NN': LC_NA[1]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LC_NA[1]_NN)}
)
LC_NA[0] = 0
LC_Ach = 1
LC_GABA = 2
LC_D1 = 3
LC_D2 = 4
LC_NA[1] = 5

PGI_GABA_NN = int(10 / 340 * number_of_neuron)
if PGI_GABA_NN < DEFAULT : PGI_GABA_NN = DEFAULT
PGI_Glu_NN = int(10 / 340 * number_of_neuron)
if PGI_Glu_NN < DEFAULT : PGI_Glu_NN = DEFAULT

PGI = (
{'Name': 'PGI[PGI_GABA]', 'NN': PGI_GABA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', PGI_GABA_NN)},
{'Name': 'PGI[PGI_Glu]', 'NN': PGI_Glu_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', PGI_Glu_NN)}
)
PGI_GABA = 0
PGI_Glu = 1

BNST_Glu_NN = int(10 / 340 * number_of_neuron)
if BNST_Glu_NN < DEFAULT : BNST_Glu_NN = DEFAULT
BNST_GABA_NN = int(10 / 340 * number_of_neuron)
if BNST_GABA_NN < DEFAULT : BNST_GABA_NN = DEFAULT
BNST_Ach_NN = int(10 / 340 * number_of_neuron)
if BNST_Ach_NN < DEFAULT : BNST_Ach_NN = DEFAULT

BNST = (
{'Name': 'BNST[BNST_Glu]', 'NN': BNST_Glu_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', BNST_Glu_NN)},
{'Name': 'BNST[BNST_GABA]', 'NN': BNST_GABA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', BNST_GABA_NN)},
{'Name': 'BNST[BNST_Ach]', 'NN': BNST_Ach_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', BNST_Ach_NN)}
)
BNST_Glu = 0
BNST_GABA = 1
BNST_Ach = 2

Amy_Glu_NN = int(10 / 340 * number_of_neuron)
if Amy_Glu_NN < DEFAULT : Amy_Glu_NN = DEFAULT
Amy_Ach_NN = int(10 / 340 * number_of_neuron)
if Amy_Ach_NN < DEFAULT : Amy_Ach_NN = DEFAULT
Amy_GABA_NN = int(10 / 340 * number_of_neuron)
if Amy_GABA_NN < DEFAULT : Amy_GABA_NN = DEFAULT

Amy = (
{'Name': 'Amy[Amy_Glu]', 'NN': Amy_Glu_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Amy_Glu_NN)},
{'Name': 'Amy[Amy_Ach]', 'NN': Amy_Ach_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Amy_Ach_NN)},
{'Name': 'Amy[Amy_GABA]', 'NN': Amy_GABA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Amy_GABA_NN)}
)
Amy_Glu = 0
Amy_Ach = 1
Amy_GABA = 2

RN_5-HT_NN = int(10 / 340 * number_of_neuron)
if RN_5-HT_NN < DEFAULT : RN_5-HT_NN = DEFAULT
RN_a1_NN = int(10 / 340 * number_of_neuron)
if RN_a1_NN < DEFAULT : RN_a1_NN = DEFAULT
RN_a2_NN = int(10 / 340 * number_of_neuron)
if RN_a2_NN < DEFAULT : RN_a2_NN = DEFAULT

RN = (
{'Name': 'RN[RN_5-HT]', 'NN': RN_5-HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', RN_5-HT_NN)},
{'Name': 'RN[RN_a1]', 'NN': RN_a1_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', RN_a1_NN)},
{'Name': 'RN[RN_a2]', 'NN': RN_a2_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', RN_a2_NN)}
)
RN_5-HT = 0
RN_a1 = 1
RN_a2 = 2

Thalamus_Glu_NN = int(10 / 340 * number_of_neuron)
if Thalamus_Glu_NN < DEFAULT : Thalamus_Glu_NN = DEFAULT

Thalamus = (
{'Name': 'Thalamus[Thalamus_Glu]', 'NN': Thalamus_Glu_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Thalamus_Glu_NN)},
)
Thalamus_Glu = 0

PVN_GABA_NN = int(10 / 340 * number_of_neuron)
if PVN_GABA_NN < DEFAULT : PVN_GABA_NN = DEFAULT

PVN = (
{'Name': 'PVN[PVN_GABA]', 'NN': PVN_GABA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', PVN_GABA_NN)},
)
PVN_GABA = 0


Striatum = (
)

LTD_a1_NN = int(10 / 340 * number_of_neuron)
if LTD_a1_NN < DEFAULT : LTD_a1_NN = DEFAULT
LTD_a2_NN = int(10 / 340 * number_of_neuron)
if LTD_a2_NN < DEFAULT : LTD_a2_NN = DEFAULT
LTD_Ach_NN = int(10 / 340 * number_of_neuron)
if LTD_Ach_NN < DEFAULT : LTD_Ach_NN = DEFAULT

LTD = (
{'Name': 'LTD[LTD_a1]', 'NN': LTD_a1_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LTD_a1_NN)},
{'Name': 'LTD[LTD_a2]', 'NN': LTD_a2_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LTD_a2_NN)},
{'Name': 'LTD[LTD_Ach]', 'NN': LTD_Ach_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', LTD_Ach_NN)}
)
LTD_a1 = 0
LTD_a2 = 1
LTD_Ach = 2

PrH_GABA_NN = int(10 / 340 * number_of_neuron)
if PrH_GABA_NN < DEFAULT : PrH_GABA_NN = DEFAULT

PrH = (
{'Name': 'PrH[PrH_GABA]', 'NN': PrH_GABA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', PrH_GABA_NN)},
)
PrH_GABA = 0


NTS = (
)

AcbCore_Ach_NN = int(10 / 340 * number_of_neuron)
if AcbCore_Ach_NN < DEFAULT : AcbCore_Ach_NN = DEFAULT
AcbCore_GABA[0]_NN = int(10 / 340 * number_of_neuron)
if AcbCore_GABA[0]_NN < DEFAULT : AcbCore_GABA[0]_NN = DEFAULT

AcbCore = (
{'Name': 'AcbCore[AcbCore_Ach]', 'NN': AcbCore_Ach_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', AcbCore_Ach_NN)},
{'Name': 'AcbCore[AcbCore_GABA[0]]', 'NN': AcbCore_GABA[0]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', AcbCore_GABA[0]_NN)}
)
AcbCore_Ach = 0
AcbCore_GABA[0] = 1

Prefrontalcortex_Glu[1]_NN = int(10 / 340 * number_of_neuron)
if Prefrontalcortex_Glu[1]_NN < DEFAULT : Prefrontalcortex_Glu[1]_NN = DEFAULT
Prefrontalcortex_Glu[0]_NN = int(10 / 340 * number_of_neuron)
if Prefrontalcortex_Glu[0]_NN < DEFAULT : Prefrontalcortex_Glu[0]_NN = DEFAULT

Prefrontalcortex = (
{'Name': 'Prefrontalcortex[Prefrontalcortex_Glu[1]]', 'NN': Prefrontalcortex_Glu[1]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Prefrontalcortex_Glu[1]_NN)},
{'Name': 'Prefrontalcortex[Prefrontalcortex_Glu[0]]', 'NN': Prefrontalcortex_Glu[0]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Prefrontalcortex_Glu[0]_NN)}
)
Prefrontalcortex_Glu[1] = 0
Prefrontalcortex_Glu[0] = 1

Ab_NA_NN = int(10 / 340 * number_of_neuron)
if Ab_NA_NN < DEFAULT : Ab_NA_NN = DEFAULT

Ab = (
{'Name': 'Ab[Ab_NA]', 'NN': Ab_NA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Ab_NA_NN)},
)
Ab_NA = 0

VTA_DA[0]_NN = int(10 / 340 * number_of_neuron)
if VTA_DA[0]_NN < DEFAULT : VTA_DA[0]_NN = DEFAULT
VTA_a1_NN = int(10 / 340 * number_of_neuron)
if VTA_a1_NN < DEFAULT : VTA_a1_NN = DEFAULT
VTA_DA[1]_NN = int(10 / 340 * number_of_neuron)
if VTA_DA[1]_NN < DEFAULT : VTA_DA[1]_NN = DEFAULT

VTA = (
{'Name': 'VTA[VTA_DA[0]]', 'NN': VTA_DA[0]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', VTA_DA[0]_NN)},
{'Name': 'VTA[VTA_a1]', 'NN': VTA_a1_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', VTA_a1_NN)},
{'Name': 'VTA[VTA_DA[1]]', 'NN': VTA_DA[1]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', VTA_DA[1]_NN)}
)
VTA_DA[0] = 0
VTA_a1 = 1
VTA_DA[1] = 2

Aa_NA_NN = int(10 / 340 * number_of_neuron)
if Aa_NA_NN < DEFAULT : Aa_NA_NN = DEFAULT

Aa = (
{'Name': 'Aa[Aa_NA]', 'NN': Aa_NA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Aa_NA_NN)},
)
Aa_NA = 0

AcbShell_GABA[1]_NN = int(10 / 340 * number_of_neuron)
if AcbShell_GABA[1]_NN < DEFAULT : AcbShell_GABA[1]_NN = DEFAULT

AcbShell = (
{'Name': 'AcbShell[AcbShell_GABA[1]]', 'NN': AcbShell_GABA[1]_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', AcbShell_GABA[1]_NN)},
)
AcbShell_GABA[1] = 0

Motorcortex_Glu_NN = int(10 / 340 * number_of_neuron)
if Motorcortex_Glu_NN < DEFAULT : Motorcortex_Glu_NN = DEFAULT

Motorcortex = (
{'Name': 'Motorcortex[Motorcortex_Glu]', 'NN': Motorcortex_Glu_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Motorcortex_Glu_NN)},
)
Motorcortex_Glu = 0

