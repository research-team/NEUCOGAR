__author__ = "Alexey Panzer"
__version__ = "2.0.0"
__tested___ = "07.11.2017 NEST 2.12.0 Python 3"

import api_globals

__logger = api_globals.log.getLogger('api_connections')

def Connect(pre, post, synapse, weight, delay=None, rec_weight=False):
	"""
	Establish a connection between two neurons Population

	:param pre: (object) origin (pre-synaptic) neurons Population
	:param post: (object) target (post-synaptic) neurons Population:
	:param synapse: (object): synapse model
	:param weight: (float): synaptic strength
	:param delay: (list) interval distribution (low, high) or if it None use the data in parameters
	:param rec_weight: (bool) the flag to add weigth recorder
	:return:
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
	if post.getNeuronNumber() > api_globals.max_syn_per_nrn:
		current_synapses = api_globals.max_syn_per_nrn
	else:
		current_synapses = post.getNeuronNumber()

	# Create dictionary of connection rules
	conn_spec = {
		'rule': 'fixed_outdegree',          # fixed number of output connections
		'outdegree': current_synapses,      # number of output connections
		'multapses': True,                  # multiple connections between a pair of nodes
		'autapses': False                   # self-connections
	}
	# Create dictionary of synapse behavior and change weight parameter
	syn_spec = synapse.buildSynapseSpec()
	syn_spec['weight'] = float(weight)
	# Connect neurons in the normal mode
	api_globals.NEST.Connect(pre.getNeurons(),
	                         post.getNeurons(),
	                         conn_spec=conn_spec,
	                         syn_spec=syn_spec)

	# Check if connection must include weight recorder
	if rec_weight:
		# Create weight recorder with parameters
		weight_recorder = api_globals.NEST.Create('weight_recorder',
		                                          1,
		                                          {'to_memory': False,
		                                           'to_file': True,
		                                           'label': '{}_{}'.format(pre.getBrainPartName() +
		                                                                   pre.getNeurotransmitter(),
		                                                                   post.getBrainPartName() +
		                                                                   post.getNeurotransmitter())})
		# Get connections for weight recording
		connections_list = api_globals.NEST.GetConnections(pre.getNeurons()[ : api_globals.rec_weight_nrn_num],
		                                                   post.getNeurons()[ : api_globals.rec_weight_nrn_num])
		# Add to them weight recorder
		for connection in connections_list:
			print(connection)
			api_globals.NEST.SetStatus( connections_list, 'weight_recorder', weight_recorder[0])



	# Update number of synapses
	created_synapses = current_synapses * pre.getNeuronNumber()
	# Increment global number of synapses
	api_globals.global_syn_number += created_synapses
	# synapse_mem_usage = (created_synapses * api_globals.MEM_PER_SYNAPSE) >>  20
	synapse_mem_usage = round((created_synapses * api_globals.MEM_PER_STATIC_SYNAPSE) / (1024 ** 2), 2)
	api_globals.syn_mem_usage += synapse_mem_usage

	# Show data of a new connection
	__logger.info('{0} [{1}] ({2:,}) to {3} [{4}] ({5:,}) by 1:{6:,} = {7:,} synapses = {8} MB. Weight={9} {10}'.format(
		pre.getBrainPartName(),		# 0
		pre.getNeurotransmitter(),	# 1
		pre.getNeuronNumber(),		# 2
		post.getBrainPartName(),  	# 3
		post.getNeurotransmitter(),	# 4
		post.getNeuronNumber(),		# 5
		current_synapses,           # 6
		created_synapses,  			# 7
		synapse_mem_usage,  		# 8
		weight,						# 9
		"[+w_rec]" if rec_weight else "" # 10
	))


def ConnectVolumeTransmitters(*args):
	for part in args:
		print(part[api_globals.k_name])


def ConnectPoissonGenerator(part, start=api_globals.NEST.GetKernelStatus('resolution'), stop=9999999,
                            rate=250, conn_percent=100, weight=None):
	"""
	Poisson_generator - simulate neuron firing with Poisson processes statistics.

	Description:
		The poisson_generator simulates a neuron that is firing with Poisson statistics, i.e. exponentially
		distributed interspike intervals. It will generate a _unique_ spike train for each of it's targets.
		If you do not want this behavior and need the same spike train for all targets, you have to use a
		parrot neuron inbetween the poisson generator and the targets.

	Args:
		part		 (array): IDs of neurons
		start	   (double): begin of device application with resp. to origin in ms
		stop		(double): end of device application with resp. to origin in ms
		rate		(double): mean firing rate in Hz
		probability (double): percent of connection probability
		weight	  (double): strength of a signal (nS)
	"""

	outdegree = int(part.getNeuronNumber() * conn_percent / 100)

	generator = api_globals.NEST.Create('poisson_generator', 1, {'rate': float(rate),
														  'start': float(start),
														  'stop': float(stop)})
	conn_spec = {'rule': 'fixed_outdegree',
				 'outdegree': outdegree}
	syn_spec = {
		'weight': float(weight),
		'delay': float(api_globals.pg_delay)}

	api_globals.NEST.Connect(generator, part.getNeurons(), conn_spec=conn_spec, syn_spec=syn_spec)

	__logger.info("(ID:{0}) to {1} ({2}/{3}). Interval: {4}-{5}ms".format(
		generator[0],
		part.getBrainPartName() + part.getNeurotransmitter(),
		outdegree,
		part.getNeuronNumber(),
		start,
		stop
	))


def ConnectDetector(part, detect=api_globals.N_detect):
	"""
	bla bla

	Description:
		blabla

	Args:
		part (array): brain part
		detect (int): number of neurons which will be under detector watching
	"""

	name = part[api_globals.k_name]
	detector_param = {'label': name,
					  'withgid': True,
					  'to_file': True,
					  'to_memory': False}  # withweight true

	number = part[api_globals.k_NN] if part[api_globals.k_NN] < detect else detect
	tracing_ids = part[api_globals.k_IDs][:number]
	detector = api_globals.nest.Create('spike_detector', params=detector_param)
	api_globals.nest.Connect(tracing_ids, detector)
	__logger.info("(ID:{0}) to {1} ({2}/{3})".format(detector[0], name, len(tracing_ids), part[api_globals.k_NN]))


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
	name = part[api_globals.k_name]
	multimeter_param = {'label': name,
						'withgid': True,
						'withtime': True,
						'to_file': True,
						'to_memory': False,
						'interval': 0.1,
						'record_from': ['V_m']}
	tracing_ids = part[api_globals.k_IDs][:api_globals.N_volt]
	multimeter = api_globals.nest.Create('multimeter', params=multimeter_param)  # ToDo add count of multimeters
	api_globals.nest.Connect(multimeter, tracing_ids)
	__logger.info(
		"(ID:{0}) to {1} ({2}/{3}: {4})".format(multimeter[0], name, len(tracing_ids), part[api_globals.k_NN], tracing_ids))