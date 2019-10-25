
def fab(n):
    temp = []

    for i in range(n):
        if i == 0 :
            temp.extend([1])
        elif i == 1 :
            temp.extend([1])
        else :
            temp.extend([temp [i-1] + temp [i-2]])
    return temp

n = int(input("请输入时间(月):"))
temp = fab(n)
print(temp[n - 1])

