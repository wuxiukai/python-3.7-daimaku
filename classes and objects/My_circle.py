class My_math:
    def __init__(self,r):
        self.r = r
    def perimetr(self):
        return 2*3.14*(self.r)
    def area(self):
        return 3.14*(self.r**2)
    def surface_area(self):
        return 4*3.14*(self.r**2)
    def volnme(self):
        return 4*3.14*(self.r**3)/3
#检测代码
r = float(input("请输入半径r:"))
p = My_math(r)
print("圆的周长 = {0:.2f}".format(p.perimetr()))
print("圆的面积 = {0:.2f}".format(p.area()))
print("球的表面积 = {0:.2f}".format(p.surface_area()))
print("球的体积 = {0:.2f}".format(p.volnme()))
