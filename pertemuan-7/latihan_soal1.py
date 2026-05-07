#1
def listKendaraan(data):
    ganjil = []
    genap = []

    for plat in data:
        angka = ""
        
        
        for char in plat:
            if char.isdigit():
                angka += char
        
        
        angka_terakhir = int(angka[-1])

        if angka_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return genap, ganjil


listKendaraan_data = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

genap, ganjil = listKendaraan(listKendaraan_data)

print("Plat Genap:", genap)
print("Plat Ganjil:", ganjil)


