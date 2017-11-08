__author__  = "Alexey Panzer"
__version__ = "2.0.0"
__tested___ = "07.11.2017 NEST 2.12.0 Python 3"

import os
import datetime
import api_globals as api_globals
from SynapseModel import SynapseModel

__all_populations_objects = []
__logger = api_globals.log.getLogger('api_initialisation')


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

	api_globals.NEST.ResetKernel()


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

	These settings should be used with care, though: setting the delay extrema too wide without
	need leads to decreased performance due to more update calls and communication cycles (small dmin),
	or increased memory consumption of NEST (large dmax).
	"""
	# List of available parameters for kernel
	available_param = ['resolution', 'local_num_threads',
					   'num_rec_processes', 'num_sim_processes', 'data_path',
					   'data_prefix', 'overwrite_files', 'print_time', 'use_wfr', 'wfr_comm_interval',
					   'wfr_tol', 'wfr_max_iterations', 'wfr_interpolation_order']

	# Dict for user parameters with default parameters
	user_property = dict(overwrite_files=True,
						 local_num_threads=1,
						 resolution=0.1,
						 print_time=True,
						 max_delay=5.0,
						 min_delay=1.0)
	# Fill the dict
	for key in kwargs:
		if key in available_param:
			user_property[key] = kwargs[key]
		else:
			raise ValueError("Key {0} is not recognized".format(key))

	if 'data_path' not in kwargs:
		api_globals.current_path = "."
	else:
		api_globals.current_path = kwargs['data_path']
		if not os.path.exists(kwargs['data_path']):
			os.makedirs(kwargs['data_path'])

	api_globals.NEST.SetKernelStatus(user_property)
	for key in user_property:
		__logger.info("{0} = {1}".format(key, user_property[key]))


def CreateNetwork(simulation_neuron_number):
	# Calculate reducing coeficient to simulate neurons with proportions
	reduce_coef = simulation_neuron_number / api_globals.global_nrn_number
	for population in __all_populations_objects:
		population.reduceNeuronNumber(reduce_coef)
		population.generateNeurons()


def NeuronGroup(brain_part_name, *populations):
	"""
	Create the dictionary for the brain part by population neuron objects

	:param brain_part_name: name of the brain part for which creating
	neuron populations
	:param populations: Population objects
	:return: dict (neurotransmitter : object)
	"""
	# Organize the objects as the map
	populations_map = {}
	# For every neurons population in the brain part
	for population in populations:
		# Set name of the brain part for the neuron population object
		population.setBrainPartName(brain_part_name)
		# Add population object to the API brain parts list
		__all_populations_objects.append(population)
		# Add population to the map by NEUROTRANSMITTER key
		populations_map[ population.getNeurotransmitter() ] = population
	return populations_map


def checkParamsFloat(param_dict):
	for parameter, value in param_dict.items():
		if type(value) is not float:
			raise Warning("NEST will give error at parameter '{}={}'. "
						  "Change value to FLOAT".format(parameter, value))


def InitSynapseModel(name, nest_model, param_dict, vt=False):
	"""
	Initialize synapse model

	Descrition:
		Copy the existing NEST synapse model to the new user model

	Args:
		neurotransmitter  (int): key of neurotransmitter
		nest_model      (str): name of model
		param_dict:          (dict): parameters for new model
		vt               (bool): volume transmitter flag
	"""

	return ()
	checkParamsFloat(param_dict)
	if vt:
		param_dict['vt'] = api_globals.NEST.Create('volume_transmitter')[0]

	synapse_dict_key = '{0}_synapse'.format(neurotransmitter)
	print(param_dict)

	api_globals.synapse_models[neurotransmitter] = synapse_dict_key

	__logger.info("'{0}'{1} from '{2}'".format(synapse_dict_key, "[+vt]" if vt else "", nest_model))



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
		part[api_globals.k_model] = model

	if number:
		part[api_globals.k_NN] = number if number > api_globals.min_neurons else api_globals.min_neurons

	neuron_memory_usage = (part[api_globals.k_NN] * api_globals.nest.GetDefaults(part[api_globals.k_model])['elementsize']) >> 20
	api_globals.nrn_mem_usage += neuron_memory_usage

	tmp = []

	for _ in range(part[api_globals.k_NN]):
		tmp.append(api_globals.nest.Create(part[api_globals.k_model], 1, {'t_ref': api_globals.np.random.uniform(2.5, 4.0)})[0])
	part[api_globals.k_IDs] = list(tmp)
	__logger.info("{0} {1} '{2}' ({3}) neurons [{4}..{5}] = {6} MB".format(
		part[api_globals.k_name],
		part[api_globals.k_NN],
		part[api_globals.k_model],
		api_globals.nest.GetDefaults(part[api_globals.k_model])['type_id'],
		part[api_globals.k_IDs][0],
		part[api_globals.k_IDs][-1],
		neuron_memory_usage
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
	part[api_globals.k_model] = model


def SetNeuronNumber(part, number):
	"""
	Set neuron number for brain part

	Description:
		Set new number to the part dict by k_NN key. Can init nuerons number fewer than min_neurons!

	Args:
		part (tuple): GIDs of neurons
		number (int): neuron number
	"""
	part[api_globals.k_NN] = number


def Simulate(T):
	"""
	Start simulation

	Description:
		Set stopwatches and invoke 'Simulate' method
	"""

	__logger.info('Used memory for neurons: {} MB'.format(api_globals.nrn_mem_usage))
	__logger.info('Used memory for synapses: {} MB'.format(api_globals.syn_mem_usage))
	__logger.info('Total used memory: {} MB'.format(api_globals.nrn_mem_usage + api_globals.syn_mem_usage))

	startsimulate = datetime.datetime.now()
	api_globals.NEST.Simulate(float(T))
	endsimulate = datetime.datetime.now()
	__logger.info('... Success. {0}'.format(endsimulate - startsimulate))