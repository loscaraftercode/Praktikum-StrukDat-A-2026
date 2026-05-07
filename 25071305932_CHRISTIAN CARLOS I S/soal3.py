katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

riwayat_transaksi = set()
def proses_transaksi(katalog, nama_buku, jumlah_beli):
    ditemukan = False

    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            ditemukan = True

        if buku['stok'] >= jumlah_beli:
            total = buku['harga']*jumlah_beli
            buku['stok'] -= jumlah_beli

            print("transaksi berhenti")
            print("buku :", buku['nama'])
            print("Jumlah beli :", jumlah_beli)
            print("Total harga :", total)

            riwayat_transaksi.add(buku['nama'])
        else:
            print("stok tidak mencukupi")

        break

    if not ditemukan:
        print("buku tidak ditemukan")
        
#3 transaksi di program utama
proses_transaksi(katalog, "Belajar Python", 2)
print()

proses_transaksi(katalog, "Struktur Data", 1)
print()

proses_transaksi(katalog, "Belajar Python", 1)
print()

#buat riwayat transaksi nya
print("Riwayat buku yang pernah dibeli:")
for buku in riwayat_transaksi:
    print("-", buku)
