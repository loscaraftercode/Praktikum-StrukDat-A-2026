katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

def cari_buku(katalog, keyword):
    hasil = []

    for buku in katalog:
        if keyword.lower() in buku['nama'].lower():
            hasil.append(buku)
            
        if len(hasil) == 0:
            print("buku tidak ditemukan")
        
        return hasil
    
keyword = input("masukkan keyword pencarian buku:")
hasil_pencarian = cari_buku(katalog, keyword)

if hasil_pencarian:
        print("\n Hasil pencarian")
for buku in hasil_pencarian:
    print(f"Nama Buku : {buku['nama']}")
    print(f"Harga     : Rp {buku['harga']}")
    print(f"Stok      : {buku['stok']}")
    print("-" * 25)
    