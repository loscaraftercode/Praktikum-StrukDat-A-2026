#python Data Types
# variabel bisa menyimpan berbagai jenis tipe data, berbagai jenis tipe data bisa menghasilkan sesuatu yg berbeda beda, maka dari itu type data sangat penting.
# tipe data yang umum digunakan di python:
#text type: str
#numeric types: int, float, complex
#sequence types: list, tuple, range
#mapping type: dict
#set types: set, frozenset
#boolean type: bool
#binary types: bytes, bytearray, memoryview
#none type: NoneType

#get the type
#kita bisa mengetahui tipe data apa yang dipakai pada sebuah objek dengan ppakai fungsi type()
a = 7
print (type(a))  #output: <class 'int'> yang artinya  a bertipe integer

#setting the Data type
x = "greeting people" 
print(type(x))  #output: <class 'str'>
b = 15 
print(type(b)) #output: <class 'int'>
c = 9.8
print(type(c)) #output: <class 'float'>
d = 3 + 6j
print (type(d)) #output: <class 'complex'>
e = ["loscar", "after", "design"]
print (type(e)) #output: <class 'list'>
f = ("afterdesign", "aftercode", "afteraudio")
print (type(f)) #output: <class 'tuple'>
g = range(10)
print (type(g)) #output: <class 'range'>
h = {"name": "loscar", "brand": "afterdesign"}
print (type(h)) #output: <class 'dict'>
i = {"loscar", "after", "design"}
print (type(i)) #output: <class 'set'>
j = frozenset({"aftercode", "afteraudio", "aftervideo"})
print (type(j)) #output: <class 'frozenset'>
k = True 
print (type(k)) #output: <class 'bool'>
l = b"Hello" 
print (type(l)) #output: <class 'bytes'>
m = bytearray(10)
print (type(m)) #output: <class 'bytearray'>
n = memoryview(bytes(10)) 
print (type(n)) #output: <class 'memoryview'>
o = None
print (type(o)) #output: <class 'NoneType'>
# intinya tipe data akan diatur secara otomatis, setelah dimasukan suatu nilai ke dalam variabelnya.
# dan sari itu kita bisa mengetahui tipe data dengan fungsi type().

#setting the specifixc Data type
#jika kita ingin menyentukan tipe data tertentu pada saat membuat variabel, kita bisa menggunakan constructor fungsi:
# 5 contoh dari atas:
a = str("loscarafterdesign") # maka a bertipe string
print (a)
print (type(a)) 
#output: loscarafterdesign dan <class 'str'>
b = int(15) # maka b bertipe integer
print (b)
print (type(b))
#output: 15 dan <class 'int'>
c = float(9.8) # maka c bertipe float
print (c)
print (type(c))
#output: 9.8 dan <class 'float'>
d = complex(3 + 6j) # maka d bertipe complex
print (d)
print (type(d))
#output: (3+6j) dan <class 'complex'>
e = list(("loscar", "after", "design")) # maka e bertipe list
print (e)
print (type(e))
#output: ['loscar', 'after', 'design'] dan <class 'list'>

