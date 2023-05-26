
from visualiser import draw_dot
from graphviz import Source,Digraph
import math

class Value:
    def __init__(self,data,_children=(),op="",label=""):
        
        # if list then multiple pointers to same child may occur : not needed???
        
        self.data=data
        self._prev=set(_children)
        self._op=op
        self.label=label
        
    def __repr__(self) -> str:
        return f"Value({self.data})"
    
    def __add__(self,second):
        return Value(self.data+second.data,(self,second),"+")
    
    def __mul__(self,second):
        return Value(self.data*second.data,(self,second),"*")
    
    def __pow__(self,second):
        return Value(self.data**second.data,(self,second),"**")
    
    def __sub__(self,second):
        return Value(self.data-second.data, (self,second),"-")
    
    def tanh(self):
        x=self.data
        t=(math.exp(2*x)-1)/( math.exp(2*x)+1)
        out=Value(t,(self,),"tanh")
        return out

#input nodes
x1=Value(3.0,label="x1")
x2=Value(4.0,label="x2")

#weights
w1=Value(-3.0,label="w1")
w2=Value(5.0,label="w2")

# bias of neuron
b=Value(8.0,label="b")

# x1*w1+x2*w2+b (sigma xi*wi+b) where b is bias

x1w1=x1*w1
x1w1.label="x1w1"

x2w2=x2*w2
x2w2.label="x2w2"

x1w1x2w2=x1w1+x2w2
x1w1x2w2.label="x1w1x2w2"

n=x1w1x2w2+b
n.label="n"
o=n.tanh()
draw_dot(o)