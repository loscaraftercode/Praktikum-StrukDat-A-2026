def tambah_buku(nama, harga, stok):
    
    if harga <= 0:
        print("error")
        return None
    
    if stok < 0:
        print("error")
        return None
    
    
    buku = {
    "nama" : nama,
    "harga" : harga,
    "stok" : stok
    }
    return buku 

daftar_buku = []
for i in range(3):
    print(f"\n input buku ke-{i+1}")
        
    nama = input("masukan nama buku:")
    harga = int(input("masukkan harga buku:"))
    stok = int(input("masukkan stok buku:"))

    data_buku = tambah_buku(nama, harga, stok)

if data_buku != None:
        daftar_buku.append(data_buku)
        
        print("\nDaftar Buku di PyBook Store:")
for buku in daftar_buku:
    print(buku)

