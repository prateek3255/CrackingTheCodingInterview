n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
    


for layer in range(int(n/2)):
    first=layer
    last=n-1-layer
    for i in (first,last):
        offset=i-first
        top=l[first][i]
        l[first][i]=l[last-offset][first]
        l[last-offset][first]=l[last][last-offset]
        l[last][last-offset]=l[i][last]
        l[i][last]=top

print(l) 

