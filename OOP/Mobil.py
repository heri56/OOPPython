class Mobil(object):
    def __init__(self, merk):
        print("Mobil Dibuat")
        self.merk = merk
    def __str__(self):
        rep = "Mobil objek\n"
        rep += "Nama: " +self.merk+ "\n"
        return rep
    def namamerkmobil(self):
        print("Nama Merk Mobil", self.merk, "\n")
    def roda(self):
        print("Roda 4")
call1 = Mobil("Avanza")
call2 = Mobil("Xenia")
call1.roda()

call1 = Mobil("Avanza")
call1.namamerkmobil()
call2.namamerkmobil()
input("\n\nPress key")