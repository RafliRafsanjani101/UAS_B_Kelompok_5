# Sistem Informasi Produksi dan Manajemen Produk Hanari Bakery
**Repositori: `UAS_B_Kelompok_5`**

Proyek ini merupakan tugas **UAS Mata Kuliah Pemrograman Berorientasi Objek (PBO)** dengan studi kasus sistem produksi toko roti **Hanari Bakery**. Program ini dibangun dengan menerapkan prinsip **OOP** dan prinsip **SOLID** menggunakan bahasa Python.

---

## Fitur Aplikasi

✅ Tambah produk baru  
✅ Tampilkan semua produk  
✅ Hitung estimasi profit berdasarkan jumlah produksi  
✅ Simulasi proses produksi:  
- Pengadonan  
- Pengembangan (jika ada)  
- Pemanggangan  
- Topping  

---

## Struktur Program

`produk.py`  : Berisi abstract class `ProdukRoti` dan interface `ProsesProduksi`  
`roti.py`    : Berisi turunan class roti: `RotiManis`, `Croissant`, `ButterCookies`, dan `Muffin`  
`main.py`    : Berisi program utama dengan menu interaktif CLI  

---

## Penerapan Konsep OOP

### ✅ Abstraction
- Class `ProdukRoti` sebagai abstract class  
- Interface `ProsesProduksi` dengan method wajib: `adonan()`, `pengembangan()`, `panggang()`, `topping()`

### ✅ Inheritance
- Class `RotiManis`, `Croissant`, `ButterCookies`, `Muffin` mewarisi dari `ProdukRoti`

### ✅ Polymorphism
- Method `produksi()` dapat memanggil metode yang sesuai di setiap jenis roti

### ✅ Encapsulation
- Atribut dan method dibungkus dalam class secara modular

---

## Diagram Class

Lihat file `uml_diagram.png` di dalam repositori ini untuk melihat visualisasi struktur class secara lengkap.

---

## Flowchart

Lihat file `Flowchart.png` di dalam repositori ini untuk melihat flowchart dari program ini.
