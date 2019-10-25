f=open('E:\\test.txt')

single = []
double = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
       (role,line_spoken) = each_line.split('.',1)
       int(role)
       if role == '1':
           single.append(line_spoken)
       elif role =='2':
           double.append(line_spoken)
    else:
         file_name_single = 'single_' + str(count) + '.txt'
         file_name_double = 'double_' + str(count) + '.txt'

         single_file = open(file_name_single,'w')
         double_file = open(file_name_double,'w')

         single_file.writelines(single)
         double_file.writelines(double)

         single_file.close()
         double_file.close()

         single = []
         double = []
         count += 1

f.close()

         
