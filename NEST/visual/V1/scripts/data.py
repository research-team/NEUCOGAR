from property import *

# Layer   GLu   GABA
L2_ratio = ( 2,  2, 0)
L3_ratio = (16,  2, 2)
L4_ratio = (16, 16, 8)
L5_ratio = ( 8,  0, 0)
L6_ratio = (12,  0, 0)

# Neuron number in layer
L2_NN = GlobalColumns * sum(L2_ratio)
L3_NN = GlobalColumns * sum(L3_ratio)
L4_NN = GlobalColumns * sum(L4_ratio)
L5_NN = GlobalColumns * sum(L5_ratio)
L6_NN = GlobalColumns * sum(L6_ratio)

# Additional function for finding good columns positions
def init_area(Layer_NN, Layer_ratio):
    Layer_X = int(pow(Layer_NN, 0.5))
    Layer_Y = Layer_X
    while Layer_X % (sum(Layer_ratio) / 2) != 0:
        Layer_X += 1
    while Layer_X * Layer_Y > Layer_NN:
        Layer_Y -= 1
    Layer_Y += 2 if (Layer_Y % 2 == 0) else 1
    return Layer_X, Layer_Y

# Layers column positioning X and Y
L2_X, L2_Y = init_area(L2_NN, L2_ratio)
L3_X, L3_Y = init_area(L3_NN, L3_ratio)
L4_X, L4_Y = init_area(L4_NN, L4_ratio)
L5_X, L5_Y = init_area(L5_NN, L5_ratio)
L6_X, L6_Y = init_area(L6_NN, L6_ratio)

# Tuples of layers to simplify code structure
L2_tuple = ({k_name: 'L2 [GABA 0]'},
            {k_name: 'L2 [GABA 1]'},
            {k_name: 'void'},
            (L2_X, L2_Y),                                        # area | Axis X: 323 neurons and axis Y: 316 neurons
            (L2_ratio[L2_GABA0] / 2, L2_ratio[L2_GABA1] / 2, 0)) # step | Glu_step, GABA_step

L3_tuple = ({k_name: 'L3 [Glu]'},
            {k_name: 'L3 [GABA 0]'},
            {k_name: 'L3 [GABA 1]'},
            (L3_X, L3_Y),
            (L3_ratio[L3_Glu] / 2, L3_ratio[L3_GABA0] / 2, L3_ratio[L3_GABA1] / 2))

L4_tuple = ({k_name: 'L4 [Glu 0]'},
            {k_name: 'L4 [Glu 1]'},
            {k_name: 'L4 [GABA]'},
            (L4_X, L4_Y),
            (L4_ratio[L4_Glu0] / 2, L4_ratio[L4_Glu1] / 2, L4_ratio[L4_GABA] / 2))

L5_tuple = ({k_name: 'L5 [Glu]'},
            {k_name: 'void'},
            {k_name: 'void'},
            (L5_X, L5_Y),
            (L5_ratio[L5_Glu] / 2, 0, 0))

L6_tuple = ({k_name: 'L6 [Glu]'},
            {k_name: 'void'},
            {k_name: 'void'},
            (L6_X, L6_Y),
            (L6_ratio[L6_Glu] / 2, 0, 0))

# Another parts of model
V1 = ({k_name: 'V1 [Glu]'}, )
Thalamus = ({k_name: 'Thalamus [Glu] generator'},
            {k_name: 'Thalamus [Glu] result'})

# Initialize neuron number of additional parts
Thalamus[Glu_generator][k_NN] = 1000
Thalamus[Glu_result][k_NN] = 2000
V1[V1_Glu][k_NN] = 1000

# Create one structure (list) of all layers
Cortex = [L2_tuple, L3_tuple, L4_tuple, L5_tuple, L6_tuple]