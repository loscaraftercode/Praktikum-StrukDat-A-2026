#SeT

#Set ditulis menggunakan tanda kurung kurawal `{ }`.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
#Set tidak dapat memiliki dua item dengan nilai yang sama.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #duplikasi akan diabaikan

#Get the Length of a Set
#Untuk mengetahui berapa banyak item yang dimiliki sebuah set, gunakan fungsi `len()`.

thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

#Set Items - Data Types
#Item dalam set dapat berupa tipe data apa pun:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

#Sebuah set dapat berisi berbagai tipe data yang berbeda:
set1 = {"abc", 34, True, 40, "male"} 

#type()
#Dari sudut pandang Python, set didefinisikan sebagai objek dengan tipe data `set`.

myset = {"apple", "banana", "cherry"}
print(type(myset)) #output: <class 'set'> 

#The set() Constructor
#Kita juga dapat menggunakan konstruktor `set()` untuk membuat sebuah set.
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#Python - Access Set Items
#Access Items
#Kamu tidak dapat mengakses item dalam set dengan menggunakan indeks atau key.
#Namun, kamu bisa melakukan perulangan pada item set menggunakan for loop, atau memeriksa apakah suatu nilai tertentu ada di dalam set dengan menggunakan kata kunci in.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

#Periksa apakah `"banana"` ada di dalam set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #output true
#Periksa apakah `"banana"` tidak ada di dalam set:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset) #output: false

#Change Items & Add Items 
#Setelah sebuah set dibuat, kamu tidak dapat mengubah item-itemnya, tetapi kamu bisa menambahkan item baru.

#Untuk menambahkan satu item ke dalam set, gunakan metode `add()`.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 

#Add Sets
#Untuk menambahkan item dari set lain ke dalam set yang sedang digunakan, gunakan metode `update()`.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 

#Add Any Iterable
#Objek dalam metode `update()` tidak harus berupa set, tetapi bisa berupa objek iterable apa pun (seperti tuple, list, dictionary, dan lain-lain).

#thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 

#Python - Remove Set Items
#Remove Item
#Untuk menghapus sebuah item dalam set, gunakan metode remove() atau discard().
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) #remove()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) #discard()

#pop
#Nilai yang dikembalikan (return value) dari metode `pop()` adalah item yang dihapus(acak)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) 

#clear
#mengosongkan isi set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) 

#del
#menghapus set itu sendiri
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) 


#Python - Loop Sets
#loop items
#Kamu bisa melakukan perulangan pada item-item dalam set dengan menggunakan **for loop**.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

#Python - Join Sets
#Join Sets
#Ada beberapa cara untuk menggabungkan dua atau lebih set di Python.

#Union, mmtode `union()` mengembalikan set baru yang berisi semua item dari kedua set.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

#Kamu bisa menggunakan operator `|` sebagai pengganti metode `union()`, dan hasilnya akan sama.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) 

#Join Multiple Sets
#Semua metode dan operator penggabungan dapat digunakan untuk menggabungkan beberapa set sekaligus.


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) 


#Saat menggunakan operator `|`, pisahkan setiap set dengan operator `|` tambahan.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) 

#Join a Set and a Tuple
#Metode union() memungkinkan kamu untuk menggabungkan sebuah set dengan tipe data lain, seperti list atau tuple. Hasilnya akan tetap berupa set.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) 

#Update
#Metode update() memasukkan semua item dari satu set ke dalam set lainnya.
#update() akan mengubah set asli, dan tidak mengembalikan set baru.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 

#Intersection
#Metode `intersection()` akan mengembalikan set baru yang hanya berisi item-item yang ada di kedua set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) 

#Kamu bisa menggunakan operator `&` sebagai pengganti metode `intersection()`, dan hasilnya akan sama.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) 

#Difference
#Metode `difference()` akan mengembalikan set baru yang hanya berisi item dari set pertama yang tidak terdapat pada set lainnya.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) 

#Kamu bisa menggunakan operator `-` sebagai pengganti metode `difference()`, dan hasilnya akan sama.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) 

#Symmetric Differences
#Metode `symmetric_difference()` akan menyimpan hanya elemen-elemen yang TIDAK ada di kedua set (yaitu elemen yang berbeda di masing-masing set).
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) 


#Kamu bisa menggunakan operator `^` sebagai pengganti metode `symmetric_difference()`, dan hasilnya akan sama.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) 

#Python frozenset

#frozenset adalah versi immutable (tidak dapat diubah) dari set.
#Seperti set, frozenset berisi elemen yang unik (tidak duplikat), tidak berurutan, dan tidak dapat diubah.
#Namun, berbeda dengan set, elemen dalam frozenset tidak dapat ditambahkan maupun dihapus.

#Gunakan konstruktor `frozenset()` untuk membuat sebuah **frozenset** dari objek iterable apa pun.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))