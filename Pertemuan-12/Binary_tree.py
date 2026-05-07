from logging import root


class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
#3 metode audit
#1. audit preorder
def traverse_preorder(node, result):
    if node is None:
        return 
    result.append(node.data)
    traverse_preorder(node.left, result)
    traverse_preorder(node.right, result)

#2. audit inorder
def traverse_inorder(node, result):
    if node is None:
        return
    traverse_inorder(node.left, result)
    result.append(node.data)
    traverse_inorder(node.right, result)

#3. audit postorder
def traverse_postorder(node, result):
    if node is None:
        return
    traverse_postorder(node.left, result)
    traverse_postorder(node.right, result)
    result.append(node.data)

#operasi yang diimplementasikan
def insert_manual(node, data):
    if node is None:
        return Treenode(data)
    

    if data < node.data:
        node.left = insert_manual(node.left, data)
    else:
        node.right = insert_manual(node.right, data)

    return node 

def get_leaf_node(node, result):
    if node is None:
        return
    if node.left is None and node.right is None:
        result.append(node.data)
    get_leaf_node(node.left, result)
    get_leaf_node(node.right, result)


def main_output():

    print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
    print("=========================================")
    print("[INFO] Membangun Struktur Gudang...")

    root = Treenode("A")
    root.left = Treenode("B")
    root.right = Treenode("C")
    root.left.left = Treenode("D")
    root.left.right = Treenode("E")
    root.right.left = Treenode("F")

    print("[INFO] Struktur berhasil dibuat.\n")
    
    print("[INFO] Struktur berhasil dibuat.\n")

    preorder_hasil, inorder_hasil, postorder_hasil = [], [], []
    traverse_preorder(root, preorder_hasil)
    traverse_inorder(root, inorder_hasil)
    traverse_postorder(root, postorder_hasil)

    print("HASIL AUDIT:")
    print("1. Pre-order : " ," - " .join(preorder_hasil))
    print("2. In-order : ", " - ".join(inorder_hasil))
    print("3. Post-order : ", " - ".join(postorder_hasil))

    # leaf
    leaf = []
    get_leaf_node(root, leaf)

    print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf))
    print("======================================")
    print(" AUDIT SELESAI!")

#skenario pengujian


if __name__ == "__main__":
    main_output()