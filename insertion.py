class Tree:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.right = None
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
                
