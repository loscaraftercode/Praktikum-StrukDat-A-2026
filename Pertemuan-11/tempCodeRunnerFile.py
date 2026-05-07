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
    print(f"Kode buku {kode_buku} ditemukan di rak A pada indeks ke-{index}")
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