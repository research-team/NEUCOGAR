'''
Created on Feb 2, 2015
@author: kamil
'''
from numpy import floor, empty, array, zeros, set_printoptions, nan
import numpy as np
from pybrain.datasets import SupervisedDataSet
from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.structure.networks.feedforward import FeedForwardNetwork
from pybrain.supervised import BackpropTrainer
import pickle
import random
import matplotlib.pyplot as plt

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

    def getFullDataSet(self):
        res = zeros((50**4, 4))
        a = 0
        b = 0
        c = 0
        d = 0
        for i in range(len(res)):
            if (a % 50 == 0):
                a = 0
            a = a + 1
            if (i % 2 == 0):
                if (b % 50 == 0):
                    b = 0
                b = b + 1

            if (i % 4 == 0):
                if (c % 50 == 0):
                    c = 0
                c = c + 1
            if (i % 8 ==0):
                if (d % 50 == 0):
                    d = 0
                d = d + 1
            res[i][0] = a
            res[i][1] = b
            res[i][2] = c
            res[i][3] = d

        res += 75

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

        testArr = self.generate_training_set()
        for i in range(2000):
            print floor(testArr[0][i]),floor(testArr[1][i])


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
        # self.test(trained)
        # return
        import matplotlib.pyplot as plt

        value = 150
        plt.figure(1)
        plt.title("["+str(value)+",50"+",x,"+"y"+"]")
        for i in range(50,500, 5):
            print i
            for j in range(50, 500, 5):
                color = 'black'

                if np.around(trained.activate([value,50,i,j]))[0] == np.float32(1.0):
                    color = 'red'
                else:
                    color = 'blue'

                x = i
                y = j
                plt.scatter(x,y,c=color,s = 20, label = color, alpha=0.9, edgecolor = 'none')
        plt.grid(True)

        plt.figure(2)
        plt.title("["+str(value)+",100"+",x,"+"y"+"]")
        for i in range(50,500, 5):
            print i
            for j in range(50, 500, 5):
                color = 'black'

                if np.around(trained.activate([value,100,i,j]))[0] == np.float32(1.0):
                    color = 'red'
                else:
                    color = 'blue'

                x = i
                y = j
                plt.scatter(x,y,c=color,s = 20, label = color, alpha=0.9, edgecolor = 'none')
        plt.grid(True)

        plt.figure(3)
        plt.title("["+str(value)+",150"+",x,"+"y"+"]")
        for i in range(50,500, 5):
            print i
            for j in range(50, 500, 5):
                color = 'black'

                if np.around(trained.activate([value,150,i,j]))[0] == np.float32(1.0):
                    color = 'red'
                else:
                    color = 'blue'

                x = i
                y = j
                plt.scatter(x,y,c=color,s = 20, label = color, alpha=0.9, edgecolor = 'none')
        plt.grid(True)

        plt.show()



mlp = MLP()
mlp.run()