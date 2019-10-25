a = str(input("请输入带有符号的温度："))
if a[-1] in ['F','f']:
    c = eval(a[0:-1])-32/1.8
    print("C温度为：{0:.2f}C".format(c))
elif a[-1] in ['C','c']:
    f = 1.8*eval(a[0:-1])+32
    print("F温度为：{0:.2f}F".format(f))
else:
    print("error")
