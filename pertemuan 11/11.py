#no.01
def tampilkan_pesan():
    print("Fungsi berhasil dipanggil!")

# Memanggil fungsi tanpa argumen
tampilkan_pesan()
#no.02
def periksa_status(aktif):
    if aktif:
        print("Sistem dalam kondisi: ON")
    else:
        print("Sistem dalam kondisi: OFF")

# Memanggil fungsi dengan argumen False
periksa_status(False)

#no.03
def hitung_luas_persegi(sisi):
    return sisi * sisi  # Ekspresi hasil perhitungan dikembalikan

# Menyimpan nilai return ke dalam variabel 'luas'
luas = hitung_luas_persegi(5)

print(f"Luas persegi adalah: {luas}")

#no.04
def simpan_ke_log(pesan):
    print(f"Logging: {pesan}")
    return True  # Fungsi mengembalikan nilai, tapi kita bisa mengabaikannya

# Pemanggilan fungsi tanpa menangkap nilai kembaliannya
simpan_ke_log("Sistem berhasil dimulai")

#no.05
def periksa_data(input_data):
    if input_data is None:
        return "Data belum diisi"
    else:
        return f"Data diterima: {input_data}"

# Memanggil fungsi dengan nilai None
hasil = periksa_data(None)
print(hasil)

#no.06
def hitung_total(daftar_angka):
    return sum(daftar_angka)

angka = [10, 20, 30]
total = hitung_total(angka)
print(total)

#no.07
def tampilkan_daftar(item):
    for i in item:
        print(f"Item: {i}")

# Memanggil dengan list yang berbeda
tampilkan_daftar(["Apel", "Jeruk"])
tampilkan_daftar(["Buku", "Pulpen", "Pensil"])
#no.08
def buat_daftar_angka(n):
    return [i for i in range(1, n + 1)]

hasil = buat_daftar_angka(5)
print(hasil)

#no.09(kuis 23)
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    hasil = tahun_kabisat(th)
    print(th, "->", end=" ")
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")


#no.10(kuis 24)
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12: return None
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
    return hari_per_bulan[bulan - 1]

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(thn, bln, "->", end=" ")
    hasil = hari_didalam_bulan(thn, bln)
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")


#no.11(kuis 25)
def hari_didalam_bulan(tahun, bulan):
    # Memeriksa tahun kabisat untuk bulan Februari
    if bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return 29
        return 28
    # List hari untuk bulan lainnya
    hari_per_bulan = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return hari_per_bulan[bulan - 1]

def validasi_tanggal(tahun, bulan, hari):
    if tahun < 1 or bulan < 1 or bulan > 12:
        return False
    if hari < 1 or hari > hari_didalam_bulan(tahun, bulan):
        return False
    return True

# Contoh:
print(validasi_tanggal(2024, 2, 29)) # True
print(validasi_tanggal(2023, 2, 29)) # False

#no.12(kuis 26)
def cek_prima(n):
    if n < 2:
        return False
    # Mengecek apakah ada pembagi dari 2 sampai n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Contoh penggunaan:
print(cek_prima(7))  # Output: True
print(cek_prima(10)) # Output: False

#no.13(kuis 27)
def cek_prima(n):
    if n < 2:
        return False
    # Optimasi: hanya perlu cek hingga akar kuadrat dari n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# no.14(kuis28)
prima_list = [i for i in range(1, 21) if cek_prima(i)]
print(f"Bilangan prima 1-20: {prima_list}")


def Liter100km_ke_mpg(liter):
    # 1 galon = 3.785411784 liter, 1 mil = 1609.344 meter (1.609344 km)
    return 235.215 / liter

def mpg_ke_Liter100km(mpg):
    return 235.215 / mpg

print(Liter100km_ke_mpg(3.9))
print(mpg_ke_Liter100km(60.3))