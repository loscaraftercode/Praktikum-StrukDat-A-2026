#ini adalah program utama

#terdapat tabel kurs
#input user
#hasil format

from tabulate import tabulate
from kurs import kurs 
from konverter import konversi

# buat menampilkan tabel kurs
print("=== KONVERSI MATA UANG ===")

data_tabel = []
for kode, nilai in kurs.items():
    if kode != "IDR":
        data_tabel.append([kode, f"{nilai:,}".replace(",",",")])

print(tabulate(data_tabel, headers=["kode", "kurs"], tablefmt="outline")) 

#inputan user

asal = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
tujuan = input ("ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("jumlah: "))

#hasil konversi
hasil = konversi(asal,tujuan,jumlah)

#format rupiah
jumlah_format = f"{jumlah:,.0f}".replace(",", ".")
hasil_format = f"{hasil:,.2f}".replace(",", ".")

print(f"\nRp {jumlah_format} = {hasil_format} {tujuan}")

