from LinkedListNode import node

l=[1,2,3,4,5,6,7,8,9,10]
head=node(l[0])
for i in range(1,len(l)):
    head.appendToLast(node(l[i]))

def kThLast(k):
    p1=head
    p2=head
    for i in range(k):
        if p1.next==None:
            return None
        else:
            p1=p1.next
    while p1.next!=None:
        p2=p2.next
        p1=p1.next
    return p2

# print(kThLast(5).data)
