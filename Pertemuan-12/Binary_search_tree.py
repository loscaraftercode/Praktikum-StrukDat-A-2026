class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None
    
    
class BST:
    def __init__(self):
        self.root = None
    #insert
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] berhasil memasukkan : ID {id_buku} -  {judul}")
            return
        
        current = self.root

        while True:
            # masuk dari kiri
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = new_node
                    print(f"[INSERT] berhasil memasukkan : ID {id_buku} -  {judul}")
                    return
                current = current.left
            
            # masuk dari kanan
            else:
                if current.right is None:
                    current.right = new_node
                    print(f"[INSERT] berhasil memasukkan : ID {id_buku} -  {judul}")
                    return
                current = current.right
            
    #search
    def search(self, id_buku):
        current = self.root    

        while current is not None:

            if id_buku == current.id_buku:
                print(f"[SEARCH] Mencari ID {id_buku}.... Ditemukan! Judul: {current.judul}")
                return 
            
            elif id_buku < current.id_buku:
                current = current.left

            else:
                current = current.right
        
        print(f"[SEARCH] Mencari ID {id_buku}.... Data Tidak ditemukan!")

    #inorder traversal
    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(f"{node.id_buku} - {node.judul}")
            self.traversal_inorder(node.right)
    
    #get min
    def get_min(self):
        current = self.root

        while current.left is not None:
            current = current.left
        
        return current.id_buku
    
    #get max
    def get_max(self):
        current = self.root

        while current.right is not None:
            current = current.right
        
        return current.id_buku
    
    # height tree
    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

# Main Program

def main():

    bst = BST()

    print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
    print("=========================================")

    #menginsert data
    bst.insert(50, "Dasar Pemrograman")
    bst.insert(30, "Struktur Data")
    bst.insert(70, "Kecerdasan Buatan")
    bst.insert(20, "Matematika Diskrit")
    bst.insert(40, "Basis Data")
    bst.insert(60, "Jaringan Komputer")
    bst.insert(80, "Sistem Operasi")

    #memanggil inorder
    print("\n[INFO] Koleksi Buku (Inorder Traversal):")
    bst.traversal_inorder(bst.root)

    # Search buku
    print()
    bst.search(60)
    bst.search(100)

    # min dan max
    print(f"\n[STATISTIK] ID terkecil: {bst.get_min()}")
    print(f"[STATISTIK] ID terbesar: {bst.get_max()}")

    # height atau tinggi
    print(f"\n[INFO] Tinggi (height) Tree: {bst.height(bst.root)}")

    print("\n=========================================")
    print("Simulasi Selesai")

if __name__ == "__main__":
    main()