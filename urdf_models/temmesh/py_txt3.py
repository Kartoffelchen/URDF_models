#path = 'temmesh3.obj'
#path2 = 'temmesh4.obj'

path = 'test_txt.txt'
path2 = 'test_txt6.txt'

with open(path,'r+') as f:  
  lines = f.readlines()
  print('length of lines:',len(lines))
  lines = lines[0].split(']')
  print('length of lines:',len(lines))
  for index in range(len(lines)):
    print('original:',lines[index])
    if '[' in lines[index]:
      lines[index] = lines[index].replace('[','')
    print('remove [:',lines[index])
    if "'" in lines[index]:
      lines[index] = lines[index].replace("'","")
    print("remove ':",lines[index])
    lines[index]+='\n'
  f.writelines(lines)
  
  f.close()
