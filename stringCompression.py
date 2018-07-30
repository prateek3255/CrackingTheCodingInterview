s=input()
cc=''
count=1
l=[]
for i in s:
    if i==cc:
        count+=1
    else:
        l.append((cc,count))
        count=1
    cc=i
l.append((cc,count))
t=""
for i in range(1,len(l)):
   t=t+l[i][0]+str(l[i][1])
print(t) 

