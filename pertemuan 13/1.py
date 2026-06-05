#no1

# Membuat tuple
buah = ("apel", "mangga", "jeruk", "pisang")

# Menampilkan seluruh isi tuple
print("Isi tuple:", buah)

# Menampilkan salah satu data pada tuple
print("Data pertama:", buah[0])

# Menampilkan jumlah data dalam tuple
print("Jumlah data:", len(buah))

#no2
# Membuat tuple
buah = ("apel", "mangga", "jeruk")

# Menampilkan isi tuple
print(buah)

# Mengakses salah satu data pada tuple
print("Buah pertama:", buah[0])

# Menghitung jumlah data dalam tuple
print("Jumlah data:", len(buah))

#no3

# Membuat tuple
angka = (1, 2, 3, 4)

# Mengubah tuple dengan cara mengubahnya menjadi list
data = list(angka)

# Memodifikasi data
data[1] = 10

# Mengubah kembali menjadi tuple
angka = tuple(data)

# Menampilkan hasil
print("Tuple setelah dimodifikasi:", angka)

#no4
# 1. Membuat data (Tuple)
nilai_tugas = (80, 90)
nilai_ujian = (75, 85)

# 2. Menggunakan len()
print(len(nilai_tugas))       # Output: 2 (menghitung jumlah data)

# 3. Menggunakan operator +
semua_nilai = nilai_tugas + nilai_ujian
print(semua_nilai)            # Output: (80, 90, 75, 85) (menggabungkan data)

# 4. Menggunakan operator *
nilai_kembar = (50,) * 3
print(nilai_kembar)           # Output: (50, 50, 50) (mengulang data)

# 5. Menggunakan in dan not in
print(90 in semua_nilai)      # Output: True (karena 90 ada di dalam data)
print(100 not in semua_nilai)  # Output: True (karena 100 memang tidak ada)

#no5

# 1. Membuat tuple berisi data koordinat (x, y, z)
titik_koordinat = (10, 20, 30)

# 2. Penugasan simultan (Tuple Unpacking)
x, y, z = titik_koordinat

# 3. Mencetak hasil
print(f"Nilai x: {x}")
print(f"Nilai y: {y}")
print(f"Nilai z: {z}")

#no6

# 1. Membuat dictionary berisi data identitas siswa
identitas_siswa = {
    "nama": "Andi",
    "umur": 17,
    "kota": "Bandung"
}

# 2. Menampilkan seluruh isi dictionary
print(identitas_siswa)

#no7
# Membuat dictionary data siswa
siswa = {
    "nama": "Rian",
    "kelas": 12,
    "jurusan": "IPA"
}

# Mengakses isi menggunakan kunci (key)
print(siswa["nama"])     # Output: Rian
print(siswa.get("kelas")) # Output: 12

#no8
# Membuat dictionary data buku
buku = {
    "judul": "Laskar Pelangi",
    "penulis": "Andrea Hirata",
    "tahun": 2005
}

# Mengambil semua kunci menggunakan method keys()
semua_kunci = buku.keys()
print(semua_kunci)  # Output: dict_keys(['judul', 'penulis', 'tahun'])

#no9
# Membuat dictionary data produk
produk = {
    "nama": "Laptop",
    "harga": 15000000,
    "stok": 5
}

# Mengambil semua nilai menggunakan method values()
semua_nilai = produk.values()
print(semua_nilai)  # Output: dict_values(['Laptop', 15000000, 5])

#no10
# Membuat dictionary data pengguna
pengguna = {
    "nama": "Budi",
    "email": "budi@example.com",
    "status": "aktif"
}

# Mengambil pasangan kunci dan nilai menggunakan method items()
semua_item = pengguna.items()
print(semua_item) 
# Output: dict_items([('nama', 'Budi'), ('email', 'budi@example.com'), ('status', 'aktif')])

#no11
# Membuat dictionary data transaksi
transaksi = {
    "ID": 101,
    "barang": "Buku",
    "harga": 25000
}

# Menghapus pasangan kunci dan nilai terakhir yang dimasukkan
barang_dihapus = transaksi.popitem()

print(f"Data yang dihapus: {barang_dihapus}")
print(f"Sisa dictionary: {transaksi}")
# Output:
# Data yang dihapus: ('harga', 25000)
# Sisa dictionary: {'ID': 101, 'barang': 'Buku'}

#no12

# Membuat dictionary data stok barang
stok = {
    "buku": 10,
    "pensil": 20
}

# Modifikasi nilai dengan mengakses kuncinya
stok["buku"] = 15

# Menambah pasangan kunci dan nilai baru
stok["penghapus"] = 5

print(stok)
# Output: {'buku': 15, 'pensil': 20, 'penghapus': 5}

#no13
# Membuat dictionary data stok barang
stok = {
    "buku": 10,
    "pensil": 20
}

# Modifikasi nilai dengan mengakses kuncinya
stok["buku"] = 15

# Menambah pasangan kunci dan nilai baru
stok["penghapus"] = 5

print(stok)
# Output: {'buku': 15, 'pensil': 20, 'penghapus': 5}

#no14

try:
    angka_pembilang = 10
    angka_pembagi = 0  # Nilai telah diubah menjadi 0
    
    # Melakukan operasi pembagian
    hasil = angka_pembilang / angka_pembagi
    print(f"Hasil pembagian: {hasil}")

except ZeroDivisionError:
    print("Kesalahan: Tidak bisa melakukan pembagian dengan angka nol.")



#no15
# Program menangani beberapa jenis kesalahan sekaligus
try:
    data = [10, 0]
    hasil = data[0] / data[1] # Memicu ZeroDivisionError
    print(hasil)
except (ZeroDivisionError, IndexError) as e:
    print(f"Terjadi kesalahan: {e}")