class Node():
    def __init__(self, data): #constructor
        self.data = data

class stack():
    def __init__(self):
        self.head = None
        self.tail = None

    def addTail(self, data):
        databaru = Node(data)
        if self.head == None:
            self.head = databaru
            self.tail = databaru
        else:
            self.tail.next = databaru
            self.tail = databaru
    
    def display(self):
        pass
    

def main():
    linkedlist = LL()

    for i in range(9):
        linkedlist.addTail(i)
    

main()