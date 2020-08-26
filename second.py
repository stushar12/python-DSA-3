class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size=0

    def insertEnd(self,data):

        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    
    def evenodd(self):
        actualNode=self.head
        evenstart=None
        evenend=None
        oddstart=None
        oddend=None
        while(actualNode is not None):
            if(actualNode.data%2==0):
                if(evenstart is None):
                    evenstart=actualNode
                    evenend=actualNode
                else:
                    evenend.nextNode=actualNode
                    evenend=actualNode
            else:
                if(oddstart is None):
                    oddstart=actualNode
                    oddend=actualNode
                else:
                    oddend.nextNode=actualNode
                    oddend=actualNode
            
            actualNode=actualNode.nextNode

        
        self.head=evenstart
        if(oddstart is not None):
            if(evenstart is not None):
                evenend.nextNode=oddstart
                oddend.nextNode=None
            else:
                self.head=oddstart
                oddend.nextNode=None
        
        elif (evenstart is not None):
            pass
        else:
            print("\n None\n")



        

    def traverseList(self) :
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode


linkedlist=LinkedList()
b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert   \n 2 to traverse \n 3 to adjust even nodes followed by odd ones \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist.insertEnd(a)
    elif b==2:
        linkedlist.traverseList()
    elif b==3:
        linkedlist.evenodd()