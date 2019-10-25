import TemperatureFormula as f
t_c = float(input('请输入摄氏温度：'))
print('摄氏温度={0:.2f},华氏温度={1:.2f}'.format(t_c,f.TemperatureConverter.c2f(t_c)))
t_f = float(input('请输入华氏温度：'))
print('华氏温度={0:.2f},摄氏温度={1:.2f}'.format(t_f,f.TemperatureConverter.f2c(t_f)))
