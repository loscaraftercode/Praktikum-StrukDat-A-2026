
# DATA AWAL

pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", "kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", "kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", "kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", "kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", "kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", "kembali": False},
]

# SOAL 1

def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("-----------------------------------------------")

    no = 1
    for p in pengunjung_hari_ini:
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(no, "|", p["id"], "|", p["nama"], "|", p["usia"], "|", p["kategori"], "|", status)
        no += 1


def filter_belum_kembali():
    belum = [p["nama"] for p in pengunjung_hari_ini if not p["kembali"]]
    belum.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI =====")
    no = 1
    for nama in belum:
        print(str(no) + ". " + nama)
        no += 1

    print("Total belum kembali:", len(belum), "pengunjung")



# SOAL 2

def info_perpustakaan():
    info = (
        "Perpustakaan Kampus Terpadu",
        "Jl. Pendidikan No. 5, Pekanbaru",
        "0761-54321"
    )

    print("\nInfo Perpustakaan:")
    print("Nama :", info[0])
    print("Alamat :", info[1])
    print("Telp :", info[2])


def rekap_kategori():
    kategori_unik = set()

    for p in pengunjung_hari_ini:
        kategori_unik.add(p["kategori"])

    print("\nKategori Buku Unik:", kategori_unik)
    print("Jumlah kategori:", len(kategori_unik))

    rekap = {}
    for k in kategori_unik:
        jumlah = 0
        for p in pengunjung_hari_ini:
            if p["kategori"] == k:
                jumlah += 1
        rekap[k] = jumlah

    print("\nRekap per kategori:")
    for k in rekap:
        print(k, ":", rekap[k], "pengunjung")

    max_jumlah = 0
    for k in rekap:
        if rekap[k] > max_jumlah:
            max_jumlah = rekap[k]

    terbanyak = []
    for k in rekap:
        if rekap[k] == max_jumlah:
            terbanyak.append(k)

    print("Kategori terbanyak:", ", ".join(terbanyak), "(", max_jumlah, "pengunjung )")



# SOAL 3 (OOP)

class pengunjung:
    jumlah = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        pengunjung.jumlah += 1

    # getter
    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori

    def tampilkan_info(self):
        print("ID:", self.__id)
        print("Nama:", self.__nama)
        print("Kategori:", self.__kategori)


    def hitung_pengunjung():
        return pengunjung.jumlah


class pengunjung_prioritas(pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        pengunjung.__init__(self, id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        pengunjung.tampilkan_info(self)
        print("Prioritas:", self.prioritas)

        if self.prioritas == "Mendesak":
            print("** Layani segera! **")


# SOAL 4 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)

        if self.head == None:
            self.head = node_baru
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node_baru

    def tampilkan(self):
        print("\n===== ANTRIAN PEMINJAMAN =====")
        current = self.head
        no = 1

        while current != None:
            d = current.data
            print("[" + str(no) + "]", d["id"], "-", d["nama"], "|", d["kategori"])
            current = current.next
            no += 1

        print("Total antrian:", self.hitung())

    def panggil_berikutnya(self):
        if self.head == None:
            print("Antrian kosong")
        else:
            print("\nMemanggil pengunjung berikutnya...")
            d = self.head.data
            print("Silakan masuk:", d["nama"], "(", d["id"], ")-", d["kategori"])
            self.head = self.head.next

    def cari(self, nama):
        print("\nMencari", nama)
        current = self.head
        posisi = 1

        while current != None:
            if current.data["nama"] == nama:
                d = current.data
                print("Ditemukan:", d["id"], "-", d["nama"], "|", d["kategori"], "(posisi ke-", posisi, ")")
                return
            current = current.next
            posisi += 1

        print("Tidak ditemukan")

    def hapus_berdasarkan_id(self, id):
        print("\nMenghapus ID", id)

        current = self.head
        prev = None

        if current != None and current.data["id"] == id:
            print(current.data["nama"], "berhasil dihapus")
            self.head = current.next
            return

        while current != None and current.data["id"] != id:
            prev = current
            current = current.next

        if current != None:
            print(current.data["nama"], "berhasil dihapus")
            prev.next = current.next
        else:
            print("ID tidak ditemukan")

    def hitung(self):
        current = self.head
        jumlah = 0

        while current != None:
            jumlah += 1
            current = current.next

        return jumlah


# MAIN PROGRAM

tampilkan_pengunjung()
filter_belum_kembali()
info_perpustakaan()
rekap_kategori()


p1 = pengunjung("M001", "Rina", "Fiksi")
p2 = pengunjung_prioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
print()
p2.tampilkan_info()

print("Total pengunjung:", pengunjung.hitung_pengunjung())

antrian = AntrianPeminjaman()

antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})

antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("M003")
antrian.tampilkan()
antrian.cari("Taufik")
print("Total antrian:", antrian.hitung())