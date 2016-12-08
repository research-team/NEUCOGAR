import os
import sys
import time
import logging
import datetime
import numpy as np
from parts import *
from time import clock
from synapses import *
from simulation_params import *
from collections import defaultdict

import nest.topology as tp

spike_generators = {}   # dict name_part : spikegenerator
spike_detectors = {}    # dict name_part : spikedetector
multimeters = {}        # dict name_part : multimeter
startsimulate = 0
endsimulate = 0
txt_result_path = ""    # path for txt results
all_parts = tuple()     # tuple of all parts
SYNAPSES = 0            # synapse number
NEURONS = 0             # neurons number
times = []              # store time simulation
save_path = ""
logging.basicConfig(format='%(name)s.%(levelname)s: %(message)s.', level=logging.DEBUG)
logger = logging.getLogger('function')

connections = dict()
parts = dict()


def getAllParts():
    return all_parts


def generate_positions(NN):
    """
    Generates uniformly random 3D positions for inner and outer layers
    Args:
        NN: Total number of neurons

    Returns: (list of inner positions, list of outer positions)

    """
    NN_in = int(NN * (1 - (1-BOUND*2)**3))
    NN_out = NN - NN_in

    inner = np.random.uniform(-.5+BOUND, .5-BOUND, (NN_in, 3)).tolist()
    outer = [[np.random.uniform(.5-BOUND, .5)*(1 if np.random.uniform() > 0.5 else -1) for a in range(3)] for b in range(NN_out)]

    return inner, outer


