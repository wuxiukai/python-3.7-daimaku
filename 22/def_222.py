def power(x,y):
    if y == 0:
        return 1
    else:
        return x*power(x,y - 1)

number = int(input('请输入一个整数：'))
index = int(input('请输入一个整数：'))
result = power(number,index)

print("%d 的 %d 次幂是 %d"%(number,index,result))
