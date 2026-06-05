#no.01
a = 10
b = 10
print(a >= b)

#no.02
# Mengambil input dari user dan mengubahnya menjadi tipe data intenger
n = int(input("Masukkan angka n: "))

# Membandingkan n dengan 100
if n > 100:
    print(True)
elif n < 100:
    print(False)
else:
    print("Angka n sama dengan 100")

#no.03
nilai = 80
if nilai >= 75:
    print ("Di atas rata rata")

#no.04
nilai = 85
if nilai >= 90:
    print("Nilai A")
if nilai >= 80:
    print("Nilai B")
if nilai >= 70:
    print("Nilai C")

#no.05
nilai = 70
if nilai >= 75:
    print("Anda Lulus")
else:
    print("Anda Tidak Lulus")

#no.06
nilai = 85
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
elif nilai >= 70:
    print("Nilai Anda C")
else:
    print("Nilai Anda D")

#no.07
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if angka1 > angka2:
    print("Angka pertama lebih besar dari angka kedua")
elif angka1 < angka2:
    print("Angka pertama lebih kecil dari angka kedua")
else:
    print("Kedua angka sama")

#no.08
# Logika untuk mencari angka terbesar
a = int(input("Masukkan angka:"))
b = int(input("Masukkan angka:"))
c = int(input("Masukkan angka:"))


if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c
#Menampilkan hasil
print(f"Angka terbesar adalah: {terbesar}")

#no.09
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
terbesar = max(angka1, angka2)
print("Angka terbesar adalah:", terbesar)

#no.10
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
terbesar = max(angka1, angka2)
print("Angka terbesar adalah:", terbesar)

