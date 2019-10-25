def age(n):
    if n == 1:
        return 10
    else:
        return age(n - 1) + 2

print('哈哈，我知道了，第五个人的年龄是 %d 岁！'%age(5))
