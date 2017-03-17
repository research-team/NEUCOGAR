import logging
import globals as glob

logging.basicConfig(format='%(name)s.%(levelname)s: %(message)s.', level=logging.DEBUG)
logger = logging.getLogger('api_initialisation')

def ResetKernel():
    """
    Simply function of reset kernel
    :return: None
    """
    glob.nest.ResetKernel()

def SetKernelStatus(**kwargs):
    """
    Set kernel status with available property
    :param kwargs:
        data_path               (string) - a
        local_num_threads       (int)    - a
        off_grid_spiking        (bool)   - a
        print_time              (bool)   - a
        time                    (float)  - a
        num_processes           (int)    - a
        overwrite_files         (bool)   - a
        total_num_virtual_procs (int)    - a
        tics_per_ms             (float)  - a
        data_prefix             (string) - a
        resolution              (float)  - a
    :return: None
    """
    # Reset old kernel
    glob.nest.ResetKernel()
    # List of available parameters for kernel
    available_param = ['data_path', 'local_num_threads', 'off_grid_spiking', 'print_time', 'time',
                      'num_processes', 'overwrite_files', 'total_num_virtual_procs', 'tics_per_ms',
                      'data_prefix', 'resolution']
    # Dict for user parameters with one default parameter
    user_property = {'data_path' : glob.current_path}
    # Fill the dict
    for key in kwargs:
        if key in available_param:
            user_property[key] = kwargs[key]
        else:
            raise ValueError("Key {0} is not recognized".format(key))
    # Set kernel status
    glob.nest.SetKernelStatus(user_property)


def InitNeuronModel():
    glob.nest.SetDefaults('iaf_psc_exp', iaf_neuronparams)
    pass


def InitSynapseModel(synapse_type, params, common_params, volume_transmitter=False):
    build_dict = dict()
    if volume_transmitter:
        build_dict['vt'] = glob.nest.Create('volume_transmitter')[0]
    build_dict.update(common_params)
    build_dict.update(params)
    '''
    ОТКУДА БРАТЬ УНИКАЛЬНЫЕ ПАРАМЕТРЫ fix
    '''
    if synapse_type in (glob.dopa_synapse_ex, glob.dopa_synapse_in):
        glob.nest.CopyModel('stdp_dopamine_synapse', synapse_type, build_dict)
    elif synapse_type in (glob.sero_synapse_ex, glb.sero_synapse_in):

    glob.neurotransmitters[neurotransmitter] = synapse_type
    del build_dict

def Create(neuron, number, params):
    """

    :param neuron:
    :param number:
    :param params:
    :return: tuple
    """
    return nest.Create(neuron, number, params)

def Simulate():
    glob.startsimulate = datetime.datetime.now()
    glob.nest.Simulate(T)
    glob.endsimulate = glob.startsimulate - datetime.datetime.now()
    logger.debug('* * * Simulation completed successfully')
