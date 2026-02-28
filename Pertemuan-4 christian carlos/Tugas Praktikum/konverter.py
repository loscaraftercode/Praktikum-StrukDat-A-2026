#Konverter uang

from kurs import kurs

def konversi(mata_uang_asal, mata_uang_tujuan, jumlah):
    # di ubah ke rupiah dulu
    ke_uang_idr = jumlah * kurs[mata_uang_asal]

    # ubah ke mata uang tujuan
    hasil = ke_uang_idr / kurs[mata_uang_tujuan]

    return hasil

