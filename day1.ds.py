#SLLcreation
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def dispaly(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data," -->",end=" ")
                temp=temp.next

obj=SLL()
n1=Node(12)
obj.head=n1
n2=Node(24)
n1.next=n2
n3=Node(30)
n2.next=n3
obj.dispaly()

#SLL.insrtion.beg
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

        
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while (temp):
                print(temp.data,"-->>",end=" ")
                temp=temp.next

obj=SLL()
n=Node(2)
obj.head=n
n1=Node(4)
n.next=n1
n2=Node(6)
n1.next=n2
print("before inserting")
obj.display()
print(" ")
print("after inserting")
obj.insert_begining(24)
obj.display()


#sll.insert.end

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
       if self.head is None:
            print("empty")
       else:
            temp=self.head
            while temp:
                print(temp.data," -->",end=" ")
                temp=temp.next

       
obj=SLL()
n=Node(2)
obj.head=n
n1=Node(4)
n.next=n1
n2=Node(6)
n1.next=n2
print("before inserting")
obj.display()
print(" ")
print("after inserting")
obj.insert_end(24)
obj.display()

