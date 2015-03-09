import numpy as np
import pickle

from pybrain.datasets import SupervisedDataSet
from pybrain.structure import RecurrentNetwork, IdentityConnection, FeedForwardNetwork
from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.supervised import BackpropTrainer

from neuromodulation.connection import NMConnection
import root


def generateTrainingData(size=100):
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


    # data.saveToFile(root.path()+"/res/dataSet")
    return data

def getDatasetFromFile(path):
    return SupervisedDataSet.loadFromFile(path)

# def getRecNetFromFile(path):

def exportNN(net, fileName = root.path()+"/res/recNN"):
    fileObject = open(fileName, 'w')
    pickle.dump(net, fileObject)
    fileObject.close()

def importNN(fileName = root.path()+"/res/recNN"):
    fileObject = open(fileName, 'r')
    net = pickle.load(fileObject)
    fileObject.close()
    return net

def trainedANN():
    n = RecurrentNetwork()

    n.addInputModule(LinearLayer(4, name='in'))
    n.addModule(SigmoidLayer(6, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

    # n.addRecurrentConnection(NMConnection(n['out'], n['hidden'], name='nmc'))
    # n.addRecurrentConnection(IdentityConnection(n['out'], n['hidden'], name='ic'))

    n.sortModules()
    # d = generateTrainingData()
    d = getDatasetFromFile(root.path()+"/res/dataSet")
    t = BackpropTrainer(n, d, learningrate=0.001, momentum=0.99)

    # FIXME: I'm not sure the recurrent ANN is going to converge
    # so just training for fixed number of epochs

    while True:
        globErr = t.train()
        print globErr
        if globErr < 0.01:
            break

    return n

def draw_connections(net):
    # for mod in n.modules:
    #     for conn in n.connections[mod]:
    #         print conn
    #         for cc in range(len(conn.params)):
    #             print conn.whichBuffers(cc), conn.params[cc]

    for mod in net.modules:
      print "Module:", mod.name
      if mod.paramdim > 0:
        print "--parameters:", mod.params
      for conn in net.connections[mod]:
        print "-connection to", conn.outmod.name
        if conn.paramdim > 0:
           print "- parameters", conn.params
      if hasattr(net, "recurrentConns"):
        print "Recurrent connections"
        for conn in net.recurrentConns:
           print "-", conn.inmod.name, " to", conn.outmod.name
           if conn.paramdim > 0:
              print "- parameters", conn.params


def run():
    n = trainedANN()

    draw_connections(n)
    # n = importNN()

    # n.__setattr__("recurrentConns", IdentityConnection(n['out'], n['hidden'], name='ic'))
    # n.__setattr__("recurrentConns", None);
    # n.addRecurrentConnection(IdentityConnection(n['out'], n['hidden'], name='ic'))
    for x in [(10, 15, 150, 160), (10, 15, 150, 160), (150, 160, 10, 15), (150, 160, 10, 15)]:
        print("n.activate(%s) == %s\n" % (x, n.activate(x)))

if __name__ == "__main__":
    run()
