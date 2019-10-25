a = (44,78,90,-80,55)
total = 0
try:
    for i in a:
        if i < 0 : raise ValueError(str(i) + "为负数")
        total += i
    print('合计=',total)
except ValueError:
    print('数值不能为负')
    except Exception:
        print('发生异常')
