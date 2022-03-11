class Node():
    def __init__(self, data): #constructor
        self.data = data
        self.next = None

class linkstack():
    def __init__(self): #constructor
        self.head = None
        self.tail = None
    
    def pushData(self, data): #truelly it's = addHead
        newdata = Node(data)
        if self.head == None:
            self.head = newdata
            self.tail = newdata
        else:
            newdata.next = self.head
            self.head = newdata
    
    def popData(self): #truelly it's = removeHead
        if self.head == None:
            print("error stack sudah kosong")
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    
    def peekData(self): #truelly it's = peekHead
        if self.head == None:
            return "error stack sudah kosong"
        else:
            return self.head.data
    

def func_test(numbers_list):
    stacked_list = linkstack()
    reversed_numbers = []
    for i in numbers_list:
        stacked_list.pushData(i)
    for j in range(len(numbers_list)):
        reversed_numbers.append(stacked_list.peekData())
        stacked_list.popData()
    return reversed_numbers