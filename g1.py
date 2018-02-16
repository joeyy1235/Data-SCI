import sys
import subprocess
import glob




for x1 in range(0,20):
 for x2 in range(10,30):
  for x3 in range(2,22):
   f = open('training_data.txt','a')
   st = str(x1)+" "+str(x2)+" "+str(x3)+" "+str((3*x1)+(2*x2)+(4*x3))+"\n" 
   f.write(st)
