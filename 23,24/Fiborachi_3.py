temp = []
def fab(x,y):
    y = x % 2
    x = x // 2
    global temp
    
    if x == 0:
        temp_1 = ''
        while len(temp)>0:
            temp_1 += str(temp.pop())
        return temp_1
    else:
        temp.extend([y])
        print(x)
        return fab(x,y)
    
x = int(input('请输入一个十进制数：'))
temp = fab(x,0)

print('%d的二进制数是 %s'%(x,temp))

