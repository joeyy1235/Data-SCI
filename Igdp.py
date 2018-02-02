import sys
import math
num=0
def learn(filename,alpha,t_thres,filename2):
 f=open(filename,'r')
 in_p=[]
 j_w=[]
 global num
 w0=0.1
 for line in f:
    s=line.split()
    num=len(s)
    in_p.append(s)
 k_base=[]
 #assuming the knowledge base is 0.1 for all w initially
 for k in range(num-1):
  base=float(raw_input("Enter value w\n"))
  k_base.append(base)
 print "#####K_base####"+str(k_base)+"\n"
# k_base=[float(0.1) for x in range(num-1)]
 t_sample=len(in_p)
 t_step=1
 flag=0
 
 while(t_step<=2 or flag==1):
        cost=0
        for p in range(t_sample):
         h_w=w0*1
         print "length of kbase "+str(len(k_base))+"\n"
         for h in range(len(k_base)):
                h_w=h_w+(k_base[h]*float(in_p[p][h]))
                print "value at "+str(h)+" iteration is "+str(h_w)+"\n"
         print "value of h_w"+str(h_w)+"\n"
         w0=w0+alpha*((float(in_p[p][-1])-h_w))*1
         print "value of w0"+str(w0)+"\n"
         for i in range(len(k_base)):
                k_base[i]=k_base[i]+alpha*(float(in_p[p][-1])-h_w)*float(in_p[p][i])
                print "value of "+str(i)+" k_base"+str(k_base[i])+"with inp as"+str(in_p[p][-1])+"\n"
         cost=cost+0.5*math.pow((h_w-float(in_p[p][-1])),2)
        j_w.append(cost)
        t_step=t_step+1
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
 sum=w0*1   
 for ab in f1:
    x=ab.split()
    for v in range(len(x)):
        sum=sum+k_base[v]*float(x[v])
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