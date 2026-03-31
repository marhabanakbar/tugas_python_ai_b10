# ============================================================
# TUGAS 4 - Struktur Data Python
# Mata Kuliah : AI B10
# ============================================================


# ============================================================
# 1. LIST – AKSES & MANIPULASI
# ============================================================
print("=" * 60)
print("1. LIST – AKSES & MANIPULASI")
print("=" * 60)

data_list = ["Python", 42, "AI", 3.14, "Belajar", 99, "Coding"]

print(f"List awal       : {data_list}")
print(f"Elemen pertama  : {data_list[0]}")
print(f"Elemen terakhir : {data_list[-1]}")
print(f"Slicing [1:6:2] : {data_list[1:6:2]}")

# append()
print(f"\nSebelum append()  : {data_list}")
data_list.append("Machine Learning")
print(f"Sesudah append()  : {data_list}")

# insert()
print(f"\nSebelum insert()  : {data_list}")
data_list.insert(2, "Data Science")
print(f"Sesudah insert(2) : {data_list}")

# extend()
print(f"\nSebelum extend()  : {data_list}")
data_list.extend(["Deep Learning", "Neural Network"])
print(f"Sesudah extend()  : {data_list}")

# pop()
print(f"\nSebelum pop()     : {data_list}")
item_pop = data_list.pop()
print(f"Sesudah pop()     : {data_list}")
print(f"Item yang dihapus : {item_pop}")

# remove()
print(f"\nSebelum remove()  : {data_list}")
data_list.remove(42)
print(f"Sesudah remove(42): {data_list}")


# ============================================================
# 2. TUPLE – IMMUTABILITY & UNPACKING
# ============================================================
print("\n" + "=" * 60)
print("2. TUPLE – IMMUTABILITY & UNPACKING")
print("=" * 60)

data_tuple = ("Padang", "Jakarta", "Bandung", "Surabaya", "Medan", "Yogyakarta")

print(f"Tuple             : {data_tuple}")
print(f"Panjang tuple     : {len(data_tuple)}")
print(f"Indeks ke-0       : {data_tuple[0]}")
print(f"Indeks ke-2       : {data_tuple[2]}")
print(f"Indeks terakhir   : {data_tuple[-1]}")

# Unpacking dengan *rest
kota1, kota2, *rest = data_tuple
print(f"\nUnpacking:")
print(f"  kota1 = {kota1}")
print(f"  kota2 = {kota2}")
print(f"  *rest = {rest}")

# Tuple bersifat immutable
print(f"\nTuple bersifat IMMUTABLE - tidak bisa diubah nilainya setelah dibuat.")


# ============================================================
# 3. SET – KEUNIKAN & OPERASI HIMPUNAN
# ============================================================
print("\n" + "=" * 60)
print("3. SET – KEUNIKAN & OPERASI HIMPUNAN")
print("=" * 60)

set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}

print(f"Set A             : {set_a}")
print(f"Set B             : {set_b}")

print(f"\nUnion (A | B)             : {set_a | set_b}")
print(f"Intersection (A & B)      : {set_a & set_b}")
print(f"Difference (A - B)        : {set_a - set_b}")
print(f"Symmetric Diff (A ^ B)    : {set_a ^ set_b}")

# Duplikat otomatis hilang
set_duplikat = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"\nSet dengan duplikat {{{1, 2, 2, 3, 3, 3, 4, 4, 4, 4}}} → {set_duplikat}")
print("Duplikat otomatis dihapus oleh Set!")


# ============================================================
# 4. DICTIONARY – KEY/VALUE DASAR
# ============================================================
print("\n" + "=" * 60)
print("4. DICTIONARY – KEY/VALUE DASAR")
print("=" * 60)

mahasiswa = {
    "nama"     : "Marhaban Akbar",
    "nim"      : "2024001234",
    "angkatan" : 2024,
    "kota"     : "Padang"
}

print(f"Data awal         : {mahasiswa}")

