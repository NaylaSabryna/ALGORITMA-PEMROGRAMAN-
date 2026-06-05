#no.1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

angka = [12, 24, 32, 16, 22]
print("Hasil:", bubble_sort(angka))

#no.2
def interactive_bubble():
    n = int(input("Masukkan jumlah data: "))
    data = []
    for i in range(n):
        item = int(input(f"Data ke-{i+1}: "))
        data.append(item)
    
    print(f"Data awal: {data}")
    
    # Proses sorting
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print(f"Langkah ke-{i+1}: {data}")

interactive_bubble()
data_mahasiswa = [85, 90, 78, 92, 88]

#no.3
data_mahasiswa = [85,90,78,92,88]
# Menggunakan method .sort() untuk mengubah list asli
data_mahasiswa.sort()

print("Data setelah diurutkan:", data_mahasiswa)

#No.4
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
buah.reverse()

print("Hasil Reverse:", buah)

#No.5
list_a = [1, 2, 3]
list_b = list_a 
# Menyalin referensi, bukan data

list_b.append(4)

print("List A:", list_a)
print("List B:", list_b)

#No.6
angka = [0, 10, 20, 30, 40, 50, 60]

# Mengambil data dari indeks 1 sampai SEBELUM indeks 4
sub_angka = angka[1:4]

print("Hasil Slicing:", sub_angka)

#No.7

data = ["A", "B", "C", "D", "E", "F"]

# Mengambil dari indeks 1 (positif) sampai SEBELUM indeks -2 (negatif)
hasil = data[1:-2]

print("Hasil Slice [1:-2]:", hasil)

#No.8
angka = [10, 20, 30, 40, 50, 60, 70]

# Mengambil dari indeks -5 sampai SEBELUM indeks 5
hasil = angka[-5:5]

print("Hasil Slice [-5:5]:", hasil)

#No.9
warna = ["Merah", "Hijau", "Biru", "Kuning", "Ungu"]

# Mengambil semua elemen dari awal sampai sebelum indeks 3
hasil = warna[:3]

print("Hasil Slice [:3]:", hasil)

#No.10
data = [100, 200, 300, 400, 500]

# Mengambil semua elemen mulai dari indeks 2 sampai akhir
hasil = data[2:]

print("Hasil Slice [2:]:", hasil)

#No.11
list_asli = ["Python", "Java", "C++"]
list_salinan = list_asli[:]

list_salinan.append("PHP")

print("List Asli:", list_asli)
print("List Salinan:", list_salinan)

#No.12
angka = [10, 20, 30, 40, 50, 60]

# Menghapus elemen dari indeks 1 sampai sebelum indeks 4
del angka[1:4]

print("Setelah dihapus:", angka)

#No.13
data = ["A", "B", "C", "D"]

# Menggunakan slicing untuk mengosongkan list
data[:] = []

print("Isi data sekarang:", data)

#No.14
kendaraan = ["Mobil", "Motor", "Sepeda"]

# Menghapus variabel list sepenuhnya
del kendaraan

# Mencoba mencetak list yang sudah dihapus akan error
try:
    print(kendaraan)
except NameError:
    print("Variabel kendaraan sudah tidak ditemukan!")
    
#No.15
aftar_nama = ["Nayla", "Sabryna", "Informatika"]

# Memeriksa keberadaan elemen
cek_nama = "Nayla" in daftar_nama

print(f"Apakah 'Nayla' ada di list? {cek_nama}")

if "Python" in daftar_nama:
    print("Python ditemukan!")
else:
    print("Python tidak ada dalam daftar.")
    
#No.16
nim_terdaftar = ["240101", "240102", "240103"]
cek_nim = "240105"

if cek_nim not in nim_terdaftar:
    print(f"NIM {cek_nim} belum terdaftar di sistem.")
else:
    print(f"NIM {cek_nim} sudah ada.")
    
#No.17
nilai_tugas = [80, 90, 75, 85, 95]

total_nilai = sum(nilai_tugas)
rata_rata = total_nilai / len(nilai_tugas)

print(f"Jumlah nilai: {total_nilai}")
print(f"Rata-rata: {rata_rata}")

#No.18
data_stok = ["Buku", "Pensil", "Penghapus", "Penggaris"]
print(f"Stok saat ini: {data_stok}")

# Menambah data dan mengurutkannya
data_stok.append("Spidol")
data_stok.sort()

print("Setelah diperbarui & diurutkan:")
for item in data_stok:
    print(f"- {item}")
    
#No.19 
skor_ujian = [72, 85, 98, 60, 88, 76, 95]

# Mencari nilai tertinggi dan terendah
nilai_tertinggi = max(skor_ujian)
nilai_terendah = min(skor_ujian)

print(f"Daftar Skor: {skor_ujian}")
print(f"Skor Tertinggi: {nilai_tertinggi}")
print(f"Skor Terendah: {nilai_terendah}")

# Menampilkan pesan jika ada yang mendapat nilai sempurna
if 100 in skor_ujian:
    print("Selamat! Ada yang mendapat nilai 100.")
else:
    print("Belum ada yang mendapat nilai sempurna.")

#No.20 (Kuis 21)
ebakan = [3, 7, 11, 42, 34, 49]
hasil_undi = [5, 9, 11, 42, 3, 49]

# Inisialisasi penghitung angka benar
angka_benar = 0

# Cek setiap angka di tebakan
for angka in tebakan:
    if angka in hasil_undi:
        angka_benar += 1

print(f"Tebakan Anda: {tebakan}")
print(f"Hasil Undian: {hasil_undi}")
print(f"Berapa kali menebak dengan benar? {angka_benar} kali")

#No.21 (Kuis 22)

list_awal = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Hint: Gunakan list baru sebagai temporary work area
list_unik = []

for angka in list_awal:
    # Cek apakah angka sudah ada di list baru
    if angka not in list_unik:
        list_unik.append(angka)

print(f"List Awal: {list_awal}")
print(f"List Unik (Tanpa Duplikat): {list_unik}")