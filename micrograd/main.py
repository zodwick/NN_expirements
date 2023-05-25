class Value:
    def __init__(self,data):
        self.data=data
        
    def __repr__(self) -> str:
        return f"Value({self.data})"
    
    def __add__(self,second):
        return Value(self.data+second.data)
    
    def __mul__(self,second):
        return Value(self.data*second.data)
    
    def __pow__(self,second):
        return Value(self.data**second.data)
    
    def __sub__(self,second):
        return Value(self.data-second.data)
    
    


a=Value(1)
print(a)