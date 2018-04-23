class Item:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.future = None
        self.past = None

class StackThem:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def push(self, value):
        IT = Item(value, self.length)
        if self.length == 0:
            self.head = IT
        else:
            IT.past = self.tail
            self.tail.future = IT
            self.tail = IT
            self.length += IT

    def pop(self, value):
        IT = Item(value, self.length)
        if self.length == 0:
                print ("Empty Stack")
        else:
            IT.future = self.head
            self.head.past = IT
            self.head = IT
            self.length -= IT

Stack = StackThem()
Stack.push(7)
Stack.push(3)
Stack.push(14)
Stack.push(1)
Stack.push(21)
Stack.push(0)
Stack.push(0)
Stack.push(56)

print(Stack)
