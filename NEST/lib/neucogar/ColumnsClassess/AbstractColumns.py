__author__ = "Alexey Panzer"
__version__ = "1.0.3"
__tested___ = "27.11.2017 NEST 2.12.0 Python 3"

import numpy as np
from neucogar import api_kernel
from neucogar.LayersClasses.MotorCortexLayers import MotorCortexLayers

_logger = api_kernel.log.getLogger('AColumns')

class AbstractColumns:
	"""
	Abstract column class contains basic functions for own implementation
	of column classes.
	"""

	def __init__(self):
		self._columns = {}          # column index : Layers Objects
		self._column_mapping = []   # just a matrix wih column indexes
		self._width_x = 0           # width of the column map
		self._height_y = 0          # height of the column map


	def columns(self, index):
		"""
		Get layers object of column by index

		Args:
			index (int): columns number
		Returns:
			MotorCortexLayers: layers object
		"""
		return self._columns[index]


	def getColumnsIndexes(self):
		"""
		Returns:
			list: list of column keys
		"""
		return self._columns.keys()


	def __getPosByIndex(self, colum_index):
		"""
		By columns map size returns position of the column (x,y)

		Args:
			colum_index (int): index of the column
		Returns:
			tuple: column positions x and y
		"""
		pos_y = colum_index // self._width_x
		pos_x = colum_index % self._width_x

		return pos_x, pos_y


	def _getColumnNeighbors(self, column_index):
		"""
		Finds neighbors of current column by position on the column map

		Args:
			column_index (int): index of the column
		Returns:
			list: indexes of column neighbors
		"""
		column_neighbors = []

		column_number = len(self._column_mapping)

		right = left = top = bottom = False
		pos_x, pos_y = self.__getPosByIndex(column_index)

		if column_index + 1 < self._width_x * (pos_y + 1):
			column_neighbors.append(column_index + 1)
			right = True
		if column_index - 1 >= pos_y * self._width_x:
			column_neighbors.append(column_index - 1)
			left = True
		if column_index + self._width_x < column_number:
			column_neighbors.append(column_index + self._width_x)
			bottom = True
		if column_index - self._width_x >= 0:
			column_neighbors.append(column_index - self._width_x)
			top = True
		if top:
			if right:
				column_neighbors.append(column_index - self._width_x + 1)
			if left:
				column_neighbors.append(column_index - self._width_x - 1)
		if bottom:
			if right:
				column_neighbors.append(column_index + self._width_x + 1)
			if left:
				column_neighbors.append(column_index + self._width_x - 1)
		_logger.info("Column #{} has {} neighbors".format(column_index, column_neighbors))

		return column_neighbors


	def _setConnectomes(self):
		pass