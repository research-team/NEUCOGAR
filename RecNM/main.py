from matplotlib import patches
import numpy as np
import pickle
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import RecurrentNetwork, FeedForwardNetwork
from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.supervised import BackpropTrainer
import matplotlib.pyplot as plt
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml import NetworkWriter, NetworkReader
from image_processing import get_cat_dog_trainset, get_cat_dog_testset

from neuromodulation.connection import NMConnection
import root

def generateTrainingData(size=10000, saveAfter = False):
    """
    Creates a set of training data with 4-dimensioanal input and 2-dimensional output
    with `size` samples
    """
    np.random.seed()
    data = SupervisedDataSet(4,2)
    for i in xrange(1, int(size/2)):
        [a, b] = np.random.random_integers(1, 100, 2)
        [c, d] = np.random.random_integers(100, 500, 2)
        data.addSample((a, b, c, d), (-1, 1))

    for i in xrange(1, int(size/2)):
        [a, b] = np.random.random_integers(100, 500, 2)
        [c, d] = np.random.random_integers(1, 100, 2)
        data.addSample((a, b, c, d), (1, -1))

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

def exportRFCNN(net, fileName = root.path()+"/res/recRFCNN"):
    fileObject = open(fileName, 'w')
    pickle.dump(net, fileObject)
    fileObject.close()

def importRFCNN(fileName = root.path()+"/res/recRFCNN"):
    fileObject = open(fileName, 'r')
    net = pickle.load(fileObject)
    fileObject.close()
    return net

def exportCatDogANN(net, fileName = root.path()+"/res/cat_dog_params"):
    arr = net.params
    np.save(fileName, arr)

def exportCatDogRNN(net, fileName = root.path()+"/res/cat_dog_nm_params"):
    # arr = net.params
    # np.save(fileName, arr)
    # fileObject = open(fileName+'.pickle', 'w')
    # pickle.dump(net, fileObject)
    # fileObject.close()
    NetworkWriter.writeToFile(net, fileName+'.xml')

def exportCatDogRFCNN(net, fileName = root.path()+"/res/cat_dog_fc_params"):
    # arr = net.params
    # np.save(fileName, arr)
    # fileObject = open(fileName+'.pickle', 'w')
    # pickle.dump(net, fileObject)
    # fileObject.close()
    NetworkWriter.writeToFile(net, fileName+'.xml')

