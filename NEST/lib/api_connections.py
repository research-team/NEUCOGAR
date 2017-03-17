import globals as glob

def SetSynapseMaxNumber(maximal, part=None):
    if part is not None:
        glob.synapse_number_limitation[part[glob.k_name]] = maximal
    else:
        glob.max_synapses = maximal


def Connect(pre, post, neurotransmitter=GABA, weight_coef=1, conn_prob=1.):
    """

    :param pre:
    :param post:
    :param neurotransmitter:
    :param weight_coef:
    :param conn_prob:
    :return:
    """
    if type(pre) is dict:
        if glob.k_IDs in pre:
            pre = tuple(pre[glob.k_IDs])
    if type(post) is dict:
        if glob.k_IDs in post:
            post = tuple(post[glob.k_IDs])

    # Set new weight value (weight_coef * basic weight)
    glob.neurotransmitters[neurotransmitter][0]['weight'] = weight_coef * glob.neurotransmitters[neurotransmitter][glob.basic_weight]
    # Correlate number of synapses
    current_synapses = int(len(post) * conn_prob)

    if current_synapses > glob.max_synapses:
        current_synapses = glob.max_synapses
    elif current_synapses < glob.min_synapses:
        current_synapses = glob.min_synapses
    # Update number of synapses
    glob.synapse_number += current_synapses * len(pre)
    # Create dictionary of connection rules
    conn_spec = {'rule': 'fixed_outdegree',
                 'outdegree': current_synapses,
                 'multapses': True,  # multiple connections between a pair of nodes
                 'autapses': False}  # self-connections
    '''
    SYN SPEC каждый раз?
    '''

    build_dict = dict()
    if volume_transmitter:
        build_dict['vt'] = glob.nest.Create('volume_transmitter')[0]
    build_dict.update(common_params)
    build_dict.update(params)

    if synapse_type in (glob.dopa_synapse_ex, glob.dopa_synapse_in):
        glob.nest.CopyModel('stdp_dopamine_synapse', synapse_type)

    glob.neurotransmitters[neurotransmitter] = synapse_type
    del build_dict

    syn_spec = {

    }
    '''
    тест
    '''
    # Connect neurons
    glob.nest.Connect(pre[glob.k_IDs], post[glob.k_IDs], conn_spec=conn_spec, syn_spec=glob.neurotransmitters[neurotransmitter][0])
    # Show data of a new connection
    print 'Connect {0} to {1} W= {2:<6} P_conn= {3:<4}% ({4}/{5})'.format(
        pre[glob.k_IDs],
        post[glob.k_IDs],
        glob.neurotransmitters[neurotransmitter][glob.model]['weight'],
        conn_prob * 100,
        current_synapses, len(post))


def ConnectPoissonGenerator(part, startTime=1, stopTime=glob.T, rate=250, coef_part=1, weight=glob.w_Glu):
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
    generator = nest.Create('poisson_generator', 1, {'rate' : float(rate),
                                                     'start': float(startTime),
                                                     'stop' : float(stopTime)})
    conn_spec = {'rule': 'fixed_outdegree',
                 'outdegree': int(part[glob.k_NN] * coef_part)}
    syn_spec = {
        'weight': weight,
        'delay': glob.pg_delay}   #FixMe change to standard or delete

    glob.nest.Connect(generator, part[glob.k_IDs], conn_spec=conn_spec, syn_spec=syn_spec)
    logger.debug("Connect Poisson generator ({0}) to {1}".format(generator, part[glob.k_name]))


def ConnectDetector(part, detect=N_detect):
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

    detector = nest.Create('spike_detector', params=detector_param)
    glob.nest.Connect(part[glob.k_IDs][:number], detector)
    logger.debug("Connect Detector {0} to {1}. Tracing {2} neurons".format(detector, name, part[glob.k_IDs][:number]))


def ConnectMultimeter(part):
    """

    :param part:
    :return:
    """
    multimeter_param = {'label': name,
                        'withgid': True,
                        'withtime': True,
                        'to_file': True,
                        'to_memory': False,
                        'interval': 0.1,
                        'record_from': ['V_m']}
    name = part[glob.k_name]
    multimeter = nest.Create('multimeter', params=multimeter_param)  # ToDo add count of multimeters
    glob.nest.Connect(multimeter, part[glob.k_IDs][:glob.N_volt])
    logger.debug("Connect Multimeter {0} to {1}. Tracing {2} neurons".format(multimeter, name, part[glob.k_IDs][:glob.N_volt]))