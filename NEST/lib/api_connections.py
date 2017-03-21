__author__  = "Alexey Panzer"
__version__ = "1.5"
__tested___ = "22.03.2017"

import api_globals as glob

logger = glob.logging.getLogger('api_connections')


def SetSynapseMaxNumber(maximal, part=None):
    if part is not None:
        glob.synapse_number_limitation[part[glob.k_name]] = maximal
    else:
        glob.max_synapses = maximal

def Connect(pre, post, neurotransmitter=glob.GABA, weight_coef=1, conn_prob=1.):
    """

    :param pre:
    :param post:
    :param neurotransmitter:
    :param weight_coef:
    :param conn_prob:
    :return:
    """
    '''
    if type(pre) is dict:
        if glob.k_IDs in pre:
            pre = tuple(pre[glob.k_IDs])
    if type(post) is dict:
        if glob.k_IDs in post:
            post = tuple(post[glob.k_IDs])
    '''
    # Set new weight value (weight_coef * basic weight)
    new_weight = weight_coef * glob.synapse_models[neurotransmitter][glob.basic_weight]
    glob.nest.SetDefaults(glob.synapse_models[neurotransmitter][glob.model], dict(weight=new_weight))

    # Correlate number of synapses
    current_synapses = int(post[glob.k_NN] * conn_prob)
    if current_synapses > glob.max_synapses:
        current_synapses = glob.max_synapses
    elif current_synapses < glob.min_synapses:
        current_synapses = glob.min_synapses
    # Update number of synapses
    glob.synapse_number += current_synapses * pre[glob.k_NN]

    # Create dictionary of connection rules
    conn_spec = {'rule': 'fixed_outdegree',
                 'outdegree': current_synapses,
                 'multapses': True,  # multiple connections between a pair of nodes
                 'autapses': False}  # self-connections

    # Connect neurons
    glob.nest.Connect(pre[glob.k_IDs], post[glob.k_IDs], conn_spec=conn_spec, syn_spec=glob.synapse_models[neurotransmitter][glob.model])

    # Show data of a new connection
    logger.info('{0} to {1} W={2} P_conn={3}% ({4}/{5})'.format(
        pre[glob.k_name],
        post[glob.k_name],
        #glob.nest.GetDefaults(glob.synapse_models[neurotransmitter][glob.model])['weight'],
        new_weight,
        conn_prob * 100,
        current_synapses, post[glob.k_NN]))


def ConnectPoissonGenerator(part, startTime=1, stopTime=glob.T, rate=250, coef_part=1, weight=None):
    """
    Create and connect Poisson generator
    :param part: (dict) brain part
    :param startTime: (float) start spiking
    :param stopTime: (float) stop spiking
    :param rate: (float) frequency
    :param coef_part: (float) percent of connection probability
    :param weight: (float) strength of a signal
    :return:
    """
    outdegree = int(part[glob.k_NN] * coef_part)

    generator = glob.nest.Create('poisson_generator', 1, {'rate' : float(rate),
                                                          'start': float(startTime),
                                                          'stop' : float(stopTime)})
    conn_spec = {'rule': 'fixed_outdegree',
                 'outdegree': outdegree}
    syn_spec = {
        'weight': float(weight),
        'delay': float(glob.pg_delay)}   #FixMe change to standard or delete

    glob.nest.Connect(generator, part[glob.k_IDs], conn_spec=conn_spec, syn_spec=syn_spec)

    logger.info("(ID:{0}) to {1} ({2} of {3})".format(
        generator[0],
        part[glob.k_name],
        outdegree,
        part[glob.k_NN]))


def ConnectDetector(part, detect=glob.N_detect):
    """

    :param part: (dict) brain part
    :param detect: (int) number of neurons which will be under detector watching
    :return:
    """
    name = part[glob.k_name]
    detector_param = {'label': name,
                      'withgid': True,
                      'to_file': True,
                      'to_memory': False} #withweight true

    number = part[glob.k_NN] if part[glob.k_NN] < detect else detect
    tracing_ids = part[glob.k_IDs][:number]
    detector = glob.nest.Create('spike_detector', params=detector_param)
    glob.nest.Connect(tracing_ids, detector)
    logger.info("(ID:{0}) to {1}. Tracing {2} of {3} neurons".format(detector[0], name, len(tracing_ids), part[glob.k_NN]))


def ConnectMultimeter(part, **kwargs):
    """

    :param part:
    :return:
    """
    multimeter_param = {'label': part[glob.k_name],
                        'withgid': True,
                        'withtime': True,
                        'to_file': True,
                        'to_memory': False,
                        'interval': 0.1,
                        'record_from': ['V_m']}
    tracing_ids = part[glob.k_IDs][:glob.N_volt]
    multimeter = glob.nest.Create('multimeter', params=multimeter_param)  # ToDo add count of multimeters
    glob.nest.Connect(multimeter, tracing_ids)
    logger.debug("Connected Multimeter(ID:{0}) to {1}. Tracing {2} of {3} neurons".format(multimeter[0], part[glob.k_name], len(tracing_ids), part[glob.k_NN]))