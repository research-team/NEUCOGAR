import numpy as np
from numpy import dot

from pybrain.structure.connections.connection import Connection


class NMConnection(Connection):
	"""Simulates neuromodulation with randomized connection"""
	def __init__(self, *args, **kwargs):
		Connection.__init__(self, *args, **kwargs)
		n = self.outdim # self.indim*self.outdim # connect only 1 input neuron to random output
		self.params = np.random.random_integers(0, 1, n)

	def _forwardImplementation(self, inbuf, outbuf):
		outbuf += self.params*inbuf[0]

	def _backwardImplementation(self, outerr, inerr, inbuf):
		inerr += dot(self.params, outerr)
		# no calculation for self.derivs - we don't want to "educate" this connection
		# this is why we don't inherit `ParameterContainer`
