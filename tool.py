class Tool(Callable):
    def __init__(self,name:str,description:str,function):
        self.name=name
        self.description=description
        self.function=function
    
    def __call__(self,*args,**kwargs):
        return self.function(*args,**kwargs)