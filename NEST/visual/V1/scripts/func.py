import os
import sys
import nest
import time
import logging
import datetime
import numpy as np
import nest.topology as tp
import matplotlib.pyplot as plt
from collections import defaultdict
from parameters import *
from time import clock
from data import *


dictPosition_NeuronID = {}  # position (1,0,1) : 6 neuron ID
spikegenerators = {}        # dict name_part : spikegenerator
spikedetectors = {}         # dict name_part : spikedetector
txtResultPath = ""          # path for txt result
startsimulate = 0           # begin of simulation
endsimulate = 0             # end of simulation
SAVE_PATH = ""              # path to save results
SYNAPSES = 0                # number of synapses
NEURONS = 0                 # number of neurons
times = []                  # list for writing time simulation

FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('function')


def availableNeighboursList(x, step_L, Y, maximum):
    coord = []
    right = left = top = bottom = False
    if x + 1 < Y + step_L:
        coord.append(x + 1)
        right = True
    if x - 1 >= Y:
        coord.append(x - 1)
        left = True
    if x + step_L < maximum:
        coord.append(x + step_L)
        top = True
    if x - step_L >= 0:
        coord.append(x - step_L)
        bottom = True
    if top:
        if right:
            coord.append(x + step_L + 1)
        if left:
            coord.append(x + step_L - 1)
    if bottom:
        if right:
            coord.append(x - step_L + 1)
        if left:
            coord.append(x - step_L - 1)
    print x, coord
    return coord


def build_model():
    global NEURONS
    nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    layerNumberZ = 6
    neuronID = 2

    for layer in Cortex:
        columns = layer[area][X_area]
        rows    = layer[area][Y_area]
        print rows
        NEURONS += rows * columns

        for y in range(rows):
            for x in range(columns):
                dictPosition_NeuronID[ (float(x), float(y) , float(layerNumberZ)) ] = neuronID
                neuronID+=1

        layerNumberZ -= 1
        logger.debug("{0} {1} neurons".format(layer[Glu][k_name][:2], rows * columns))
        logger.debug("X: {0} ({1}neu x {2}col) \n".format(layer[area][X_area], sum(layer[step]), layer[area][X_area] / sum(layer[step])) +
                     " " * 16 +
                     "Y: {0} ({1}neu x {2}col)".format(layer[area][Y_area], 2, layer[area][Y_area] / 2 ))

    model_3D = tp.CreateLayer({'positions': dictPosition_NeuronID.keys(),
                               'elements': 'iaf_psc_exp',
                               'extent': [1000.0, 1000.0, 100.0],
                               'edge_wrap': False})

    # TODO uncomment if you want to see the 3D model
    tp.PlotLayer(model_3D)
    plt.show()

    # Build another parts
    for part in tuple(sorted(Thalamus + V1)):
        part[k_model] = 'iaf_psc_exp'
        part[k_IDs] = nest.Create(part[k_model], part[k_NN])
        NEURONS += part[k_NN]
        logger.debug("{0} [{1}, {2}] {3} neurons".format(part[k_name], part[k_IDs][0],
                                                         part[k_IDs][0] + part[k_NN] - 1, part[k_NN]))


def marking_columns():
    layerNumberZ = 6
    realLayer = 2
    for layer in Cortex:
        column = 0
        logger.debug("Marking Layer # {0}".format(layerNumberZ))
        for Y_border in range(0, layer[area][Y_area], 2):
            for X_border in range(0, layer[area][X_area], sum(layer[step])):
                FirstPartNeuronsPositions = list()
                SecondPartNeuronsPositions = list()
                ThirdPartNeuronsPositions = list()
                for X in range(X_border, X_border + layer[step][0], 1):
                    FirstPartNeuronsPositions.append(dictPosition_NeuronID[ (float(X), float(Y_border),   float(layerNumberZ)) ])
                    FirstPartNeuronsPositions.append(dictPosition_NeuronID[ (float(X), float(Y_border+1), float(layerNumberZ)) ])
                if layer[step][1] != 0:
                    for X in range(X_border + layer[step][0], X_border + layer[step][0] + layer[step][1], 1):
                        SecondPartNeuronsPositions.append(dictPosition_NeuronID[ (float(X), float(Y_border),   float(layerNumberZ)) ])
                        SecondPartNeuronsPositions.append(dictPosition_NeuronID[ (float(X), float(Y_border+1), float(layerNumberZ)) ])
                if layer[step][2] != 0:
                    for X in range(X_border + layer[step][0] + layer[step][1], X_border + sum(layer[step]), 1):
                        ThirdPartNeuronsPositions.append(dictPosition_NeuronID[(float(X), float(Y_border), float(layerNumberZ))])
                        ThirdPartNeuronsPositions.append(dictPosition_NeuronID[(float(X), float(Y_border + 1), float(layerNumberZ))])
                layer[0][column] = FirstPartNeuronsPositions
                layer[1][column] = SecondPartNeuronsPositions
                layer[2][column] = ThirdPartNeuronsPositions
                column+=1
        layerNumberZ-=1
        realLayer += 1


