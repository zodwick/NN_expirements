from graphviz import Source, Digraph
import math


class Value:
    def __init__(self, data, _children=(), op="", label=""):

        # if list then multiple pointers to same child may occur : not needed???

        self.data = data
        self._gradient = lambda: None
        self._prev = set(_children)
        self.grad = 0
        self._op = op
        self.label = label

    def __repr__(self) -> str:
        return f"Value({self.data})"

    def __add__(self, other):

        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.data+other.data, (self, other), "+")

        def _gradient():
            self.grad += 1*out.grad
            other.grad += 1*out.grad

        out._gradient = _gradient
        # calling function to calculate gradient of output wrt self and other storing in grad attribute of self and other
        return out

    def __sub__(self, other):
        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.data+other.data, (self, other), "+")

        def _gradient():
            self.grad += 1*out.grad
            other.grad += (-1*out.grad)

        out._gradient = _gradient
        # calling function to calculate gradient of output wrt self and other storing in grad attribute of self and other
        return out

    def __mul__(self, other):
        print(self, other)
        if not isinstance(other, Value):
            other = Value(other)
        out = Value(self.data*other.data, (self, other), "*")

        def _gradient():
            self.grad += other.data*out.grad
            other.grad += self.data*out.grad
        out._gradient = _gradient
        return out

    def __rmul__(self, other):
        print(self, other)
        # a is self and 2 is other
        return self*other

    def backpropogate(self):
        topo_list = []
        self.grad = 1

        def build_backprop_list(x: Value):
            visited = set()
            for children in x._prev:
                if children not in visited:
                    visited.add(children)
                    build_backprop_list(children)
            topo_list.append(x)

        build_backprop_list(self)
        for node in reversed(topo_list):
            node._gradient()

    def tanh(self):

        x = self.data
        t = (math.exp(2*x)-1)/(math.exp(2*x)+1)
        out = Value(t, (self,), "tanh")

        def _gradient():
            self.grad += (1-t**2)*out.grad

        # we make it += because we can have multiple children and we want to add all the gradients(accummulate)

        out._gradient = _gradient
        return out

    def exp(self):
        x = self.data
        out = Value(math.exp(x), (self,), "exp")

        def _gradient():
            # out.data is the local gradient of exp wrt x 
            self.grad += out.dat * out.grad
            
        out._gradient = _gradient
        return out
            
            
    def __pow__(self,other):
        assert isinstance(other,int | float)
        out = Value(self.data**other,(self,),"**")
        
        
        def _gradient():
            local_gradient=other*(self.data**(other-1))
            self.grad += local_gradient*out.grad
            
        out._gradient = _gradient
        return out
    


def main():

    # input nodes
    x1 = Value(2.0, label="x1")
    x2 = Value(0.0, label="x2")

    # weights
    w1 = Value(-3.0, label="w1")
    w2 = Value(1.0, label="w2")

    # bias of neuron
    b = Value(6.88137, label="b")

    # x1*w1+x2*w2+b (sigma xi*wi+b) where b is bias

    # x1w1 = x1*w1
    # x1w1.label = "x1w1"

    # x2w2 = x2*w2
    # x2w2.label = "x2w2"

    # x1w1x2w2 = x1w1+x2w2
    # x1w1x2w2.label = "x1w1x2w2"

    # n = x1w1x2w2+b
    # n.label = "n"
    # o = n.tanh()
    # o.label = "o"
    # o.backpropogate()

    a = Value(2.0)
    print(5*a)


main()
