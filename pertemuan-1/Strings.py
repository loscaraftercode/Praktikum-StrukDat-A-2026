#python strings
# string adalah tipe data yang digunakan untuk menyimpan teks, yang diapit oleh tanda kutip tunggal atau ganda.
# "strings" sama dengan 'strings'
print ("loscarafterdesign")
print ('loscarafterdesign')
# keduanya sama saja.

#quotes inseide quotes
# artinya kutip[ di dalam kutip 
print ("dia bernama 'loscarafterdesign'")
print ('dia bernama "loscarafterdesign"')

#asign string to a variable 
#masukan strings ke dalam variable
a = "loscar"
print(a)
# output: loscar"

#multiline strings
# membuat strings lebih dari satu baris, gunakan 3 tanda kutip ganda
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt"""
print(a) 

#atau gunakan 3 tanda kutip tunggal:
a = '''Lorem ipsum dolor sit amet,
consctetur adipiscing elit,
sed do eiusmod tempor incididunt'''
print(a) 

#python slicing string
#slicing
# kita bisa mendapatkan sebuah bagian dari string dengan cara "slicing"
#menampilkan character dari posisi ke 2 sampai posisi ke 6|
b = "selamat datang"
print (b[2:6]) # output : lamat
#note : psosii pertama dimulai dari 0

#slice from the start
b = "bagaimana hari mu?"
print (b[:7]) # output : bagaimana

#slice to the end
b = "percobaan slicing"
print (b[5:]) # output : obaan slicing

#negative indexing
b = "Hello, loscarafterdesign"
print(b[-9:-2]) # output : erdesig
#note: negative indexing berarti mulai dari akhir string

#python modify strings 
#ubah string menjadi huruf kecil dan besar
#contoh :
a = "wellcone Back, Loscarafterdesign!"
print(a.upper()) # output: WELLCOME BACK, LOSCARAFTERDESIGN!
a = "wellcone Back, Loscarafterdesign!"
print(a.lower()) # output: wellcome back, loscarafterdesign!

#remove whitespace
#whitespace adalah spasi, tab, atau karakter baris baru di awal atau akhir string.
a ="     Hello, World!"
print(a.strip()) # output: "Hello, World!"
# karakter whitespace dihilangkan dengan fungsi strip()

#replace string
a = "Loscarafterdesign"
print(a.replace("design", "code")) # output: Loscaraftercode
# karakter atau kata tertentu dapat diganti dengan fungsi replace()

#split string
a = "Hello, loscarafterdesign, la,ft,d"
print(a.split(",")) # output: ['Hello', ' loscarafterdesign', ' la', 'ft', 'd']
# string dapat dipecah menjadi beberapa bagian dengan fungsi split(), berdasarkan karakter tertentu

#python string concatenation
# menggabungkan 2 atau lebih string dengan operator +
a = "loscar"
b = "afterdesign"
c = a + b
print(c) # output: loscarafterdesign
#kita juga bisa menambahkan spasi di antara string yg digabungkan
a = "loscar "
b = "afterdesign"
c = a + " " + b
print(c) # output: loscar afterdesign

#python format string
# kita tidak bisa menggabungkan string dengan angka secara langsung menggunakan operator +
age = 20
txt = "nama saya loscar, dan saya berusia " + age # akan berjalan error
# kita bisa menggabungkan string dengan nilai variabel menggunakan fungsi format()
age = 20
txt = f"nama saya loscar, dan saya berusia {age}"
print(txt) # output: nama saya loscar, dan saya berusia 20

#placeholders and modifiers
# placeholders mencakup variabel, o[erasi, fungsi dan modifier didalam string yang diformat.
total = 230
txt = f'total buah yang dibeli adalah {total}'
print(txt) # output: total buah yang dibeli adalah 230

# modifier digunakan dengan menambahkan tanda titik dua (:)diikuti dengan format sah. seperti .2f 
price = 49.99
txt = f'harga produk adalah {price:.2f} dollar'
print(txt) # output: harga produk adalah 49.99 dollar

#placeholder juga memiliki operasi matematika:
txt = f'total harga setelah diskon adalah {price * 0.8:.2f} dollar'
print(txt) # output: total harga setelah diskon adalah 39.99 dollar

#python escape characters
# escape characters digunakan untuk memasukan karakter khusus kedalam string.
# contoh escape characters: adalah backslash (\) diikuti dengan karakter khusus
# contoh:
txt = "We are the descentdents of "Adveshlaesh" from the north star" # akan menjadi error
txt = "We are the descentdents of \"Adveshlaesh\" from the north star" #benar
# output: We are the descentdents of "Adveshlaesh" from the north star

#strings methods
#python memiliki banyak metode string bawaan yang dapat digunakan untuk memanipulasi string.
#contoh beberapa:
#capitalize() untuk mengubah huruf pertama menjadi huruf besar
a = "hello, loscarafterdesign"
print(a.capitalize()) # output: Hello, loscarafterdesign
#casefold() untuk mengubah string menjadi huruf kecil
a = "Hello, Loscarafterdesign"
print(a.casefold()) # output: hello, loscarafterdesign
#center() untuk memusatkan string
a = "loscarafterdesign"
print(a.center(30)) # output:        loscarafterdesign
#count() untuk menghitung berapa kali sebuah nilai muncul dalam string
a = "loscar afterdesign loscar afterdesign"
print(a.count("loscar")) # output: 2
#encode() untuk mengubah string menjadi encoded versi
a = "loscarafterdesign"
print(a.encode()) # output: b'loscarafterdesign'
#endswith() untuk memeriksa apakah string diakhiri dengan nilai tertentu
a = "hello, loscarafterdesign"
print(a.endswith("design")) # output:True
