



def check(s1,s2):

    d={}
    
    
    
    if ((len(s1)-len(s2))>=2):
        return False
    
    for i in s1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    
    for i in s2:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
            
    count=0
    for i in d:
        if d[i]%2!=0:
            count+=1
        if count>1:
            return False
    return True 

s1=input()
s2=input()
print(check(s1, s2))       