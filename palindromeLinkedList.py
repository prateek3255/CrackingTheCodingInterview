from LinkedListNode import node

l=[1,0,2,0]
head=node(l[0])
for i in range(1,len(l)):
    head.appendToLast(node(l[i]))

def palindrome(head):
    s1=""
    s2=""
    temp=None
    while head!=None:
        s1=s1+str(head.data)
        temp2=head.next
        head.next=temp
        temp=head
        head=temp2
    head=temp
    while head!=None:
        s2=s2+str(head.data)
        head=head.next
    return s1==s2
print(palindrome(head))