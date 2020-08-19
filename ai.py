import random
import math
class Nuron:
    def __init__(self):
        self.bias = 0.5
        self.value = 0
    def calc_output(self, node_input):
        self.value = self.sigmoid(node_input)+self.bias
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
    def get_largest_output(self):
        largest_output = self.nurons_in_layer[0]
        largest_output_position = 0
        for x in range(len(self.nurons_in_layer)):
            if(self.nurons_in_layer[x].value>largest_output.value):
                largest_output = self.nurons_in_layer[x]
                largest_output_position = x
        return(largest_output_position)
    def print_outputs(self):
        for x in range (len(self.nurons_in_layer)):
            print(x, self.nurons_in_layer[x].value)

class Brain:
    def __init__(self, hidden_layers, nodes_in_layer, end_layer_nodes):
        pass
LayerTest = Layer(3)
LayerTest.randomize_layer(0.5)
LayerTest.get_layer_total(4)
LayerTest.print_outputs()
print(LayerTest.get_largest_output())
