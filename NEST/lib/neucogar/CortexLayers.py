import neucogar.api_globals
from neucogar.namespaces import *
from neucogar.Nucleus import Nucleus

class AbstractLayer:
	_dict_layers = {}

	def layers(self, nucleus_name):
		"""
		Return nucleus object by nulceus name

		Args:
			nucleus_name (str): nucleus name

		Returns:
			Nucleus

		"""
		return self._dict_layers[nucleus_name]

	def setConnectomes(self):
		pass


class MotorCortexLayers(AbstractLayer):
	"""
	Class implementation of Motor cortex layers
	"""

	_dict_layers = {}

	def __init__(self):
		"""
		???
		"""
		self._dict_layers[L2] = Nucleus("Layer 2")
		self._dict_layers[L3] = Nucleus("Layer 3")
		self._dict_layers[L4] = Nucleus("Layer 4")
		self._dict_layers[L5A] = Nucleus("Layer 5A")
		self._dict_layers[L5B] = Nucleus("Layer 5B")
		self._dict_layers[L6] = Nucleus("Layer 6")

		self.layers(L2).addSubNucleus(Glu, number=546, params=nrn_parameters)
		self.layers(L2).addSubNucleus(GABA, number=107, params=nrn_parameters)

		self.layers(L3).addSubNucleus(Glu, number=1145, params=nrn_parameters)
		self.layers(L3).addSubNucleus(GABA, number=123, params=nrn_parameters)

		self.layers(L4).addSubNucleus(Glu, number=1656, params=nrn_parameters)
		self.layers(L4).addSubNucleus(GABA, number=140, params=nrn_parameters)

		self.layers(L5A).addSubNucleus(Glu, number=454, params=nrn_parameters)
		self.layers(L5A).addSubNucleus(GABA, number=90, params=nrn_parameters)

		self.layers(L5B).addSubNucleus(Glu, number=641, params=nrn_parameters)
		self.layers(L5B).addSubNucleus(GABA, number=131, params=nrn_parameters)

		self.layers(L6).addSubNucleus(Glu, number=1288, params=nrn_parameters)
		self.layers(L6).addSubNucleus(GABA, number=127, params=nrn_parameters)

	
	def setConnectomes(self):
		"""
		Set connectomes between layers

		"""
		#self.layers(L2).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L2_to_L2)
		self.layers(L2).nuclei(Glu).connect(self.layers(L2).nuclei(GABA), synapse=Glu, weight=0.7, conn_prob=L2_to_L2)
		#self.layers(L2).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L2_to_L3)
		self.layers(L2).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L2_to_L5A)
		#self.layers(L2).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L2_to_L5B)
		self.layers(L2).nuclei(GABA).connect(self.layers(L2).nuclei(Glu), synapse=GABA, weight=1.5)

		self.layers(L3).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L3_to_L2)
		#self.layers(L3).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L3_to_L3)
		self.layers(L3).nuclei(Glu).connect(self.layers(L3).nuclei(GABA), synapse=Glu, weight=0.5, conn_prob=L3_to_L3)
		#self.layers(L3).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L3_to_L5A)
		self.layers(L3).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L3_to_L5B)
		self.layers(L3).nuclei(GABA).connect(self.layers(L3).nuclei(Glu), synapse=GABA, weight=1.5)

		self.layers(L4).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=Glu, weight=0.6, conn_prob=L4_to_L2)
		self.layers(L4).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=Glu, weight=0.6, conn_prob=L4_to_L3)
		self.layers(L4).nuclei(Glu).connect(self.layers(L4).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L4_to_L4)
		self.layers(L4).nuclei(Glu).connect(self.layers(L4).nuclei(GABA), synapse=Glu, weight=0.5, conn_prob=L4_to_L4)
		self.layers(L4).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=Glu, weight=0.6, conn_prob=L4_to_L5A)
		self.layers(L4).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=Glu, weight=0.6, conn_prob=L4_to_L5B)
		self.layers(L4).nuclei(GABA).connect(self.layers(L4).nuclei(Glu), synapse=GABA, weight=1.5)

		#self.layers(L5A).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L5A_to_L2)
		self.layers(L5A).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L5A_to_L3)
		#self.layers(L5A).nuclei(Glu).connect(self.layers(L4).nuclei(Glu), synapse=Glu, weight=0.5, conn_prob=L5A_to_L4)
		self.layers(L5A).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L5A_to_L5A)
		self.layers(L5A).nuclei(Glu).connect(self.layers(L5A).nuclei(GABA), synapse=Glu, weight=0.5, conn_prob=L5A_to_L5A)
		#self.layers(L5A).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu),  synapse=Glu, weight=1.0, conn_prob=L5A_to_L5B)
		#self.layers(L5A).nuclei(Glu).connect(self.layers(L6).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L5A_to_L6)
		self.layers(L5A).nuclei(GABA).connect(self.layers(L5A).nuclei(Glu), synapse=GABA, weight=1.5)

		self.layers(L5B).nuclei(Glu).connect(self.layers(L2).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L5B_to_L2)
		#self.layers(L5B).nuclei(Glu).connect(self.layers(L3).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L5B_to_L3)
		#self.layers(L5B).nuclei(Glu).connect(self.layers(L4).nuclei(Glu), synapse=Glu, weight=0.8, conn_prob=L5B_to_L4)
		#self.layers(L5B).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L5B_to_L5B)
		self.layers(L5B).nuclei(Glu).connect(self.layers(L5B).nuclei(GABA), synapse=Glu, weight=0.5, conn_prob=L5B_to_L5B)
		self.layers(L5B).nuclei(Glu).connect(self.layers(L6).nuclei(Glu),   synapse=Glu, weight=1.0, conn_prob=L5B_to_L6)
		self.layers(L5B).nuclei(GABA).connect(self.layers(L5B).nuclei(Glu), synapse=GABA, weight=1.5)

		self.layers(L6).nuclei(Glu).connect(self.layers(L4).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L6_to_L4)
		self.layers(L6).nuclei(Glu).connect(self.layers(L5A).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L6_to_L5A)
		#self.layers(L6).nuclei(Glu).connect(self.layers(L5B).nuclei(Glu), synapse=Glu, weight=1.0, conn_prob=L6_to_L5B)
		#self.layers(L6).nuclei(Glu).connect(self.layers(L6).nuclei(Glu), synapse=Glu, weight=0.7, conn_prob=L6_to_L6)
		self.layers(L6).nuclei(Glu).connect(self.layers(L6).nuclei(GABA), synapse=Glu, weight=0.5, conn_prob=L6_to_L6)
		self.layers(L6).nuclei(GABA).connect(self.layers(L4).nuclei(Glu), synapse=GABA, weight=1.5)
		self.layers(L6).nuclei(GABA).connect(self.layers(L6).nuclei(Glu), synapse=GABA, weight=1.5)


