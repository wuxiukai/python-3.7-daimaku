import sys

n = int(sys.argv[1])
power = 1
i = 0
f = open('out.log','w')
sys.stdout = f

while i<= n :
    print(str(i),'',str(power))
    power = 2 * power
    i = i + 1
    
sys.stdout = sys.__stdout__
sys.stdout.write('done!')
