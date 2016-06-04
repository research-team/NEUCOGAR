import nest
import numpy as np

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

number_of_neuron = 18567100
DEFAULT = 10 = 10

raphenucleus = (
)

lateralcortex_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if lateralcortex_5HT_NN < DEFAULT : lateralcortex_5HT_NN = DEFAULT

lateralcortex = (
{'Name': 'lateralcortex[lateralcortex_5HT]', 'NN': lateralcortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', lateralcortex_5HT_NN)},
)
lateralcortex_5HT = 0

Basalganglia_5HT_NN = int(2593900 / 18567100 * number_of_neuron)
if Basalganglia_5HT_NN < DEFAULT : Basalganglia_5HT_NN = DEFAULT

Basalganglia = (
{'Name': 'Basalganglia[Basalganglia_5HT]', 'NN': Basalganglia_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Basalganglia_5HT_NN)},
)
Basalganglia_5HT = 0

entorhinalcortex_5HT_NN = int(635000 / 18567100 * number_of_neuron)
if entorhinalcortex_5HT_NN < DEFAULT : entorhinalcortex_5HT_NN = DEFAULT

entorhinalcortex = (
{'Name': 'entorhinalcortex[entorhinalcortex_5HT]', 'NN': entorhinalcortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', entorhinalcortex_5HT_NN)},
)
entorhinalcortex_5HT = 0

medialcortex_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if medialcortex_5HT_NN < DEFAULT : medialcortex_5HT_NN = DEFAULT

medialcortex = (
{'Name': 'medialcortex[medialcortex_5HT]', 'NN': medialcortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', medialcortex_5HT_NN)},
)
medialcortex_5HT = 0

locuscoeruleus_5HT_NN = int(1500 / 18567100 * number_of_neuron)
if locuscoeruleus_5HT_NN < DEFAULT : locuscoeruleus_5HT_NN = DEFAULT
locuscoeruleus_DA_NN = int(1500 / 18567100 * number_of_neuron)
if locuscoeruleus_DA_NN < DEFAULT : locuscoeruleus_DA_NN = DEFAULT
locuscoeruleus_NA_NN = int(1500 / 18567100 * number_of_neuron)
if locuscoeruleus_NA_NN < DEFAULT : locuscoeruleus_NA_NN = DEFAULT

locuscoeruleus = (
{'Name': 'locuscoeruleus[locuscoeruleus_5HT]', 'NN': locuscoeruleus_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', locuscoeruleus_5HT_NN)},
{'Name': 'locuscoeruleus[locuscoeruleus_DA]', 'NN': locuscoeruleus_DA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', locuscoeruleus_DA_NN)},
{'Name': 'locuscoeruleus[locuscoeruleus_NA]', 'NN': locuscoeruleus_NA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', locuscoeruleus_NA_NN)}
)
locuscoeruleus_5HT = 0
locuscoeruleus_DA = 1
locuscoeruleus_NA = 2

ventraltegmentalarea_5HT_NN = int(61000 / 18567100 * number_of_neuron)
if ventraltegmentalarea_5HT_NN < DEFAULT : ventraltegmentalarea_5HT_NN = DEFAULT
ventraltegmentalarea_DA_NN = int(61000 / 18567100 * number_of_neuron)
if ventraltegmentalarea_DA_NN < DEFAULT : ventraltegmentalarea_DA_NN = DEFAULT

ventraltegmentalarea = (
{'Name': 'ventraltegmentalarea[ventraltegmentalarea_5HT]', 'NN': ventraltegmentalarea_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', ventraltegmentalarea_5HT_NN)},
{'Name': 'ventraltegmentalarea[ventraltegmentalarea_DA]', 'NN': ventraltegmentalarea_DA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', ventraltegmentalarea_DA_NN)}
)
ventraltegmentalarea_5HT = 0
ventraltegmentalarea_DA = 1

nucleusaccumbens_5HT_NN = int(30000 / 18567100 * number_of_neuron)
if nucleusaccumbens_5HT_NN < DEFAULT : nucleusaccumbens_5HT_NN = DEFAULT
nucleusaccumbens_DA_NN = int(30000 / 18567100 * number_of_neuron)
if nucleusaccumbens_DA_NN < DEFAULT : nucleusaccumbens_DA_NN = DEFAULT

nucleusaccumbens = (
{'Name': 'nucleusaccumbens[nucleusaccumbens_5HT]', 'NN': nucleusaccumbens_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', nucleusaccumbens_5HT_NN)},
{'Name': 'nucleusaccumbens[nucleusaccumbens_DA]', 'NN': nucleusaccumbens_DA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', nucleusaccumbens_DA_NN)}
)
nucleusaccumbens_5HT = 0
nucleusaccumbens_DA = 1

Cerebralcortex_5HT_NN = int(100 / 18567100 * number_of_neuron)
if Cerebralcortex_5HT_NN < DEFAULT : Cerebralcortex_5HT_NN = DEFAULT

Cerebralcortex = (
{'Name': 'Cerebralcortex[Cerebralcortex_5HT]', 'NN': Cerebralcortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Cerebralcortex_5HT_NN)},
)
Cerebralcortex_5HT = 0

Thalamus_5HT_NN = int(5000000 / 18567100 * number_of_neuron)
if Thalamus_5HT_NN < DEFAULT : Thalamus_5HT_NN = DEFAULT

Thalamus = (
{'Name': 'Thalamus[Thalamus_5HT]', 'NN': Thalamus_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Thalamus_5HT_NN)},
)
Thalamus_5HT = 0

insularcortex_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if insularcortex_5HT_NN < DEFAULT : insularcortex_5HT_NN = DEFAULT

insularcortex = (
{'Name': 'insularcortex[insularcortex_5HT]', 'NN': insularcortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', insularcortex_5HT_NN)},
)
insularcortex_5HT = 0

Rostralgroup_A1_NN = int(6900 / 18567100 * number_of_neuron)
if Rostralgroup_A1_NN < DEFAULT : Rostralgroup_A1_NN = DEFAULT
Rostralgroup_A2_NN = int(6900 / 18567100 * number_of_neuron)
if Rostralgroup_A2_NN < DEFAULT : Rostralgroup_A2_NN = DEFAULT

Rostralgroup = (
{'Name': 'Rostralgroup[Rostralgroup_A1]', 'NN': Rostralgroup_A1_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Rostralgroup_A1_NN)},
{'Name': 'Rostralgroup[Rostralgroup_A2]', 'NN': Rostralgroup_A2_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Rostralgroup_A2_NN)}
)
Rostralgroup_A1 = 0
Rostralgroup_A2 = 1


Caudalgroup = (
)

septum_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if septum_5HT_NN < DEFAULT : septum_5HT_NN = DEFAULT

septum = (
{'Name': 'septum[septum_5HT]', 'NN': septum_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', septum_5HT_NN)},
)
septum_5HT = 0

hypothalamus_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if hypothalamus_5HT_NN < DEFAULT : hypothalamus_5HT_NN = DEFAULT

hypothalamus = (
{'Name': 'hypothalamus[hypothalamus_5HT]', 'NN': hypothalamus_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', hypothalamus_5HT_NN)},
)
hypothalamus_5HT = 0


RMg = (
)

hippocampus_5HT_NN = int(4260000 / 18567100 * number_of_neuron)
if hippocampus_5HT_NN < DEFAULT : hippocampus_5HT_NN = DEFAULT

hippocampus = (
{'Name': 'hippocampus[hippocampus_5HT]', 'NN': hippocampus_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', hippocampus_5HT_NN)},
)
hippocampus_5HT = 0


RPa = (
)

lateraltegmentalarea_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if lateraltegmentalarea_5HT_NN < DEFAULT : lateraltegmentalarea_5HT_NN = DEFAULT

lateraltegmentalarea = (
{'Name': 'lateraltegmentalarea[lateraltegmentalarea_5HT]', 'NN': lateraltegmentalarea_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', lateraltegmentalarea_5HT_NN)},
)
lateraltegmentalarea_5HT = 0

neocortex_5HT_NN = int(100 / 18567100 * number_of_neuron)
if neocortex_5HT_NN < DEFAULT : neocortex_5HT_NN = DEFAULT

neocortex = (
{'Name': 'neocortex[neocortex_5HT]', 'NN': neocortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', neocortex_5HT_NN)},
)
neocortex_5HT = 0

bednucleusofthestriaterminalis_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if bednucleusofthestriaterminalis_5HT_NN < DEFAULT : bednucleusofthestriaterminalis_5HT_NN = DEFAULT

bednucleusofthestriaterminalis = (
{'Name': 'bednucleusofthestriaterminalis[bednucleusofthestriaterminalis_5HT]', 'NN': bednucleusofthestriaterminalis_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', bednucleusofthestriaterminalis_5HT_NN)},
)
bednucleusofthestriaterminalis_5HT = 0

DR_5HT_NN = int(5800 / 18567100 * number_of_neuron)
if DR_5HT_NN < DEFAULT : DR_5HT_NN = DEFAULT

DR = (
{'Name': 'DR[DR_5HT]', 'NN': DR_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', DR_5HT_NN)},
)
DR_5HT = 0

MnR_5HT_NN = int(1100 / 18567100 * number_of_neuron)
if MnR_5HT_NN < DEFAULT : MnR_5HT_NN = DEFAULT

MnR = (
{'Name': 'MnR[MnR_5HT]', 'NN': MnR_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', MnR_5HT_NN)},
)
MnR_5HT = 0

reticularformation_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if reticularformation_5HT_NN < DEFAULT : reticularformation_5HT_NN = DEFAULT

reticularformation = (
{'Name': 'reticularformation[reticularformation_5HT]', 'NN': reticularformation_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', reticularformation_5HT_NN)},
)
reticularformation_5HT = 0

pons_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if pons_5HT_NN < DEFAULT : pons_5HT_NN = DEFAULT

pons = (
{'Name': 'pons[pons_5HT]', 'NN': pons_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', pons_5HT_NN)},
)
pons_5HT = 0

Periaqueductalgray_5HT_NN = int(1000 / 18567100 * number_of_neuron)
if Periaqueductalgray_5HT_NN < DEFAULT : Periaqueductalgray_5HT_NN = DEFAULT

Periaqueductalgray = (
{'Name': 'Periaqueductalgray[Periaqueductalgray_5HT]', 'NN': Periaqueductalgray_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', Periaqueductalgray_5HT_NN)},
)
Periaqueductalgray_5HT = 0

prefrontalcortex_5HT_NN = int(366000 / 18567100 * number_of_neuron)
if prefrontalcortex_5HT_NN < DEFAULT : prefrontalcortex_5HT_NN = DEFAULT
prefrontalcortex_DA_NN = int(366000 / 18567100 * number_of_neuron)
if prefrontalcortex_DA_NN < DEFAULT : prefrontalcortex_DA_NN = DEFAULT

prefrontalcortex = (
{'Name': 'prefrontalcortex[prefrontalcortex_5HT]', 'NN': prefrontalcortex_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', prefrontalcortex_5HT_NN)},
{'Name': 'prefrontalcortex[prefrontalcortex_DA]', 'NN': prefrontalcortex_DA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', prefrontalcortex_DA_NN)}
)
prefrontalcortex_5HT = 0
prefrontalcortex_DA = 1

striatum_5HT_NN = int(2500000 / 18567100 * number_of_neuron)
if striatum_5HT_NN < DEFAULT : striatum_5HT_NN = DEFAULT
striatum_DA_NN = int(2500000 / 18567100 * number_of_neuron)
if striatum_DA_NN < DEFAULT : striatum_DA_NN = DEFAULT

striatum = (
{'Name': 'striatum[striatum_5HT]', 'NN': striatum_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', striatum_5HT_NN)},
{'Name': 'striatum[striatum_DA]', 'NN': striatum_DA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', striatum_DA_NN)}
)
striatum_5HT = 0
striatum_DA = 1

amygdala_5HT_NN = int(3000 / 18567100 * number_of_neuron)
if amygdala_5HT_NN < DEFAULT : amygdala_5HT_NN = DEFAULT

amygdala = (
{'Name': 'amygdala[amygdala_5HT]', 'NN': amygdala_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', amygdala_5HT_NN)},
)
amygdala_5HT = 0

substantianigra_5HT_NN = int(62900 / 18567100 * number_of_neuron)
if substantianigra_5HT_NN < DEFAULT : substantianigra_5HT_NN = DEFAULT
substantianigra_DA_NN = int(62900 / 18567100 * number_of_neuron)
if substantianigra_DA_NN < DEFAULT : substantianigra_DA_NN = DEFAULT

substantianigra = (
{'Name': 'substantianigra[substantianigra_5HT]', 'NN': substantianigra_5HT_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', substantianigra_5HT_NN)},
{'Name': 'substantianigra[substantianigra_DA]', 'NN': substantianigra_DA_NN, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', substantianigra_DA_NN)}
)
substantianigra_5HT = 0
substantianigra_DA = 1

