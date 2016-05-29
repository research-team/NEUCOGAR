import nest
import numpy as np

nest.ResetKernel()
nest.SetKernelStatus({'overwrite_files': True,  'local_num_threads': 4, 'resolution': 0.1})

raphe_nucleus = (
)

lateral_cortex = (
{'Name': 'lateral_cortex[lateral_cortex_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
lateral_cortex_HT5 = 0

Basal_ganglia = (
{'Name': 'Basal_ganglia[Basal_ganglia_HT5]', 'NN': 2593900, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 2593900)},
)
Basal_ganglia_HT5 = 0

entorhinal_cortex = (
{'Name': 'entorhinal_cortex[entorhinal_cortex_HT5]', 'NN': 635000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 635000)},
)
entorhinal_cortex_HT5 = 0

medial_cortex = (
{'Name': 'medial_cortex[medial_cortex_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
medial_cortex_HT5 = 0

locus_coeruleus = (
{'Name': 'locus_coeruleus[locus_coeruleus_HT5]', 'NN': 1500, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1500)},
{'Name': 'locus_coeruleus[locus_coeruleus_DA]', 'NN': 1500, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1500)},
{'Name': 'locus_coeruleus[locus_coeruleus_NA]', 'NN': 1500, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1500)}
)
locus_coeruleus_HT5 = 0
locus_coeruleus_DA = 1
locus_coeruleus_NA = 2

ventral_tegmental_area = (
{'Name': 'ventral_tegmental_area[ventral_tegmental_area_HT5]', 'NN': 61000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 61000)},
{'Name': 'ventral_tegmental_area[ventral_tegmental_area_DA]', 'NN': 61000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 61000)}
)
ventral_tegmental_area_HT5 = 0
ventral_tegmental_area_DA = 1

nucleus_accumbens = (
{'Name': 'nucleus_accumbens[nucleus_accumbens_HT5]', 'NN': 30000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 30000)},
{'Name': 'nucleus_accumbens[nucleus_accumbens_DA]', 'NN': 30000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 30000)}
)
nucleus_accumbens_HT5 = 0
nucleus_accumbens_DA = 1

Cerebral_cortex = (
{'Name': 'Cerebral_cortex[Cerebral_cortex_HT5]', 'NN': 2593900, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 2593900)},
)
Cerebral_cortex_HT5 = 0

Thalamus = (
{'Name': 'Thalamus[Thalamus_HT5]', 'NN': 5000000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 5000000)},
)
Thalamus_HT5 = 0

insular_cortex = (
{'Name': 'insular_cortex[insular_cortex_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
insular_cortex_HT5 = 0

Rostral_group = (
{'Name': 'Rostral_group[Rostral_group_A1]', 'NN': 6900, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 6900)},
{'Name': 'Rostral_group[Rostral_group_A2]', 'NN': 6900, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 6900)}
)
Rostral_group_A1 = 0
Rostral_group_A2 = 1

Caudal_group = (
)

septum = (
{'Name': 'septum[septum_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
septum_HT5 = 0

hypothalamus = (
{'Name': 'hypothalamus[hypothalamus_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
hypothalamus_HT5 = 0

RMg = (
)

hippocampus = (
{'Name': 'hippocampus[hippocampus_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
hippocampus_HT5 = 0

RPa = (
)

lateral_tegmental_area = (
{'Name': 'lateral_tegmental_area[lateral_tegmental_area_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
lateral_tegmental_area_HT5 = 0

neocortex = (
{'Name': 'neocortex[neocortex_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
neocortex_HT5 = 0

bed_nucleus_of_the_stria_terminalis = (
{'Name': 'bed_nucleus_of_the_stria_terminalis[bed_nucleus_of_the_stria_terminalis_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
bed_nucleus_of_the_stria_terminalis_HT5 = 0

DR = (
{'Name': 'DR[DR_HT5]', 'NN': 5800, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 5800)},
)
DR_HT5 = 0

MnR = (
{'Name': 'MnR[MnR_HT5]', 'NN': 1100, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1100)},
)
MnR_HT5 = 0

reticular_formation = (
{'Name': 'reticular_formation[reticular_formation_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
reticular_formation_HT5 = 0

pons = (
{'Name': 'pons[pons_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
pons_HT5 = 0

Periaqueductal_gray = (
{'Name': 'Periaqueductal_gray[Periaqueductal_gray_HT5]', 'NN': 1000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 1000)},
)
Periaqueductal_gray_HT5 = 0

prefrontal_cortex = (
{'Name': 'prefrontal_cortex[prefrontal_cortex_HT5]', 'NN': 366000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 366000)},
{'Name': 'prefrontal_cortex[prefrontal_cortex_DA]', 'NN': 366000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 366000)}
)
prefrontal_cortex_HT5 = 0
prefrontal_cortex_DA = 1

striatum = (
{'Name': 'striatum[striatum_HT5]', 'NN': 2500000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 2500000)},
{'Name': 'striatum[striatum_DA]', 'NN': 2500000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 2500000)}
)
striatum_HT5 = 0
striatum_DA = 1

amygdala = (
{'Name': 'amygdala[amygdala_HT5]', 'NN': 3000, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 3000)},
)
amygdala_HT5 = 0

substantia_nigra = (
{'Name': 'substantia_nigra[substantia_nigra_HT5]', 'NN': 62900, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 62900)},
{'Name': 'substantia_nigra[substantia_nigra_DA]', 'NN': 62900, 'Model': 'iaf_psc_alpha', 'IDs': nest.Create('iaf_psc_alpha', 62900)}
)
substantia_nigra_HT5 = 0
substantia_nigra_DA = 1