class SensoryCortexLayer(AbstractLayer):
	"""
	Class implementation of Sensory cortex layers
	"""
	_dict_layers = {}

	def __init__(self):
		"""
		???
		"""
		self._dict_layers[L2] = Nucleus("Layer 2")
		self._dict_layers[L3] = Nucleus("Layer 3")
		self._dict_layers[L4] = Nucleus("Layer 4")
		self._dict_layers[L5] = Nucleus("Layer 5")
		self._dict_layers[L6] = Nucleus("Layer 6")

		__layers[L2].addSubNucleus(Glu, number=546, params=nrn_parameters)
		__layers[L2].addSubNucleus(GABA, number=107, params=nrn_parameters)

		__layers[L3].addSubNucleus(Glu, number=1145, params=nrn_parameters)
		__layers[L3].addSubNucleus(GABA, number=123, params=nrn_parameters)

		__layers[L4].addSubNucleus(Glu, number=1656, params=nrn_parameters)
		__layers[L4].addSubNucleus(GABA, number=140, params=nrn_parameters)

		__layers[L5A].addSubNucleus(Glu, number=454, params=nrn_parameters)
		__layers[L5A].addSubNucleus(GABA, number=90, params=nrn_parameters)

		__layers[L5B].addSubNucleus(Glu, number=641, params=nrn_parameters)
		__layers[L5B].addSubNucleus(GABA, number=131, params=nrn_parameters)

		__layers[L6].addSubNucleus(Glu, number=1288, params=nrn_parameters)
		__layers[L6].addSubNucleus(GABA, number=127, params=nrn_parameters)


	def setConnectomes(self):
		"""
		Set connectomes between layers

		"""
