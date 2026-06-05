#n0.1
def fungsi_contoh():
    # Variabel lokal 'pesan' hanya ada di sini
    pesan = "Halo, saya variabel lokal!"
    print(pesan)

# Memanggil fungsi
fungsi_contoh()

# Jika kita mencoba mengakses 'pesan' dari luar fungsi:
# print(pesan)  # Ini akan menghasilkan error (NameError)

#no.2
def penjumlahan(x):
    bilangan = 7
    return x + 7
print(penjumlahan(4))

#no.3
bilangan = 2
def perkalian_bilangan(x):
    return x * bilangan
print(perkalian_bilangan(7))

# no.4
total = 10 

def tambah_total():
    global total  # Memberitahu fungsi untuk menggunakan variabel 'total' yang global
    total = total + 5  # Memodifikasi variabel global tersebut

tambah_total()
print(total)  # Hasilnya adalah 15


# kuis imt (no.5)
berat = 65 
tinggi = 1.70

imt = berat / (tinggi * tinggi)

print(f"Berat: {berat}kg, Tinggi: {tinggi}m")
print(f"Hasil IMT: {imt:.2f}")

if imt <= 25.0:
    print("Kategori: Normal")
elif imt <= 27.0:
    print("Kategori: Gemuk")
else:
    print("Kategori: Obesitas")


 #no.6
def cetak_segitiga(n):
    for i in range(1, n + 1):
        print("*" * i)

# Memanggil fungsi
cetak_segitiga(5)

#no.07
def hitung_luas(alas, tinggi):
    """Menghitung luas segitiga berdasarkan alas dan tinggi."""
    return 0.5 * alas * tinggi

# Contoh penggunaan:
alas = 10
tinggi = 5
print(f"Luas segitiga: {hitung_luas(alas, tinggi)}")

#no.08
def hitung_keliling(sisi_a, sisi_b, sisi_c):
    """Menghitung keliling segitiga dengan menjumlahkan ketiga sisinya."""
    return sisi_a + sisi_b + sisi_c

# Contoh penggunaan:
sisi_a, sisi_b, sisi_c = 3, 4, 5
print(f"Keliling segitiga: {hitung_keliling(sisi_a, sisi_b, sisi_c)}")


#kuis faktorisasi(no.9)
n = 5
hasil = 1

for i in range(1, n + 1):
    hasil *= i

print(f"Faktorial dari {n} adalah {hasil}")

# kuis fibonacci(no.10)
jumlah_deret = 10
a, b = 1, 1

print(f"Deret Fibonacci ({jumlah_deret} angka):")
for i in range(jumlah_deret):
    print(a, end=" ")
    # Update nilai untuk iterasi berikutnya
    a, b = b, a + b

#no.11
def faktorial(n):
    # Basis kasus: faktorial 0 atau 1 adalah 1
    if n == 0 or n == 1:
        return 1
    # Langkah rekursif: n * faktorial dari (n-1)
    else:
        return n * faktorial(n - 1)

#no.12
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan untuk urutan ke-6:
print(fibonacci(6)) # Output: 8


