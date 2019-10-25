def get_digits(n,y):
    global temp
    if n == 0:
        temp.extend([y])
        temp.reverse()
        return temp
    elif y > 0:
        temp.extend([y])
    return get_digits(n//10,n%10)

temp = []
n = int(input('请输入一个数字：'))
temp = get_digits(n,-1)
print('参数%d分解出每一位的数字顺序依次为:'%n,temp)

