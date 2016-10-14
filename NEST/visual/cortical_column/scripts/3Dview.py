import nest
import numpy as np
import nest.topology as tp
import matplotlib.pyplot as plt

pos = []

L2_NN = 4
L3_NN = 20
L4_NN = 40
L5_NN = 8
L6_NN = 12

for z in range(5):
    if z == 0:
        Lnum = L6_NN
    elif z == 1:
        Lnum = L5_NN
    elif z == 2:
        Lnum = L4_NN
    elif z == 3:
        Lnum = L3_NN
    else:
        Lnum = L2_NN
    xLayer =  int(pow(Lnum, 0.5)) + 1
    yLayer =  int(pow(Lnum, 0.5))
    for x in range(xLayer):
        for y in range(yLayer):
            pos.append( [float(x) / xLayer, float(y) / yLayer, float(z)] )

l = tp.CreateLayer({'positions': pos,
                    'elements' : 'iaf_neuron',
                    'extent' : [100.0, 100.0, 100.0],
                    'edge_wrap': False})


tp.PlotLayer(l)
plt.show()