def connect(pre, post, syn_type=GABA, weight_coef=1):
    global SYNAPSES
    types[syn_type][0]['weight'] = weight_coef * types[syn_type][1]
    conn_dict = {'rule': 'all_to_all',
                 'multapses': True}
    nest.Connect(pre, post,
                 conn_spec=conn_dict,
                 syn_spec=types[syn_type][0])
    SYNAPSES += len(pre) * len(post)


def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    name = part[k_name]
    spikegenerators[name] = nest.Create('poisson_generator', 1, {'rate': float(rate),
                                                                 'start': float(startTime),
                                                                 'stop': float(stopTime)})
    nest.Connect(spikegenerators[name], part[k_IDs],
                 syn_spec=static_syn,
                 conn_spec={'rule': 'fixed_outdegree',
                            'outdegree': int(part[k_NN] * coef_part)})
    logger.debug("Generator => {0}. Element #{1}".format(name, spikegenerators[name][0]))


def connect_detector_layer(part, name):
    number = len(part)
    spikedetectors[name] = nest.Create('spike_detector', params=detector_param)
    nest.Connect(part, spikedetectors[name])
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


def connect_detector(part):
    name = part[k_name]
    number = part[k_NN] if part[k_NN] < N_detect else N_detect
    spikedetectors[name] = nest.Create('spike_detector', params=detector_param)
    nest.Connect(part[k_IDs][:number], spikedetectors[name])
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


def f_name_gen(path, name):
    return "{0}{1}_dopamine_{2}.png".format(path, name, 'noise' if generator_flag else 'static')


def simulate():
    global startsimulate, endsimulate, SAVE_PATH
    SAVE_PATH = "results/output-{0}/".format(NEURONS)
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    begin = 0

    logger.debug('* * * Simulating')
    nest.PrintNetwork()
    startsimulate = datetime.datetime.now()
    for t in np.arange(0, T, dt):
        print "SIMULATING [{0}, {1}]".format(t, t + dt)
        nest.Simulate(dt)
        end = clock()
        times.append("{0:10.1f} {1:8.1f} {2:10.1f} {3:4.1f} {4}\n".format(begin, end - begin, end,
                                                                          t, datetime.datetime.now().time()))
        begin = end
        print "COMPLETED {0}%\n".format(t/dt)
    endsimulate = datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')


def get_log(startbuild, endbuild):
    logger.info("Number of neurons  : {}".format(NEURONS))
    logger.info("Number of synapses : {}".format(SYNAPSES))
    logger.info("Building time      : {}".format(endbuild - startbuild))
    logger.info("Simulation time    : {}".format(endsimulate - startsimulate))
    logger.info("Noise              : {}".format('YES' if generator_flag else 'NO'))


def save(GUI):
    global txtResultPath
    if GUI:
        import pylab as pl
        import nest.raster_plot
        import nest.voltage_trace
        logger.debug("Saving IMAGES into {0}".format(SAVE_PATH))
        for key in spikedetectors:
            try:
                nest.raster_plot.from_device(spikedetectors[key], hist=True)
                pl.savefig(f_name_gen(SAVE_PATH, "spikes_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print(" * * * from {0} is NOTHING".format(key))
    txtResultPath = SAVE_PATH + 'txt/'
    logger.debug("Saving TEXT into {0}".format(txtResultPath))
    if not os.path.exists(txtResultPath):
        os.mkdir(txtResultPath)
    for key in spikedetectors:
        save_spikes(spikedetectors[key], name=key)
    with open(txtResultPath + 'timeSimulation.txt', 'w') as f:
        for item in times:
            f.write(item)


def save_spikes(detec, name, hist=False):
    title = "Raster plot from device '%i'" % detec[0]
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    gids = ev["senders"]
    data = defaultdict(list)

    if len(ts):
        with open("{0}@spikes_{1}.txt".format(txtResultPath, name), 'w') as f:
            f.write("Name: {0}, Title: {1}, Hist: {2}\n".format(name, title, "True" if hist else "False"))
            for num in range(0, len(ev["times"])):
                data[round(ts[num], 1)].append(gids[num])
            for key in sorted(data.iterkeys()):
                f.write("{0:>5} : {1:>4} : {2}\n".format(key, len(data[key]), sorted(data[key])))
    else:
        print "Spikes in {0} is NULL".format(name)