class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if(self.data):
            
        
##function     
def preOrder(root):
    if(root):
        print(root.info)
        preOrder(root.left)
        preOrder(root.right)
