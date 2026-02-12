#Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#bisa didupl;ikasi
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple lenghth
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#create tuple with one item
thistuple = ("apple",)
print(type(thistuple))

#tyuple items data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#data dalam tupple bisa campuran string, boolean dan integers)
tuple1 = ("abc", 34, True, 40, "male")

#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing
#artinya dimulai dari belakang
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).
#artinya indeks kedua akan dihitung tapi sampai index ke 5 tidak dihitung

#jika tidak ada batas atas
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#jika tidak ada batas akhir
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #dihitung dari belakang, maka output:('orange', 'kiwi', 'melon') 

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#Update Tuple

#Change Tuple Values
 x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 

#Add Items
#1. Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#2. Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#bisa pakai del
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #output akan error karena sudah tidak ada

#Python - Unpack Tuples
#unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
#Kalau jumlah variabelnya kurang dari jumlah datanya, kamu bisa tambahin tanda bintang (*) di nama variabel. Nanti, sisa data yang gak kebagian variabel akan dikumpulin jadi satu list di variabel itu.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#output:
#apple
#banana
#['cherry', 'strawberry', 'raspberry']

#contoh astersk di tengah:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#output:
#apple
#['mango', 'papaya', 'pineapple']
#cherry


#loop tuple
#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 

#Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 

#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 

#Python - Join Tuples