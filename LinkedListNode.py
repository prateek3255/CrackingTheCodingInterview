class node:
    def __init__(self,data):
        self.next=None
        self.data=data
    def appendToLast(self,node):
        while self.next!=None:
            self=self.next
        self.next=node
    def printAll(self):
        while self!=None:
            print(self.data)
            self=self.next
