import math
list=[]
for i in range(2,101):
    k=0
    m=int(math.sqrt(i))
    for j in range(2,m+1):
        if(i%j==0):
            k=1
            break;
    if(k==0):
        list.append(i)
for i in range(0,len(list)):
    if i==len(list)-1 :
        print(list[i])
    else:
        print(list[i],end=" ")