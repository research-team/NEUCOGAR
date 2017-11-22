from neucogar import api_globals
from neucogar.namespaces import *

logger = api_globals.log.getLogger('Population')

class Nucleus:
	"""
	Nucleus a collection of neurons that are thought to work together in performing certain functions

	"""
	__full_nucleus_name = ""
	__neurotransmitter = ""
	__nucleus_model = ""
	__neuron_number = 0
	__neuron_ids = None
	__neuron_parameters = None
	__scale_nrn_number = 1

	def __init__(self, nucleus_name):
		self.__full_nucleus_name = nucleus_name

	#  Glu : Nucleus Object
	# GABA : Nucleus Object
	__nuclei = {}

	#def addSubNucleus(self, nucleus): self.__nuclei[nucleus.getName()] = nucleus
	def addSubNucleus(self, neurotransmitter, params, number, model=HH_COND_EXP_TRAUB):
		"""

		Args:
			neurotransmitter (str):
			params (dict):
			number (int):
			model (str):
		"""
		if neurotransmitter in self.__nuclei.keys():
			raise KeyError(neurotransmitter, "this key is already used")
		self.__nuclei[neurotransmitter] = SubNucleus(neurotransmitter,
		                                          model,
		                                          params,
		                                          number)
		api_globals.global_real_nrn_number += number




	def nuclei(self, nucleus):
		"""

		Args:
			neurotransmitter (str or Nucleus): name of neurotransitter

		Returns:
			Nucleus (Nucleus): object of nucleus
		"""

		if type(nucleus) is Nucleus:
			nucleus_name = nucleus.getName()
			if nucleus_name not in self.__nuclei.keys():
				raise KeyError("The key", nucleus_name, "is not initialized in Nucleus object")
		else:
			if neurotransmitter not in self.__nuclei.keys():
				raise KeyError("The key", neurotransmitter, "is not initialized in Nucleus()")
			return self.__nuclei[neurotransmitter]


	def getBrainPartName(self):
		return self.__neuron_group_name

	def setBrainPartName(self, name):
		self.__neuron_group_name = name

	def getNeurotransmitter(self):
		return self.__neurotransmitter

	def getName(self):
		return self.__neuron_group_name + " [" + self.__neurotransmitter + "]"

	def getModel(self):
		return self.__nucleus_model

	def getNeuronNumber(self):
		return self.__neuron_number

	def getNeurons(self):
		return self.__neuron_ids

	def reduceNeuronNumber(self, coeficient):
		self.__scale_nrn_number = coeficient * 100
		self.__neuron_number = int(self.__neuron_number * coeficient)

	@staticmethod
	def useRandomDistribution(params):
		new_dict = dict(params)
		for parameter, value in new_dict.items():
			if type(value) is list:
				new_dict[parameter] = api_globals.numpy.random.uniform(value[0], value[1])
		return new_dict

	def __usage_memory(self, number, element):
		"""
		Return memory usage of this element (or number * element)

		Args:
			number (int): number of elements
			element (str or tuple): NEST element (string for synapses, tuple for devices):

		Returns:
			float: Megabytes
		"""
		# If it is an ID
		if type(element) is tuple:
			# Get name of NEST model by ID
			model = api_globals.NEST.GetStatus(element)[0]['model']
			# Get element size in bytes (for devices NEST key is 'elementsize')
			size = api_globals.NEST.GetDefaults(model)['elementsize']
		# If it is a model name
		elif type(element) is str:
			# Get element size in bytes (for synapses NEST key is 'sizeof')
			size = api_globals.NEST.GetDefaults(element)['sizeof']
		else:
			raise ValueError("Can't recognize type of input value " + element)
		# Return final size in MB
		return round(number * size / api_globals.byte2mb, 3)

	def generateNeurons(self):
		"""

		:param spec_params:
		:return:
		"""
		# If all parameters a float then all neuron will have the same parameters

		if all(self.__neuron_parameters.values()) is float:
			self.__neuron_ids = api_globals.NEST.Create(self.__nucleus_model,
			                                            self.__neuron_number,
			                                            self.__neuron_parameters)
		# If one of parameters is a list (for distribution)
		else:
			# Create temporary list for IDs
			list_of_ids = []
			# For every neuron create random distribution in listed parameters
			for _ in range(self.__neuron_number):
				list_of_ids.append(api_globals.NEST.Create(self.__nucleus_model,
				                                           1,
				                                           self.useRandomDistribution(self.__neuron_parameters))[0])
				self.__neuron_ids = tuple(list_of_ids)
		# Calculate memory usage for these created neurons
		mem_usage = round((self.__neuron_number *
		                   api_globals.NEST.GetDefaults(self.__nucleus_model)['elementsize']) /
		                  (1024 ** 2), 2)
		# Increment global value of neurons memory usage
		api_globals.nrn_mem_usage += mem_usage
		# Log actions
		logger.info("{0} {1:,} neurons ({2:.2f}% of real) = {3:,.2f} MB".format(self.getName(),
		                                                                        self.getNeuronNumber(),
		                                                                        self.__scale_nrn_number,
		                                                                        mem_usage))

	def connect(self, nucleus, synapse, weight, delay=None, conn_prob=1., rec_weight=False):
		"""
			Establish a connection between two neurons Population

			Args:
				nucleus (Nucleus): target (post-synaptic) neurons Population:
				synapse (Synapse): synapse model
				weight (float): synaptic strength
				delay (list):  interval distribution (low, high) or if it None use the data in parameters
				rec_weight (bool): the flag to add weigth recorder
			"""
		# If delay is specified for this connection then check it
		if type(delay) is list:
			nest_resoluton = api_globals.NEST.GetKernelStatus('resolution')
			if delay[0] % nest_resoluton != 0 or delay[1] % nest_resoluton != 0:
				raise Warning("Delay must be multiples of resolution")
			if delay[0] < nest_resoluton:
				raise Warning("Delay must be greater than resolution")
			if delay[1] > 8.0:
				raise Warning("Delay greater than 8.0 will rise up time of simulation")

		# Calculate synapses at this connection
		if nucleus.getNeuronNumber() > api_globals.max_syn_per_nrn:
			current_synapses = api_globals.max_syn_per_nrn
		else:
			current_synapses = post.getNeuronNumber()

		# Create dictionary of connection rules
		conn_spec = {
			'rule': 'fixed_outdegree',  # fixed number of output connections
			'outdegree': current_synapses,  # number of output connections
			'multapses': True,  # multiple connections between a pair of nodes
			'autapses': False  # self-connections
		}

		# Create dictionary of synapse behavior and change weight parameter
		syn_spec = synapse.buildSynapseSpec()
		syn_spec['weight'] = float(weight)

		# Connect neurons in the normal mode
		api_globals.NEST.Connect(self.getNeurons(),
		                         nucleus.getNeurons(),
		                         conn_spec=conn_spec,
		                         syn_spec=syn_spec)

		# Check if connection must include weight recorder
		if rec_weight:
			weight_recorder_params = {
				'to_memory': False,
				'to_file': True,
				'label': '{}_{}'.format(self.getName(), nucleus.getName())
			}
			# Create weight recorder with parameters
			weight_recorder = api_globals.NEST.Create('weight_recorder',
			                                          params=weight_recorder_params)
			# Get connections for weight recording
			connections_list = api_globals.NEST.GetConnections(self.getNeurons()[: api_globals.rec_weight_nrn_num],
			                                                   nucleus.getNeurons()[: api_globals.rec_weight_nrn_num])
			# Add to them weight recorder
			for connection in connections_list:
				print(connection)
				api_globals.NEST.SetStatus(connections_list, 'weight_recorder', weight_recorder[0])

		# Get number of synapses
		created_synapses = current_synapses * self.getNeuronNumber()
		# Update global sum of synapses
		api_globals.global_syn_number += created_synapses

		# Get memory usage of connections
		syn_mem_usage = __usage_memory(created_synapses, synapse.getModel())
		# Update global sum
		api_globals.syn_mem_usage += syn_mem_usage

		# Log actions
		__logger.info("{0} ({1:,}) to {2} ({3:,}) by 1:{4:,} = {5:,} synapses = {6} MB. Weight={7} {8}".format(
			self.getName(),  # 0
			self.getNeuronNumber(),  # 1
			nucleus.getName(),  # 2
			nucleus.getNeuronNumber(),  # 3
			current_synapses,  # 4
			created_synapses,  # 5
			syn_mem_usage,  # 6
			weight,  # 7
			"[+w_rec]" if rec_weight else ""  # 8
		))


	def ConnectPoissonGenerator(self, weight, rate,
	                            start=api_globals.NEST.GetKernelStatus('resolution'), stop=99999999, conn_percent=100):
		"""
		Poisson_generator - simulate neuron firing with Poisson processes statistics.

		The poisson_generator simulates a neuron that is firing with Poisson statistics, i.e. exponentially
		distributed interspike intervals. It will generate a _unique_ spike train for each of it's targets.
		If you do not want this behavior and need the same spike train for all targets, you have to use a
		parrot neuron inbetween the poisson generator and the targets.

		Args:
			self (object):
			weight (float): Synaptic weight of generator (nS)
			rate (int or float): Rate in HZ of spiking (Hz)
			start (int or float): Start generator at this time (ms)
			stop (int or float): Stop generator at this time (ms)
			conn_percent (int or float): Probability of connections. How much neurons will be connected to the generator
		"""

		# Set outdegree synapse number
		outdegree = int(self.getNeuronNumber() * conn_percent / 100)
		# Set generator parameters
		generator_parameterers = {
			'rate': float(rate),
			'start': float(start),
			'stop': float(stop)
		}
		# Create the Poisson generator
		generator = api_globals.NEST.Create('poisson_generator',
		                                    params=generator_parameterers)
		# Connection specification
		conn_spec = {
			'rule': 'fixed_outdegree',
			'outdegree': outdegree
		}
		# Synapse specification
		syn_spec = {
			'model': 'static_synapse',
			'weight': float(weight),
			'delay': api_globals.NEST.GetKernelStatus()['min_delay']
		}
		# Create the generator with target neurons
		api_globals.NEST.Connect(generator,
		                         self.getNeurons(),
		                         conn_spec=conn_spec,
		                         syn_spec=syn_spec)
		# Get memory usage of connections
		syn_mem_usage = __usage_memory(outdegree, "static_synapse")
		# Update global sum
		api_globals.syn_mem_usage += syn_mem_usage
		# Update global sum of synapses
		api_globals.global_syn_number += outdegree

		# Get memory usage of device
		dev_mem_usage = __usage_memory(1, generator)
		# Update global sum
		api_globals.dev_mem_usage += dev_mem_usage

		# Log actions
		__logger.info("(ID:{0}) to {1} (connected {2}%). Interval: {3}-{4} ms. Dev: {5} MB. Syn: {6} MB".format(
			generator[0],
			self.getName(),
			conn_percent,
			start,
			stop,
			dev_mem_usage,
			syn_mem_usage
		))

	def ConnectDetector(self):
		"""
		Create and connect the spike-detector device to the brain parts. It is used to record
		spikes from a single neuron or from multiple neurons at once.

		Args:
			*brain_parts (object): Sequence of brain parts (the detector connects to them)
		"""

		# Dict of detector parameters
		detector_params = {
			'label': self.getName(),  # Label is the name of the file
			'withgid': True,  # Write neuron global ID to the file
			'to_file': True,  # Flag - is writing to file
			'to_memory': False  # Flag - is writing to RAM
		}
		# Set number of tracing neurons
		tracing_neurons = self.getNeurons()[:api_globals.N_detect]

		# Create spikedetector with parameters
		spike_detector = api_globals.NEST.Create('spike_detector',
		                                         params=detector_params)

		# Connect tracing neurons to the spikedetector
		api_globals.NEST.Connect(tracing_neurons, spike_detector)

		# Get memory usage of connections
		syn_mem_usage = __usage_memory(len(tracing_neurons), 'static_synapse')
		# Update global sum
		api_globals.syn_mem_usage += syn_mem_usage
		# Update global sum of synapses
		api_globals.global_syn_number += len(tracing_neurons)

		# Get memory usage of device
		dev_mem_usage = __usage_memory(1, spike_detector)
		# Update global sum
		api_globals.dev_mem_usage += dev_mem_usage

		# Log actions
		__logger.info("(ID:{0}) to {1} (monitoring {2:.2f}% neurons) = {3} MB".format(
			spike_detector[0],
			self.getName(),
			len(tracing_neurons) / self.getNeuronNumber() * 100,
			dev_mem_usage
		))

	def ConnectMultimeter(self):
		"""
		Create and connect a multimeter to record a user-defined set of state variables from connected nodes

		Args:
			*brain_parts (object): Sequence of brain parts (the multimeter connects to them)
		"""

		# Set multimeter parameters
		multimeter_param = {
			'label': self.getName(),  # Label is the name of the file
			'withgid': True,  # Write neuron global ID to the file
			'withtime': True,  # Write time to the file
			'to_file': True,  # Flag - is writing to file
			'to_memory': False,  # Flag - is writing to RAM
			'interval': 0.1,  # Interval (ms) of getting data from neurons
			'record_from': ['V_m']  # Recording values (V_m is membrane potential)
		}
		# Set neurons ID for tracing
		tracing_neurons = self.getNeurons()[:api_globals.N_volt]
		# Create multimeter
		multimeter = api_globals.NEST.Create('multimeter',
		                                     params=multimeter_param)
		# Connect multimeter to neurons
		api_globals.NEST.Connect(multimeter, tracing_neurons)

		# Get memory usage of connections
		syn_mem_usage = __usage_memory(len(tracing_neurons), 'static_synapse')
		# Update global sum
		api_globals.syn_mem_usage += syn_mem_usage
		# Update global sum of synapses
		api_globals.global_syn_number += len(tracing_neurons)

		# Get memory usage of device
		dev_mem_usage = __usage_memory(1, multimeter)
		# Update global sum
		api_globals.dev_mem_usage += dev_mem_usage

		# Log actions
		__logger.info("(ID:{0}) to {1} (monitoring {2:.2f}% neurons). Dev: {4} MB. Syn: {5} MB".format(
			multimeter[0],
			self.getName(),
			api_globals.N_volt / self.getNeuronNumber() * 100,
			tracing_neurons,
			dev_mem_usage,
			syn_mem_usage
		))


class SubNucleus(Nucleus):
	def __init__(self, neurotransmitter, model, params, number):
		self.__neurotransmitter = neurotransmitter
		self.__neuron_model = model
		self.__neuron_number = number
		self.__neuron_parameters = params
		api_globals.global_real_nrn_number += number
