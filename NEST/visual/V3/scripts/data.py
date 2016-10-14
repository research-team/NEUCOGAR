from property import *

# Layer   GLu   GABA
L2_ratio = (26, 8)
L3_ratio = (38, 0)
L4_ratio = (28, 6)
L5_ratio = (14, 4)
L6_ratio = (20, 4)

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
L2_tuple = ({k_name: 'L2 [Glu]'},                       # dict of Glu  part in L2 (will be extanded)
            {k_name: 'L2 [GABA]'},                      # dict of GABA part in L2 (will be extanded)
            (L2_X, L2_Y),                               # area | Axis X: 323 neurons and axis Y: 316 neurons
            (L2_ratio[Glu] / 2, L2_ratio[GABA] / 2))    # step | Glu_step, GABA_step

L3_tuple = ({k_name: 'L3 [Glu]'},
            {k_name: 'void'},
            (L3_X, L3_Y),
            (L3_ratio[Glu] / 2, 0))

L4_tuple = ({k_name: 'L4 [Glu]'},
            {k_name: 'L4 [GABA]'},
            (L4_X, L4_Y),
            (L4_ratio[Glu] / 2, L4_ratio[GABA] / 2))

L5_tuple = ({k_name: 'L5 [Glu]'},
            {k_name: 'L5 [GABA]'},
            (L5_X, L5_Y),
            (L5_ratio[Glu] / 2, L5_ratio[GABA] / 2))

L6_tuple = ({k_name: 'L6 [Glu]'},
            {k_name: 'L6 [GABA]'},
            (L6_X, L6_Y),
            (L6_ratio[Glu] / 2, L6_ratio[GABA] / 2))

# Another parts of model
V1 = ({k_name: 'V1 [Glu]'}, )
V2 = ({k_name: 'V2 [Glu]'}, )
V5 = ({k_name: 'V5 [Glu]'}, )
Thalamus = ({k_name: 'Thalamus [Glu] generator'},
            {k_name: 'Thalamus [Glu] result'})

# Initialize neuron number of additional parts
Thalamus[Glu_generator][k_NN] = 2000
Thalamus[Glu_result][k_NN] = 2000
V1[V1_Glu][k_NN] = 1000
V2[V2_Glu][k_NN] = 1000
V5[V5_Glu][k_NN] = 1000

# Create one structure (list) of all layers
Cortex = [L2_tuple, L3_tuple, L4_tuple, L5_tuple, L6_tuple]