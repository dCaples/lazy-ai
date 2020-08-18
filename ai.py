import random
import math
#nuron class
class Node:
    def __init__(self):
        self.bias = 0.5
        self.value = 0
    def calc_output(self, input):
        biased_input = input*self.bias
        self.value = self.sigmoid(biased_input)
        print(self.value)
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    def randomize(self, max_change):
        change = random.uniform(max_change*-1,max_change)
        self.bias = self.bias + change

class Layer:
    def __init__(self, layer_size):
        for x in range(layer_size):
            print(x)
TestLayer = Layer(3)

