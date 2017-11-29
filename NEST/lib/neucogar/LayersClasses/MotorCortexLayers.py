from neucogar.namespaces import *
from neucogar.Nucleus import Nucleus
from .AbstractLayers import AbstractLayers
from neucogar.SynapseModel import SynapseModel

class MotorCortexLayers(AbstractLayers):
	"""
	Class implementation of the  Motor cortex layers class
	"""
	# Common variable for objects
	_nrn_parameters = {'t_ref': [2.5, 4.0],  # Refractory period
	                   'V_m': -70.0,  #
	                   'E_L': -70.0,  #
	                   'E_K': -77.0,  #
	                   'g_L': 30.0,  #
	                   'g_Na': 12000.0,  #
	                   'g_K': 3600.0,  #
	                   'C_m': 134.0,  # Capacity of membrane (pF)
	                   'tau_syn_ex': 0.2,  # Time of excitatory action (ms)
	                   'tau_syn_in': 2.0  # Time of inhibitory action (ms)
	                   }

	_glu_syn_params = {'delay': [1, 2.5],  # Synaptic delay
	                   'alpha': 1.0,  # Coeficient for inhibitory STDP time (alpha * lambda)
	                   'lambda': 0.01,  # Time interval for STDP
	                   'Wmax': 10,  # Maximum possible weight
	                   'mu_minus': 0.01,  # STDP depression step
	                   'mu_plus': 0.01  # STDP potential step
	                   }

	_gaba_syn_params = {'delay': [1, 2.5],  # Synaptic delay
	                    'alpha': 1.0,  # Coeficient for inhibitory STDP time (alpha * lambda)
	                    'lambda': 0.01,  # Time interval for STDP
	                    'Wmax': -10.0,  # Maximum possible weight
	                    'mu_minus': 0.01,  # STDP depression step
	                    'mu_plus': 0.01  # STDP potential step
	                    }

	# Setup synapse models
	_Glutamatergic = SynapseModel("Glutamatergic_layers", nest_model=STDP_SYNAPSE, params=_glu_syn_params)
	_GABAergic = SynapseModel("GABAergic_layers", nest_model=STDP_SYNAPSE, params=_gaba_syn_params)

	def __init__(self, column_index):
		# Create Nucleus objects and put into the dict of the layers
		self._dict_layers = {L2: Nucleus("Column {} Layer 2".format(column_index)),
		                     L3: Nucleus("Column {} Layer 3".format(column_index)),
		                     L4: Nucleus("Column {} Layer 4".format(column_index)),
		                     L5A: Nucleus("Column {} Layer 5A".format(column_index)),
		                     L5B: Nucleus("Column {} Layer 5B".format(column_index)),
		                     L6: Nucleus("Column {} Layer 6".format(column_index))}
		# Add sub-nucleui and create neurons without sqaling (because of flag 'forColumns'=True)
		self.layers(L2).addSubNucleus(Glu, number=546, params=self._nrn_parameters, forColumns=True)
		self.layers(L2).addSubNucleus(GABA, number=107, params=self._nrn_parameters, forColumns=True)
		self.layers(L3).addSubNucleus(Glu, number=1145, params=self._nrn_parameters, forColumns=True)
		self.layers(L3).addSubNucleus(GABA, number=123, params=self._nrn_parameters, forColumns=True)
		self.layers(L4).addSubNucleus(Glu, number=1656, params=self._nrn_parameters, forColumns=True)
		self.layers(L4).addSubNucleus(GABA, number=140, params=self._nrn_parameters, forColumns=True)
		self.layers(L5A).addSubNucleus(Glu, number=454, params=self._nrn_parameters, forColumns=True)
		self.layers(L5A).addSubNucleus(GABA, number=90, params=self._nrn_parameters, forColumns=True)
		self.layers(L5B).addSubNucleus(Glu, number=641, params=self._nrn_parameters, forColumns=True)
		self.layers(L5B).addSubNucleus(GABA, number=131, params=self._nrn_parameters, forColumns=True)
		self.layers(L6).addSubNucleus(Glu, number=1288, params=self._nrn_parameters, forColumns=True)
		self.layers(L6).addSubNucleus(GABA, number=127, params=self._nrn_parameters, forColumns=True)
		# Invoke method to create synapses
		self.setConnectomes()


	def setConnectomes(self):
		"""
		Set connectomes between layers
		"""
		# Connection probability
		L2_to_L2 = 0.093
		L2_to_L5A = 0.043

		L3_to_L2 = 0.055
		L3_to_L3 = 0.187
		L3_to_L5B = 0.018

		L4_to_L2 = 0.009
		L4_to_L3 = 0.024
		L4_to_L4 = 0.243
		L4_to_L5A = 0.007
		L4_to_L5B = 0.007

		L5A_to_L3 = 0.057
		L5A_to_L5A = 0.191

		L5B_to_L2 = 0.083
		L5B_to_L5B = 0.072
		L5B_to_L6 = 0.020

		L6_to_L4 = 0.032
		L6_to_L5A = 0.032
		L6_to_L6 = 0.028

		# Setup connectomes
		self.layers(L2).nuclei(Glu).connect(self.layers(L2).nuclei(GABA), synapse=self._Glutamatergic, weight=0.7, conn_prob=L2_to_L2)
		self.layers(L2).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L2_to_L5A)
		self.layers(L2).nuclei(GABA).connect(self.layers(L2).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)

		self.layers(L3).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L3_to_L2)
		self.layers(L3).nuclei(Glu).connect(self.layers(L3).nuclei(GABA), synapse=self._Glutamatergic, weight=0.5, conn_prob=L3_to_L3)
		self.layers(L3).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L3_to_L5B)
		self.layers(L3).nuclei(GABA).connect(self.layers(L3).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)

		self.layers(L4).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=self._Glutamatergic, weight=0.6, conn_prob=L4_to_L2)
		self.layers(L4).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=self._Glutamatergic, weight=0.6, conn_prob=L4_to_L3)
		self.layers(L4).nuclei(Glu).connect(self.layers(L4).nuclei(Glu), synapse=self._Glutamatergic, weight=0.7, conn_prob=L4_to_L4)
		self.layers(L4).nuclei(Glu).connect(self.layers(L4).nuclei(GABA), synapse=self._Glutamatergic, weight=0.5, conn_prob=L4_to_L4)
		self.layers(L4).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=self._Glutamatergic, weight=0.6, conn_prob=L4_to_L5A)
		self.layers(L4).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=self._Glutamatergic, weight=0.6, conn_prob=L4_to_L5B)
		self.layers(L4).nuclei(GABA).connect(self.layers(L4).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)

		self.layers(L5A).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L5A_to_L3)
		self.layers(L5A).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=self._Glutamatergic, weight=0.7, conn_prob=L5A_to_L5A)
		self.layers(L5A).nuclei(Glu).connect(self.layers(L5A).nuclei(GABA), synapse=self._Glutamatergic, weight=0.5, conn_prob=L5A_to_L5A)
		self.layers(L5A).nuclei(GABA).connect(self.layers(L5A).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)

		self.layers(L5B).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L5B_to_L2)
		self.layers(L5B).nuclei(Glu).connect(self.layers(L5B).nuclei(GABA), synapse=self._Glutamatergic, weight=0.5, conn_prob=L5B_to_L5B)
		self.layers(L5B).nuclei(Glu).connect(self.layers(L6).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L5B_to_L6)
		self.layers(L5B).nuclei(GABA).connect(self.layers(L5B).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)

		self.layers(L6).nuclei(Glu).connect(self.layers(L4).nuclei(Glu), synapse=self._Glutamatergic, weight=0.7, conn_prob=L6_to_L4)
		self.layers(L6).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=self._Glutamatergic, weight=1.0, conn_prob=L6_to_L5A)
		self.layers(L6).nuclei(Glu).connect(self.layers(L6).nuclei(GABA), synapse=self._Glutamatergic, weight=0.5, conn_prob=L6_to_L6)
		self.layers(L6).nuclei(GABA).connect(self.layers(L4).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)
		self.layers(L6).nuclei(GABA).connect(self.layers(L6).nuclei(Glu), synapse=self._GABAergic, weight=-1.5)

