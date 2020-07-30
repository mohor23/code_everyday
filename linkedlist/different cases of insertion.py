class node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.start_node=None
    def traverse(self):
        if self.start_node is None:
            print("the linked list is empty")
        else:
            n=self.start_node
            while n is not None:
                print(n.data)
                n=n.next
    def create_linkedlist(self):
        n=int(input("enter number of nodes you want to create"))
        if(n==0):
            return
        else:
            for i in range(0,n):
                ele=int(input("enter the value of the nodes:"))
                self.insert_at_end(ele)
    def insert_at_end(self,data):
        new_node=node(data)
        if(self.start_node==None):
            self.start_node=new_node
            return
        n=self.start_node
        while n.next is not None:
            n=n.next
        n.next=new_node
    def insert_at_beginning(self,data):
        new_node=node(data)
        new_node.next=self.start_node
        self.start_node=new_node
    def insert_at_specific_index(self,index,data):
        new_node=node(data)
        if index==1:
            new_node.next=self.start_node
            self.start_node=new_node
            return
        i=1
        n=self.start_node
        while i<index-1 and n is not None:
            n=n.next
            i=i+1
        if n is None:
            print("index out of bound")
        else:
            new_node.next= n.next
            n.next = new_node
    def insert_before_specific_element(self,x,data):
        new_node=node(data)
        if(self.start_node==None):
            print("No element in linked list")
        if x==self.start_node.data:
            new_node.next=self.start_node
            self.start_node=new_node
            return
        n = self.start_node
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node.next = n.next
            n.next = new_node
l=linked_list()
l.create_linkedlist()
l.traverse()
l.insert_at_beginning(10)
l.insert_at_specific_index(3,77)
l.insert_before_specific_element(2,55)
l.traverse()
