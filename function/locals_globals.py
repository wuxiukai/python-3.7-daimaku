a = 1
b = 2
def f(a,b):
    x = 'xyz'
    y = 'abc'
    for i in range(2):
        j = i
        k = i **2
        #print(locals())

f(1,2)
print(globals())

