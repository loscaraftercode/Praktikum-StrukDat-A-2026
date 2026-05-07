level_diskon = (
(500000, 15), # belanja >= 500.000 -> diskon 15%
(300000, 10), # belanja >= 300.000 -> diskon 10%
(100000, 5), # belanja >= 100.000 -> diskon 5%
(0, 0), # default -> tidak ada diskon
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    batas, persen = level_diskon[index]

    if total_belanja >= batas:
        nominal = total_belanja * persen / 100
        total = total_belanja - nominal
        return persen, nominal, total
    else:
        return hitung_diskon(total_belanja, level_diskon, index)
    

nama = input("Masukkan nama anda: ")
total_belanja = int(input("Masukkan total belanja: "))

persen, nominal, total_bayar = hitung_diskon(total_belanja, level_diskon)

print("\n=== RINCIAN DISKON ===")
print("Nama :", nama)
print("Total Belanja :", total_belanja)

if total_belanja < 100000:
    print("Pesan : Tidak ada diskon")
else:
    print("Persen Diskon :", persen, "%")

print("Nominal Diskon :", int(nominal))
print("Total Bayar :", int(total_bayar))

    