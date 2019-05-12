import numpy as np
import pandas as pd
import configparser

data = pd.read_csv('data.csv').to_numpy()
# X = (hours sleeping, hours studying), y = score on test
X = data[:,:2]
y = data[:,2:]

# normalize data
X = X/np.amax(X, axis=0) # maximum of X array
y = y/100 # max test score is 100

class Neural_Network(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        layers = config['layers']
        # layers
        self.inputSize = int(layers.get('inputSize'))
        self.hiddenSize = int(layers.get('hiddenSize'))
        self.outputSize = int(layers.get('outputSize'))
        # weights, random at the beginning
        self.weights1 = np.random.rand(self.inputSize,self.hiddenSize)
        self.weights2 = np.random.rand(self.hiddenSize,self.outputSize)

    def forward(self, X):
        self.hidden = np.dot(X,self.weights1)
        self.activated_hidden = self.sigmoid(self.hidden)
        print(self.activated_hidden)
        self.output = np.dot(self.activated_hidden,self.weights2)
        self.activated_output = self.sigmoid(self.output)
        print(self.activated_output)
        return self.activated_output

    def sigmoid(self, s):
        return 1/(1+np.exp(-s))

if __name__ == '__main__':
    nn = Neural_Network()
    nn.forward(X)

