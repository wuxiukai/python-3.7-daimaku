def water():
    temp = []
    
    for i in range(100,1000):
        if i == (i//100)**3 + ((i//10)%10)**3 + (i%10)**3:
            temp.append(i)

    return temp

print(water())
