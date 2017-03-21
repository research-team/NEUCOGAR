__author__  = "Alexey Panzer"
__version__ = "1.3"
__tested___ = "22.03.2017"

import os
import datetime
import api_globals as glob

logger = glob.logging.getLogger('api_initialisation')

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

    # Dict for user parameters with default parameters
    user_property = dict(overwrite_files=True,
                         local_num_threads=1,
                         resolution=0.1,
                         print_time=True)
    # Fill the dict
    for key in kwargs:
        if key in available_param:
            user_property[key] = kwargs[key]

        else:
            raise ValueError("Key {0} is not recognized".format(key))

    if 'data_path' not in kwargs:
        glob.current_path = "."
    else:
        glob.current_path = kwargs['data_path']
        if not os.path.exists(kwargs['data_path']):
            os.makedirs(kwargs['data_path'])

    # Set kernel status
    glob.nest.SetKernelStatus(user_property)

    for key in user_property:
        logger.info("{0} > {1}".format(key, user_property[key]))


def InitNeuronModel(nest_model, user_model, params):
    glob.nest.CopyModel(nest_model, user_model, params)
    logger.info("'{0}' from '{1}'".format(user_model, nest_model))


def InitSynapseModel(synapse_key, synapse_nest, params, vt=False):
    """

    :param synapse_key:
    :param synapse_nest:
    :param params:
    :param vt: volume transmitter
    :return:
    """
    build_params = dict()

    if vt:
        build_params['vt'] = glob.nest.Create('volume_transmitter')[0]
    build_params.update(params)

    user_model = '{0}_{1}'.format(synapse_nest, synapse_key)
    glob.nest.CopyModel(synapse_nest, user_model, build_params)
    glob.synapse_models[synapse_key] = (user_model, params['weight'])
    logger.info("'{0}'{1} from '{2}'".format(user_model, "[+vt]" if vt else "", synapse_nest))

    del build_params


def Create(part, model=None, number=None):
    """

    :param part:
    :param model:
    :param number:
    :return:
    """
    if model:
       part[glob.k_model] = model

    if number:
        part[glob.k_NN] = number if number > glob.min_neurons else glob.min_neurons

    part[glob.k_IDs] = glob.nest.Create(part[glob.k_model], part[glob.k_NN])
    logger.info("{0} '{1}' neurons [{2}..{3}] in {4}".format(
        part[glob.k_NN],
        part[glob.k_model],
        part[glob.k_IDs][0],
        part[glob.k_IDs][-1],
        part[glob.k_name]
        ))


def SetModel(part, model):
    """

    :param part:
    :param model:
    :return:
    """
    part[glob.k_model] = model


def SetNeuronNumber(part, number):
    """
    Can init nuerons number fewer than min_neurons
    :param part:
    :param number:
    :return:
    """
    part[glob.k_NN] = number


def Simulate():
    glob.startsimulate = datetime.datetime.now()
    glob.nest.Simulate(glob.T)
    glob.endsimulate = glob.startsimulate - datetime.datetime.now()
    logger.info('Simulation was completed successfully')