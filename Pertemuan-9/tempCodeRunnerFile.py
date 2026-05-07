
# Bagian A Double Linked List

class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None

# insert ke TAIL
def insertTail(head, judul):
    new_node = Node(judul)
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    new_node.prev = current
    return head

# print forward
def print_forward(head):
    current = head
    while current:
        print(f"Judul: {current.judul}")
        current = current.next

# print backward
def print_backward(head):
    if not head:
        return
    
    current = head
    while current.next:
        current = current.next  # ke tail dulu
    
    while current:
        print(f"Judul: {current.judul}")
        current = current.prev

# delete by judul
def delete_by_judul(head, judul):
    current = head
    while current:
        if current.judul == judul:
            if current.prev:
                current.prev.next = current.next
            else:
                head = current.next  # jika hapus head
            
            if current.next:
                current.next.prev = current.prev
            
            return head
        current = current.next
    return head

# jalankan
head = None
head = insertTail(head, "Laskar Pelangi, Andrea Hirata")
head = insertTail(head, "Bumi Manusia, Pramoedya Ananta Toer")
head = insertTail(head, "Sang Pemimpi, Andrea Hirata")

print("Forward:")
print_forward(head)

print("\nBackward:")
print_backward(head)

# hapus
head = delete_by_judul(head, "Bumi Manusia")

print("\nSetelah dihapus:")
print_forward(head)



# Bagian B Circular Linked List


class NodeC:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

def insert_tail(head, nama):
    new_node = NodeC(nama)
    if not head:
        new_node.next = new_node
        return new_node
    
    current = head
    while current.next != head:
        current = current.next
    
    current.next = new_node
    new_node.next = head
    return head

def print_antrian(head):
    if not head:
        print("antrian kosong")
        return
    
    current = head
    while True:
        print(f"Nama: {current.nama}")
        current = current.next
        if current == head:
            break

def delete_head(head):
    if not head:
        return None
    
    if head.next == head:
        return None
    
    tail = head
    while tail.next != head:
        tail = tail.next
    
    new_head = head.next
    tail.next = new_head
    return new_head

# jalankan
head = None
head = insert_tail(head, "Andi")
head = insert_tail(head, "Budi")
head = insert_tail(head, "Citra")
head = insert_tail(head, "Dina")
head = insert_tail(head, "Edo")

print("\nAntrian awal:")
print_antrian(head)

# hapus Andi
head = delete_head(head)

print("\nSetelah Andi dilayani:")
print_antrian(head)