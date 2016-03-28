'''
Primal/initial dictionary of parts

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
import numpy as np

motor = ({k_name: 'Motor cortex [Glu0]'},
         {k_name: 'Motor cortex [Glu1]'})
motor_Glu0, motor_Glu1 = np.arange(2)

striatum = ({k_name: 'Striatum [D1]'},
            {k_name: 'Striatum [D2]'},
            {k_name: 'Striatum [tan]'})
D1, D2, tan = np.arange(3)

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
snc_GABA, snc_DA = np.arange(2)

thalamus = ({k_name: 'Thalamus [Glu]'}, )
thalamus_Glu = 0

prefrontal = ({k_name: 'Prefrontal cortex [Glu0]'},
              {k_name: 'Prefrontal cortex [Glu1]'})
pfc_Glu0, pfc_Glu1 = np.arange(2)

nac = ({k_name: 'NAc [ACh]'},
       {k_name: 'NAc [GABA0]'},
       {k_name: 'NAc [GABA1]'})
nac_ACh, nac_GABA0, nac_GABA1  = np.arange(3)

vta = ({k_name: 'VTA [GABA0]'},
       {k_name: 'VTA [DA0]'},
       {k_name: 'VTA [GABA1]'},
       {k_name: 'VTA [DA1]'},
       {k_name: 'VTA [GABA2]'})
vta_GABA0, vta_DA0, vta_GABA1, vta_DA1, vta_GABA2 = np.arange(5)

pptg = ({k_name: 'PPTg [GABA]'},
        {k_name: 'PPTg [ACh]'},
        {k_name: 'PPTg [Glu]'})
pptg_GABA, pptg_ACh, pptg_Glu = np.arange(3)

amygdala = ({k_name: 'Amygdala [Glu]'}, )
amygdala_Glu = 0