'''
Created on Feb 2, 2015
@author: kamil
'''
from numpy import floor, empty, array
from pybrain.datasets import SupervisedDataSet
from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.structure.networks.feedforward import FeedForwardNetwork
from pybrain.supervised import BackpropTrainer
import pickle
import random

class MLP:

    data = SupervisedDataSet
    net = FeedForwardNetwork

    def generate_training_set(self):
        random.seed()
        ind = floor(empty((2000,4)))
        outd = floor(empty((2000, 2)))

        res = array((ind,outd))

        print ind
        print
        print outd
        print
        print res

        for i in range(2000):
            n = random.getrandbits(1)
            if n == 0:
                a = random.randint(0,100)
                b = random.randint(0,100)
                c = random.randint(100,5000)
                d = random.randint(100,5000)
                res[0][i][0] = a
                res[0][i][1] = b
                res[0][i][2] = c
                res[0][i][3] = d

                res[1][i][0] = 0
                res[1][i][1] = 1

            else:
                a = random.randint(100,5000)
                b = random.randint(100,5000)
                c = random.randint(0,100)
                d = random.randint(0,100)
                res[0][i][0] = a
                res[0][i][1] = b
                res[0][i][2] = c
                res[0][i][3] = d

                res[1][i][0] = 1
                res[1][i][1] = 0

        for i in range(2000):
            print res[0][i][0],res[0][i][1],res[0][i][2],res[0][i][3], " out", res[1][i][0],res[1][i][1]
        return res


    def make_dataset(self):
        """
        Creates a set of training data with 2-dimensioanal input and 2-dimensional output
        So how dataset have to be looks like?
        """
        self.data = SupervisedDataSet(4,2)

        self.data.addSample((1,1,150,150),(0,1))
        self.data.addSample((1,1,199,142),(0,1))
        self.data.addSample((150,120,43,12),(1,0))
        self.data.addSample((198,123,54,65),(1,0))

        return self.data


    def training(self,d):
        """
        Builds a network ,trains and returns it
        """

        self.net = FeedForwardNetwork()

        inLayer = LinearLayer(4) # 4 inputs
        hiddenLayer = SigmoidLayer(3) # 5 neurons on hidden layer with sigmoid function
        outLayer = LinearLayer(2) # 2 neuron as output layer


        "add layers to NN"
        self.net.addInputModule(inLayer)
        self.net.addModule(hiddenLayer)
        self.net.addOutputModule(outLayer)

        "create connections"
        in_to_hidden = FullConnection(inLayer, hiddenLayer)
        hidden_to_out = FullConnection(hiddenLayer, outLayer)

        "add connections"
        self.net.addConnection(in_to_hidden)
        self.net.addConnection(hidden_to_out)

        "some unknown but necessary function :)"
        self.net.sortModules()

        print self.net

        "generate big sized training set"
        trainingSet = SupervisedDataSet(4,2)

        random.seed()
        trainArr = self.generate_training_set()
        for ri in range(2000):
            input = ((trainArr[0][ri][0],trainArr[0][ri][1],trainArr[0][ri][2],trainArr[0][ri][3]))
            target = ((trainArr[1][ri][0],trainArr[1][ri][1]))
            trainingSet.addSample(input, target)

        "create backpropogation trainer"
        t = BackpropTrainer(self.net,d,learningrate=0.00001, momentum=0.99)
        while True:
            globErr = t.train()
            print "global error:", globErr
            if globErr < 0.0001:
                break

        return self.net


    def test(self,trained):
        """
        Builds a new test dataset and tests the trained network on it.
        """
    #     print "[5,6,123,156] ->", trained.activate((5,6,123,156))
    #     print "[46,68,199,163] ->", trained.activate((46,68,199,163))
    #     print "[134,101,99,99] ->", trained.activate((134,101,99,99))
    #     print "[105,188,65,55] ->", trained.activate((105,188,65,55))

        testArr = self.generate_training_set()
        for i in range(2000):
            print floor(testArr[0][i]),floor(testArr[1][i])

    #     print "[0,1] ->", trained.activate((0,1))
    #     print "[1,0] ->", trained.activate((1,0))
    #     print "[1,1] ->", trained.activate((1,1))

    def exportWeights(self, fileName):
        fileObject = open(fileName, 'w')
        pickle.dump(self.net, fileObject)
        fileObject.close()

    def importWeights(self, fileName):
        fileObject = open(fileName, 'r')
        self.net = pickle.load(fileObject)
        fileObject.close()
        return self.net

    def run(self):

        import __root__

        """
        Use this function to run build, train, and test your neural network.
        """

        trained = self.importWeights(__root__.path()+'/res/weights')
        self.test(trained)

mlp = MLP()
mlp.run()