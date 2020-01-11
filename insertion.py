class Tree:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None
    def inser(self, data):
        if(self.data):
            if(data<self.data):
                if(self.data is None):    #if there is no data on the left node
                    self.left = Tree(data)
                else:
                    self.left.inser(data)
            elif(data>self.data):
                if(self.right is None):    #if there is no data on the right node
                    self.right = Tree(data)
                else:
                    self.right.inser(data)
        else:
            self.data = data
    def printdata(self):
        if(self.left):
           self.left.printdata()
        print(self.data)
        if(self.right):
            self.right.printdata()

root = Tree(31)
root.inser(4)
root.inser(8)
root.inser(12)
root.inser(16)
root.inser(0)
root.inser(36)
root.inser(28)
print(root.printdata())
