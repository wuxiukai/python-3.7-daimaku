def common_divisor(m,n):
    r = m%n
    if r != 0:
        n=common_divisor(n,r)
    return n

def common_multiple(m,n,r):
    d=m*n/r
    return d

import random
m = random.randint(0,100)
n = random.randint(0,100)
print(str.format('m的值为：{0},n的值为：{1}',m,n))
if m<n:
    temp=m
    m=n
    n=temp
    
r=common_divisor(m,n)
d=common_multiple(m,n,r)

print(str.format('m与n的最大公约数为：{0}',r))
print(str.format('m与n的最小公倍数为：{0}',d))      
