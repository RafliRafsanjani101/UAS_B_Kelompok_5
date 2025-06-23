# main.py
from roti import RotiManis, Croissant, ButterCookies, Muffin

produk_list = []

def tambah_produk():
    nama = input("Nama produk: ")
    kode = input("Kode produk: ")
    bahan = {}
    jumlah_bahan = int(input("Jumlah bahan: "))
    for _ in range(jumlah_bahan):
        bhn = input("Nama bahan: ")
        jml = input("Jumlah: ")
        bahan[bhn] = jml
    biaya = float(input("Biaya produksi: "))
    harga = float(input("Harga jual: "))

    if "manis" in nama.lower():
        produk = RotiManis(nama, kode, bahan, biaya, harga)
    elif "croissant" in nama.lower():
        produk = Croissant(nama, kode, bahan, biaya, harga)
    elif "cookie" in nama.lower():
        produk = ButterCookies(nama, kode, bahan, biaya, harga)
    elif "muffin" in nama.lower():
        produk = Muffin(nama, kode, bahan, biaya, harga)
    else:
        print("Jenis tidak dikenali.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk.")
        return
    for p in produk_list:
        p.tampilkan_info()

def hitung_profit():
    kode = input("Masukkan kode produk: ")
    jumlah = int(input("Jumlah pcs: "))
    for p in produk_list:
        if p.kode == kode:
            print(f"Estimasi profit: {p.hitung_profit(jumlah)}")
            return
    print("Produk tidak ditemukan.")

def simulasi_produksi():
    kode = input("Masukkan kode produk: ")
    for p in produk_list:
        if p.kode == kode:
            p.adonan()
            p.pengembangan()
            p.panggang()
            p.topping()
            return
    print("Produk tidak ditemukan.")

def menu():
    while True:
        print("""
======== MENU ========
1. Tambah Produk
2. Tampilkan Produk
3. Hitung Profit
4. Simulasi Produksi
5. Keluar
======================
""")
        pilih = input("Pilih menu: ")
        if pilih == '1':
            tambah_produk()
        elif pilih == '2':
            tampilkan_produk()
        elif pilih == '3':
            hitung_profit()
        elif pilih == '4':
            simulasi_produksi()
        elif pilih == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()