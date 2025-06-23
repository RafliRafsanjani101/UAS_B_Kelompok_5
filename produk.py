# produk.py
from abc import ABC, abstractmethod

class ProsesProduksi(ABC):
    @abstractmethod
    def adonan(self): pass

    @abstractmethod
    def pengembangan(self): pass

    @abstractmethod
    def panggang(self): pass

    @abstractmethod
    def topping(self): pass

class ProdukRoti(ABC):
    def __init__(self, nama, kode, bahan, biaya, harga):
        self.nama = nama
        self.kode = kode
        self.bahan = bahan  # dict
        self.biaya = biaya
        self.harga = harga

    def tampilkan_info(self):
        print(f"\n--- Informasi Produk ---")
        print(f"Nama: {self.nama}")
        print(f"Kode: {self.kode}")
        print("Bahan:")
        for bhn, jml in self.bahan.items():
            print(f"  - {bhn}: {jml}")
        print(f"Biaya Produksi: {self.biaya}")
        print(f"Harga Jual: {self.harga}")

    def hitung_profit(self, jumlah):
        return (self.harga - self.biaya) * jumlah
