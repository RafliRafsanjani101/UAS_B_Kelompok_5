# roti.py
from produk import ProdukRoti, ProsesProduksi

class RotiManis(ProdukRoti, ProsesProduksi):
    def adonan(self): print("Mengaduk adonan roti manis...")
    def pengembangan(self): print("Roti manis dalam proses pengembangan...")
    def panggang(self): print("Roti manis sedang dipanggang...")
    def topping(self): print("Menambahkan topping pada roti manis...")

class Croissant(ProdukRoti, ProsesProduksi):
    def adonan(self): print("Mengaduk adonan croissant...")
    def pengembangan(self): print("Croissant dalam proses pengembangan...")
    def panggang(self): print("Croissant sedang dipanggang...")
    def topping(self): print("Menambahkan topping pada croissant...")

class ButterCookies(ProdukRoti, ProsesProduksi):
    def adonan(self): print("Mengaduk adonan cookies...")
    def pengembangan(self): print("Tidak ada proses pengembangan.")
    def panggang(self): print("Cookies sedang dipanggang...")
    def topping(self): print("Menambahkan topping pada cookies...")

class Muffin(ProdukRoti, ProsesProduksi):
    def adonan(self): print("Mengaduk adonan muffin...")
    def pengembangan(self): print("Muffin dalam proses pengembangan...")
    def panggang(self): print("Muffin sedang dipanggang...")
    def topping(self): print("Menambahkan topping pada muffin...")
