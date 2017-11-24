import neucogar.api_kernel
from neucogar.LayersStructure import MotorCortexLayers
from neucogar.LayersStructure import SensoryCortexLayer
import numpy as np

class AbstractColumn:
	# column index : Layers Objects
	# {0 : Layer Objects} . . .
	_columns = {}

	# 0 1 2 3 4
	# 5 6 7 8 9
	_column_mapping = []

	_width_x = 0
	_height_y = 0

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
		!!!!!!!
		Returns:
			list: list of column keys
		"""
		return self._columns.keys()


	def __getPosByIndex(self, colum_index):
		"""

		Args:
			colum_index (int):

		Returns:
			tuple: column positions x and y
		"""
		pos_y = colum_index // self._width_x
		pos_x = colum_index % self._width_x

		return pos_x, pos_y


	def _getColumnNeighbors(self, column_index):
		"""

		Args:
			column_index (int): index of the column

		Returns:
			list: indexes of column neighbors
		"""
		column_neighbors = []

		print(self._column_mapping)

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
		print(column_neighbors)

		return column_neighbors


	def setConnectomes(self):
		pass


class MotorCortexColumns(AbstractColumn):
	def __init__(self, x, y):
		"""
		Args:
			column_num (int): column number
		"""
		self._columns = {}
		self._column_mapping = []
		self._width_x = x
		self._height_y = y

		for column in range(x * y):
			self._columns[column] = MotorCortexLayers()

		self._column_mapping = np.arange(self._height_y * self._width_x).reshape((self._height_y, self._width_x))


	def setConnectomes(self):
		for column_index in self.getColumnsIndexes():
			for neighbor_index in self._getColumnNeighbors(column_index):
				self.columns(column_index).layers(L2).nuclei(Glu).connect(self.columns(neighbor_index).layers(L2).nuclei(Glu),
				                                                          synapse=Glu, weight=0.5, conn_prob=L2_to_L2)


class SensoryCortexColumns(AbstractColumn):
	def __init__(self):
		pass