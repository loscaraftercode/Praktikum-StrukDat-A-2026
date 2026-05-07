class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python

    def is_empty(self):
        # Tulis kode di sini
        if len(self.items) == 0:
            print("Riwayat Kosong!")
            return True
        else:
            return False

    def push(self, url):
        # Tulis kode di sini (Petunjuk: gunakan append)
        url = input("masukkan url yang ingin ditambahkan ke riwayat!")
        self.items.append(url)
        print(f"URL ditambahkan: {url}")
        

    def pop(self):
        # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Riwayat Kosong!")
            return None
        
        

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
        if self.is_empty():
            print("Riwayat Kosong!")
            return None
        else:
            return self.items[-1]


    def size(self):
        # Tulis kode di sini (Petunjuk: gunakan len())
        return len(self.items)



#bagian 2: implementasi dengan linked list
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        if self.top is None:
            print("Riwayat Kosong!")
            return True
        else:
            return False
        

    def push(self, url):
        # Tulis kode di sini
        # 1. Buat Node baru
        new_node = Node(url)
        # 2. Hubungkan 'next' node baru ke 'top' saat ini
        if self.top:
            new_node.next = self.top
        # 3. Jadikan node baru sebagai 'top' yang baru
        self.top = new_node
        # 4. Tambahkan nilai 'count'
        self.count += 1


    def pop(self):
        # Tulis kode di sini
        # 1. Periksa is_empty()
        if self.is_empty():
            return "Riwayat Kosong!"
        # 2. Simpan url dari 'top' saat ini
        url = self.top.url
        # 3. Geser 'top' ke node berikutnya (top = top.next)
        self.top = self.top.next
        # 4. Kurangi nilai 'count'
        self.count -= 1
        # 5. Kembalikan url yang disimpan
        return url

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
        if self.is_empty():
            return "Riwayat Kosong!"
        else:
            return self.top.url
    
    def size(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai variabel 'count')
        return self.count

#jalankan dengan input berulang untuk melihat perbedaan antara stack dengan list dan linked list
print("=== Stack dengan List ===")
stack_list = StackList()
stack_list.push("https://www.starblast.io.com")  
stack_list.push("https://www.instagram.com")  
print("Top URL:", stack_list.peek())
print("Jumlah:", stack_list.size())

# Stack dengan Linked List
print("\n=== Stack dengan Linked List ===")
stack_linked_list = StackLinkedList()
stack_linked_list.push("https://www.google.com")
stack_linked_list.push("https://www.github.com")
print("Top URL:", stack_linked_list.peek())
print("Jumlah:", stack_linked_list.size())
