import random
import math
#nuron class
class node:
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
nuron = node()
nuron.randomize(3)
