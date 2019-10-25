class TemperatureConverter:
    @staticmethod
    def c2f(t_c):               #摄氏温度到华氏温度的转换
        t_c = float(t_c)
        t_f = (t_c*9/5) + 32
        return t_f
    @staticmethod
    def f2c(t_f):               #华氏温度到摄氏温度的转换
        t_f = float(t_f)
        t_c = (t_f - 32) * 5 / 9
        return t_c
