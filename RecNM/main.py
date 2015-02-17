import numpy as np

from pybrain.datasets import SupervisedDataSet
from pybrain.structure import RecurrentNetwork
from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.supervised import BackpropTrainer

from neuromodulation.connection import NMConnection


def trainingData(size=100):
	"""
	Creates a set of training data with 4-dimensioanal input and 2-dimensional output
	with `size` samples
	"""
	data = SupervisedDataSet(4,2)

	for i in xrange(1, int(size/2)):
		[a, b] = np.random.random_integers(1, 100, 2)
		[c, d] = np.random.random_integers(100, 500, 2)
		data.addSample((a, b, c, d), (0, 1))

	for i in xrange(1, int(size/2)):
		[a, b] = np.random.random_integers(100, 500, 2)
		[c, d] = np.random.random_integers(1, 100, 2)
		data.addSample((a, b, c, d), (1, 0))

	return data

def trainedANN():
	n = RecurrentNetwork()
	
	n.addInputModule(LinearLayer(4, name='in'))
	n.addModule(SigmoidLayer(6, name='hidden'))
	n.addOutputModule(LinearLayer(2, name='out'))
	n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
	n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

	n.addRecurrentConnection(NMConnection(n['out'], n['hidden'], name='nmc'))

	n.sortModules()

	d = trainingData()
	t = BackpropTrainer(n, d, learningrate=0.001, momentum=0.99)

	# FIXME: I'm not sure the recurrent ANN is going to converge
	# so just training for fixed number of epochs
	for i in xrange(1,10):
		t.train()

	return n

def run():
	n = trainedANN()
	for x in [(10, 15, 150, 160), (10, 15, 150, 160), (150, 160, 10, 15), (150, 160, 10, 15)]:
		print("n.activate(%s) == %s\n" % (x, n.activate(x)))

if __name__ == "__main__":
	run()
