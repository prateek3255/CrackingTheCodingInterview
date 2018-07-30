s=input()
n=int(input())

s=s[:n]
r=''
for c in s:
    if c==' ':
        r=r+'%20'
    else:
        r=r+c
    
print(r)
        
