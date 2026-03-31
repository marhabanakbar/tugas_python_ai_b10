# tugas6.py

# ======================
# IMPORT & SETUP
# ======================
import numpy as np
import pandas as pd
import os
import tempfile

np.random.seed(42)


# ======================
# NUMPY – DATA & STATISTIK
# ======================
nilai_array = np.random.randint(50, 100, size=12)

rata2 = np.mean(nilai_array)
median = np.median(nilai_array)
std_dev = np.std(nilai_array)
nilai_min = np.min(nilai_array)
nilai_max = np.max(nilai_array)


# ======================
# PANDAS – DATAFRAME
# ======================
data = {
    "nama": ["Budi", "Siti", "Andi", "Rina", "Dewi"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_array[:5]
}

df = pd.DataFrame(data)

# Tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


# ======================
# FILE I/O (SUPER SAFE)
# ======================
def get_safe_path(filename="ringkasan_tugas6.txt"):
    # Gunakan folder TEMP Windows (pasti bisa ditulis)
    temp_dir = tempfile.gettempdir()
    return os.path.join(temp_dir, filename)


def tulis_ringkasan(path=None):
    if path is None:
        path = get_safe_path()

    jumlah_data = len(df)
    jumlah_lulus = len(df[df["status"] == "LULUS"])
    jumlah_tidak = len(df[df["status"] == "TIDAK LULUS"])

    with open(path, "w", encoding="utf-8") as file:
        file.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        file.write(f"Rata-rata      : {rata2:.2f}\n")
        file.write(f"Median         : {median:.2f}\n")
        file.write(f"Standar Deviasi: {std_dev:.2f}\n")
        file.write(f"Nilai Minimum  : {nilai_min}\n")
        file.write(f"Nilai Maksimum : {nilai_max}\n\n")

        file.write("=== RINGKASAN DATAFRAME ===\n")
        file.write(f"Jumlah Data    : {jumlah_data}\n")
        file.write(f"Jumlah Lulus   : {jumlah_lulus}\n")
        file.write(f"Tidak Lulus    : {jumlah_tidak}\n")

    print(f"\nFile berhasil dibuat di: {path}")


# ======================
# OOP – GRADEBOOK
# ======================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = self.df[self.df["nilai"] >= threshold]
        return round((len(lulus) / len(self.df)) * 100, 2)

    def save_summary(self, path=None):
        if path is None:
            path = get_safe_path()

        jumlah_data = len(self.df)
        jumlah_lulus = len(self.df[self.df["status"] == "LULUS"])
        jumlah_tidak = len(self.df[self.df["status"] == "TIDAK LULUS"])

        with open(path, "a", encoding="utf-8") as file:
            file.write("\n=== RINGKASAN DARI CLASS GRADEBOOK ===\n")
            file.write(f"Rata-rata Nilai : {self.average()}\n")
            file.write(f"Pass Rate (%)   : {self.pass_rate()}\n")
            file.write(f"Jumlah Data     : {jumlah_data}\n")
            file.write(f"Lulus           : {jumlah_lulus}\n")
            file.write(f"Tidak Lulus     : {jumlah_tidak}\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average()})"


# ======================
# DEMO
# ======================
if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Array Nilai:", nilai_array)
    print(f"Rata-rata: {rata2:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standar Deviasi: {std_dev:.2f}")
    print(f"Min: {nilai_min}")
    print(f"Max: {nilai_max}")

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Average:", gb.average())
    print("Pass Rate (%):", gb.pass_rate())

    # Simpan file
    tulis_ringkasan()
    gb.save_summary()

    print("\nRingkasan berhasil disimpan!")