#no.01
i = 1
while i <= 7:
    print("Angka ke-", i)
    i += 1

#no.02
pesan = ""
while pesan != "keluar":
    pesan = input("Masukkan kata (ketik 'keluar' untuk berhenti): ")
    print("Anda menulis:", pesan)

#no.03
secret_number = 777

print(
"""
+==============================================+
| Selamat datang di game saya, muggle!         |
| masukkan suatu angka dan tebak               |
| angka berapa yang saya pilih                 |
| untuk kamu.                                  |
| Jadi, berapa angka rahasianya?               |
+==============================================+
""")

# Mulai kodingan di sini
user_guess = 0

# Perulangan while akan berjalan selama tebakan salah
while user_guess != secret_number:
    # Meminta user memasukkan angka bertipe integer
    user_guess = int(input("Masukkan angka tebakanmu: "))
    
    # Mengecek apakah angka yang dimasukkan adalah angka rahasia
    if user_guess != secret_number:
        print("hahaha ! kamu nyangkut deh di Loop saya")
    else:
        # Jika tebakan benar, loop akan berhenti setelah ini
        print("Selamat, Muggle! kamu bebas sekarang!")

print("Game selesai.")

#no.04
angka = 1
while angka <= 10:
    if angka % 2 == 0:
        print(f"{angka} adalah Genap")
    else:
        print(f"{angka} adalah Ganjil")
    angka += 1


#no.05
# List angka sebagai pengganti urutan a sampai e
angka = [10, 20, 30, 40, 50]

for nilai in angka:
    if nilai > 25:
        print(f"Angka {nilai} lebih besar dari 25")
    else:
        print(f"Angka {nilai} lebih kecil atau sama dengan 25")


#no.06
print("Tabel Eksponensial Angka 2:")
for eksponen in range(1, 6):
    hasil = 2 ** eksponen
    print(f"2 pangkat {eksponen} = {hasil}")


#no.07
print("Mencari angka genap di bawah 10:")
for i in range(1, 15):
    if i % 2 != 0: # Jika angka ganjil
        continue   # Lewati dan lanjut ke angka berikutnya
    
    if i > 10:     # Jika angka sudah lebih dari 10
        break      # Hentikan seluruh perulangan
        
    print("Ketemu angka genap:", i)

#no.08
angka_rahasia = 7  # Ini angka yang harus ditebak

print("--- Selamat Datang di Game Tebak Angka Pesulap ---")
print("Pesulap memiliki angka rahasia antara 1 sampai 10.")

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))
    
    if tebakan == angka_rahasia:
        print("Luar biasa! Kamu berhasil menebak angka rahasia pesulap.")
        break  # Menghentikan perulangan karena tebakan benar
    else:
        print("Ha ha! Kamu terjebak dalam perulangan pesulap. Coba lagi!")


#no.09
# Meminta user memasukkan suatu kata
user_word = input("Masukkan sebuah kata: ")

# Mengubah kata menjadi huruf kapital
user_word = user_word.upper()

print("Hasil huruf konsonan:")
for huruf in user_word:
    # Mengecek apakah huruf adalah vokal
    if huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
        continue  # "Memakan" huruf vokal (skip ke huruf berikutnya)
    # Print huruf yang bukan vokal (konsonan)
    print(huruf)

#n0.10
hitung = 1
while hitung <= 3:
    print("Iterasi ke-", hitung)
    hitung += 1
else:
    print("Kondisi while sudah tidak terpenuhi.")

#no.11
hitung = 1
while hitung <= 3:
    print("Iterasi ke-", hitung)
    hitung += 1
else:
    print("Kondisi while sudah tidak terpenuhi.")

#no.12
x = 10
y = 5
print(x > 5 and y < 10)
print(x == 10 or y == 0)
print(not(x == y))

#n0.13
a = 2  # Biner: 10
b = 3  # Biner: 11

print(a and b) # Logical: Menghasilkan nilai b (3) karena a dianggap True
print(a & b)   # Bitwise: 10 & 11 = 10 (Hasilkan 2 secara biner)

#no.14
x = 8

# Geser ke kanan (Right Shift)
kanan = x >> 1

# Geser ke kiri (Left Shift)
kiri = x << 1

print("Hasil geser kanan:", kanan)
print("Hasil geser kiri:", kiri)

#no.15
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)