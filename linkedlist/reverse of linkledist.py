class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.start_node=None
    def insert_at_end(self,data):
        new_node=node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        else:
            n=self.start_node
            while n.next is not None:
                n=n.next
            n.next=new_node
    def creating_linked_list(self):
        n=int(input("enter number of nodes you want to create:"))
        if(n==0):
            return
        else:
            for i in range(0,n):
                ele=int(input("enter the value of the nodes:"))
                self.insert_at_end(ele)
    def traverse(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.data , " ")
                n = n.next
    def reverse(self):
        if self.start_node is None:
            print("no nodes")
        else:
            prev=None
            n=self.start_node
            while n.next is not None:
                nextt=n.next
                n.next=prev
                prev=n
                n=nextt
            self.start_node=prev
                
l=linked_list()
l.creating_linked_list()
l.traverse()
l.reverse()
l.traverse()
            
        