def importCatDogANN(fileName = root.path()+"/res/recCatDogANN"):
    n = FeedForwardNetwork()
    n.addInputModule(LinearLayer(7500, name='in'))
    n.addModule(SigmoidLayer(9000, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

    n.sortModules()
    params = np.load(root.path()+'/res/cat_dog_params.txt.npy')
    n._setParameters(params)
    return n

def importCatDogRNN(fileName = root.path()+"/res/recCatDogANN"):
    n = NetworkReader.readFrom(root.path()+"/res/cat_dog_nm_params.xml")
    return n

def trainedRNN():
    n = RecurrentNetwork()

    n.addInputModule(LinearLayer(4, name='in'))
    n.addModule(SigmoidLayer(6, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

    n.addRecurrentConnection(NMConnection(n['out'], n['out'], name='nmc'))
    # n.addRecurrentConnection(FullConnection(n['out'], n['hidden'], inSliceFrom = 0, inSliceTo = 1, outSliceFrom = 0, outSliceTo = 3))
    n.sortModules()

    draw_connections(n)
    d = getDatasetFromFile(root.path()+"/res/dataSet")
    t = BackpropTrainer(n, d, learningrate=0.001, momentum=0.75)
    t.trainOnDataset(d)

    count = 0
    while True:
        globErr = t.train()
        print globErr
        if globErr < 0.01:
            break
        count += 1
        if count == 50:
            return trainedRNN()
    # exportRNN(n)
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
        count += 1
        if count == 20:
            return trainedANN()

    exportANN(n)
    draw_connections(n)

    return n

#return trained recurrent full connected neural network
def trainedRFCNN():
    n = RecurrentNetwork()

    n.addInputModule(LinearLayer(4, name='in'))
    n.addModule(SigmoidLayer(6, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

    n.addRecurrentConnection(FullConnection(n['out'], n['hidden'], name='nmc'))

    n.sortModules()

    draw_connections(n)
    # d = generateTraininqgData()
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
        count = count + 1
        if (count == 100):
            return trainedRFCNN()

    # for i in range(100):
    #     print t.train()


    exportRFCNN(n)
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



def draw_graphics(net, path_net = None):
    red_patch = patches.Patch(color='red', label='First neuron')
    blue_patch = patches.Patch(color='blue', label='Second neuron')
    orange_patch = patches.Patch(color='orange', label='Both neurons')
    black_patch = patches.Patch(color='black', label='Neither')
    path = path_net + 'h;h;x;y/'
    k = 0
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            title = "["+str(value1)+","+str(value2)+","+"x"+","+"y"+"]"
            plt.title(title)
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    activation = net.activate([value1, value2, i, j])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                    else:
                        # activation[0] == np.float32(0.0) and activation[1] == np.float32(0.0):
                        color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, alpha=0.9, edgecolor = 'none')
                plt.grid(True)

            plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
            plt.savefig(path + title + '.png')

    path = path_net + 'h;x;h;y/'
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            title = "["+str(value1)+","+"x"+","+str(value2)+","+"y"+"]"
            plt.title(title)
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    activation = net.activate([value1, i, value2, j])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                    else:
                        # activation[0] == np.float32(0.0) and activation[1] == np.float32(0.0):
                        color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, alpha=0.9, edgecolor = 'none')
                plt.grid(True)

            plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
            plt.savefig(path + title + '.png')

    path = path_net + 'h;x;y;h/'
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            title = "["+str(value1)+","+"x"+","+"y"+","+str(value2)+"]"
            plt.title(title)
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    activation = net.activate([value1, i, j, value2])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                    else:
                        # activation[0] == np.float32(0.0) and activation[1] == np.float32(0.0):
                        color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, alpha=0.9, edgecolor = 'none')
                plt.grid(True)

            plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
            plt.savefig(path + title + '.png')

    path = path_net + 'x;h;y;h/'
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            title = "["+"x"+","+str(value1)+","+"y"+","+str(value2)+"]"
            plt.title(title)
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    activation = net.activate([i, value1, j, value2])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                    else:
                        # activation[0] == np.float32(0.0) and activation[1] == np.float32(0.0):
                        color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, alpha=0.9, edgecolor = 'none')
                plt.grid(True)

            plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
            plt.savefig(path + title + '.png')

    path = path_net + 'x;y;h;h/'
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            title = "["+"x"+","+"y"+","+str(value1)+","+str(value2)+"]"
            plt.title(title)
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    activation = net.activate([i, j, value1, value2])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                    else:
                        # activation[0] == np.float32(0.0) and activation[1] == np.float32(0.0):
                        color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, alpha=0.9, edgecolor = 'none')
                plt.grid(True)
            plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
            plt.savefig(path + title + '.png')

    path = path_net + 'x;h;h;y/'
    for value1 in [50, 100, 150]:
        for value2 in [50, 100, 150]:
            k = k + 1
            plt.figure(k)
            # plt.title("["+str(value)+",50"+",x,"+"y"+"]")
            title = "["+"x"+","+str(value1)+","+str(value2)+","+"y"+"]"
            plt.title(title)
            for i in range(50,500, 5):
                print k," ",i
                for j in range(50, 500, 5):
                    activation = net.activate([i, value1, value2, j])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                    else:
                        # activation[0] == np.float32(0.0) and activation[1] == np.float32(0.0):
                        color = 'black'
                    x = i
                    y = j
                    plt.scatter(x,y,c=color,s = 20, alpha=0.9, edgecolor = 'none')
                plt.grid(True)
            plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
            plt.savefig(path + title + '.png')
    # plt.legend(handles=[red_patch, blue_patch, orange_patch, black_patch])
    # plt.show()


def calculateCapacity(net):
    count1st = 0
    count2nd = 0
    both = 0
    neither = 0
    total = 0
    for x1 in range(0, 500, 20):
        for x2 in range(0, 500, 20):
            for x3 in range(0, 500, 20):
                for x4 in range(0, 500, 20):
                    activation = net.activate([x1, x2, x3, x4])
                    if activation[0] > np.float32(0.0) and activation[1] <= np.float32(0.0):
                        color = 'red'
                        count1st += 1
                        total += 1
                    elif activation[0] <= np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'blue'
                        count2nd += 1
                        total += 1
                    elif activation[0] > np.float32(0.0) and activation[1] > np.float32(0.0):
                        color = 'orange'
                        both += 1
                        total += 1
                    else:
                        color = 'black'
                        neither += 1
                        total += 1
        print 'iteration: ', x1
    count1st = float(count1st)*100/float(total)
    count2nd = float(count2nd)*100/float(total)
    neither = float(neither)*100/float(total)
    both = float(both)*100/float(total)

    print '1st: ', count1st
    print '2nd: ', count2nd
    print 'neither: ', neither
    print 'both', both
    return count1st, count2nd, both, neither


def trained_cat_dog_ANN():
    n = FeedForwardNetwork()
    d = get_cat_dog_trainset()
    input_size = d.getDimension('input')
    n.addInputModule(LinearLayer(input_size, name='in'))
    n.addModule(SigmoidLayer(input_size+1500, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))
    n.sortModules()
    n.convertToFastNetwork()
    print 'successful converted to fast network'
    t = BackpropTrainer(n, d, learningrate=0.0001)#, momentum=0.75)

    count = 0
    while True:
        globErr = t.train()
        print globErr
        count += 1
        if globErr < 0.01:
            break
        if count == 30:
            break


    exportCatDogANN(n)
    return n

def trained_cat_dog_RNN():
    n = RecurrentNetwork()

    d = get_cat_dog_trainset()
    input_size = d.getDimension('input')
    n.addInputModule(LinearLayer(input_size, name='in'))
    n.addModule(SigmoidLayer(input_size+1500, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))
    n.addRecurrentConnection(NMConnection(n['out'], n['hidden'], name='nmc'))
    n.sortModules()

    t = BackpropTrainer(n, d, learningrate=0.0001)#, momentum=0.75)

    count = 0
    while True:
        globErr = t.train()
        print globErr
        count += 1
        if globErr < 0.01:
            break
        if count == 30:
            break

    exportCatDogRNN(n)
    return n
def trained_cat_dog_RFCNN():
    n = RecurrentNetwork()

    d = get_cat_dog_trainset()
    input_size = d.getDimension('input')
    n.addInputModule(LinearLayer(input_size, name='in'))
    n.addModule(SigmoidLayer(input_size+1500, name='hidden'))
    n.addOutputModule(LinearLayer(2, name='out'))
    n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
    n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))
    n.addRecurrentConnection(FullConnection(n['out'], n['hidden'], name='nmc'))
    n.sortModules()

    t = BackpropTrainer(n, d, learningrate=0.0001)#, momentum=0.75)

    count = 0
    while True:
        globErr = t.train()
        print globErr
        count += 1
        if globErr < 0.01:
            break
        if count == 30:
            break

    exportCatDogRFCNN(n)
    return n


