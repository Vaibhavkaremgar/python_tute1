def prod(*args):
    total = 1
    for i in args:
        total*=i
    return total
print(prod(2,3,4,5,0.4))
def marks(**kwargs):
    for i in kwargs.keys():
        print(f"the marks of {i} are {kwargs[i]}")
marks(vaibhav= 55,nani=63,mani=45)
