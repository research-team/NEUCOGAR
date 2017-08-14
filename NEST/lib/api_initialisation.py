__author__  = "Alexey Panzer"
__version__ = "1.8.1"
__tested___ = "14.08.2017 NEST 2.12.0 Python 3"

import os
import datetime
import api_globals as glob

logger = glob.logging.getLogger('api_initialisation')

def ResetKernel():
    """
    Put the simulation kernel back to its initial state.
 
    Description:
        This function re-initializes the simulation kernel, returning it to the same state as 
        after NEST has started.  
        In particular,  
    	    - all network nodes  
    	    - all connections  
    	    - all user-defined neuron and synapse models  
        are deleted, and  
        	- time  
        	- random generators  
        are reset. The only exception is that dynamically loaded modules are not unloaded. This may 
        change in a future version of NEST. The SLI interpreter is not affected by ResetKernel.
    """

    glob.nest.ResetKernel()


def SetKernelStatus(**kwargs):
    """
    Global properties of the simulation kernel. Global properties of the simulation kernel.  
    
    Args:
        Time and resolution  
            resolution      (double): The resolution of the simulation (in ms)  
            time	        (double): The current simulation time  
            max_delay	    (double): The maximum delay in the network  
            min_delay	    (double): The minimum delay in the network  
            ms_per_tic	    (double): The number of milliseconds per tic  
            tics_per_ms	    (double): The number of tics per millisecond  
            tics_per_step	   (int): The number of tics per simulation time step  
    
        Parallel processing  
            total_num_virtual_procs (int): The total number of virtual processes  
            local_num_threads	    (int): The local number of threads
            num_processes (read)
            num_rec_processes	    (int): The number of MPI processes reserved for recording spikes  
            num_sim_processes	    (int): The number of MPI processes reserved for simulating neurons  
    
        Random number generators  
            grng_seed     (int): Seed for global random number generator used  synchronously by all virtual 
                                 processes to  create, e.g., fixed fan-out connections  (write only).  
            rng_seeds   (array): Seeds for the per-virtual-process random number generators used for most 
                                 purposes. Array with one integer per virtual process, all must be unique and 
                                 differ from grng_seed (write only).  

        Output  
            data_path     (string): A path, where all data is written to (default is the current directory)  
            data_prefix	  (string): A common prefix for all data files  
            overwrite_files (bool): Whether to overwrite existing data files  
            print_time      (bool): Whether to print progress information during the simulation  
    
        Waveform relaxation method (wfr)  
            use_wfr	               (bool): Whether to use waveform relaxation method  
            wfr_comm_interval	 (double): Desired waveform relaxation communication interval  
            wfr_tol	             (double): Convergence tolerance of waveform relaxation method  
            wfr_max_iterations	    (int): Maximal number of iterations used for waveform relaxation  
            wfr_interpolation_order (int): Interpolation order of polynomial used in wfr iterations  
    
        Miscellaneous  
            dict_miss_is_error	   (bool): Whether missed dictionary entries are treated as errors  
    """

    glob.nest.ResetKernel()
    # List of available parameters for kernel
    available_param = ['resolution', 'time', 'max_delay', 'min_delay', 'ms_per_tic',
                       'tics_per_ms', 'tics_per_step', 'total_num_virtual_procs', 'local_num_threads',
                       'num_rec_processes', 'num_sim_processes', 'grng_seed', 'rng_seeds', 'data_path',
                       'data_prefix', 'overwrite_files', 'print_time', 'use_wfr', 'wfr_comm_interval',
                       'wfr_tol', 'wfr_max_iterations', 'wfr_interpolation_order', 'dict_miss_is_error']

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
        logger.info("{0} = {1}".format(key, user_property[key]))


def CheckDuplicates(parts):
    part_names = [part for part in parts[0][glob.k_name]]

    if len(part_names) != len(set(part_names)):
        ValueError('The tuple has duplicates, please delete them!')
    return tuple(sorted(parts, key=lambda x: x[glob.k_name]))


def InitNeuronModel(nest_model, user_model, params):
    """
    Initialize neuron model
    
    Descrition:
        Copy the existing NEST neuron to the new user model 
        
    Args:
        nest_model (string): Name of the NEST model 
        user_model (string): Name of the user model
        params       (dict): Params for the neuron
    """

    glob.nest.CopyModel(nest_model, user_model, params)
    logger.info("'{0}' from '{1}'".format(user_model, nest_model))


def InitSynapseModel(neurotransmitter, synapse_nest, params, vt=False):
    """
    Initialize synapse model
    
    Descrition:
        Copy the existing NEST synapse model to the new user model 
        
    Args:
        neurotransmitter  (int): key of neurotransmitter
        synapse_nest      (str): name of model
        params:          (dict): parameters for new model
        vt               (bool): volume transmitter flag
    """

    build_params = dict()

    if vt:
        build_params['vt'] = glob.nest.Create('volume_transmitter')[0]

    build_params.update(params)

    user_model = '{0}_{1}'.format(synapse_nest, neurotransmitter)
    glob.nest.CopyModel(synapse_nest, user_model, build_params)
    glob.synapse_models[neurotransmitter] = (user_model, params['weight'])
    logger.info("'{0}'{1} from '{2}'".format(user_model, "[+vt]" if vt else "", synapse_nest))

    del build_params


def Create(part, model=None, number=None):
    """
    Create neurons
    
    Description:
        Generates 'number' new neurons of the supplied 'model' type. If 'number' is not given, a 'min_neurons' 
        node is created. The objects are added as children of the current working node
   
    Args:
        part  (tuple):  neurons GIDs of a brain part
        model   (str):  model name
        number  (int):  neuron number
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
    Set model name for bran part 
    
    Description: 
        Set new model to the part dict by k_model key

    Args:
        part (tuple): GIDs of neurons
        model  (str): model name

    """
    part[glob.k_model] = model


def SetNeuronNumber(part, number):
    """
    Set neuron number for brain part
    
    Description: 
        Set new number to the part dict by k_NN key. Can init nuerons number fewer than min_neurons!

    Args:
        part (tuple): GIDs of neurons
        number (int): neuron number
    """
    part[glob.k_NN] = number


def Simulate(T):
    """
    Start simulation
        
    Description:
        Set stopwatches and invoke 'Simulate' method
    """
    startsimulate = datetime.datetime.now()
    glob.nest.Simulate(float(T))
    endsimulate = datetime.datetime.now()
    logger.info('... Success. {0}'.format(endsimulate - startsimulate))