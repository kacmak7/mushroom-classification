import numpy as np
import pandas as pd
import configparser

data = pd.read_csv('data.csv',header=None).to_numpy()
# X = (hours sleeping, hours studying), y = score on test
X = data[:,:2]
y = data[:,2:]

# normalize data
X = X/np.amax(X, axis=0) # maximum of X array
y = y/100 # max test score is 100

class Neural_Network:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        layers = config['layers']
        # 3 layers
        self.inputSize = int(layers.get('inputSize'))
        self.hiddenSize = int(layers.get('hiddenSize'))
        self.outputSize = int(layers.get('outputSize'))
        # weights, random at the beginning
        self.weights1 = np.random.rand(self.inputSize,self.hiddenSize)
        self.weights2 = np.random.rand(self.hiddenSize,self.outputSize)

    def forward(self, X):
        self.hidden = np.dot(X,self.weights1)
        print(self.hidden)
        self.activated_hidden = self.sigmoid(self.hidden)
        print()
        self.output = np.dot(self.activated_hidden,self.weights2)
        self.activated_output = self.sigmoid(self.output)
        print(self.activated_hidden)
        print(self.activated_output)
        return self.activated_output

    def backward(self,X,y,output):
        self.output_error = y - output
        self.output_delta = self.output_error*self.sigmoidPrime(output)

        self.hidden_error = self.output_delta.dot(self.weights2.T)
        self.hidden_delta = self.hidden_error*self.sigmoidPrime(self.hidden)

        self.weights1 += X.T.dot(self.hidden_delta)
        self.weights2 += self.hidden.T.dot(self.output_delta)
    
    def train(self, X, y, epochs = 100):
        for i in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)

    def sigmoid(self,s):
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self,s):
        return s*(1-s)

nn = Neural_Network()
nn.train(X, y)

#test 
nn.forward(X)
print('input')
print(X)
print('output')
print(nn.output)
print('expected output')
print(y)