# Tambah key baru
mahasiswa["jurusan"] = "Teknik Informatika"
print(f"\nSetelah tambah key 'jurusan'  : {mahasiswa}")

# Ubah nilai key
mahasiswa["kota"] = "Jakarta"
print(f"Setelah ubah 'kota' → Jakarta : {mahasiswa}")

# Hapus key
del mahasiswa["angkatan"]
print(f"Setelah hapus key 'angkatan' : {mahasiswa}")

print(f"\nkeys()   : {list(mahasiswa.keys())}")
print(f"values() : {list(mahasiswa.values())}")
print(f"items()  : {list(mahasiswa.items())}")

print("\nIterasi key: value :")
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")


# ============================================================
# 5. NESTED STRUCTURES
# ============================================================
print("\n" + "=" * 60)
print("5. NESTED STRUCTURES")
print("=" * 60)

daftar_buku = [
    {"judul": "Belajar Python",        "penulis": "Guido van Rossum", "tahun": 2018},
    {"judul": "Deep Learning",         "penulis": "Ian Goodfellow",   "tahun": 2016},
    {"judul": "Clean Code",            "penulis": "Robert C. Martin", "tahun": 2008},
    {"judul": "AI Modern",             "penulis": "Stuart Russell",   "tahun": 2021},
    {"judul": "Data Science Handbook", "penulis": "Jake VanderPlas",  "tahun": 2019},
]

print("Semua judul buku:")
for buku in daftar_buku:
    print(f"  - {buku['judul']} ({buku['tahun']})")

# Filter buku terbit >= 2018
tahun_filter = 2018
buku_baru = [b["judul"] for b in daftar_buku if b["tahun"] >= tahun_filter]
print(f"\nBuku terbit >= {tahun_filter} (list comprehension):")
for judul in buku_baru:
    print(f"  - {judul}")


# ============================================================
# 6. COMPREHENSION & UTILITAS
# ============================================================
print("\n" + "=" * 60)
print("6. COMPREHENSION & UTILITAS")
print("=" * 60)

# List comprehension: angka genap dan kuadrat dari 1-20
angka_genap  = [x for x in range(1, 21) if x % 2 == 0]
angka_kuadrat = [x**2 for x in range(1, 21)]
print(f"Angka genap 1-20  : {angka_genap}")
print(f"Kuadrat 1-20      : {angka_kuadrat}")

# Dict comprehension: genap/ganjil untuk 1-10
genap_ganjil = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(f"\nDict genap/ganjil : {genap_ganjil}")

# Set comprehension: huruf unik dari kalimat
kalimat = "Belajar Python itu Menyenangkan"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf.isalpha()}
print(f"\nKalimat           : '{kalimat}'")
print(f"Huruf unik (set)  : {huruf_unik}")


# ============================================================
# 7. KEANGGOTAAN & PENCARIAN SEDERHANA
# ============================================================
print("\n" + "=" * 60)
print("7. KEANGGOTAAN & PENCARIAN SEDERHANA")
print("=" * 60)

buah_list = ["Apel", "Mangga", "Pisang", "Jeruk", "Semangka"]
buah_set  = {"Apel", "Durian", "Rambutan", "Mangga"}

print(f"List buah : {buah_list}")
print(f"Set buah  : {buah_set}")

# Cek keanggotaan dengan 'in'
cari1 = "Mangga"
cari2 = "Durian"

print(f"\n'{cari1}' in list  → {cari1 in buah_list}")
print(f"'{cari2}' in list  → {cari2 in buah_list}")
print(f"'{cari1}' in set   → {cari1 in buah_set}")
print(f"'{cari2}' in set   → {cari2 in buah_set}")

# Menggunakan index()
if cari1 in buah_list:
    print(f"\nPosisi '{cari1}' di list → indeks {buah_list.index(cari1)}")

if cari2 not in buah_list:
    print(f"'{cari2}' tidak ditemukan di list!")


print("\n" + "=" * 60)
print("Program selesai. Terima kasih!")
print("=" * 60)