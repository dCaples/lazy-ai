import math
#nuron class
class node:
    def __init__(self):
        self.bias = 0.5
        self.value = 0
    def calc_output(self, input):
        biased_input = input*self.bias 
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
nuron = node()
nuron.calc_output(2)
