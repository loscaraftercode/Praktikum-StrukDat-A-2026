#soal 1
thislist = [75, 80, 65, 90, 85]
thislist.append(95)
del thislist[2]
thislist.sort()
nilaiTertinggi = thislist[4]
nilaiTerendah = thislist[2]
ratarata = (thislist[0] + thislist[1] + thislist[2] + thislist[3] + thislist[4]) / 5 
print(thislist)
print("nilai tertinggi", nilaiTertinggi)
print("nilai terendah", nilaiTerendah)
print(len(thislist))
print (ratarata)
print("/n")
#soal 2
thistuple = ("D001", "Dr. Andi", "Struktur Data", 12)
print(thistuple [1], thistuple[2])
for i in thistuple:
    print(i)
#kelebihan tuple dibanding list adalah, tuple bersifat tidak dapat diubah, lebih cepat, dapat digunakan sebagai kunci dictionary, dan menggunakan memori lebih sedikit 
print("/n")
#soal 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
keunikan_A = keahlian_A - keahlian_B
keunikan_B = keahlian_B - keahlian_A
print("keahlian A =", keahlian_A)
keahlian_A.update(keahlian_B)
print(keahlian_A)
print("keunikan A adalah:" , keunikan_A)
print("keunikan B adalah:",  keunikan_B)

print("Java" in keahlian_B,  ", Java bukan keahlian mahasiswa B")
print("/n")
#soal 4
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80 }
}

