def myfunc(*args):
    for i in args:
        if i % 2 == 0:
            return[i]
myfunc(1,2,3,4,5)