import sys
a = sys.argv[:]
print('参数个数= ',len(a))
for j in range(len(a)):
    print('sys.argv[{0}] = {1}'.format(j,sys.argv[j]))
