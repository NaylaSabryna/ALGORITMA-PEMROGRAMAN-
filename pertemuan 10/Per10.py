#Nomer 1
# Daftar harga asli beberapa barang
harga_asli = [10000, 25000, 50000, 75000]

# Menghitung harga setelah diskon 10% untuk setiap barang
harga_diskon = [int(harga * 0.9) for harga in harga_asli]

print(harga_diskon)

#Nomer 2
#  rak sepatu dengan 2 lantai
# Setiap lantai punya 3 kotak
rak_sepatu = [
    ["Sepatu A", "Sepatu B", "Sepatu C"], # Lantai 0 (Atas)
    ["Sepatu D", "Sepatu E", "Sepatu F"]  # Lantai 1 (Bawah)
]

# Cara mengambil "Sepatu E":
# Lantai 1 (Lantai Bawah), Kotak nomor 1 (Tengah)
print(rak_sepatu[1][1])

#Nomer 3
# List multidimensi yang menyimpan data rak buku
# Format: [Nama Genre, [Daftar Judul Buku]]
perpustakaan = [
    ["Fiksi", ["Harry Potter", "Naruto"]],
    ["Non-Fiksi", ["Biografi", "Sejarah"]]
]

# Mengambil judul buku "Naruto"
print(perpustakaan[0][1][1])

#Nomer 4
# Membuat fungsi untuk menghitung luas dengan parameter p dan l
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah: {luas}")

# Memanggil fungsi dengan mengisi nilai parameter (argumen)
hitung_luas(10, 5)

#Kuis 1
# Membuat daftar bilangan 1-10, ambil yang genap, lalu kali 3
hasil_kuis = [x * 3 for x in range(1, 11) if x % 2 == 0]

print(hasil_kuis)

#Kuis 2
# Membuat array 2 dimensi ukuran 3x3 berisi angka 1-9
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Menampilkan seluruh isi array menggunakan perulangan
for baris in matriks:
    print(baris)

#Kuis 3
data = [[2, 4], [6, 8], [10, 12]]

# Menggunakan nested list comprehension untuk meratakan list
flatten = [angka for sublist in data for angka in sublist]

print(flatten)

#Slice 4
# Fungsi untuk menghitung luas persegi panjang
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

# Memanggil fungsi
hasil = hitung_luas(8, 5)

# Menampilkan hasil
print("Luas persegi panjang:", hasil)