#python numbers
# ada 3 tipe data nomor di python:
# int
# float
# complex

# variabel dengan tipe data nomor akan terbentuk setelah memaskan nilai:, contoh:
a = 5 #int
b = 5.5 #float
c = 5j #complex

#pakai fungsi type() untuk mengetahui tipe data:
print(type(a))  
print(type(b))
print(type(c))

#output: <class 'int'>, <class 'float'>, <class 'complex'>

int 
# tipe data int adalah bilangan bulat, positif atau negatif, tanpa desimal.
a = 10
print(type(a))  #output: <class 'int'>
b = -300 
print(type(b)) #output: <class 'int'>
c = 0
print(type(c)) #output: <class 'int'>
d = 1234567890123456789
print(type(d)) #output: <class 'int'>
#python memiliki ukuran integer yang tidak terbatas.

float 
# tipe data bilangan desimal, yang  berkoma, baik positif atau negatif.
a = 10.5
print(type(a))  #output: <class 'float'>
b = -300.78 
print(type(b)) #output: <class 'float'>
c = 0.0
print(type(c)) #output: <class 'float'>

# float juga bisa ditulis dalam notasi ilmih yaitu "e" jika angka lebih dari 10:
a = 1.5e2
b = 2.5e3
c = -3.5e4
print(type(a))
print(type(b))
print(type(c))

complex
# tipe data cpmplex adalah bilangan imajiner.
a = 2 + 3j
print(type(a))  #output: <class 'complex'>
b = -5j 
print(type(b)) #output: <class 'complex'>
c = 7j
print(type(c)) #output: <class 'complex'>
# bilangan komplek ditulis dengan "j" sebagai bagian imajinernya.

#type conversion 
# kita bisa mengkonversi tipe data nomor ke tipe data lain dengan fungsi bawaan:
# contoh:
a = 5    # int
b = 2.0  # float
c = 1j   # complex 

# konversi int ke float:
a = float(a)
print(a) # output: 5.0
print(type(a)) # output: <class 'float'>

# konversi float ke int:
b = int(b)
print(b) # output: 2
print(type(b)) # output: <class 'int'>

# konversi int ke complex:
a = complex(a)
print(a) # output: (5+0j)
print(type(a)) # output: <class 'complex'>

# konversi float ke complex: 
b = complex(b)
print(b) # output: (2+0j)
print(type(b)) # output: <class 'complex'>

# konversi complex ke int atau float tidak bisa, akan menghasilkan error:
# c = int(c) # akan menghasilkan error.
# c = float(c) # akan menghasilkan error.

#Random Number
#python tidak memiliki tipe data khusus untuk nomor acak sepeti random () fungsi.
# namun python memiliki modul bawaan yang disebut random yang dapat digunakan untuk menghasilkan nomor acak:

import random
print(random.randomrange(1,9)) # output: nomor acak antara 1 dan 9 (bebas sampai berapa)
