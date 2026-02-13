#Dictionares
#untuk menampilkan item yang dapat diubah tetapi tidak dapat di duplikat

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items
#untuk menampilikan isi dari item.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicates Not Allowed
# tidak bisa memiiki 2 item yang samaa
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) 

#Dictionary Length
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))


#Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) 

#The dict() Constructor
#bisa pakai dict() untuk bikin dictionary

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#Python - Access Dictionary Items
#Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#bisa paka get() untuk mengaksesnya dengan hasil yang sama
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")

#get keys
#akan menampilkan daftar yang ada dari semnua kunci dari dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
 
#jika ingin menambah item baru , dan akan update senbdirinya
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

#Get Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x) #akan menampilkan isi dari nilai yang ada pada dictionary


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change 
# disini kita bisa mengubah isi dari dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change 
#disini kita bisa menambah itembaru pada dictionary

#Get Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
  # ini mengecek apakah atributnya ada di dictoinary

#Python - Change Dictionary Items

#Change Values
#kita bisa mengubah nilai pada spesifik item berdasarkan atribut yang ada:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


#Update Dictionary
#menggunakan metode update(), untuk memperbarui isi dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) 

#Python - Add Dictionary Items
#Adding Items
#kita bisa menambahkan item baru pada dictionary menggunakan index atribut baru dan memberikan nya nilai
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Update Dictionary
#kita bisa memperbaruhi dictionary dengan item baru, walaupun item sebelumnya tidak ada
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 

#Python - Remove Dictionary Items
#Removing Items
#cada beberapa cara menghapus item dari dictionary

#pop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

#pop item
#menghapus item dengan nama tertentu
#menghapus item yang dimasukan terakhir
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 

#del
# menghapus item dengan nama tertentu
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 

#del juga bisa menghapus dictionary skelaigus
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) 

#clear
# mengosongkan isi dari dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 


#Python - Loop Dictionaries

#loop akan mengembaliikan nilai berupa atribut yang ada pada dictionary. ada beberapa metode:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #ini akan mengembalikan nilai dengan menampilkan semua atribut yang ada pada dictionary satu per satu

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])#ini akan mengembalikan nilai dengan menampilkan semua nilai pada atribut di dictionary satu persatu.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x) #fungsinya sama, tapi bisa menggunakan metode bernama values() untuk menampilkan nilai pada atribut

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x) #fungsinya sama, tapi bisa menggunakan metode bernama keys() untuk menampilkan seluruh atribut yang ada

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y) #disini kita bisa menampilkan keduanya, atribut dan nilainya menggunakan metode items()

#Python - Copy Dictionaries

#Copy a Dictionary
#Ada beberapa cara untuk membuat salinan (copy), salah satu caranya adalah menggunakan metode bawaan Dictionary yaitu `copy()`.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Cara lain untuk membuat salinan adalah dengan menggunakan fungsi bawaan `dict()`.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) 

#Python - Nested Dictionaries
#Nested Dictionaries
#Sebuah dictionary dapat berisi dictionary lainnya, ini disebut sebagai **nested dictionaries** (dictionary bersarang).
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#Atau, jika kamu ingin menambahkan tiga dictionary ke dalam sebuah dictionary baru:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

#Access Items in Nested Dictionaries
#Untuk mengakses item dari nested dictionary, kamu menggunakan nama dictionary-nya, dimulai dari dictionary yang paling luar (outer dictionary):
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

#Loop Through Nested Dictionaries
#Kamu bisa melakukan perulangan (loop) pada sebuah dictionary dengan menggunakan metode `items()` seperti ini:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

