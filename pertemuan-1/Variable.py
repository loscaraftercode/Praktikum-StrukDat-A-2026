#Python Variables
#Membuat variabel di python gak perlu  di deklarasikan data:
x = 20  # x bertipe integer (int)
y ="Python is fun" # y bertipe string (str)
print(x)
print(y)

#casting, kita bisa menentukan tipe data saat membuat variabel:
x = str(5) #maka x bertipe string bukan integer, outuput: '5'
y = int(4) #maka y bertipe integer, output: 4
z = float(6) #maka z bertipe float, output: 6.0

#Get the type
#kita bisa mengetahui tipe data apa pada variabel dengan pakai fungsi type()
a = 7
b = "loscarafterdesign"
print(type(a))  #output: <class 'int'>
print(type(b)) #output: <class 'str'>
# kutip tungga atau ganda bisa digunakan untuk string?
c ="carlos"
# itu sama dengan
c ='carlos'

#case sensitive
# nama Variabole sangat sensitif, jadi huruf besar dan kecil berpengaruh:
d = 20
D = "Duapuluh"
print(d)  # output: 20
#maka D tidak menggantikan d

#Variable Names
# aturan penamaan variabel di python:
varsaya = "loscarafterdesign"#benar
var_saya = "loscarafterdesign"#benar
_var_saya = "loscarafterdesign"#benar
varSaya = "loscarafterdesign"#benar
VARSAYA = "loscarafterdesign"#benar
varsaya2 = "loscarafterdesign"#benar

#2varsaya = "loscarafterdesign"#salah, karena diawali dengan angka
#var-saya = "loscarafterdesign"#salah, karena ada tanda strip (-)
#var saya = "loscarafterdesign"#salah, karena ada spasi

#multi world variable names
# nama variabel bisa lebih dari 1 kata, ada beberapa cara:
myVariableName = "loscarafterdesign"#camel case
MyVariableName = "loscarafterdesign"#pascal case
my_variable_name = "loscarafterdesign"#snake case

#Asign Multiple Values:
#many values to multiple variables
# memungkinkan kita untuk mengisikan sebuah nila ke beberapa variabel sekaligus:
a, b, c = "loscar", "after", "design"
print (a) # output: loscar
print (b) # output: after
print (c) # output: design

#one value to multiple variables
# memungkinkan kita untuk mengisikan sebuah nilai ke beberapa variabel sekaligus:
r = s = t = "Adtercode"
print (r) # output: Adtercode

#unpack a collection
# kita bisa mengunpack sebuah koleksi ke beberapa variabel sekaligus:
pheriferals = ["mouse", "keyboard", "monitor"]
x, y, z = pheriferals
print (x) # outpunya: mouse
print (y) # outpunya: keyboard
print (z) # outpunya: monitor

#output variables
#fungsi print() digunakan untuk menampilkan variabel:
x = "beyond your limits"
print (x) # output: beyond your limits

#fungsi print() dapat menampilkan  beberapa variabel sekaligus yang dipisah dengan koma:
x = "beypnd"
y = "your"
z = "limits"
print (x, y, z) # output: beyond your limits

# sama seperti sebelum nya, kita bisa pakai operator + untuk menggabungkan beberapa variabel:
print (x + y + z)

# untuk angka, operator + akan berfungsi sebagai operasi matematika bukan penggabungan  :
a = 9
b = 8 
print (x + y) #output = 17 

# jika menampilakan teks dan angka dalam satu print(), gunakan koma (,) bukan tanda plus (+):
x = 6
y = "afterdesign"
print(x + y) # akan menghasilkan error

x = 6
y = "afterdesign"
print(x, y) # output: 6 afterdesign (benar) 

#global variable
#jika ada variable yang dibuat diluar fungsi maka itu adalah variabel global dan dapat diakses didalam maupun diluar fungsi:
a = "after"
d = "design"

def myfunc():
    print("loscar " + a + d)

myfunc() # output: loscar afterdesign

# jika ada variabel yang sama dibuat didalam fungsi, maka variabel lokal didalam fungsi akan menggantikan variabel global:
a = "after"

def myfunc():
    a = "design"
    print("loscar " + a)
myfunc() # 

print ("loscar " + a)
# output: loscar design
# output: loscar after 

#the global keyword
# saat membuat variabel di dalam fungsi. variabel itu akan bersifat lokal, dan hanya bisa digunakan dalam fungsi itu
def myfunc():
    global a #untuk membuat variable global dalam fungsi, gunakan kata kunci "global"
    a = "afterdesign"
myfunc()
print ("This is " + a) # output: This is afterdesign")

# pakai kata kunci "global" untuk mengubah variabel global didalam fungsi:
# contoh, untuk mengubah nilai variabel global didalam fungsi, gunakan kata kunci global saat menrujuk variabel itu:
x = "Executive"

def myfunc():
    global x
    x = "Design"
myfunc()
print("loscar " + x) # output: loscar Design
