#soal 1
pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
"Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
"Irfan Maulana", "Joko Susilo"
]

namaPasien = input("Masukkan nama pasien yang ingin dicari: ")

if namaPasien in pasien:
    index = pasien.index(namaPasien)
    print(f"[{namaPasien}] ditemukan di urutan ke-{index+1} dalam daftar pasien.")
else:
    print(f"[{namaPasien}] tidak ditemukan dalam daftar pasien.")

#soal 2

#pakai binary search
def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1
    count = 0  

    while left <= right:
        mid = (left + right) // 2
        count += 1  

        if arr[mid] == targetVal:
            return mid, count

        elif arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1, count


id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]


idMasukan = int(input("Masukkan ID karyawan yang dicari: "))

nomorInput, jumlahPerbandingan = binarySearch(id_karyawan, idMasukan)

if nomorInput != -1:
    print(f"ID {id_karyawan[nomorInput]} karyawan ditemukan di indeks ke-{nomorInput} dalam daftar")
else:    
    print(f"ID {idMasukan} karyawan tidak ditemukan dalam daftar.")

print(f"Jumlah perbandingan: {jumlahPerbandingan}")

#print banyak proses perbandingan


#soal 3

rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

#program 
#mencari kode buku rak A pakai linear search

kode_buku = input("Masukkan kode buku yang ingin dicari: ") 
print("mencari di Rak A (linear Search)")
if kode_buku in rak_a:
    
    
    index = rak_a.index(kode_buku)
    print(f"Kode buku {kode_buku} ditemukan di rak A pada indeks ke-{index+1}")
else:
    print(f"Kode buku {kode_buku} tidak ditemukan di rak A.")   

#mencari kode buku yang sama di rak B  pakai binary search

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        elif arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if kode_buku in rak_b:
    index = binarySearch(rak_b, kode_buku)
    print("mencari di Rak B (binary Search)")
    if index != -1:
        print(f"Kode buku {kode_buku} ditemukan di rak B pada indeks ke-{index + 1}")
    else:
        print(f"Kode buku {kode_buku} tidak ditemukan di rak B.")

#menampilkan hasil pencarian kode buku di rak A dan rak B

if kode_buku in rak_a:
    index_a = rak_a.index(kode_buku)
    print(f"Kode buku {kode_buku} ditemukan di rak A pada indeks ke-{index_a + 1}")
else:
    print(f"Kode buku {kode_buku} tidak ditemukan di rak A.")

if kode_buku in rak_b:
    index_b = binarySearch(rak_b, kode_buku)
    if index_b != -1:
        print(f"Kode buku {kode_buku} ditemukan di rak B pada indeks ke-{index_b + 1}")
    else:
        print(f"Kode buku {kode_buku} tidak ditemukan di rak B.")

#menampilkan kesimpulan
if kode_buku in rak_a:
    print(f"Kesimpulan: Buku {kode_buku} tersedia di Rak A.")   
elif kode_buku in rak_b:
    print(f"Kesimpulan: Buku {kode_buku} tersedia di Rak B.")
else:
    print(f"Kesimpulan: Buku {kode_buku} tidak tersedia di Rak A maupun Rak B.")

"""
a) Mengapa binary search tidak bisa langsung digunakan di Rak A?
jawaban: Binary search tidak bisa langsung digunakan di Rak A karena binary search hanya dapat digunakan pada data yang sudah terurut. Rak A tidak memiliki buku yang terurut, sehingga kita harus menggunakan linear search untuk mencari kode buku di Rak A terlebih dahulu sebelum menggunakan binary search di Rak B yang sudah terurut.
b) Jika Rak B memiliki 1.000 buku, berapa maksimal langkah yang
dibutuhkan binary search?
jawaban: Maksimal langkah yang dibutuhkan binary search untuk mencari 1.000 buku adalah log2(1000) ≈ 10 langkah.
c) Jika Rak A memiliki 1.000 buku, berapa maksimal langkah yang
dibutuhkan linear search?
jawaban: Maksimal langkah yang dibutuhkan linear search untuk mencari 1.000 buku adalah 1.000 langkah.
"""