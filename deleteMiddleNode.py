from LinkedListNode import node

l=[1,2,3,4,5,6,7,8,9,10]
head=node(l[0])
for i in range(1,len(l)):
    head.appendToLast(node(l[i]))


def delete(node):
    if node!=None and node.next!=None:
        node.data=node.next.data
        node.next=node.next.next

Node=head
for i in range(int(len(l)/2)):
    Node=Node.next

delete(Node)

head.printAll()