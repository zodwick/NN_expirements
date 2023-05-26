
from visualiser import draw_dot, visualize_graph,write_dot_file
from graphviz import Source,Digraph

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
# dot_representation=(draw_dot(d))
# dot = Digraph(format='png')
# dot.engine = 'dot'
# dot.body.append(dot_representation)


write_dot_file(d, 'graph.dot')

# Render the graph
dot = Digraph(format='png')
dot.engine = 'dot'
dot.render('graph', format='png', cleanup=True)