from LinkedListNode import node

l=[7,1,6]
head1=node(l[0])
for i in range(1,len(l)):
    head1.appendToLast(node(l[i]))

l=[5,9,2]
head2=node(l[0])
for i in range(1,len(l)):
    head2.appendToLast(node(l[i]))

n1=0
n2=0
count=0
while head1!=None:
    n1+=head1.data*10**count
    count+=1
    head1=head1.next

count=0

while head2!=None:
    n2+=head2.data*10**count
    count+=1
    head2=head2.next

n=n1+n2

head=None
temp=head
while n!=0:
    r=n%10
    n=int(n/10)
    if head==None:
        head=node(r)
        temp=head
    else:
        temp.next=node(r)
        temp=temp.next

head.printAll()