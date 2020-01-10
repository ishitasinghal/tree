class Tree:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None
    def insert(self, data):
        if(self.data):
            if(data<self.data):
                if(self.data is None):    #if there is no data on the left node
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif(data>self.data):
                if(self.data is None):    #if there is no data on the right node
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def printdata(self):
        if(self.left):
           self.left.printdata()
        print(self.data)
        if(self.right):
            self.right.printdata()

root = Tree(31)
root.insert(4)
root.insert(8)
root.insert(12)
root.insert(16)
root.insert(0)
root.insert(36)
root.insert(28)
print(root.printdata())
                
