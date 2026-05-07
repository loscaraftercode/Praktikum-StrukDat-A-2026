#mensimulasikan sistem antrian rumah sakit menggunakan queue berbasi linked list manual.


# NODE (Representasi Pasien)

class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None



# queue linked list

class Queue:
    def __init__(self):
        self.head = None   # depan
        self.tail = None   # belakang
        self._size = 0

    # 1. enqueue (tambah pasien)
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"[DAFTAR] {nama.upper()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    # 2. dequeue (panggil pasien)
    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None

        removed = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama.upper()} (keluhan: {removed.keluhan})")
        return removed

    # 3. peek (lihat depan)
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")

    # 4. is_empty
    def is_empty(self):
        return self.head is None

    # 5. size
    def size(self):
        return self._size

    # 6. clear
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # Tambahan: tampilkan antrian
    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        no = 1
        while current:
            print(f"{no}. {current.nama.upper()} → {current.keluhan}")
            current = current.next
            no += 1


#simulasi sistem antrian poli umum di rumah sakit


print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================\n")

antrian = Queue()

# 1. cek kosong
print("[CEK] Apakah antrian kosong?", "→ YA, antrian masih kosong." if antrian.is_empty() else "→ TIDAK")

# 2–4 daftar pasien
antrian.enqueue("Budi", "demam tinggi")
antrian.enqueue("Ani", "batuk pilek")
antrian.enqueue("Citra", "sakit kepala")

# 5 jumlah pasien
print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

# 6 peek
antrian.peek()

# 7 dequeue
antrian.dequeue()

# 8 tambah pasien lagi
antrian.enqueue("Dodi", "nyeri perut")

# 9 tampilkan antrian
antrian.display()

# 10 dequeue lagi
antrian.dequeue()

# 11 jumlah sisa
print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

# 12 clear
antrian.clear()

# 13 cek lagi
print("[CEK] Apakah antrian kosong?", "→ YA, antrian sudah kosong." if antrian.is_empty() else "→ TIDAK")

print("\n====================================")
print("Simulasi Selesai!")
print("====================================")