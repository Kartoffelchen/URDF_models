#path = 'temmesh3.obj'
#path2 = 'temmesh4.obj'

path = 'test_txt.txt'
path2 = 'test_txt4.txt'

with open(path,'r') as f_w:  
  lines = f_w.readlines()
  length = len(lines)
  with open(path2,'w') as f_w2: 
    lines2 = []
    for line in lines:
      if(line[0]=='v' and line[1]!='n'):
        line = line.split()
        print('line[0]',line[0])
        print('line[1]',line[1])
        line[-1] = '255'
        #line = line[0],line[1],line[2],line[3],255,255,255
        #line = 'v '+str(line[1])+' '+str(line[2])+' '+str(line[3])+' 255 0 0 \n'
        line = ' '.join(line)
        line+='\n'
        lines2.append(line)
      else:        
        lines2.append(line)      
    f_w2.writelines(lines2)
    f_w2.close()
  f_w.close()


