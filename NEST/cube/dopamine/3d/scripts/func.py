import numpy as np
from time import clock, time

import datetime

import nest.topology as tp
from output import *
from parts import *
from synapses import *

import globals as g

connections = dict()
parts = dict()


def get_all_parts():
    return g.all_parts


def generate_positions(nn):
    """
    Generates uniformly random 3D positions for inner and outer layers
    Args:
        nn: Total number of neurons

    Returns: (list of inner positions, list of outer positions)

    """
    NN_in = int(nn * (1 - (1 - BOUND * 2) ** 3))
    NN_out = nn - NN_in

    inner = np.random.uniform(-.5 + BOUND, .5 - BOUND, (NN_in, 3)).tolist()
    outer = [[np.random.uniform(.5 - BOUND, .5) * (1 if np.random.uniform() > 0.5 else -1) for a in range(3)] for b in
             range(NN_out)]

    return inner, outer


def generate_neurons(nn):
    """
    Generates layers for all declared parts.
    NB: This function doesn't connect anything.

    Args:
        nn: Desired number of neurons in entire network (actual number may be slightly different)

    Returns: None

    """
    logger.debug("* * * Start generate neurons")

    parts_no_dopa = gpe + gpi + stn + amygdala + (vta[vta_GABA0], vta[vta_GABA1], vta[vta_GABA2], snc[snc_GABA]) + \
                    striatum + motor + prefrontal + nac + pptg + thalamus + snr
    parts_with_dopa = (vta[vta_DA0], vta[vta_DA1], snc[snc_DA])
    g.all_parts = tuple(sorted(parts_no_dopa + parts_with_dopa))

    NN_coef = float(nn) / sum(item[k_NN] for item in g.all_parts)

    for part in g.all_parts:
        part[k_NN] = NN_minimal if int(part[k_NN] * NN_coef) < NN_minimal else int(part[k_NN] * NN_coef)
    g.NEURONS = sum(item[k_NN] for item in g.all_parts)

    logger.debug('Initialized: {0} neurons'.format(g.NEURONS))

    # Init neuron models with our parameters
    nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    nest.SetDefaults('iaf_psc_alpha', iaf_neuronparams)

    # Parts without dopamine
    for part in parts_no_dopa:
        part[k_model] = 'iaf_psc_exp'
    # Parts with dopamine
    for part in parts_with_dopa:
        part[k_model] = 'iaf_psc_alpha'

    # Creating neurons
    # For each part, create inner and outer layers
    for part in g.all_parts:
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


def add_connection(pre, post, syn_type=GABA, weight_coef=1, params=None):
    """
    Adds connection to dictionary for further connecting

    Args:
        pre: source layer
        post: target layer
        syn_type: synapse type
        weight_coef: weight coefficient for connection
        params: custom connection parameters, will override defaults

    Returns: None

    """
    if not pre[k_name] in connections:
        connections[pre[k_name]] = []

    connections[pre[k_name]].append((post, syn_type, weight_coef, params))


def connect(pre, post, syn_type=GABA, weight_coef=1, params=None):
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
    if params is not None:
        conn_dict.update(params)

    tp.ConnectLayers(pre[k_outer], post[k_outer], conn_dict)

    # Show data of new connection
    count = len(nest.GetConnections(source=pre[k_outer_ids], target=post[k_outer_ids]))
    g.SYNAPSES += count
    log_connection(pre, post, synapses[syn_type][model], conn_dict['weights'], count)


def connect_all():
    """
        Creates all the connections (intra layer + inter layer)
    """

    for name, ts in connections.iteritems():
        total = parts[name][k_NN_inner]

        for t in ts:
            total += t[0][k_NN_outer]

        syn_total = min(MaxSynapses, total) - 1
        connect_inner(parts[name], int(syn_total * ((.0 + parts[name][k_NN_inner]) / total)))

        for t in ts:
            number_of_connections = int(syn_total * ((t[0][k_NN_outer] + .0) / total))
            conn_dict = {
                'number_of_connections': number_of_connections,
                'mask': {'spherical': {  # A simple workaround for nest problem with number_of_connections
                    'radius': 2.
                }},
            }
            if t[3] is not None:
                conn_dict.update(t[3])

            connect(parts[name], t[0], t[1], t[2], conn_dict)  # TODO ugly


def connect_inner(layer, syn_oi, syn_type=GABA, weight_coef=1, custom_dict=None):
    """
        Creates connections inside layer
    """
    # TODO max number of connections
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


def connect_generator(part, start_time=1, stop_time=T, rate=250, coef_part=1):
    name = part[k_name]
    g.spike_generators[name] = nest.Create('poisson_generator', 1, {'rate': float(rate),
                                                                    'start': float(start_time),
                                                                    'stop': float(stop_time)})
    conn_dict = {'rule': 'fixed_outdegree',
                 'outdegree': int(part[k_NN_outer] * coef_part)}
    # Connect generator and part IDs with connection specification and synapse specification
    nest.Connect(g.spike_generators[name], part[k_outer_ids], conn_spec=conn_dict, syn_spec=static_syn)
    # Show data of new generator
    logger.debug("Generator => {0}. Element #{1}".format(name, g.spike_generators[name][0]))


def connect_detector(part):
    name = part[k_name]
    # Init number of neurons which will be under detector watching
    number = part[k_NN] if part[k_NN] < N_detect else N_detect
    n_in = number * part[k_NN_inner] / part[k_NN]
    n_out = number - n_in

    source = part[k_inner_ids][:n_in] + part[k_outer_ids][:n_out]
    g.spike_detectors[name] = nest.Create('spike_detector', params=detector_param)
    nest.Connect(source, g.spike_detectors[name])
    # Show data of new detector
    logger.debug("Detector => {0}. Tracing {1} neurons".format(name, number))


def connect_multimeter(part):
    name = part[k_name]
    g.multimeters[name] = nest.Create('multimeter', params=multimeter_param)  # ToDo add count of multimeters

    n_in = N_volt * part[k_NN_inner] / part[k_NN]
    n_out = N_volt - n_in
    target = part[k_inner_ids][:n_in] + part[k_outer_ids][:n_out]
    nest.Connect(g.multimeters[name], target)
    logger.debug("Multimeter => {0}. On {1}".format(name, target))


def simulate():
    begin = 0
    set_paths("../results/{0}-{1}/".format(g.NEURONS, int(time()) % 10000))
    nest.PrintNetwork()
    logger.debug('* * * Simulating')
    g.startsimulate = datetime.datetime.now()

    for t in np.arange(0, T, dt):
        print "SIMULATING [{0}, {1}]".format(t, t + dt)
        nest.Simulate(dt)
        end = clock()
        g.times.append("{0:10.1f} {1:8.1f} "
                       "{2:10.1f} {3:4.1f} {4}\n".format(begin, end - begin, end, t, datetime.datetime.now().time()))
        begin = end
        print "COMPLETED {0}%\n".format(t / T * 100 + 1)
    g.endsimulate = datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')
