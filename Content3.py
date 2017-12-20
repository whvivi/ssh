import os 
os.chdir('C:\\wing')       
if not os.path.exists('test1.txt'): 
  exit(-1)                         
lines = open('test1.txt').readlines()  
fp = open('test1.txt','w')  
for s in lines:
          fp.write( s.replace('love','hate').replace('yes','no'))    
fp.close()  
