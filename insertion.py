class Tree:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None
    def treein(self, data):
        if(self.data):
            if(data<self.data):
                if(self.left is None):    #if there is no data on the left node
                    self.left = Tree(data)
                else:
                    self.left.treein(data)
            elif(data>self.data):
                if(self.right is None):    #if there is no data on the right node
                    self.right = Tree(data)
                else:
                    self.right.treein(data)
        else:
            self.data = data
    def printdata(self):
        if(self.left):
           self.left.printdata()
        print(self.data)
        if(self.right):
            self.right.printdata()

root = Tree(31)
root.treein(4)
root.treein(8)
root.treein(12)
root.treein(16)
root.treein(0)
root.treein(36)
root.treein(28)
print(root.printdata())
