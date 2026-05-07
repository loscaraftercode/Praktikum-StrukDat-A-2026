
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #Langkah 1
        new = Node(data)

        #Langkah 2
        if self.root is None:
            #Jika iya
            self.root = new
            return
        
        #Langkah 3
        P = self.root
        Q = self.root

        #Langkah 4
        while Q is not None and new.data != P.data:
            #Langkah 5
            P = Q
            
            #Langkah 6
            if new.data < P.data:
                Q = P.left
            
        #Langkah 7
        if new.data == P.data:
            #Jika iya
            print("Datanya Duplikat")

        #Langkah 8
        if new.data < P.data:
            #Jika iya
            P.left = new
        #Jika tidak
        else:
            P.right = new
            
bst = BinarySearchTree() 

bst.insert(23)
bst.insert(45)
bst.insert(50) 
bst.insert(78) 
bst.insert(78)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' --> ')
        in_order(node.right)

in_order(bst.root)

