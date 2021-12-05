class MyClass(object):
    l=0
    b=0
    def __init__(self,a,b):
        self.b=a
        self.l=b
    def __new__(cls,l,b):
        return b*l

obj = MyClass(10,12)
print (obj)