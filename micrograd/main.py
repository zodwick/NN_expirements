from graphviz import Source,Digraph
import math

class Value:
    def __init__(self,data,_children=(),op="",label=""):
        
        # if list then multiple pointers to same child may occur : not needed???
        
        self.data=data
        self._gradient=lambda:None
        self._prev=set(_children)
        self.grad=0
        self._op=op
        self.label=label
        
    def __repr__(self) -> str:
        return f"Value({self.data})"
    
    def __add__(self,second):
        out= Value(self.data+second.data,(self,second),"+")
        def _gradient():
            self.grad=1*out.grad
            second.grad=1*out.grad
            
        out._gradient=_gradient
        #calling function to calculate gradient of output wrt self and second storing in grad attribute of self and second
        return out
    
    def __mul__(self,second):
        out= Value(self.data*second.data,(self,second),"*")
        def _gradient():
            self.grad=second.data*out.grad
            second.grad=self.data*out.grad
        out._gradient=_gradient
        return out   


    def backpropogate(self):
      topo_list=[]
      self.grad=1

      def build_backprop_list(x:Value):
        visited=set()
        for children in x._prev:
          if children not in visited:
            visited.add(children)
            build_backprop_list(children)
        topo_list.append(x)

      build_backprop_list(self)
      for node in reversed(topo_list):
          node._gradient()

      
              
    # def __pow__(self,second):
    #     return Value(self.data**second.data,(self,second),"**")
    
    # def __sub__(self,second):
    #     return Value(self.data-second.data, (self,second),"-")

    
    def tanh(self):
        
        x=self.data
        t=(math.exp(2*x)-1)/( math.exp(2*x)+1)
        out=Value(t,(self,),"tanh")
        def _gradient():
            self.grad=(1-t**2)*out.grad
            
        out._gradient=_gradient
        return out


#input nodes
x1=Value(2.0,label="x1")
x2=Value(0.0,label="x2")

#weights
w1=Value(-3.0,label="w1")
w2=Value(1.0,label="w2")

# bias of neuron
b=Value(6.88137,label="b")

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
o.label="o"
o.backpropogate()


print(x1.grad)