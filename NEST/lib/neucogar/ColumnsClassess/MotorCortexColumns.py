import numpy as np
import neucogar.api_kernel as api_kernel
from neucogar.namespaces import *
from neucogar.SynapseModel import SynapseModel
from neucogar.ColumnsClassess.AbstractColumns import AbstractColumns
from neucogar.LayersClasses.MotorCortexLayers import MotorCortexLayers


class MotorCortexColumns(AbstractColumns):
	"""
	Implementation of the AbstractColumns class with overrided methods
	"""
	_logger = api_kernel.log.getLogger("MotorCortexColumns")
	_glu_syn_params = {'delay': [1, 2.5],  # Synaptic delay
						'alpha': 1.0,  # Coeficient for inhibitory STDP time (alpha * lambda)
						'lambda': 0.01,  # Time interval for STDP
						'Wmax': 10,  # Maximum possible weight
						'mu_minus': 0.01,  # STDP depression step
						'mu_plus': 0.01  # STDP potential step
	                   }
	_Glutamatergic = SynapseModel("Glutamatergic_columns", nest_model=STDP_SYNAPSE, params=_glu_syn_params)


	def __init__(self, width, height):
		"""
		Args:
			width (int): size (width) of the column structure
			height (int): size (height) of the column structure
		"""
		self._columns = {}
		self._width_x = width
		self._height_y = height
		self._column_mapping = np.arange(height * width).reshape((height, width))
		# Create cortex columns (by layers)
		for column in range(width * height):
			self._logger.info("column {} of {}".format(column + 1, width * height))
			self._columns[column] = MotorCortexLayers(column)
		# Connect columns
		self._setConnectomes()

	def _setConnectomes(self):
		# Setup synapse model
		for column_index in self.getColumnsIndexes():
			for neighbor_index in self._getColumnNeighbors(column_index):
				self.columns(column_index).layers(L2).nuclei(Glu).connect(
					self.columns(neighbor_index).layers(L2).nuclei(Glu), synapse=self._Glutamatergic, weight=0.5, conn_prob=0.093)
