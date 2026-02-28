mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80 }
}

sum = 0

for x, y in mahasiswa.items():
    for a, b in y.items():
        if a == "ipk":
            sum+= b 

print(sum/3)

mahasiswa.update({
    "M004" : {"nama": "Sheravintyu", "prodi": "sastra mesin", "ipk": "3.99"  }
})

print(mahasiswa)

