s=input()
r=input()

if(len(s)==len(r)):
    s=sorted(s)
    r=sorted(r)
    
    if(s==r):
        print("permutation")
    else:
        print("not permutation")
else:
    print("not permutation")
