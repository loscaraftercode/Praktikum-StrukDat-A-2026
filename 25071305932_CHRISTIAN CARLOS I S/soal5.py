

katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

log_transaksi = []
riwayat_transaksi = set()

level_diskon = (
    (500000, 15),
    (300000, 10),
    (100000, 5),
    (0, 0)
)


def tambah_buku(nama, harga, stok):

    if harga <= 0:
        print("Harga tidak valid")
        return None

    if stok < 0:
        print("Stok tidak valid")
        return None

    buku = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    return buku


