s=input()
d={}
for c in s:
    if c not in d:
        d[c]=1
    else:
        print("not unique")
        break
if c==s[len(s)-1]:
    print("unique")
        

