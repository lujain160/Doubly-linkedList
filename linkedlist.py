from node import Node
class LinkedList:
    def __init__(self):
        self.head=None
    def instert_at_front(self,data):
        newNode=Node(data)
        if self.head:
            newNode.next=self.head
            self.head.previouse=newNode
        self.head=newNode           
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
            newNode.previouse=current  
    def insert_after(self,target_Node,data):
        if target_Node is None:
            return
        newNode=Node(data)
        newNode.next=target_Node.next
        if target_Node.next:
            target_Node.next.previouse=newNode
        target_Node.next=newNode
        newNode.previouse=target_Node
    def get_first_node(self):
        return self.head
    def get_last_node(self):
        if self.head is None:
            return
        current=self.head
        while current.next is not None:
            current=current.next
        return current   
    def get_node(self,data):
        current=self.head
        while current is not None and current.data!=data:
            current=current.next
        return current
    def delete_node(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            self.head.previouse=None
            return
        current=self.head
        while current and current.data !=data:
            current=current.next
        if current is None:
            return
        if current.next:
            current.next.previouse=current.previouse    
        if current.previouse:
            current.previouse.next=current.next    
    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print()    
