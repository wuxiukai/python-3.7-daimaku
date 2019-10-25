import math
def area(r):
    return math.pi*r**2
def volume(r):
    return math.pi*r**3*4/3
def main():
    R = float(input('请输入半径：'))
    print('圆面积= {0:.2f}'.format(area(R)))
    print('球体的体积= {0:.2f}'.format(volume(R)))
if __name__ == '__main__':
    main()
    
