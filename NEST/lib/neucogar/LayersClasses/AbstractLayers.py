__author__ = "Alexey Panzer"
__version__ = "1.0.3"
__tested___ = "27.11.2017 NEST 2.12.0 Python 3"

from neucogar.namespaces import *
from neucogar.Nucleus import Nucleus

class AbstractLayers:
	"""

	"""
	def __init__(self):
		self._dict_layers = {}

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
