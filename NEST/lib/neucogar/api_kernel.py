__author__  = "Alexey Panzer"
__version__ = "2.0.3"
__tested___ = "27.11.2017 NEST 2.12.0 Python 3"

import datetime
import logging as log
import os
import sys
from collections import defaultdict

log.basicConfig(format='%(name)s::%(funcName)s %(message)s', level=log.INFO)
__logger = log.getLogger('api_kernel')

if 'nest' not in sys.modules:
	import nest as NEST
	__logger.info("NEST has been imported")
	NEST.ResetKernel()
	__logger.info("NEST kernel has been reset")

__all_populations_objects = []

# Common information
global_syn_number = 0
global_real_nrn_number = 0
global_sim_nrn_number = 0

nulcei_global_list = []

start_build = 0
end_build = 0

rec_weight_nrn_num = 5

# Neurons number for spike detector
N_detect = 300

# Neurons number for multimeter
N_volt = 5

# Generator delay
pg_delay = 5.

min_neurons = 10
max_syn_per_nrn = 10000

# Global value of memory usage
byte2mb = 1024 ** 2
syn_mem_usage = 0
nrn_mem_usage = 0
dev_mem_usage = 0

def SetKernelStatus(**kwargs):
	"""
	Global properties of the simulation kernel. Global properties of the simulation kernel.

	Args:
		resolution (float): The resolution of the simulation (in ms)
		total_num_virtual_procs (int): The total number of virtual processes
		local_num_threads (int): The local number of threads
		num_rec_processes (int): The number of MPI processes reserved for recording spikes
		num_sim_processes (int): The number of MPI processes reserved for simulating neurons
		grng_seed (int): Seed for global random number generator used  synchronously by all virtual
						 processes to  create, e.g., fixed fan-out connections  (write only).
		rng_seeds (array): Seeds for the per-virtual-process random number generators used for most
						   purposes. Array with one integer per virtual process, all must be unique and
						   differ from grng_seed (write only).
		data_path (str): A path, where all data is written to (default is the current directory)
		data_prefix (str): A common prefix for all data files
		overwrite_files (bool): Whether to overwrite existing data files
		print_time (bool): Whether to print progress information during the simulation
		use_wfr	(bool): Whether to use waveform relaxation method
		wfr_comm_interval (double): Desired waveform relaxation communication interval
		wfr_tol (float): Convergence tolerance of waveform relaxation method
		wfr_max_iterations (int): Maximal number of iterations used for waveform relaxation
		wfr_interpolation_order (int): Interpolation order of polynomial used in wfr iterations

	These settings should be used with care, though: setting the delay extrema too wide without
	need leads to decreased performance due to more update calls and communication cycles (small dmin),
	or increased memory consumption of NEST (large dmax).
	"""

	# List of available parameters for kernel
	available_param = ['resolution', 'local_num_threads', 'num_rec_processes', 'num_sim_processes',
	                   'data_path', 'data_prefix', 'overwrite_files', 'print_time', 'use_wfr',
	                   'wfr_comm_interval', 'wfr_tol', 'wfr_max_iterations', 'wfr_interpolation_order']
	# Dict for user parameters with default parameters
	user_property = dict(overwrite_files=True,
						 local_num_threads=1,
						 resolution=0.1,
						 print_time=True,
	                     data_path='./',
						 max_delay=5.0,
						 min_delay=1.0)
	# Fill the user property by new params
	for key, value in kwargs.items():
		if key in available_param:
			user_property[key] = value
		else:
			raise ValueError("Key {0} is not recognized".format(key))
	# Create data folder
	data_path = user_property['data_path']
	# Create dir if you are not in the current dir
	if data_path != './':
		if not os.path.exists(data_path):
			os.makedirs(data_path)
	# Set kernel status
	NEST.SetKernelStatus(user_property)
	# Log action
	for key in user_property:
		__logger.info("{0} = {1}".format(key, user_property[key]))


def CreateNetwork(simulation_neuron_number):
	"""
	Calculate coeficient of simulation/real neurons, reduce them in populations and create

	Args:
		simulation_neuron_number (int): global neuron number for simulation
	"""
	global global_sim_nrn_number
	# Calculate reducing coeficient for simulation with proportions
	reduce_coef = simulation_neuron_number / global_real_nrn_number
	# Reduce and create all neuron populations
	for nucleus in nulcei_global_list:
		nucleus._reduceNeuronNumber(reduce_coef)
		nucleus._createNeurons()
		global_sim_nrn_number += nucleus.getNeuronNumber()



def checkParamsFloat(param_dict):
	"""
	Function for checking all parameters in dict on variable type

	Args:
		param_dict (dict): Dcitionary of parameters

	Raises:
		Warnings: If parameter is not float, NEST will give Error

	"""
	for parameter, value in param_dict.items():
		if type(value) is not float:
			raise Warning("NEST will give error at parameter '{}={}'. "
						  "Change value to FLOAT".format(parameter, value))


def __mergeResultFiles():
	"""
	After simulation merge splitted files by threads and save
	"""
	# Get path of txt resutls
	results_path = NEST.GetKernelStatus()['data_path']
	# Create structure - the dict of a lists. Main file (string) : child files (list)
	files_map = defaultdict(list)
	# Build tree of rough (threaded) files
	files_list = [file for file in os.listdir(results_path) if os.path.isfile("{}/{}".format(results_path, file))]

	for threaded_file in files_list:
		main_file_name = "{}.{}".format(threaded_file.split('-')[0],    # Get body name of the file without thread number
		                                threaded_file.split('.')[-1])   # Get file format
		# Add child file to the main_file's list in dictionary
		files_map[main_file_name].append(threaded_file)
	# For every main_file in dict an his childs list
	for main_file, child_files in files_map.items():
		# Write to the main file
		with open("{}/{}".format(results_path, main_file), 'w') as f_main:
			# Get data from every child files and write to the main file
			for threaded_file in child_files:
				with open("{}/{}".format(results_path, threaded_file), 'r') as f_child:
					for line in f_child:
						f_main.write(line)
				# Delete finished needless child file
				os.remove("{}/{}".format(results_path, threaded_file))


def Simulate(time):
	"""
	"""

	# Output memory usage
	__logger.info("Used memory for neurons: {:,.3f} MB".format(nrn_mem_usage))
	__logger.info("Used memory for synapses: {:,.3f} MB".format(syn_mem_usage))
	__logger.info("Used memory for devices: {:,.3f} MB".format(dev_mem_usage))
	__logger.info("Total used memory: {:,.3f} MB".format(nrn_mem_usage +
	                                                     syn_mem_usage +
	                                                     dev_mem_usage))
	__logger.info("Total number of neurons {:,}".format(global_sim_nrn_number))
	__logger.info("Total number of synapses {:,}".format(global_syn_number))
	#
	startsimulate = datetime.datetime.now()
	__logger.info("Total number of connections {:,}".format(NEST.GetKernelStatus()['num_connections']))
	# Simulation
	NEST.Simulate(float(time))

	#
	endsimulate = datetime.datetime.now()
	# Log actions
	__logger.info('Success. {0}'.format(endsimulate - startsimulate))
	# Merge splitted results files by threads to one thread file
	__mergeResultFiles()