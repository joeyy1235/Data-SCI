import sys
import random
import math
import matplotlib.pyplot as plt
centroids=[]
dat=[]
dict={}
def main():
 f=open("new.txt","r")
 k=input("Enter k")
 decider=1
 for line in f:
    s=line.split()
    dat.append(s)
# print dat
# print dat[1][1]
 l=len(dat)
 count=0
 iteration=0
# print k
 while(count != k):
    x=random.choice(dat)
    if x not in centroids:
     centroids.append(x)
     count=count+1
# print centroids
#looping here
 while decider==1:
  decider=0
  for var in dat:
   ind=minimum(centroids,var)
#  print 'point'+str(var)+'lies in '+str(ind)+'\t'+str(centroids)+'\n'
   c=dat.index(var)
   if iteration==0:
    dict[c]=ind
    decider=1
   elif iteration!=0 and dict[c]!=ind :
    dict[c]=ind
    decider=1
   else:
    dict[c]=ind
  iteration=iteration+1
#calculating mean to find new centroids
  mean()
#  print ' decider '+str(decider)+' \n'
#  print "After Iteration "+str(iteration)+"\n"
#  print dict
# print 'Final Output \n'   
# print dict 
 fig(k)
    
    
    
    
    
    
def minimum(centroids,point):
 l=len(centroids)
 min=9999
 index=9999
 dist=0
 for var in range(l):
  dist=math.sqrt(math.pow(float(centroids[var][0])-float(point[0]),2)+math.pow(float(centroids[var][1])-float(point[1]),2))
#  print 'distance from'+str(centroids[var])+' is'+str(dist)+'\n'
  if dist < min:
    min=dist
    index=var
#  print 'minimum dist '+str(min)+' and index is '+str(index)+'\n'
 return index


def mean():
 print "At mean"
 l1=len(centroids) 
 for i in range(l1):
   sum_x=0
   sum_y=0
   obs=0
   for key in dict.keys():
    if dict[key]==i:
        sum_x=sum_x+float(dat[key][0])
        sum_y=sum_y+float(dat[key][1])
        obs=obs+1
   centroids[i][0]=sum_x/obs
   centroids[i][1]=sum_y/obs
#   print '\n'
#   print centroids  
        
def fig(k):
 x=[]
 y=[]
 for i in range(k):
  for key in dict.keys():
   if dict[key]==i:
    x.append(float(dat[key][0]))
    y.append(float(dat[key][1]))
    #plt.scatter(x[-1],y[-1],marker='o')
#  x.append(float(centroids[i][0]))
#  y.append(float(centroids[i][1]))
  plt.scatter(x,y,marker='o')
  plt.scatter(float(centroids[i][0]),float(centroids[i][1]),marker='s')
  del x[:]
  del y[:]
 plt.show()
main()