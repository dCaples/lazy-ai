import random
import math
#nuron class
class Nuron:
    def __init__(self):
        self.bias = 0.5
        self.value = 0
    def calc_output(self, input):
        biased_input = input*self.bias
        self.value = self.sigmoid(biased_input)
        return(self.value)
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    def randomize(self, max_change):
        change = random.uniform(max_change*-1,max_change)
        self.bias = self.bias + change

class Layer:
    def __init__(self, layer_size):
        self.layer_total = 0
        self.nurons_in_layer = []
        for x in range(layer_size):
            self.nurons_in_layer.append(Nuron())
    def get_layer_total(self, layer_input):
        self.layer_total = 0
        for x in range(len(self.nurons_in_layer)):
            self.layer_total = self.layer_total+self.nurons_in_layer[x].calc_output(layer_input)
        return(self.layer_total)

    def randomize_layer(self, max_change):
        for x in range(len(self.nurons_in_layer)):
            self.nurons_in_layer[x].randomize(max_change)

TestLayer = Layer(5)
TestLayer.randomize_layer(.5)
print(TestLayer.get_layer_total(10))
TestNode = Nuron()
TestNode.bias = -10
print(TestNode.calc_output(1))
