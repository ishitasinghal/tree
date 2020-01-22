class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if(self.data):
            if(data<self.data):
                if(self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif(data>self.data):
                if(self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
                
    def preOrder(root):
        if(root):
            print(root.info, end = " ")
            preOrder(root.left)
            preOrder(root.right)
            
    def postOrder(root):
    if(root.left):
        postOrder(root.left)
    if(root.right):
        postOrder(root.right)
    print(root.info, end = " ")

        
root = Node(1)
root.insert(2)
root.insert(5)
root.insert(3)
root.insert(6)
root.insert(4)
root.preOrder(self,root)
root.postOrder(self, root)


            
        
##function     
def preOrder(root):
    if(root):
        print(root.info)
        preOrder(root.left)
        preOrder(root.right)
        
def postOrder(root):
    if(root.left):
        postOrder(root.left)
    if(root.right):
        postOrder(root.right)
    print(root.info, end = " ")

def inOrder(root):
    if(root.left):
        inOrder(root.left)
    print(root.info, end = ' ')
    if(root.right):
        inOrder(root.right)
