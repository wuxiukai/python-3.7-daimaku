import math
a = float(input('请输入系数a：'))
b = float(input('请输入系数b：'))
c = float(input('请输入系数c：'))
if a == 0 and b == 0:
    print('无解')
elif a == 0 and b != 0:
    print('有一个实根：x={0}'.format(-c/b))
elif b**2 - 4*a*c == 0:
    print('有两个相等的实根：x1=x2={0} '.format(-b/2*a))
elif b**2 - 4*a*c > 0:
    x1 = -b/2*a + math.sqrt(b**2 - 4*a*c) / 2*a
    x2 = -b/2*a - math.sqrt(b**2 - 4*a*c) / 2*a
    print(str.format('有两个不相等的实根：x1={0} x={1}',x1,x2))
else:
    realPart = -b/2*a
    imagPart = math.sqrt(4*a*c - b**2)/2*a
    x1=complex(realPart,imagPart)
    x2=complex(realPart,-imagPart)
    print(str.format('有两个共轭复数根：x1={0} x2={1}',x1,x2))
    
