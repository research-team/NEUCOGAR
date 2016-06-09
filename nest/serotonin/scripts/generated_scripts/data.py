import nest
import numpy as np

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

raphenucleus = (
)

lateralcortex = (
{'Name': 'lateralcortex[lateralcortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
lateralcortex_5HT = 0

Basalganglia = (
{'Name': 'Basalganglia[Basalganglia_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
Basalganglia_5HT = 0

entorhinalcortex = (
{'Name': 'entorhinalcortex[entorhinalcortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
entorhinalcortex_5HT = 0

medialcortex = (
{'Name': 'medialcortex[medialcortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
medialcortex_5HT = 0

locuscoeruleus = (
{'Name': 'locuscoeruleus[locuscoeruleus_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'locuscoeruleus[locuscoeruleus_DA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'locuscoeruleus[locuscoeruleus_NA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
locuscoeruleus_5HT = 0
locuscoeruleus_DA = 1
locuscoeruleus_NA = 2

ventraltegmentalarea = (
{'Name': 'ventraltegmentalarea[ventraltegmentalarea_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'ventraltegmentalarea[ventraltegmentalarea_DA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
ventraltegmentalarea_5HT = 0
ventraltegmentalarea_DA = 1

nucleusaccumbens = (
{'Name': 'nucleusaccumbens[nucleusaccumbens_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'nucleusaccumbens[nucleusaccumbens_DA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
nucleusaccumbens_5HT = 0
nucleusaccumbens_DA = 1

Cerebralcortex = (
{'Name': 'Cerebralcortex[Cerebralcortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
Cerebralcortex_5HT = 0

Thalamus = (
{'Name': 'Thalamus[Thalamus_5HT]', 'NN': 200, 'Model': 'iaf_psc_exp', 'IDs': nest.Create('iaf_psc_exp', 200)},
)
Thalamus_5HT = 0

insularcortex = (
{'Name': 'insularcortex[insularcortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
insularcortex_5HT = 0

Rostralgroup = (
{'Name': 'Rostralgroup[Rostralgroup_A1]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'Rostralgroup[Rostralgroup_A2]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
Rostralgroup_A1 = 0
Rostralgroup_A2 = 1

Caudalgroup = (
)

septum = (
{'Name': 'septum[septum_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
septum_5HT = 0

hypothalamus = (
{'Name': 'hypothalamus[hypothalamus_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
hypothalamus_5HT = 0

RMg = (
)

hippocampus = (
{'Name': 'hippocampus[hippocampus_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
hippocampus_5HT = 0

RPa = (
)

lateraltegmentalarea = (
{'Name': 'lateraltegmentalarea[lateraltegmentalarea_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
lateraltegmentalarea_5HT = 0

neocortex = (
{'Name': 'neocortex[neocortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
neocortex_5HT = 0

bednucleusofthestriaterminalis = (
{'Name': 'bednucleusofthestriaterminalis[bednucleusofthestriaterminalis_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
bednucleusofthestriaterminalis_5HT = 0

DR = (
{'Name': 'DR[DR_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
DR_5HT = 0

MnR = (
{'Name': 'MnR[MnR_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
MnR_5HT = 0

reticularformation = (
{'Name': 'reticularformation[reticularformation_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
reticularformation_5HT = 0

pons = (
{'Name': 'pons[pons_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
pons_5HT = 0

Periaqueductalgray = (
{'Name': 'Periaqueductalgray[Periaqueductalgray_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
Periaqueductalgray_5HT = 0

prefrontalcortex = (
{'Name': 'prefrontalcortex[prefrontalcortex_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'prefrontalcortex[prefrontalcortex_DA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
prefrontalcortex_5HT = 0
prefrontalcortex_DA = 1

striatum = (
{'Name': 'striatum[striatum_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'striatum[striatum_DA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
striatum_5HT = 0
striatum_DA = 1

amygdala = (
{'Name': 'amygdala[amygdala_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
)
amygdala_5HT = 0

substantianigra = (
{'Name': 'substantianigra[substantianigra_5HT]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)},
{'Name': 'substantianigra[substantianigra_DA]', 'NN': 10, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 10)}
)
substantianigra_5HT = 0
substantianigra_DA = 1

