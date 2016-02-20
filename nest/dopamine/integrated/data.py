'''
Primal/initial dicts of parts

It contains:
    Motor Cortex
    Striatum
    GPe: globus pallidus external
    GPi: globus pallidus internal
    STN: subthalamic nucleus
    SNr: substantia nigra pars reticulata
    SNc: substantia nigra pars compacta
    Thalamus
    Prefrontal cortex
    NAc: Nucleus Accumbens
    VTA: Ventral Tegmental Area
    PPTg: Pedunculopontine Tegmental nucleus
    Amygdala
Prefix description:
    GABA - GABA
    Glu - glutamate
    ACh - acetylcholine
    DA  - dopamine
'''
from property import *

motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_Glu0 = 0
motor_Glu1 = 1

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'})
D1 = 0
D2 = 1
tan = 2

gpe = ({k_name: 'GPe [GABA]'}, )
gpe_GABA = 0

gpi = ({k_name: 'GPi [GABA]'}, )
gpi_GABA = 0

stn = ({k_name: 'STN [Glu]'}, )
stn_Glu = 0

snr = ({k_name: 'SNr [GABA]'}, )
snr_GABA = 0

snc = ({k_name: 'SNc [GABA]'},
       {k_name: 'SNc [DA]'})
snc_GABA = 0
snc_DA = 1

thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'})
pfc_Glu0 = 0
pfc_Glu1 = 1

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'})
nac_ACh = 0
nac_GABA0 = 1
nac_GABA1 = 2

vta = ({k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [DA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [DA1]'},
       {k_name: 'VTA [GABA2]'})
vta_GABA0 = 0
vta_DA0 = 1
vta_GABA1 = 2
vta_DA1 = 3
vta_GABA2 = 4

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA = 0
pptg_ACh = 1
pptg_Glu = 2

amygdala = ({k_name: 'Amygdala [Glu]'}, )
amygdala_Glu = 0