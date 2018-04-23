class Item:
	def __init__(self, value, index):
		self.value = value
		self.index = index
		self.future = None
		self.past = None
	
	


class MyQueue:
    def __init__(self):
            self.head = None
            self.tail = None
            self.length = 0
		
    def add(self, value):
                IT = Item(value, self.length)
                if self.length == 0:
                        self.head = IT
                else:
                        IT.past = self.tail
                        self.tail.future = IT
                        self.tail = IT
                        self.length += IT

    def pop(self):
        pass
        return self.head

    def append(self, value):
            pass
            return self.tail
    

	
	
	
NewQueue = MyQueue()
NewQueue.add(7)
NewQueue.add(3)
NewQueue.add(14)
NewQueue.add(1)
NewQueue.add(21)
NewQueue.add(0)
NewQueue.add(0)
NewQueue.add(56)

