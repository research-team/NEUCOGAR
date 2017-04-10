__author__  = "Alexey Panzer"
__version__ = "1.7"
__tested___ = "10.04.2017 NEST 2.12.0"

import api_globals as glob

logger = glob.logging.getLogger('api_connections')


def SetSynapseMaxNumber(maximal, part=None):
    if part is not None:
        glob.synapse_number_limitation[part[glob.k_name]] = maximal
    else:
        glob.max_synapses = maximal


def Connect(pre, post, neurotransmitter=glob.GABA, conc_coef=1., conn_prob=1.):
    """
    Establish a connection between two nodes or lists of nodes
    
    Description:
        Redefine weight, connection number with limit checking, setup parameters and invoke nest origin method
    
    Args:
        pre (list): neurons GIDs of origin part
        post (list): neurons GIDs of target part
        neurotransmitter (int): key of a neurotrasmitter
        conc_coef (float): coeficient of transmitter concetration (weight)
        conn_prob (float): connection probability (from 0 to 1)
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
    new_weight = conc_coef * glob.synapse_models[neurotransmitter][glob.basic_weight]
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
                 'multapses': glob.multapses,  # multiple connections between a pair of nodes
                 'autapses': glob.autapses}  # self-connections

    # Connect neurons
    glob.nest.Connect(pre[glob.k_IDs], post[glob.k_IDs], conn_spec=conn_spec, syn_spec=glob.synapse_models[neurotransmitter][glob.model])

    # Show data of a new connection
    logger.info('{0} to {1} W={2}(x{3}) P_conn={4}% ({5}/{6})'.format(
        pre[glob.k_name],
        post[glob.k_name],
        #glob.nest.GetDefaults(glob.synapse_models[neurotransmitter][glob.model])['weight'],
        new_weight,
        conc_coef,
        conn_prob * 100,
        current_synapses, post[glob.k_NN]))

def ConnectVolumeTransmitters(*args):
    for part in args:

        print part[glob.k_name]

def ConnectPoissonGenerator(part, start=1, stop=glob.T, rate=250, prob=1., weight=None):
    """
    Poisson_generator - simulate neuron firing with Poisson processes statistics.
    
    Description:    
        The poisson_generator simulates a neuron that is firing with Poisson statistics, i.e. exponentially 
        distributed interspike intervals. It will generate a _unique_ spike train for each of it's targets. 
        If you do not want this behavior and need the same spike train for all targets, you have to use a  
        parrot neuron inbetween the poisson generator and the targets.  
  
    Args:
        part         (array): IDs of neurons 
        start       (double): begin of device application with resp. to origin in ms  
        stop	    (double): end of device application with resp. to origin in ms
        rate	    (double): mean firing rate in Hz  
        probability (double): percent of connection probability
        weight      (double): strength of a signal (nS)
    """

    outdegree = int(part[glob.k_NN] * prob)

    generator = glob.nest.Create('poisson_generator', 1, {'rate' : float(rate),
                                                          'start': float(start),
                                                          'stop' : float(stop)})
    conn_spec = {'rule': 'fixed_outdegree',
                 'outdegree': outdegree}
    syn_spec = {
        'weight': float(weight),
        'delay': float(glob.pg_delay)}

    glob.nest.Connect(generator, part[glob.k_IDs], conn_spec=conn_spec, syn_spec=syn_spec)

    logger.info("(ID:{0}) to {1} ({2} of {3}) Interval: {4}-{5}ms".format(
        generator[0],
        part[glob.k_name],
        outdegree,
        part[glob.k_NN],
        start,
        stop
    ))


def ConnectDetector(part, detect=glob.N_detect):
    """
    bla bla
    
    Description:
        blabla
    
    Args:
        part (array): brain part
        detect (int): number of neurons which will be under detector watching
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
    la bla
    
    Description:
        blalala
    
    Args:
        part (array): neurons GIDs of a brain part
        ....
        ....
        ....
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
    logger.info("(ID:{0}) to {1}. Tracing {2} of {3} neurons".format(multimeter[0], part[glob.k_name], len(tracing_ids), part[glob.k_NN]))