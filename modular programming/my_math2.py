import my_math1
def main():
    print('123 + 100 = ',my_math1.add(123,100))  #加
    print('123 - 100 = ',my_math1.sub(123,100))  #减
    print('123 * 100 = ',my_math1.mul(123,100))  #乘
    print('123 / 100 = ',my_math1.div(123,100))  #除
    print('2 ** 10 = ',my_math1.pow(2,10))       #幂
if __name__ == '__main__':      #如果独立运行时，则运行测试代码
    main()
