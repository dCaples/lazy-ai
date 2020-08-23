import random
import math
class Nuron:
    def __init__(self):
        self.bias = 0.5
        self.value = 0
    def calc_output(self, node_input):
        self.value = self.sigmoid(node_input)+self.bias
        return(self.value)
    def calc_output_no_sigmoid(self, node_input):
            self.value = node_input+self.bias
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
    def get_layer_total_from_array(self, input_array):
        self.layer_total = 0
        for x in range(len(input_array)):
            self.nurons_in_layer[x].calc_output_no_sigmoid(input_array[x])
            self.layer_total = self.layer_total+self.nurons_in_layer[x].value
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
    def print_data(self):
        print("printing outputs!")
        for x in range (len(self.nurons_in_layer)):
            print("the value of ", x,"is ", self.nurons_in_layer[x].value)
            print(x, self.nurons_in_layer[x].value)

class Brain:
    def __init__(self, layers_to_create):
        self.reward = 0
        self.layers_array = []
        self.output = 0
        for x in range(len(layers_to_create)):
            self.layers_array.append(Layer(layers_to_create[x]))
    def randomize_brain(self, max_change):
        for x in range(len(self.layers_array)):
            self.layers_array[x].randomize_layer(max_change)
    def print_layers(self):
        for x in range(len(self.layers_array)):
            self.layers_array[x].print_data()
    def calculate(self, input_data):
        self.layers_array[0].get_layer_total_from_array(input_data)
        for x in range(len(self.layers_array)):
           # dont do this for the first one, which we allready calculated
            if(x == 0):
                continue
            #get the layer total of the previous layer and calculate this one
            self.layers_array[x].get_layer_total(self.layers_array[x-1].layer_total)
        self.output = self.layers_array[-1].get_largest_output()
        return self.output
class Evolution:
    def __init__(self, layers_to_create, brains_in_evolution):
        for x in range(brains_in_evolution):
            print("hello:")
BrainTest = Brain([3,3,3])
BrainTest.randomize_brain(0.5)
print(BrainTest.calculate([1,0,0]))
