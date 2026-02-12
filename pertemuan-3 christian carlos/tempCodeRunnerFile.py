#latihan
class Person:
    def __init__(self, nama, jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur



class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur, gaji):
        super().__init__(nama, jenis_kelamin, umur)
        self._gaji = gaji   # protected

    def get_gaji(self):
        return self._gaji


class Rekening:
    def __init__(self, no_rekening, pin):
        self.no_rekening = no_rekening
        self.__pin = pin   # private

    def get_pin(self):
        return self.__pin

    def set_pin(self, pin_baru):
        self.__pin = pin_baru




p1 = Person("Carlos", "Laki-laki", 20)
print("Nama Person:", p1.nama)
print("Jenis Kelamin:", p1.jenis_kelamin)
print("Umur:", p1.umur)

print()


k1 = Karyawan("Andi", "Laki-laki", 25, 5000000)
print("Nama Karyawan:", k1.nama)
print("Gaji:", k1.get_gaji())

print()


r1 = Rekening("123456789", "1234")
print("No Rekening:", r1.no_rekening)
print("PIN:", r1.get_pin())

r1.set_pin("4321")
print("PIN Baru:", r1.get_pin())
