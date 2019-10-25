def findstr(str_ing,str_compare):
    count = 0

    for i in range(len(str_ing)):
        if str_ing[i] == str_compare[0] and str_ing[i+1] ==str_compare[1]:
            count += 1
        else:
            print("在目标字符串中未找到字符串！")

    return count

str_ing = str(input("请输入目标字符串："))
str_compare = str(input("请输入子字符串（两个字符串）："))

print(str.format("子字符串在目标字符串中出现{0}次。",findstr(str_ing,str_compare)))

    
