
from visualiser import draw_dot, visualize_graph

class Value:
    def __init__(self,data,children=(),op="",label=""):
        
        # if list then multiple pointers to same child may occur : not needed???
        
        self.data=data
        self._prev=set(children)
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
    
    


a=Value(4)
b=Value(-5)
c=Value(6)
d=a+a
print(d._prev)
draw_dot(d)
visualize_graph(d)