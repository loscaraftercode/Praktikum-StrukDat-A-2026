#python boolean
# boleean merepresentasikan "true" atau "false" 
print (95 > 34) #output : true
print (5 == 10) #output : salah
print (23 < 21) #output : salah

#jika kita pakai kondisi:
a = 12
b = 14

if b < a :
    print("b lebih kecil dari a")
else:
    print("b tidak besar dari a")

#evaluate values and variables
# fungsi bool() buat ngecek nilai itu dianggap true atau false.

print(bool("Visual"))
print(bool(10))

#output: true dan true

x = "Saya"
y ="kamu"
z = "23"

print(bool(x))
prin(bool(y))
print(bool(z))

#output: true

#banyak nilai yang bernilai benar:
# banyak tipe string bernilai true, kecuali string kosong
# banyak tipe angka bernilai benar, kecuali 0
# banyak tipe list, tuple, set dan dictionary berniilai benar, kecualli kosong

#contoh:
bool("christian carlos")
bool(125)
bool(["pekanbaru", "bangau", "sakti"])
#output : true untuk ketiganya

# contoh values yang salah:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#karena jika tidak di isi akan bernilai salah.

#Functions can Return a Boolean
# kita bisa membuat fungsi ayang akan mengembalikan nilai bolean
#contoh:
def myFunction() :
  return True

print(myFunction()) 

#kita bisa menjalankan code berdasarkan jawaban boolean dari fungsi:
#contoh print "iya" jika benar dan jika salah print "tidak":
def myFunction() :
  return True

if myFunction():
  print("iya")
else:
  print("tidak")

#kita bisa mengecek suatu objek apakah sebuah integer atau tidak:
a = 125
print(isinstance(x, init))
