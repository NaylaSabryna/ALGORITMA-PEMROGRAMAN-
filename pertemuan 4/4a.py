#no01
def input_nama():
    nama = input("Masukkan nama:")
    print("Nama kamu adalah:",nama)
input_nama()   

#no02
def input_data(Hello):
   data = input (Hello)
   print("Hasil input", data)
input_data("Masukkan pesan mu:")

#no.03
a = input("Masukkan angka pertama: ")
b = input("Masukkan angka kedua: ")
print (a + b)

#no.04
a = input("Masukkan angka pertama: ")
b = input("Masukkan angka kedua: ")
print (a + b)

#no.05
a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))
hypo = (a**2 + b**2) ** 0.5
print("Sisi miring segitiga adalah:", hypo)

#no.06
kata1 = "Hallo"
kata2 = "Dunia"
hasil = kata1 + " " + kata2
print(hasil)


#no.07
kata1 = "Hallo"
kata2 = "Dunia"
hasil = kata1 + " " + kata2
print(hasil)

#no.08
kata1 = "Hallo"
kata2 = "Dunia"
hasil = kata1 + " " + kata2
print(hasil)

#no.09
nilai = 77.7
print("Nilai akhir: " + str(nilai))

#no.10
nama = "Nayla"
umur =  12
tinggi = 175
print(type(nama))
print(type(umur))
print(type(tinggi))

#no.11
nama = "Nayla"
umur =  12
tinggi = 175
print(type(nama))
print(type(umur))
print(type(tinggi))

#no.12
x = float(input("Masukkan nilai x: "))
# Menghitung dari bagian paling bawah ke atas
y = 1.0 / (x + (1.0 / (x + (1.0 / (x + (1.0 /x))))))
print("Hasil dari variabel y adalah:", y)

#no.13

jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

total_menit = menit + durasi
menit_akhir = total_menit % 60

jam_tambahan = total_menit // 60
jam_akhir = (jam + jam_tambahan) % 24

print(f"Acara akan berakhir pukul {jam_akhir:02d}:{menit_akhir:02d}")



