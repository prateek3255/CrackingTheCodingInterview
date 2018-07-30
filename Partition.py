from LinkedListNode import node

l=[3,5,8,5,10,2,1]
head=node(l[0])
for i in range(1,len(l)):
    head.appendToLast(node(l[i]))

def part(pivot):
    linked1=None
    linked2=None
    temp=head
    while temp!=None:
        newNode = node(temp.data)
        if temp.data<pivot:
            if linked1==None:
                linked1=newNode
            else:
                linked1.appendToLast(newNode)
        else:
            if linked2==None:
                linked2=newNode
            else:
                linked2.appendToLast(newNode)
        temp=temp.next
    linked1.appendToLast(linked2)
    return linked1

node=part(5)
node.printAll()