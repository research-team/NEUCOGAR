from property import *

# Layer   GLu   GABA
L1_ratio = (8, 0)   #only glu
L2_ratio = (16, 4)
L3_ratio = (32, 0)  #only glu
L4_ratio = (26, 6)
L5_ratio = (42, 0)  #only glu
L6_ratio = (74, 0)  #only glu

# Neuron number in layer
L1_NN = GlobalColumns * sum(L1_ratio)
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
L1_X, L1_Y = init_area(L1_NN, L1_ratio)
L2_X, L2_Y = init_area(L2_NN, L2_ratio)
L3_X, L3_Y = init_area(L3_NN, L3_ratio)
L4_X, L4_Y = init_area(L4_NN, L4_ratio)
L5_X, L5_Y = init_area(L5_NN, L5_ratio)
L6_X, L6_Y = init_area(L6_NN, L6_ratio)

# Tuples of layers to simplify code structure
L1_tuple = ({k_name: 'L1 [Glu]'},  # dict of Glu  part in L2 (will be extanded)
            {k_name: 'void'},  # dict of GABA part in L2 (will be extanded)
            (L1_X, L1_Y),  # area | Axis X: 323 neurons and axis Y: 316 neurons
            (L1_ratio[Glu] / 2, 0))  # step | Glu_step, GABA_step

L2_tuple = ({k_name: 'L2 [Glu]'},
            {k_name: 'L2 [GABA]'},
            (L2_X, L2_Y),
            (L2_ratio[Glu] / 2, L2_ratio[GABA] / 2))

L3_tuple = ({k_name: 'L3 [Glu]'},
            {k_name: 'void'},
            (L3_X, L3_Y),
            (L3_ratio[Glu] / 2, 0))

L4_tuple = ({k_name: 'L4 [Glu]'},
            {k_name: 'L4 [GABA]'},
            (L4_X, L4_Y),
            (L4_ratio[Glu] / 2, L4_ratio[GABA] / 2))

L5_tuple = ({k_name: 'L5 [Glu]'},
            {k_name: 'void'},
            (L5_X, L5_Y),
            (L5_ratio[Glu] / 2, 0))

L6_tuple = ({k_name: 'L6 [Glu]'},
            {k_name: 'void'},
            (L6_X, L6_Y),
            (L6_ratio[Glu] / 2, 0))

# Another parts of model
StartV = ({k_name: 'Start [Glu]'}, )
V4 = ({k_name: 'V4 [DA]'}, )
testArea = ({k_name: 'testArea [Glu]'}, )

# Initialize neuron number of additional parts
V4[DA][k_NN] = 90
StartV[Glu][k_NN] = 1000
testArea[Glu][k_NN] = 1000

# Create one structure (list) of all layers
Cortex = [L1_tuple, L2_tuple, L3_tuple, L4_tuple, L5_tuple, L6_tuple]