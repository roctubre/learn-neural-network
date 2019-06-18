import numpy as np


class Node():
    def __init__(self, params=[]):
        self.in_nodes = params
        self.value = 0
        
    def forward(self):
        return NotImplementedError
       
    def backward(self):
        return NotImplementedError        

class Input_Node(Node):
    def __init__(self, value = 0):
        Node.__init__(self, value)
        self.value = value
    
    #def forward(self, value):
    #    this.value = value

        
class Linear(Node):
    def __init__(self, inputs, weights, bias):
        Node.__init__(self, [inputs, weights, bias])
        
    def forward(self):
        inputs = np.array([x.value for x in self.in_nodes[0]])
        weights = np.array([w.value for w in self.in_nodes[1]])
        bias = self.in_nodes[2].value
        self.value = bias + np.sum(inputs*weights)
        

if __name__ == "__main__":
    a, b = Input_Node(4), Input_Node(3)
    w1, w2 = Input_Node(4), Input_Node(3)
    bias = Input_Node(1)
    inputs = [a, b]
    weights = [w1, w2]
    lin = Linear(inputs, weights, bias)
    lin.forward()
    print(lin.value)
    
    print("End.")