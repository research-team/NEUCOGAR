from keys import *
import numpy as np
"""
Primal/initial dictionary of parts
It contains:
    -Motor Cortex
    -Striatum
    -GPe:       globus pallidus external
    -GPi:       globus pallidus internal
    -STN:       subthalamic nucleus
    -SNr:       substantia nigra pars reticulata
    -SNc:       substantia nigra pars compacta
    -Thalamus
    -Prefrontal cortex
    -NAc:       Nucleus Accumbens
    -VTA:       Ventral Tegmental Area
    -PPTg:      Pedunculopontine Tegmental nucleus
    -Amygdala
Prefix description:
    -GABA - GABA
    -Glu  - glutamate
    -ACh  - acetylcholine
    -DA   - dopamine
"""
motor = ({k_name: 'Motor cortex'},)
motor_cortex = 0

striatum = ({k_name: 'Striatum'},)
striatumR = 0

vta = ({k_name: 'Ventral Tegmental Area'},
       {k_name: 'VTA [a1]'})
ventral_tegmental_area, vta_a1 = np.arange(2)

lc = ({k_name: 'Locus Coeruleus'},
      {k_name: 'LC [D1]'},
      {k_name: 'LC [D2]'})
locus_coeruleus, lc_D1, lc_D2 = np.arange(3)

prh = ({k_name: 'Perirhinal cortex'},)
perirhinal_cortex = 0

pgi = ({k_name: 'Nucleus paragigantocellularis lateralis'},)
nucleus_paragigantocellularis_lateralis = 0

rn = ({k_name: 'RN [a1]'},
      {k_name: 'RN [a2]'})
rn_a1, rn_a2 = np.arange(2)

bnst = ({k_name: 'Bed nucleus of the stria terminalis'},)
bed_nucleus_of_the_stria_terminalis = 0

nts = ({k_name: 'NTS [A1]'},
       {k_name: 'NTS [A2]'})
nts_a1, nts_a2 = np.arange(2)

ldt = ({k_name: 'Laterodorsal tegmentum'},
       {k_name: 'LDT [A1]'},
       {k_name: 'LDT [A2]'})
laterodorsal_tegmentum,  LDT_a1, LDT_a2 = np.arange(3)

pf = ({k_name: 'Prefrontal Cortex'},)
prefrontal_cortex = 0

motor[motor_cortex][k_NN] = 60

striatum[striatumR][k_NN] = 30

vta[ventral_tegmental_area][k_NN] = 30
vta[vta_a1][k_NN] = 30

lc[locus_coeruleus][k_NN] = 30
lc[lc_D1][k_NN] = 30
lc[lc_D2][k_NN] = 30

prh[perirhinal_cortex][k_NN] = 30

pgi[nucleus_paragigantocellularis_lateralis][k_NN] = 30

rn[rn_a1][k_NN] = 30
rn[rn_a2][k_NN] = 30

bnst[bed_nucleus_of_the_stria_terminalis][k_NN] = 30

nts[nts_a1][k_NN] = 30
nts[nts_a2][k_NN] = 30

ldt[laterodorsal_tegmentum][k_NN] = 30
ldt[LDT_a1][k_NN] = 30
ldt[LDT_a2][k_NN] = 30

pf[prefrontal_cortex][k_NN] = 30
