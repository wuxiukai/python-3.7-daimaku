import global_variable

def tax(x):
    return x * global_variable.TAX2

a = [1000,1200,1500,2000]
for i in a:
    print(i,tax(i))
