class Value:
    def __init__(self,data):
        self.data=data
        
    def __repr__(self) -> str:
        return f"Value({self.data})"
    


a=Value(1)
print(a)