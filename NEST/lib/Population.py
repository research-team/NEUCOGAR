import api_globals

class Population:
	"""

	"""

	__neuron_group_name = ""
	__neurotransmitter = ""
	__neuron_model = ""
	__neuron_number = 0
	__neuron_ids = None
	__neuron_parameters = None

	def __init__(self, neurotransmitter, model, params, number):
		self.__neurotransmitter = neurotransmitter
		self.__neuron_model = model
		self.__neuron_number = number
		self.__neuron_parameters = params
		api_globals.global_nrn_number += number

	def getBrainPartName(self):
		return self.__neuron_group_name

	def setBrainPartName(self, name):
		self.__neuron_group_name = name

	def getNeurotransmitter(self):
		return self.__neurotransmitter

	def getModelName(self):
		return self.__neuron_model

	def getNeuronNumber(self):
		return self.__neuron_number

	def getNeurons(self):
		return self.__neuron_ids

	def reduceNeuronNumber(self, coeficient):
		self.__neuron_number = int(self.__neuron_number * coeficient)


	@staticmethod
	def useRandomDistribution(params):
		new_dict = dict(params)
		for parameter, value in new_dict.items():
			if type(value) is list:
				new_dict[parameter] = api_globals.numpy.random.uniform(value[0], value[1])
		return new_dict


	def generateNeurons(self):
		"""

		:param spec_params:
		:return:
		"""
		# If one of parameters is a list (for distribution)
		if all(self.__neuron_parameters.values()) is float:
			self.__neuron_ids = api_globals.NEST.Create(self.__neuron_model,
														self.__neuron_number,
														self.__neuron_parameters)
		# If all parameters a float then all neuron will have the same parameters
		else:

			# Create temporary list for IDs
			list_of_ids = []
			# For every neuron create random distribution in listed parameters
			for _ in range(self.__neuron_number):
				list_of_ids.append(api_globals.NEST.Create(self.__neuron_model,
														   1,
														   self.useRandomDistribution(self.__neuron_parameters))[0])
				self.__neuron_ids = tuple(list_of_ids)

