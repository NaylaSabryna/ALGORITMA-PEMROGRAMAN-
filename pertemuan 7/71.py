#no.01
buah = ["Apel", "Jeruk", "Mangga"]
print(buah[0])
print(buah[2])

#no.02
angka = [12, 10, 17]
for x in angka:
    print("Isi list:", x)

#no.03
hobi = ["Membaca", "Renang", "Coding", "Musik"]
jumlah = len(hobi)
print("Jumlah hobi saya ada:", jumlah)

#no.04
hewan = ["Kucing", "Kelinci", "Burung"]
# Menghapus "Kelinci" dari list
hewan.remove("Kelinci")
print(hewan)

#no.05
warna = ["Merah", "Hijau", "Biru", "Kuning"]
# Mengambil elemen terakhir
print(warna[-1])
# Mengambil elemen kedua dari belakang
print(warna[-2])

#no.06
topi_list = [1, 2, 3, 4, 5]

# Langkah 1: Ganti nilai tengah (indeks 2) dengan input user
topi_list[2] = int(input("Masukkan angka pengganti: "))

# Langkah 2: Hapus elemen terakhir
del topi_list[-1]

# Langkah 3: Tampilkan panjang list
print("Panjang list:", len(topi_list))

print(topi_list)

#no.07
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

###

angka.append(4)

print(len(angka))
print(angka)

###

angka.insert(0, 222)
print(len(angka))
print(angka)

# Tambahkan nilai 333 pada index ke-1
angka.insert(1, 333)
# Print panjang listnya
print(len(angka))
# Print isi listnya
print(angka)

#no.08
my_list = [] # membuat list kosong

# Mengisi list dengan append yang berulang
for i in range(5):
    my_list.append(i + 1)

print(my_list)

#no.09
my_list = [] # membuat list kosong

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

#no.10
my_list = [10, 1, 8, 3, 5]
total = 0

# Menelusuri setiap elemen di dalam list
for i in range(len(my_list)):
    total += my_list[i]

print("Total jumlah isi list:", total)


#no.11
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

# Melakukan penukaran posisi (Swapping)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("List setelah dibalik:", my_list)

#no.12
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


#no.13
# Langkah 1: Buat list kosong dengan nama exo
exo = []
print("Langkah 1: ", exo)

# Langkah 2: Gunakan method append() untuk menambahkan Suho, Kai, Chanyeol, Sehun
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2: ", exo)

# Langkah 3: Gunakan for untuk menambahkan anggota sisa
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for nama in anggota_baru:
    exo.append(nama)
print("Langkah 3: ", exo)

# Langkah 4: Hapus anggota: Kris, Luhan, dan Tao
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4: ", exo)

# Langkah 5: Gunakan method insert() untuk menambahkan Xiumin pada elemen ketiga dari terakhir
# Indeks -2 dipilih agar Xiumin berada tepat di posisi ke-3 jika dihitung dari belakang
exo.insert(-2, "Xiumin")
print("Langkah 5: ", exo)

print("Jumlah anggota exo: ", len(exo))