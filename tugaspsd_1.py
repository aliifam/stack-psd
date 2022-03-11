class Node():
    def __init__(self, data): #constructor
        self.data = data
        self.next = None

class linkstack():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addHead(self, data):
        newdata = Node(data)
        if self.head == None:
            self.head = newdata
            self.head = newdata
        else:
            newdata.next = self.head
            head = newdata
    
    def removeHead(self):
        if self.head == None:
            print("error stack sudah kosong")
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    
    def peekHead(self):
        if self.head == None:
            return "error stack sudah kosong"
        else:
            return self.head.data
    

def main():
    linkedlist = LL()

    for i in range(9):
        linkedlist.addTail(i)
    

main()

"""
untuk membalik angka maka gunakan stack,
dengan konsepnya yang LIFO maka bisa dilakukan
push data -> peek data -> pop data, terus menerus
hingga data pada stack kosong,
kali ini method yang digunakan :

- addhead = push
- removehead = pop
- peekhead = peek
"""