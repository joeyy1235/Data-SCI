import sys
import math
I=0
H=0
O=0
X=[]
V=[]
h_f=[]
Y=[]
o_f=[]
d=[]
E_F=[]
Sum_E=[]
delta2=[]
delta1=[]
count=0
def learn(filename,a,t_st,w1,w2,flag):
 global I
 global H
 global O
 global X
 global h_f
 global Y
 global o_f
 global d
 global E_F
 global delta1
 global delta2
 global count
 global Sum_E
 f=open(filename,'r')
 for line in f:
  V=[0.0]*H
  Y=[0.0]*O
  d=[0.0]*O
  delta1=[0.0]*H
  delta2=[0.0]*O  
  X.append(1.0)
  s=line.split()
  for k in range(len(s)-1):
   X.append(int(s[k]))
#  print "V="+str(len(V))+"X="+str(len(X))+"\n"
  for i in range(len(V)):
   for j in range(len(X)):
#    print "i="+str(i)+"j="+str(j)+"\n"
    V[i]=V[i]+X[j]*w1[i][j]
  h_f=[calc(c) for c in V]
  h_f.insert(0,1.0)
  print h_f
  for i in range(len(Y)):
   for j in range(len(h_f)):
    Y[i]=Y[i]+h_f[j]*w2[i][j]
  print "##Y\n"
  print Y
  if flag==1:
   o_f=[calc(ab) for ab in Y]
   print "TEST Results"
   print "O layer\n"
   print o_f
   sys.exit(0)
  elif flag==0:
    o_f=[calc(ab) for ab in Y]
    print "O layer\n"
    print o_f
  for q in range(len(d)):
    if q==int(s[-1]):
        d[q]=1
    else:
        d[q]=0
  sum=0
  for q in range(len(d)):
    sum=sum+math.pow(d[q]-o_f[q],2)
  print "##d\n"
  print d
  E_F.append(0.5*sum)
  print "##E_F\n"
  print E_F
  delta2=[(d[i]-o_f[i])*o_f[i]*(1-o_f[i]) for i in range(O)]
  print "delta2\n"
  print delta2
    
  for i in range(H):
    for j in range(len(delta2)):
     delta1[i]=delta1[i]+delta2[j]*w2[j][i+1]
  print "delta1\n"
  print delta1
# weight updation between hidden to output
  for i in range(O):
        for j in range(len(h_f)):
            w2[i][j]=w2[i][j]+a*delta2[i]*h_f[j]
# weight updation between input to hidden
  for i in range(H):
        for j in range(len(X)):
           w1[i][j]=w1[i][j]+a*delta1[i]*X[j]
  print "w1"
  print w1
  print "w2"
  print w2
  X[:]=[]
 sum1=0
 for ab in E_F:
       sum1=sum1+ab
 Sum_E.append(sum1)
 sum1=0
 E_F[:]=[]
 print "Sum_E"
 print Sum_E
 print "Difference"+str(Sum_E[count]-Sum_E[count-1])+"\n"
 if count!=0:
      if abs(Sum_E[count]-Sum_E[count-1]) < t_st :
         print "Finish" 
      else:
        count=count+1
        learn(filename,a,t_st,w1,w2,0)
 else:
      count=count+1
      learn(filename,a,t_st,w1,w2,0)
 print 
def calc(a):
 s=1.0+math.exp(-a)
 r=1.0/float(s)
 return r

def main():
  global I
  global H
  global O
  global w1
  global w2
  if len(sys.argv) != 3:
    print 'usage: ./ml.py filename filename'
    sys.exit(1)
  
  filename = sys.argv[1]
  filename1 = sys.argv[2]
  flag=0
  I=int(raw_input("Number of Features\n"))
  H=int(raw_input("Number of Nodes in Hidden Layer\n"))
  O=int(raw_input("Number of Nodes in Output Layer\n"))
  a=float(raw_input("Learning Rate\n"))
  t_st=float(raw_input("Threshold\n"))
  w1=[[0.0]*(I+1)]*H
  w2=[[0.0]*(H+1)]*O
  print "Input the weights (between input layer and Hidden layer)\n"
  for i in range(H):
#   for j in range(I+1):
    w1[i]=[0.1 for kl in range(I+1)]
  print "Input the weights (between hidden layer and output layer)\n"
  for i in range(O):
#  for j in range(H+1):
    w2[i]=[0.1 for ml in range(H+1)]
  learn(filename,a,t_st,w1,w2,flag)
  flag=1
  learn(filename1,a,t_st,w1,w2,flag)
  print "##W1##\n"
  print w1
  print "##W2##\n"
  print w2
if __name__ == '__main__':
  main()