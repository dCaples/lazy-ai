import copy
import random
import math
class Node:
    def __init__(self):
        self.bias = 0.5
        self.weight = 1
        self.value = 0
    def calc_output(self, node_input):
        self.value = self.sigmoid(node_input+self.bias)*self.weight
        return(self.value)
    def calc_output_no_sigmoid(self, node_input):
        self.value = self.weight*(node_input+self.bias)
        return(self.value)
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    def randomize(self, max_bias_change, max_weight_change):
        change = random.uniform(max_bias_change*-1,max_bias_change)
        self.bias = self.bias + change
        change = random.uniform(max_weight_change*-1, max_weight_change)
        self.weight = self.weight+change

class Layer:
    def __init__(self, layer_size):
        self.layer_total = 0
        self.nodes_in_layer = []
        for x in range(layer_size):
            self.nodes_in_layer.append(Node())
    def get_layer_total(self, layer_input):
        self.layer_total = 0
        for x in range(len(self.nodes_in_layer)):
            self.layer_total = self.layer_total+self.nodes_in_layer[x].calc_output(layer_input)
        return(self.layer_total)
    def get_layer_total_from_array(self, input_array):
        self.layer_total = 0
        for x in range(len(input_array)):
            self.nodes_in_layer[x].calc_output_no_sigmoid(input_array[x])
            self.layer_total = self.layer_total+self.nodes_in_layer[x].value
        return(self.layer_total)
    def randomize_layer(self, max_bias_change, max_weight_change):
        for x in range(len(self.nodes_in_layer)):
            self.nodes_in_layer[x].randomize(max_bias_change, max_weight_change)
    def get_largest_output(self):
        largest_output = self.nodes_in_layer[0]
        largest_output_position = 0
        for x in range(len(self.nodes_in_layer)):
            if(self.nodes_in_layer[x].value>largest_output.value):
                largest_output = self.nodes_in_layer[x]
                largest_output_position = x
        return(largest_output_position)
    def print_data(self):
        print("printing outputs!")
        for x in range (len(self.nodes_in_layer)):
            print("the value of ", x,"is ", self.nodes_in_layer[x].value)
            print(x, self.nodes_in_layer[x].value)

class Network:
    def __init__(self, layers_to_create):
        self.reward = 0
        self.layers_array = []
        self.output = 0
        for x in range(len(layers_to_create)):
            self.layers_array.append(Layer(layers_to_create[x]))
    def randomize_network(self, max_bias_change, max_weight_change):
        for x in range(len(self.layers_array)):
            self.layers_array[x].randomize_layer(max_bias_change, max_weight_change)
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
    def __init__(self, layers_to_create, networks_in_evolution):
        self.networks = []
        self.best_network = None
        for x in range(networks_in_evolution):
            self.networks.append(Network(layers_to_create))
    def randomize(self, max_bias_change, max_weight_change):
        for x in range(len(self.networks)):
            self.networks[x].randomize_network(max_bias_change, max_weight_change)
    def learn(self, input, desired_output):
        self.best_network = self.networks[0]
        best_network_pos = 0
        #calculate each and reward them based on how good they performed
        for x in range(len(self.networks)):
            self.networks[x].reward = 3 - abs(desired_output - self.networks[x].calculate(input))
        #find the one with the most reward and set it to the best
        for x in range(len(self.networks)):
            if(self.networks[x].reward>self.best_network.reward):
                self.best_network = self.networks[x]
                best_network_pos = x

        for x in range(len(self.networks)):
            self.networks[x] = copy.deepcopy(self.best_network)

        #randomize


EvolutionTest = Evolution([3,3,3], 3)
EvolutionTest.randomize(.1,.1)
EvolutionTest.learn([0,0,1],2)
for x in range(50):
    EvolutionTest.learn([0,0,1],2)
    EvolutionTest.randomize(.01,.01)
print(EvolutionTest.best_network.calculate([0,0,1]))
