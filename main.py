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
