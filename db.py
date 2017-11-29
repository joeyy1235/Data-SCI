import sys
import random
import math
import matplotlib.pyplot as plt
dat=[]
new=[]
x_axis=[]
y_axis=[]
e=0
core=[]
def main():
 global e
 global dat
 global new
 global core
 f=open("input1.txt","r")
 e=input("Enter eps(dis)\n")
 minpts=input("Minimum number of points")
 for line in f:
    s=line.split()
    dat.append(s)
 l=len(dat)
#creting copy of the list
 global new
 new=dat[:]
#searching for all the core points
# print new

 for var in new:
   count=0
   for var1 in new:
    dist=math.sqrt(math.pow(float(var[0])-float(var1[0]),2)+math.pow(float(var[1])-float(var1[1]),2))
    if dist <= e:
     count=count+1
   if count >= minpts:
    core.append(var)
 l_core=len(core)
 print core
 for var2 in core:     
   reachable(var2)
   plt.scatter(x_axis,y_axis,marker='o')
# plt.scatter(float(a[0]),float(a[1]),marker='s')
   del x_axis[:]
   del y_axis[:]
 print new
 for abc in new:
  plt.scatter(float(abc[0]),float(abc[1]),marker='^')
 plt.show()
def reachable(a):
 
# global new
 if a in core and a in new:
#  print str(a)+"this is a \n"
#  print "here"
  x_axis.append(float(a[0]))
  y_axis.append(float(a[1]))
  new.remove(a)
  for var in dat:
    if var in new:
      dist=math.sqrt(math.pow(float(a[0])-float(var[0]),2)+math.pow(float(a[1])-float(var[1]),2))
#  print str(var)+" and a = "+str(a)+" dist= "+str(dist)+" e= "+str(e)+"\n"
      if dist <= e:
#    print str(var)+"\n"
       if var not in core:
        x_axis.append(float(var[0]))
        y_axis.append(float(var[1]))
        new.remove(var)
       reachable(var)

main()