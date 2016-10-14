"""
It contains:
    Striatum
    Thalamus
    PfC: Prefrontal cortex
    NAc: Nucleus Accumbens
    VTA: Ventral Tegmental Area
    Amygdala
    Medial cortex
    Cerebral cortex
    Neocortex
    Lateral cortex
    Entorhinal cortex
    Septum
    Pons
    Lateral tegmental area
    Locus coeruleus
    Bed nucleus of the stria terminalis
    Raphe nucleus
    Rostral group
    DR: dorsal raphe nucleus
    MnR: Median raphe nucleus
    RMg
    RPa
    Reticular formation
    Periaqueductal gray
    Hippocampus
    Hypothalamus
    Substantia nigra
    Insular cortex
    Basal ganglia


Prefix description:
    DA - dopamine
    5HT - Serotonin
    NA - Noradrenaline
    A1 - Noradrenaline A1 receptors
    A2 - Noradrenaline A2 receptors
"""
from property import *
import numpy as np

striatum = ({k_name: 'Striatum [DA]'},
            {k_name: 'Striatum [5HT]'})
striatum_DA, striatum_5HT = np.arange(2)

thalamus = ({k_name: 'Thalamus [5HT]'}, )
thalamus_5HT = 0

pfc = ({k_name: 'Prefrontal cortex [DA]'},
       {k_name: 'Prefrontal cortex [5HT]'})
pfc_DA, pfc_5HT = np.arange(2)

nac = ({k_name: 'NAc [DA]'},
       {k_name: 'NAc [5HT]'})
nac_DA, nac_5HT  = np.arange(2)

vta = ({k_name: 'VTA [DA]'},
       {k_name: 'VTA [5HT]'})
vta_DA, vta_5HT = np.arange(2)

amygdala = ({k_name: 'Amygdala [5HT]'}, )
amygdala_5HT = 0

medial_cortex = ({k_name: 'Medial cortex [5HT]'}, )
medial_cortex_5HT = 0

cerebral_cortex = ({k_name: 'Cerebral cortex [5HT]'}, )
cerebral_cortex_5HT = 0

neocortex = ({k_name: 'Neocortex [5HT]'}, )
neocortex_5HT = 0

lateral_cortex = ({k_name: 'Lateral cortex [5HT]'}, )
lateral_cortex_5HT = 0

entorhinal_cortex = ({k_name: 'Entorhial cortex [5HT]'}, )
entorhinal_cortex_5HT = 0

septum = ({k_name: 'Septum [5HT]'}, )
septum_5HT = 0

pons = ({k_name: 'Pons [5HT]'}, )
pons_5HT = 0

lateral_tegmental_area = ({k_name: 'Lateral tegmental area [5HT]'}, )
lateral_tegmental_area_5HT = 0

locus_coeruleus = ({k_name: 'Locus coeruleus [DA]'},
                   {k_name: 'Locus coeruleus [5HT]'},
                   {k_name: 'Locus coeruleus [NA]'})
locus_coeruleus_DA, locus_coeruleus_5HT, locus_coeruleus_NA = np.arange(3)

bed_nucleus_of_the_stria_terminalis = ({k_name: 'Bed nucleus of the stria terminalis [5HT]'}, )
bed_nucleus_of_the_stria_terminalis_5HT = 0

rostral_group = ({k_name: 'Rostral group [A1]'},
                 {k_name: 'Rostral group [A2]'})
rostral_group_A1, rostral_group_A2 = np.arange(2)

dr = ({k_name: 'DR  [5HT]'}, )
dr_5HT = 0

mnr = ({k_name: 'MnR  [5HT]'}, )
mnr_5HT = 0

reticular_formation = ({k_name: 'Reticular formation [5HT]'}, )
reticular_formation_5HT = 0

periaqueductal_gray = ({k_name: 'Periaqueductal gray [5HT]'}, )
periaqueductal_gray_5HT = 0

hippocampus = ({k_name: 'Hippocampus [5HT]'}, )
hippocampus_5HT = 0

hypothalamus = ({k_name: 'Hypothalamus [5HT]'}, )
hypothalamus_5HT = 0

substantia_nigra = ({k_name: 'Substantia nigra [DA]'},
                    {k_name: 'Substantia nigra [5HT]'})
substantia_nigra_DA, substantia_nigra_5HT = np.arange(2)

insular_cortex = ({k_name: 'Insular cortex [5HT]'}, )
insular_cortex_5HT = 0


basal_ganglia = ({k_name: 'basal ganglia [5HT]'}, )
basal_ganglia_5HT = 0

rmg = ({k_name: 'rmg [5HT]'}, )
rmg_5HT = 0

rpa = ({k_name: 'rpa [5HT]'}, )
rpa_5HT = 0