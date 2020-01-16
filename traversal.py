class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if(self.data):
            
        
##function     
def preOrder(root):
    list1 = []
    if(root):
        list1.append(root.info)
        if(root.left):
            preOrder(root.left)
        else:
            preOrder(root.right)
     print(list1)
