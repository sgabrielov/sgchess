# -*- coding: utf-8 -*-

import bitstring
import random
import numpy as np
import pickle

# NEURAL NETWORK CONFIGURATION

# Number of nodes in each of the columns
COL_NODES = [808,16,1]

# Number of nodes in output column
OUT_NODES = 1

# END CONFIGURATION


class NeuralNet:
    """
    The class which represents operations for the neural network

    ...

    Attributes
    ----------


    Methods
    -------

    """
    
    node_list = []
    biases = []
    
    #def __init__(self):
        
       
        
        
    def loadinputbits(self, inbits: bitstring.BitArray):
        
        self.node_values = []
        self.z_values = []
        
        if(len(inbits)!=COL_NODES[0]):
            raise ValueError("Expected %d input bits, received %d" % (COL_NODES[0], len(inbits)))
            
        self.node_values.append(np.array(inbits))
        
        
    def loadeval(self, position_eval:float = 0):
        
        self.position_eval = position_eval
        if(self.position_eval > 10):
            self.position_eval = 10
        if(self.position_eval < -10):
            self.position_eval = 10
            
    def loadweights(self, filename:str):
        with open(filename, 'rb') as fp:
            self.node_list = pickle.load(fp)
                
    def loadbiases(self, filename:str):
        with open(filename, 'rb') as fp:
            self.biases = pickle.load(fp)
        
    def saveweights(self, filename:str):
        with open(filename, 'wb') as fp:
            pickle.dump(self.node_list, fp)
            print("saved to %s" % (filename))
        
    def savebiases(self, filename:str):
        with open(filename, 'wb') as fp:
            pickle.dump(self.biases, fp)
            print("saved to %s" % (filename))
        
    def processrow(self, row: list):
                
        self.loadinputbits(bitstring.BitArray(row[0][2]))
        
        self.loadeval(row[0][3])        
        
            
    def getintputbits(self):
        return self.node_values[0].bin
    
    def geteval(self):
        return self.position_eval
        
    def initializeweights(self, zeroinit:bool = False):
        
        
        randmin = -1
        randmax = 1
        
        # A list of numpy arrays representing the biases of each node
        blist = []
                
        # A temporary variable that will be used to store a weights matrix, in numpy array form
        mlist = []
        
        # A list of numpy arrays representing the node values for every column
        nlist = []
             
        
        
        # Create a new numpy object that will store the weights matrix and biases array for the interactions
        # between the input layer and first hidden layer

        # Add these numpy objects to lists for storage
        
        ### FOR MEMORY SAVINGS ###
        # Load only one weights and biases matrix at a time from disk
        
        ### INPUT LAYER <-----> FIRST HIDDEN LAYER ###
        
        # mlist.append(np.empty((COL_NODES[0], IN_NODES)))
        # blist.append(np.empty(COL_NODES[0]))
        
        # print(np.shape(mlist[0]))
        # print(np.shape(blist[0]))

        
        # for i in range(COL_NODES[0]):
        #     blist[0][i] = self.getrandom()
        #     for j in range(IN_NODES):
        #         mlist[0][i][j] = self.getrandom()
                
                
        
        # ### HIDDEN LAYER <-----> HIDDEN LAYER ###
        
        # for i in range(1, NUMCOLS):
            
        #     mlist.append(np.empty((COL_NODES[i], COL_NODES[i-1])))
        #     blist.append(np.empty(COL_NODES[i]))
            
        #     for j in range(COL_NODES[i]):
        #         blist[i][j] = self.getrandom()
        #         for k in range(COL_NODES[i-1]):
        #             mlist[i][j][k] = self.getrandom()
                    
        # ### LAST HIDDEN LAYER <-----> OUTPUT LAYER ###
        
        # mlist.append(np.empty((OUT_NODES, COL_NODES[NUMCOLS-1])))
        # blist.append(np.empty(OUT_NODES))
        
        # for i in range(OUT_NODES):
        #     blist[NUMCOLS][i] = self.getrandom()
        #     for j in range(COL_NODES[NUMCOLS-1]):
        #         mlist[NUMCOLS][i][j] = self.getrandom()
        
        # Initialize all weights and bises with random values
        
        for i in range(len(COL_NODES)-1):
            mlist.append(np.empty((COL_NODES[i+1], COL_NODES[i])))
            blist.append(np.empty(COL_NODES[i+1]))
            
            for j in range(COL_NODES[i+1]):
                blist[i][j] = self.getrandom()
                for k in range(COL_NODES[i]):
                    mlist[i][j][k] = self.getrandom()
        
        
        self.node_list = mlist       
        self.biases = blist
                
        
                
    def getrandom(self, randmin:int = -1, randmax:int = 1, zeroinit:bool = False):
        if(zeroinit):
            return 0
        else:
            return random.random() * (randmax - randmin) + randmin
    
    def printweights(self):
        
        # print("Hidden column 1:")
        # for i in range(COL_NODES[0]):
        #     for j in range(IN_NODES):
        #         print("HC%d   %f   IN%d" % (i+1, self.node_list[0][i][j], j+1))
        #     print("HC%d bias: %f" % (i+1, self.biases[0][i]))
        
        # for i in range(1, NUMCOLS):
        #     print("Hidden column %d" % (i+1))
        #     for j in range(COL_NODES[i]):
        #         for k in range(COL_NODES[i-1]):
        #             print("HC%d   %f   HC%d" % (j+1, self.node_list[i][j][k], k+1))
        #         print("HD%d bias: %f" % (j+1, self.biases[0][j]))
        
        # print("Output Column:")            
        # for i in range(OUT_NODES):
        #     for j in range(COL_NODES[NUMCOLS-1]):
        #         print("OC%d   %f   HC%d" % (i+1, self.node_list[NUMCOLS][i][j], j+1))
        #     print("OC%d bias: %f" % (i+1, self.biases[NUMCOLS][i]))
        
        for i in range(0, len(COL_NODES)-1):
            print("Column %d" % (i))
            for j in range(COL_NODES[i+1]):
                for k in range(COL_NODES[i]):
                    print("Node%d   %f   Node%d" % (j+1, self.node_list[i][j][k], k+1))
    
    # Processes the calculations of the columns, weights, biases of the network
    # Returns the output vector of the network    
    
    def feedforward(self, input_vector:np.ndarray, weights:np.ndarray, biases:np.ndarray):
        
        for w, b in zip(weights, biases):
            z = self.getz(w, input_vector, b)
            input_vector = self.sigmafy(z)
            self.z_values.append(z)
            self.node_values.append(input_vector)
        
        #print(self.node_values)
        return input_vector
    
    def expandoutput(self, outputnode:np.array):
        
        mineval = -10
        maxeval = 10
        
        
        return outputnode[0] * (maxeval - mineval) + mineval
    
    def compressoutput(self, outputnode:np.array):
        mineval = -10
        maxeval = 10
        
        return (outputnode - mineval) / (maxeval - mineval)
        
    def calcoutput(self):        
              
        self.output_value = self.expandoutput(self.feedforward(self.node_values[0], self.node_list, self.biases))
        
                    
    def sigmafy(self, x:np.float64):
        
        return 1 / (1 + (1/np.exp(x)))
        
    def dsigmafy(self, x:float):
        
        return (self.sigmafy(x) * (1 - self.sigmafy(x)))
    
    def dCda(self, a:float, y:float):
        
        return 2 * (a - self.compressoutput(y))
    
    def dadz(self, z:float):
        
        return self.dsigmafy(z)
    
    def dzdw(self, w:float):
        
        return w
    
    def dCdw(self, next_node:float, last_node:float, y:float, w:float, b:float):
        return self.dzdw(last_node) * self.dsigmafy(next_node*w+b)*self.dCda(next_node, y)
    
    def dCdb(self, next_node:float, last_node:float, y:float, w:float, b:float):
        return self.dsigmafy(next_node*w+b)*self.dCda(next_node, y) 
    
    def getz(self, weight:np.ndarray, node:np.ndarray, bias:np.ndarray):
        return np.dot(weight, node) + bias
    
    def backpropagate(self):
        
        #print(self.node_list[0])
        gradients = []
        bias_gradients = []
        sumgradients = 0
        sumbiases = 0
        sumofdeltas = 0
        delta = 0
        
        dCda_values = []
        
        
        for i in range(len(COL_NODES)-1):
            gradients.append(np.empty((COL_NODES[i+1], COL_NODES[i])))
            dCda_values.append(np.empty((COL_NODES[i+1])))
            bias_gradients.append(np.empty(COL_NODES[i+1]))
        for i in range(len(self.node_list)-1, -1, -1):
            #print("i: %d " % (i))
            for j in range(len(self.node_list[i])):
                #print("j: %d " % (j), end='')
                if(i == len(self.node_list)-1):
                    #print(dCda_values)
                    dCda_values[i][j] = self.dCda(self.node_values[i+1][j], self.position_eval)
                    #print(self.output_value)
                    #print("dCda_values[%d][%d] = 2(%f - %f) = %f" % (i,j,self.node_values[i+1][j], self.position_eval, dCda_values[i][j]))
                else:
                    delta = 0
                    
                    for jj in range(len(gradients[i+1])):     
                        # print("jj:%d " % (jj), end='')
                        # print(dCda_values[i+1][jj])
                        # print(self.dsigmafy(self.z_values[i+1][jj]))
                        # print(self.node_list[i+1][jj][j])
                        # print("########################")
                        
                        delta += dCda_values[i+1][jj] * self.dadz(self.z_values[i+1][jj]) * self.node_list[i+1][jj][j]
                        #print("delta += %f * %f * %f = %f" % (dCda_values[i+1][jj], self.dadz(self.z_values[i+1][jj]), self.node_list[i+1][jj][j], delta))
                        #print("delta: %f" % (delta))
                    dCda_values[i][j] = delta
                    #print("dCda_values[%d][%d] = %f" % (i,j,dCda_values[i][j]))
                    
                    #print(dCda_values)
                bias_gradients[i][j] =  dCda_values[i][j] * self.dadz(self.z_values[i][j])  
                sumbiases += abs(bias_gradients[i][j])
                for k in range(len(self.node_list[i][j])):
                    #print("k:%d " % (k), end='')
                    # print(self.dCda(self.node_values[i+1][j], self.position_eval))
                    # print(self.dsigmafy(self.z_values[i][j]))
                    # print(self.node_values[i][k])
                    # print("########################")
                    #print("gradients[%d][%d][%d] = %f * %f * %f" % (i,j,k,dCda_values[i][j], self.dadz(self.z_values[i][j]), self.node_values[i][k]))
                    gradients[i][j][k] = dCda_values[i][j] * self.dadz(self.z_values[i][j]) * self.node_values[i][k]
                    sumgradients += abs(gradients[i][j][k])
            #print()       
            self.node_list[i] -= gradients[i]
            self.biases[i] -= bias_gradients[i]
        #print(self.node_values)
        #print(dCda_values)
        #print(self.z_values)
        
        #print(bias_gradients)
        #print(gradients)
        
        #print(self.node_list)
        #print(self.biases)
        #print(sumbiases + sumgradients, end=' : ')
        #print(self.output_value - self.position_eval, end=' : ')
        #print((self.output_value - self.position_eval)/(sumbiases + sumgradients))
        #print(self.node_list)
                    
        
        
        # for i in range(len(self.node_values[len(self.node_values)-1])):
        #     delta = delta + self.dCda(self.node_values[len(self.node_values)-1][i], self.position_eval)
        
        # for i in range(len(COL_NODES)-1, 0, -1):
        #     for j in range(COL_NODES[i-1]):
        #         #bias_gradients[i][j] = self.dCdb(self.node_values[i][j], self.node_values[i-1][j], self.position_eval, self.node_list[i][j][k], self.biases[i][j])
        #         for k in range(COL_NODES[i]):
        #             #tmp = delta * self.dadz(self.node_list[i][j] * self.node_values[i][j] + self.biases[j]) * self.dzdw(self.node_list[i][k])
        #             tmp = delta * self.dadz(self.node_list[i-1][0])
                    

        #             sumofdeltas = sumofdeltas + tmp
        #             #gradients[i][j][k] = self.bias_gradients[i][j] * self.dzdw(last_node)
         
        #print(gradients)
        #print(bias_gradients)
    #     for i in range(0, len(COL_NODES)-1):
    #         gradients.append(np.empty((COL_NODES[i+1], COL_NODES[i])))
    #         bias_gradients.append(np.empty(COL_NODES[i+1]))
                
    #     print(gradients)
        
        
    #     # for i in range(len(COL_NODES)-1, 0 ,-1):
    #     #     for j in range(COL_NODES[i-1]):
    #     #         for k in range(COL_NODES[i]):
    #     #             sumofdeltas = 0
    #     #             for in range(COL_NODES[i]):
    #     #                 delta = 
    #     #             delta = self.dCda()
    #     #             sumofdeltas += delta
    #     #             gradients[i][j][k] = delta
                
        
    #     # sumofdeltas = 0
    #     # delta = 1
    #     # for i in range(COL_NODES[NUMCOLS-1]):
    #     #     for j in range(OUT_NODES):
    #     #         delta = self.dCda(self.node_list[NUMCOLS][i][j], self.position_eval) * self.dadz(node_list[NUMCOLS-1][i])
                
    #     #     gradient_vectors[NUMCOLS-1][i] = sumofdeltas
        
        
        
    def getoutput(self):
        return self.output_value