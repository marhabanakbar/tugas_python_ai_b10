# ============================================================
# TUGAS 3 - Dasar Python
# Mata Kuliah : AI B10
# ============================================================

# ============================================================
# 1. DEKLARASI VARIABEL DAN TIPE DATA
# ============================================================

nama_kota    = "Padang"          # string
jumlah_siswa = 30                # integer
nilai_rata    = 87.5             # float
lulus        = True              # boolean
mata_pelajaran = ["Matematika", "Bahasa Indonesia", "IPA", "IPS", "Bahasa Inggris"]  # list

print("=" * 50)
print("1. DEKLARASI VARIABEL DAN TIPE DATA")
print("=" * 50)
print(f"Nama Kota     : {nama_kota}     (tipe: {type(nama_kota).__name__})")
print(f"Jumlah Siswa  : {jumlah_siswa}      (tipe: {type(jumlah_siswa).__name__})")
print(f"Nilai Rata-rata: {nilai_rata}    (tipe: {type(nilai_rata).__name__})")
print(f"Status Lulus  : {lulus}       (tipe: {type(lulus).__name__})")
print(f"Mata Pelajaran: {mata_pelajaran}  (tipe: {type(mata_pelajaran).__name__})")


# ============================================================
# 2. MANIPULASI STRING
# ============================================================

kalimat = "Selamat Datang di Kelas Python AI"

print("\n" + "=" * 50)
print("2. MANIPULASI STRING")
print("=" * 50)
print(f"Kalimat asli    : {kalimat}")
print(f"Huruf besar     : {kalimat.upper()}")
print(f"Huruf kecil     : {kalimat.lower()}")
print(f"Panjang string  : {len(kalimat)} karakter")

# Menggabungkan string
sapaan = "Halo" + ", " + nama_kota + "!"
print(f"Gabungan string : {sapaan}")


# ============================================================
# 3. OPERASI MATEMATIKA SEDERHANA
# ============================================================

angka1 = 20
angka2 = 6

print("\n" + "=" * 50)
print("3. OPERASI MATEMATIKA SEDERHANA")
print("=" * 50)
print(f"Angka 1  : {angka1}")
print(f"Angka 2  : {angka2}")
print(f"Penjumlahan (+)       : {angka1} + {angka2} = {angka1 + angka2}")
print(f"Pengurangan (-)       : {angka1} - {angka2} = {angka1 - angka2}")
print(f"Perkalian (*)         : {angka1} * {angka2} = {angka1 * angka2}")
print(f"Pembagian (/)         : {angka1} / {angka2} = {angka1 / angka2:.2f}")
print(f"Pembagian Bulat (//)  : {angka1} // {angka2} = {angka1 // angka2}")
print(f"Sisa Bagi (%)         : {angka1} % {angka2} = {angka1 % angka2}")


# ============================================================
# 4. LIST DAN AKSES ELEMEN
# ============================================================

buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Semangka"]

print("\n" + "=" * 50)
print("4. LIST DAN AKSES ELEMEN")
print("=" * 50)
print(f"List awal          : {buah}")
print(f"Elemen pertama [0] : {buah[0]}")
print(f"Elemen ketiga  [2] : {buah[2]}")
print(f"Elemen terakhir[-1]: {buah[-1]}")

# Menambah item baru
buah.append("Durian")
print(f"\nSetelah append('Durian') : {buah}")

# Menghapus item
buah.remove("Jeruk")
print(f"Setelah remove('Jeruk')  : {buah}")

# Pop elemen terakhir
item_dihapus = buah.pop()
print(f"Setelah pop()            : {buah}  (dihapus: '{item_dihapus}')")


# ============================================================
# 5. INPUT DARI USER
# ============================================================

print("\n" + "=" * 50)
print("5. INPUT DARI USER")
print("=" * 50)

nama_user = input("Masukkan nama Anda : ")
umur_user = input("Masukkan umur Anda : ")

print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
print("Senang bertemu dengan Anda!")

print("\n" + "=" * 50)
print("Program selesai. Terima kasih!")
print("=" * 50)