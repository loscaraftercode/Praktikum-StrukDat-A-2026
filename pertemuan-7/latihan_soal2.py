class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def tambahKendaraan(self, plat):
        newNode = Node(plat)

        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newNode

    def hapusKendaraan(self, plat):
        current = self.head

        
        if current and current.data == plat:
            self.head = current.next
            return

        prev = None
        while current and current.data != plat:
            prev = current
            current = current.next

        
        if current is None:
            print("Kendaraan tidak ditemukan")
            return

        prev.next = current.next


    
    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



antrian = LinkedList()

antrian.tambahKendaraan("kendaraan 1")
antrian.tambahKendaraan("kendaraan 2")
antrian.tambahKendaraan("kendaraan 3")
antrian.tambahKendaraan("kendaraan 4")

print("Antrean kendaraan:")
antrian.tampilkan()

print("\nKendaraan mogok: kendaraan 2")
antrian.hapusKendaraan("kendaraan 2")

print("Antrean setelah kendaraan dihapus:")
antrian.tampilkan()