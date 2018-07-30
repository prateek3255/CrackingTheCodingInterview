s=input()
st=set(input().split())
st.discard(' ')
count=0
for i in st:
    if s.count(i)%2!=0:
        count+=1
if count<=1:
    print('True')
else:
    print('False')