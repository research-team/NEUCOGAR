import numpy as np
import pickle

from pybrain.datasets import SupervisedDataSet, SequentialDataSet
from pybrain.structure import RecurrentNetwork, IdentityConnection, FeedForwardNetwork
from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.supervised import BackpropTrainer, RPropMinusTrainer
import matplotlib.pyplot as plt

from neuromodulation.connection import NMConnection
import root


def generateTrainingData(size=100, saveAfter = False):
    """
    Creates a set of training data with 4-dimensioanal input and 2-dimensional output
    with `size` samples
    """
    np.random.seed()
    data = SupervisedDataSet(4,2)
    for i in xrange(1, int(size/2)):
        [a, b] = np.random.random_integers(1, 100, 2)
        [c, d] = np.random.random_integers(100, 500, 2)
        data.addSample((a, b, c, d), (0, 1))

    for i in xrange(1, int(size/2)):
        [a, b] = np.random.random_integers(100, 500, 2)
        [c, d] = np.random.random_integers(1, 100, 2)
        data.addSample((a, b, c, d), (1, 0))

    if saveAfter:
        data.saveToFile(root.path()+"/res/dataSet")
    return data

def getDatasetFromFile(path = "/res/dataSet"):
    return SupervisedDataSet.loadFromFile(path)

# def getRecNetFromFile(path):

def exportANN(net, fileName = root.path()+"/res/recANN"):
    fileObject = open(fileName, 'w')
    pickle.dump(net, fileObject)
    fileObject.close()

def importANN(fileName = root.path()+"/res/recANN"):
    fileObject = open(fileName, 'r')
    net = pickle.load(fileObject)
    fileObject.close()
    return net

def exportRNN(net, fileName = root.path()+"/res/recRNN"):
    fileObject = open(fileName, 'w')
    pickle.dump(net, fileObject)
    fileObject.close()

def importRNN(fileName = root.path()+"/res/recRNN"):
    fileObject = open(fileName, 'r')
    net = pickle.load(fileObject)
    fileObject.close()
    return net

def trainedRNN():
    n = RecurrentNetwork()

    n.addInputModule(LinearLayer(4, name='in'))
    n.addModule(SigmoidLayer(6, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

    n.addRecurrentConnection(NMConnection(n['out'], n['hidden'], name='nmc'))

    n.sortModules()

    draw_connections(n)
    # d = generateTrainingData()
    d = getDatasetFromFile(root.path()+"/res/dataSet")
    t = BackpropTrainer(n, d, learningrate=0.001, momentum=0.75)
    t.trainOnDataset(d)
    # FIXME: I'm not sure the recurrent ANN is going to converge
    # so just training for fixed number of epochs

    count = 0
    while True:
        globErr = t.train()
        print globErr
        if globErr < 0.01:
            break
        # count = count + 1
        # if (count == 100):
        #     break

    # for i in range(100):
    #     print t.train()


    exportRNN(n)
    draw_connections(n)

    return n

def trainedANN():
    n = FeedForwardNetwork()

    n.addInputModule(LinearLayer(4, name='in'))
    n.addModule(SigmoidLayer(6, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

    n.sortModules()

    draw_connections(n)
    # d = generateTrainingData()
    d = getDatasetFromFile(root.path()+"/res/dataSet")
    t = BackpropTrainer(n, d, learningrate=0.001, momentum=0.75)
    t.trainOnDataset(d)
    # FIXME: I'm not sure the recurrent ANN is going to converge
    # so just training for fixed number of epochs

    count = 0
    while True:
        globErr = t.train()
        print globErr
        if globErr < 0.01:
            break
        # count = count + 1
        # if (count == 100):
        #     break

    # for i in range(100):
    #     print t.train()


    exportANN(n)
    draw_connections(n)

    return n

def draw_connections(net):

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

def initial_with_zeros(net):
    zeros = ([10.0]*len(net.params))
    net._setParameters(zeros)



def draw_graphics(net):

    k = 0
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            plt.title("["+"x"+","+str(value1)+","+"y"+","+str(value2)+"]")
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    if np.around(net.activate([i, value1, j, value2]))[0] == np.float32(1.0):
                        color = 'red'
                    else:
                        if np.around(net.activate([i, value1, j, value2]))[0] == np.float32(0.0):
                            color = 'blue'
                        else:
                            color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, label = color, alpha=0.9, edgecolor = 'none')
                plt.grid(True)

    plt.show()

def run():
    # n = trainedANN()
    # n = importANN()

    # n = trainedRNN()
    n = importRNN()

    # for x in [(1, 15, 150, 160),    (1, 15, 150, 160),
    #           (100, 110, 150, 160), (150, 160, 10, 15),
    #           (150, 160, 10, 15),   (200, 200, 100, 100),
    #           (10, 15, 300, 250),   (250, 300, 15, 10)]:
    #     print("n.activate(%s) == %s\n" % (x, n.activate(x)))

    draw_graphics(n)

if __name__ == "__main__":
    run()
