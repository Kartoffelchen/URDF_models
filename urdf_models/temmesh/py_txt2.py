#path = 'temmesh3.obj'
#path2 = 'temmesh4.obj'

path = 'test_txt5.txt'
path2 = 'test_txt6.txt'

with open(path,'r+') as f:  
  list1 = [1,2,3,4,5]
  list2 = ['1','2','3','4','5']
  str1 = ' '.join(str(list1))
  f.write(str1)
  f.write('\n')
  str2 = ' '.join(list2)
  f.write(str2)
  f.write('\n')
  str3 = ' '.join(str(list2))
  f.write(str3)
  f.write('\n')
  str4 = '+'.join(str(list2))
  f.write(str4)
  f.write('\n')
  str5 = '+'.join(str(list1))
  f.write(str5)
  f.write('\n')
  f.close()