def generate_neurons(NNumber):
    """
    Generates layers for all declared parts.
    NB: This function doesn't connect anything.

    Args:
        NNumber: Desired number of neurons in entire network (actual number may be slightly different)

    Returns: None

    """
    global NEURONS, all_parts
    logger.debug("* * * Start generate neurons")

    parts_no_dopa = gpe + gpi + stn + amygdala + (vta[vta_GABA0], vta[vta_GABA1], vta[vta_GABA2], snc[snc_GABA]) + \
                    striatum + motor + prefrontal + nac + pptg + thalamus + snr
    parts_with_dopa = (vta[vta_DA0], vta[vta_DA1], snc[snc_DA])

    all_parts = tuple(sorted(parts_no_dopa + parts_with_dopa))

    NN_coef = float(NNumber) / sum(item[k_NN] for item in all_parts)

    for part in all_parts:
        part[k_NN] = NN_minimal if int(part[k_NN] * NN_coef) < NN_minimal else int(part[k_NN] * NN_coef)
    NEURONS = sum(item[k_NN] for item in all_parts)

    logger.debug('Initialized: {0} neurons'.format(NEURONS))

    # Init neuron models with our parameters
    nest.SetDefaults('iaf_psc_exp',   iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    # Parts without dopamine
    for part in parts_no_dopa:
        part[k_model] = 'iaf_psc_exp'
    # Parts with dopamine
    for part in parts_with_dopa:
        part[k_model] = 'iaf_psc_alpha'

    # Creating neurons
    # For each part, create inner and outer layers
    for part in all_parts:
        positions_inner, positions_outer = generate_positions(part[k_NN])

        specs_inner = {
            'positions': positions_inner,
            'elements': part[k_model]
        }

        specs_outer = {
            'positions': positions_outer,
            'elements': part[k_model]
        }

        part[k_outer] = tp.CreateLayer(specs_outer)
        part[k_inner] = tp.CreateLayer(specs_inner)

        part[k_outer_ids] = nest.GetNodes(part[k_outer])[0]
        part[k_inner_ids] = nest.GetNodes(part[k_inner])[0]

        part[k_NN_inner], part[k_NN_outer] = len(positions_inner), len(positions_outer)

        parts[part[k_name]] = part

        logger.debug("Created {0} [{1}, {2}] {3} neurons".format(part[k_name],
                                                                 part[k_outer][0], part[k_inner][0], part[k_NN]))


def log_connection(pre, post, syn_type, weight):
    global SYNAPSES
    count = len(nest.GetConnections(source=pre[k_outer_ids], target=post[k_outer_ids]))
    SYNAPSES += count
    logger.debug("{0} -> {1} ({2}) w[{3}] // "
                 "{4}x{5}={6} synapses".format(pre[k_name], post[k_name], syn_type[:-8], weight, pre[k_NN],
                                               MaxSynapses if post[k_NN] > MaxSynapses else post[k_NN], count))


def add_connection(pre, post, syn_type=GABA, weight_coef=1, dict=None):
    """
    Adds connection to dictionary for further connecting

    Args:
        pre: source layer
        post: target layer
        syn_type: synapse type
        weight_coef: weight coefficient for connection
        dict: custom connection parameters, will override defaults

    Returns: None

    """
    if not pre[k_name] in connections:
        connections[pre[k_name]] = []

    connections[pre[k_name]].append((post, syn_type, weight_coef, dict))


def connect(pre, post, syn_type=GABA, weight_coef=1, dict=None):
    """
        Connects outer parts of two 3d layers
    """

    # Create dictionary of connection rules
    conn_dict = {'connection_type': 'divergent',
                 'weights': .0 + weight_coef * synapses[syn_type][basic_weight],
                 'delays': {'linear': {  # linear is y = ax+c TODO appropriate function
                     'c': 0.1,
                     'a': 0.05
                 }},
                 #  'number_of_connections': (MaxSynapses if post[k_NN] > MaxSynapses else post[k_NN]) - 1
                 'synapse_model': synapses[syn_type][model]
    }
    if dict is not None:
        conn_dict.update(dict)

    tp.ConnectLayers(pre[k_outer], post[k_outer], conn_dict)
    # Show data of new connection
    log_connection(pre, post, synapses[syn_type][model], conn_dict['weights'])


def connect_all():
    """
        Creates all the connections (intra layer + inter layer)
    """

    for name, ts in connections.iteritems():
        total = parts[name][k_NN_inner]

        for t in ts:
            total += t[0][k_NN_outer]

        syn_total = min(MaxSynapses, total) - 1
        connect_inner(parts[name], int(syn_total * ((.0 + parts[name][k_NN_inner])/ total)))

        for t in ts:
            # TODO nest crashing when number of connections is specified
            number_of_connections = int(syn_total * ( (t[0][k_NN_outer] + .0) / total ))
            conn_dict = {
                # 'number_of_connections': number_of_connections
            }
            if t[3] is not None:
                conn_dict.update(t[3])

            connect(parts[name], t[0], t[1], t[2], conn_dict)  # TODO ugly


def connect_inner(layer, syn_oi, syn_type=GABA, weight_coef=1, custom_dict=None):
        """
            Creates connections inside layer
        """
        # TODO number of connections
        # TODO use mask, kernel and number of connections together

        syn_total = min(MaxSynapses, layer[k_NN]) - 1
        syn_ii = syn_total * layer[k_NN_inner] / layer[k_NN]
        syn_io = syn_total * layer[k_NN_outer] / layer[k_NN]

        # Create dictionary of connection rules
        conn_dict = {'connection_type': 'divergent',
                     'weights': .0 + weight_coef * synapses[syn_type][basic_weight],
                     'delays': {'linear': {  # linear is y = ax+c TODO appropriate function and parameters
                         'c': 0.1,
                         'a': 0.05
                     }},
                     'mask': {'spherical': {
                         'radius': R
                     }},
                     'kernel': {'gaussian': {  # TODO appropriate kernel
                         "p_center": 0.5,
                         "sigma": 2.
                     }},
                     'synapse_model': synapses[syn_type][model]
        }
        if custom_dict is not None:
            conn_dict.update(custom_dict)

        conn_dict_ii = dict(conn_dict)
        conn_dict_io = dict(conn_dict)
        conn_dict_oi = dict(conn_dict)

        tp.ConnectLayers(layer[k_inner], layer[k_inner], conn_dict_ii)
        tp.ConnectLayers(layer[k_inner], layer[k_outer], conn_dict_io)
        tp.ConnectLayers(layer[k_outer], layer[k_inner], conn_dict_oi)

        logger.debug("%s inner connected" % layer[k_name])


pg_count = 0
def connect_generator(part, startTime=1, stopTime=T, rate=250, coef_part=1):
    global pg_count
    name = part[k_name]
    # Add to spike_generators dict a new generator

    # model_name = 'pg'+str(pg_count)
    # pg_count += 1
    # nest.CopyModel('poisson_generator', model_name, {
    #     'rate' : float(rate),
    #     'start': float(startTime),
    #     'stop' : float(stopTime)
    # })
    #
    # layer_dict = {
    #     'elements': model_name,
    #     'positions': [[0., 0., 0.]]
    # }
    # spike_generators[name] = tp.CreateLayer(layer_dict)
    # # Create dictionary of connection rules
    # conn_dict = {'connection_type': 'divergent',
    #              # 'number_of_connections': int(part[k_NN] * coef_part),
    #              'synapse_model': 'static_synapse'
    #              }
    # #tp.ConnectLayers(spike_generators[name], part[k_outer], conn_dict)

    spike_generators[name] = nest.Create('poisson_generator', 1, {'rate' : float(rate),
                                                                  'start': float(startTime),
                                                                  'stop' : float(stopTime)})
    conn_dict = {'rule': 'fixed_outdegree',
                 'outdegree': int(part[k_NN_outer] * coef_part)}
    # Connect generator and part IDs with connection specification and synapse specification
    nest.Connect(spike_generators[name], part[k_outer_ids], conn_spec=conn_dict, syn_spec=static_syn)
    # Show data of new generator
    logger.debug("Generator => {0}. Element #{1}".format(name, spike_generators[name][0]))


def connect_detector(part):
    name = part[k_name]
    # Init number of neurons which will be under detector watching
    number = part[k_NN] if part[k_NN] < N_detect else N_detect
    # Add to spikeDetectors a new detector
    spike_detectors[name] = nest.Create('spike_detector', params=detector_param)
    # Connect N first neurons ID of part with detector
    nest.Connect(part[k_outer_ids][:number], spike_detectors[name])  # TODO
    nest.Connect(part[k_inner_ids][:number], spike_detectors[name])
    # Show data of new detector
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


def connect_multimeter(part):
    name = part[k_name]
    multimeters[name] = nest.Create('multimeter', params=multimeter_param)  # ToDo add count of multimeters
    nest.Connect(multimeters[name], (part[k_outer_ids][:N_volt]))
    logger.debug("Multimeter => {0}. On {1}".format(name, part[k_outer_ids][:N_volt]))


'''Generates string full name of an image'''
def f_name_gen(path, name):
    return "{0}{1}{2}.png".format(path, name, "+dopa" if dopamine_flag else "")


def simulate():
    global startsimulate, endsimulate, save_path
    begin = 0
    save_path = "../results/output-{0}/".format(NEURONS)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    nest.PrintNetwork()
    logger.debug('* * * Simulating')
    startsimulate = datetime.datetime.now()
    for t in np.arange(0, T, dt):
        print "SIMULATING [{0}, {1}]".format(t, t + dt)
        nest.Simulate(dt)
        end = clock()
        times.append("{0:10.1f} {1:8.1f} "
                     "{2:10.1f} {3:4.1f} {4}\n".format(begin, end - begin, end, t, datetime.datetime.now().time()))
        begin = end
        print "COMPLETED {0}%\n".format(t/T * 100 + 1)
    endsimulate = datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')


def get_log(startbuild, endbuild):
    logger.info("Number of neurons  : {}".format(NEURONS))
    logger.info("Number of synapses : {}".format(SYNAPSES))
    logger.info("Building time      : {}".format(endbuild - startbuild))
    logger.info("Simulation time    : {}".format(endsimulate - startsimulate))
    logger.info("Dopamine           : {}".format('YES' if dopamine_flag else 'NO'))


def save(GUI):
    global txt_result_path
    if GUI:
        import pylab as pl
        import nest.raster_plot
        import nest.voltage_trace
        N_events_gen = len(spike_generators)
        for key in spike_detectors:
            try:
                nest.raster_plot.from_device(spike_detectors[key], hist=True)
                pl.savefig(f_name_gen(SAVE_PATH, "spikes_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print("From {0} is NOTHING".format(key))
                N_events_gen -= 1
        for key in multimeters:
            try:
                nest.voltage_trace.from_device(multimeters[key])
                pl.savefig(f_name_gen(SAVE_PATH, "volt_" + key.lower()), dpi=dpi_n, format='png')
                pl.close()
            except Exception:
                print("From {0} is NOTHING".format(key))
        print "Results {0}/{1}".format(N_events_gen, len(spike_detectors))

    txt_result_path = save_path + 'txt/'
    logger.debug("Saving TEXT into {0}".format(txt_result_path))
    if not os.path.exists(txt_result_path):
        os.mkdir(txt_result_path)
    for key in spike_detectors:
        save_spikes(spike_detectors[key], name=key)

    #save_voltage(multimeters)

    with open(txt_result_path + 'timeSimulation.txt', 'w') as f:
        for item in times:
            f.write(item)


def save_spikes(detec, name, hist=False):
    title = "Raster plot from device '%i'" % detec[0]
    ev = nest.GetStatus(detec, "events")[0]
    ts = ev["times"]
    gids = ev["senders"]
    data = defaultdict(list)

    if len(ts):
        with open("{0}@spikes_{1}.txt".format(txt_result_path, name), 'w') as f:
            f.write("Name: {0}, Title: {1}, Hist: {2}\n".format(name, title, "True" if hist else "False"))
            for num in range(0, len(ev["times"])):
                data[round(ts[num], 1)].append(gids[num])
            for key in sorted(data.iterkeys()):
                f.write("{0:>5} : {1:>4} : {2}\n".format(key, len(data[key]), sorted(data[key])))
    else:
        print "Spikes in {0} is NULL".format(name)


def save_voltage(multimeters):
    import h5py

    print "Write to HDF5 file"
    filename = "voltage.hdf5"
    timestamp = datetime.datetime.now()

    with h5py.File(filename, "w") as f:
        f.attrs['default'] = 'entry'
        f.attrs['file_name'] = filename
        f.attrs['file_time'] = str(timestamp)

        f.create_dataset(key, data=nest.GetStatus(multimeters[key], "events")[0]["V_m"])
        f.close()
    print "wrote file:", filename
    #title = "Membrane potential"
    #ev = nest.GetStatus(detec, "events")[0]
    #with open("{0}@voltage_{1}.txt".format(txt_result_path, name), 'w') as f:
    #    f.write("Name: {0}, Title: {1}\n".format(name, title))
    #    print int(T / multimeter_param['interval'])
    #    for line in range(0, int(T / multimeter_param['interval'])):
    #        for index in range(0, N_volt):
    #            print "{0} {1} ".format(ev["times"][line], ev["V_m"][line])
    #        #f.write("\n")
    #        print "\n"