def get_class(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        if arr[i] > 0:
            arr[i] = 1
        else:
            arr[i] = 0
    return arr

def run():
    # n = trainedANN()
    # n1 = importANN()
    total_first = []
    total_second = []
    total_both = []
    total_neither = []
    for i in range(10):
        n2 = trainedRNN()
        res = calculateCapacity(n2)
        total_first.append(res[0])
        total_second.append(res[1])
        total_both.append(res[2])
        total_neither.append(res[3])

    print 'first: mean', np.mean(total_first), 'variance', np.var(total_first)
    print 'second: mean', np.mean(total_second), 'variance', np.var(total_second)
    print 'both: mean', np.mean(total_both), 'variance', np.var(total_both)
    print 'neither: mean', np.mean(total_neither), 'variance', np.var(total_neither)
    exit()
    # n2 = importRNN()

    # n = trainedRFCNN()
    # n3 = importRFCNN()
    # draw_graphics(n1, path_net=root.path() + '/Graphics/ANN/')
    # draw_graphics(n2, path_net=root.path() + '/Graphics/RNMNN/')
    # draw_graphics(n3, path_net=root.path() + '/Graphics/RFCNN/')

    # calculateCapacity(n1)
    # calculateCapacity(n3)

    exit()
    # print 'ann:'
    # for x in [(1, 15, 150, 160),    (1, 15, 150, 160),
    #           (100, 110, 150, 160), (150, 160, 10, 15),
    #           (150, 160, 10, 15),   (200, 200, 100, 100),
    #           (10, 15, 300, 250),   (250, 300, 15, 10)]:
    #     print("n.activate(%s) == %s\n" % (x, n.activate(x)))
    # calculateCapacity(n)
    # draw_graphics(n)
    print "hello"
    n = importCatDogANN()
    # exit()
    # n = importCatDogRFCNN()

    # NetworkWriter.writeToFile(n, root.path()+'/res/text.xml')
    # n = NetworkReader.readFrom(root.path()+'/res/text.xml')
    print type(n)
    # exit()
    ds = get_cat_dog_testset()
    for inp, targ in ds:
        activate = n.activate(inp)
        print "activate:", activate, "expected:", targ
    # draw_graphics(n)

# n = 4
# print np.random.random_integers(0, 1, n)
# exit()
# generateTrainingData(saveAfter=True)
if __name__ == "__main__":
    run()

"""
RNN(neuromodulation):
1st:  3095
2nd:  2643229
neither:  28162
both 3575514

RNN(neuromodulation new)
1st:  3533955
2nd:  1977645
neither:  0
both 738400

ANN:
1st:  9803
2nd:  46325
neither:  425659
both 5768213

Recurrent fully connected neural network
1st:  504753
2nd:  555727
neither:  1768
both 5187752
"""