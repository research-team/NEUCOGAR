__author__  = "Alexey Panzer"
__version__ = "1.0.5"
__tested___ = "27.11.2017 NEST 2.12.0 Python 3"

from neucogar import api_kernel

_logger = api_kernel.log.getLogger('SynapseModel')

class SynapseModel:
	"""
	Synapse object
	"""

	def __init__(self, user_model, nest_model, params):
		self.__synapse_user_model = user_model
		self.__synapse_nest_model = nest_model
		self.__synapse_parameters = dict(self._int2Float(params))
		self.__synapse_parameters['weight'] = self.__synapse_parameters['Wmax']
		# Check if this model is already creatd
		if user_model in api_kernel.NEST.Models():
			raise KeyError("User model '{}' is already created".format(user_model))
		# Create a volume transmitter for synapse with neuromodulators
		if nest_model in ["stdp_dopamine_synapse",
						  "stdp_serotonin_synapse",
						  "stdp_noradrenaline_synapse"]:
			# Create and set volume transmitter
			self.__volume_transmitter = api_kernel.NEST.Create("volume_transmitter")
			# Add volume transmitter to the synapse parameters
			self.__synapse_parameters['vt'] = self.__volume_transmitter[0]
			# Create model with defaults parameters and volume transmitter
			api_kernel.NEST.CopyModel(nest_model,   # NEST model name
									  user_model,   # User model name
									  {'vt': self.__volume_transmitter[0]}) # Set VT to the model
		# if the synapse without neuromodulators
		else:
			# Copy original NEST model with default parameters
			api_kernel.NEST.CopyModel(nest_model, user_model)
			# Set the empty volume transmitter
			self.__volume_transmitter = None
		# Log actions
		_logger.info("{0} synapse ({1}) {2}".format(self.__synapse_user_model,
		                                            self.__synapse_nest_model,
		                                           "[+vt]" if self.__volume_transmitter else ""))


	def getModel(self):
		return self.__synapse_user_model


	def buildSynapseSpec(self):
		"""
		Write parameters from user style to the NEST readable

		Returns:
			dict: dict of the NEST readable format of parameters
		"""
		new_params_dict = dict(self.__synapse_parameters)
		for parameter, value in new_params_dict.items():
			if type(value) is list:
				new_params_dict[ parameter ] = {
					'distribution' : 'uniform',
				    'low' : float(value[0]),
				    'high': float(value[1])
				}
		new_params_dict['model'] = self.__synapse_user_model
		return new_params_dict


	@staticmethod
	def _int2Float(params_dict):
		for parameter, value in params_dict.items():
			if type(value) is int:
				params_dict[parameter] = float(value)
		return params_dict
