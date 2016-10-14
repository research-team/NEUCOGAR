from property import *

# Layer   Split on neurmodulation blocks
L2_ratio = ( 2,  2, 0)
L3_ratio = (16,  2, 2)
L4_ratio = (16, 16, 8)
L5_ratio = ( 8,  0, 0)
L6_ratio = (12,  0, 0)

# Neuron number in layer
L2_NN = sum(L2_ratio)
L3_NN = sum(L3_ratio)
L4_NN = sum(L4_ratio)
L5_NN = sum(L5_ratio)
L6_NN = sum(L6_ratio)

# Tuples of layers to simplify code structure
L2_tuple = ({k_name: 'L2 [GABA 0]'},
            {k_name: 'L2 [GABA 1]'},
            {k_name: 'void'},
            (2, 2),
            (L2_ratio[L2_GABA0] / 2, L2_ratio[L2_GABA1] / 2, 0))

L3_tuple = ({k_name: 'L3 [Glu]'},
            {k_name: 'L3 [GABA 0]'},
            {k_name: 'L3 [GABA 1]'},
            (10, 2),
            (L3_ratio[L3_Glu] / 2, L3_ratio[L3_GABA0] / 2, L3_ratio[L3_GABA1] / 2))

L4_tuple = ({k_name: 'L4 [Glu 0]'},
            {k_name: 'L4 [Glu 1]'},
            {k_name: 'L4 [GABA]'},
            (20, 2),
            (L4_ratio[L4_Glu0] / 2, L4_ratio[L4_Glu1] / 2, L4_ratio[L4_GABA] / 2))

L5_tuple = ({k_name: 'L5 [Glu]'},
            {k_name: 'void'},
            {k_name: 'void'},
            (4, 2),
            (L5_ratio[L5_Glu] / 2, 0, 0))

L6_tuple = ({k_name: 'L6 [Glu]'},
            {k_name: 'void'},
            {k_name: 'void'},
            (6, 2),
            (L6_ratio[L6_Glu] / 2, 0, 0))

Thalamus = ({k_name: 'Thalamus [Glu]}'}, )
Thalamus[Glu_generator][k_NN] = 2000
# Create one structure (list) of all layers
Cortex = [L2_tuple, L3_tuple, L4_tuple, L5_tuple, L6_tuple]