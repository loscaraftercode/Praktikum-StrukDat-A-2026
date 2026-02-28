stok_barang = [15, 40, 30, 10, 25]
stok_barang = [15, 40, 30, 10, 25]

# a
index_nilai = stok_barang.index(10)
stok_barang[index_nilai] = 50

# b
stok_barang.append(5)
stok_barang.sort(reverse=True)

# c
total = sum(stok_barang)
print("Total stok:", total)

# d
rata_rata = total / len(stok_barang)
print("Status:", "Stok Aman" if rata_rata > 20 else "Waspada")

print("Stok akhir:", stok_barang)

#2
data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for nama, poin in data_aktivitas:
    if poin > 80:
        print(f"{nama} mendapatkan predikat Gold")
    elif 50 <= poin <= 80:
        print(f"{nama} mendapatkan predikat Silver")
    else:
        print(f"{nama} mendapatkan predikat Bronze")


#3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
mahasiswa_unik = ukm_coding | ukm_robotik
print("yang mendaftar pada ukm coding adalah:", ukm_coding - ukm_robotik)
print("mahasiswa yang unik adalah", mahasiswa_unik)
print("Andi" in ukm_robotik)

#4
gudang_pc = [ 
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20} 
] 

gudang_pc[1].update({"kategori": "Aksesoris"})
gudang_pc.append({"item": "Headset", "harga": 350000, "stok" : 8}) 
print(gudang_pc)

for x in gudang_pc:
    print(f"Item: {x["item"]} | Total Aset: Rp {x["harga"]*x["stok"]}")
