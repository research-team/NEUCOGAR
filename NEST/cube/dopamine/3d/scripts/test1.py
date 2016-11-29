import nest, nest.topology as tp
import numpy as np
import pylab
import math
from func import *


def plot_connections(layer_dict, conn_dict, file_name):
    conn_dict['synapse_model'] = 'static_synapse'
    layer = tp.CreateLayer(layer_dict)

    tp.ConnectLayers(layer, layer, conn_dict)

    fig = tp.PlotLayer(layer)
    tp.PlotTargets(tp.FindCenterElement(layer), layer, fig=fig,
                   tgt_color='red')
    pylab.savefig(file_name)
    #pylab.show()

    tp.DumpLayerConnections(layer, conn_dict['synapse_model'], file_name+".dump")

    positions = tp.GetTargetPositions(layer, layer)


l2d_specs = {
    "rows": 25,
    "columns": 25,
    "elements": 'iaf_neuron'
}
# A simple 2D grid layer
layer_2d_grid = tp.CreateLayer(l2d_specs)


positions_3d = [[np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5)]
                for a in xrange(200)]

positions_2d = [[np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5)]
                for b in xrange(2000)]

l3d_specs = {
    "elements": 'iaf_neuron',
    "positions": positions_3d
}

l2d1_specs = {
    "elements": 'iaf_neuron',
    "positions": positions_2d
}

layer_3d = tp.CreateLayer(l3d_specs)

conn_dict0 = {
    "connection_type": 'divergent',
    "mask": {"circular": {"radius": 0.25}},
    "allow_autapses": False
}

# Random connections with decreasing probability, gaussian probability kernel
conn_dict1 = {
    "connection_type": 'convergent',
    "kernel": {
        "gaussian": {"p_center": 0.5, "sigma": 2.}
    },
    "mask": {"spherical": {"radius": 0.35}}
}

# Random connectivity with fixed number of inbound connections
conn_dict2 = {
    "connection_type": 'divergent',
    "kernel": 1.,  # fixed probability
    "number_of_connections": 5
}

conn_dict3 = {
    "connection_type": "divergent",
    "mask": {
        "spherical": {"radius": 0.35}
    },
}

tp.ConnectLayers(layer_2d_grid, layer_2d_grid, conn_dict0)


def plot_all():
    plot_connections(l2d_specs, conn_dict0, 'conn0.png')
    nest.ResetKernel()
    #plot_connections(l2d1_specs, conn_dict1, 'conn11.png')
    nest.ResetKernel()
    plot_connections(l2d_specs, conn_dict2, 'conn2.png')
    nest.ResetKernel()
    plot_connections(l3d_specs, conn_dict3, 'conn3.png')


def get_delta(pos1, pos2):
    delta = math.sqrt(sum([(pos1[i]-pos2[i])**2 for i in range(len(pos1))]))
    if delta > 0.35:
        print "FOUND"
    return delta


def check_distance():
    layer = tp.CreateLayer(l3d_specs)
    tp.ConnectLayers(layer, layer, conn_dict1)

    nodes = nest.GetChildren(layer)[0]

    positions = tp.GetPosition(nodes)
    target_positions = tp.GetTargetPositions(nodes, layer)

    deltas = filter(lambda x: x > 0.35,
                    [[get_delta(positions[i], pos2) for pos2 in target_positions[i]] for i in range(len(positions))])
    print len(deltas)

check_distance()