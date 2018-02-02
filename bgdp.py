import sys
import math
num=0
def learn(filename,alpha,t_thres,filename2):
 f=open(filename,'r')
 in_p=[]
 global num
 w0=0.1
 for line in f:
    s=line.split()
    num=len(s)
    in_p.append(s)
 #assuming the knowledge base is 0.1 for all w initially
 k_base=[]
 #assuming the knowledge base is 0.1 for all w initially
 for k in range(num-1):
  base=float(raw_input("Enter value of w \n"))
  k_base.append(base)
 print "#####K_base####"+str(k_base)+"\n"
 t_sample=len(in_p)
 h_w=[]
 j_w=[]
 t_step=1
 flag=0
 while(t_step<=2 or flag==1):
         cost=0
#        print "Training Step "+str(t_step)+"\n"
         h_w[:]=[]
         for p in range(t_sample):          
          h_w.append(w0*1)
          print "length of kbase "+str(len(k_base))+"\n"
          for h in range(len(k_base)):
                h_w[p]=h_w[p]+(k_base[h]*float(in_p[p][h]))
                #print "value at "+str(h)+" iteration is "+str(h_w[p])+"\n"
          print "value of h_w "+str(p)+" = "+str(h_w[p])+"\n"
         for q in range(t_sample):
            w0=w0+alpha*((float(in_p[q][-1])-h_w[q]))*1
            print "value of w0"+str(w0)+"\n"
            for i in range(len(k_base)):
                k_base[i]=k_base[i]+alpha*(float(in_p[q][-1])-h_w[q])*float(in_p[q][i])
                print "first quantity y = "+str(float(in_p[q][-1]))+"second quantity h_w "+str(h_w[q])+" third quantity x"+str(float(in_p[q][i]))+" value of i ="+str(i)+" value of q "+str(q)+"\n"
                print "value of k_base"+str(k_base[i])+"with inp as"+str(in_p[p][-1])+"\n"
         t_step=t_step+1
         print "##val "+str(float(in_p[0][1]))+"\n"
         for i in range(t_sample):
                cost=cost+0.5*math.pow((h_w[i]-float(in_p[i][-1])),2)
         j_w.append(cost)
         if(len(j_w)>=2):
            diff=abs(j_w[-1]-j_w[-2])
            if diff < t_thres :
                flag=0
            else :
                flag=1 
 print "w0 = "+str(w0)+"\n"
 for i in range(len(k_base)):
  print "w"+str(i+1)+" = "+str(k_base[i])+"\n"
 f1=open(filename2,'r')
 print filename2  
 for ab in f1:
    sum=w0*1
    x=ab.split()
    print "val "+str(len(x))+"\n"
    for v in range(len(x)):
        sum=sum+(k_base[v]*float(x[v]))
    print " Result "+str(sum)+"\n"
    
def main():
  if len(sys.argv) != 3:
    print 'usage: ./ml.py filename'
    sys.exit(1)

  
  filename = sys.argv[1]
  filename2 = sys.argv[2]
  t_st=float(raw_input("Threshold\n"))
  a=float(raw_input("Learning Rate\n"))
  learn(filename,a,t_st,filename2)
if __name__ == '__main__':
  main()