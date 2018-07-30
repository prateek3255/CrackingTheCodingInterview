A=[[1,2,6,2],[3,0,4,5],[0,3,9,7
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        ],[4,7,8,11]]
m=4
n=4
rows=set()
columns=set()
for i in range(m):
    for j in range(n):
        if A[i][j]==0:
            rows.add(i)
            columns.add(j)
for i in rows:
    A[i]=[0]*n

for j in columns:
    for i in range(m):
        A[i][j]=0
        
print(A)