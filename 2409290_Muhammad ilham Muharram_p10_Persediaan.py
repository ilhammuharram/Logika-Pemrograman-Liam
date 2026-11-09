print("Logika Pemrograman - Teknik Logistik UPI")
print("Pertemuan 10: Struktur Algoritma")
"""Menghitung total nilai persediaan beserta biaya penyimpanan."""

# Konstanta
TARIF_SIMPAN = 0.02

# Masukan
jumlah_unit = int(input("Jumlah unit     : "))
harga_satuan = float(input("Harga satuan   : "))

# Proses
total_nilai = jumlah_unit * harga_satuan
biaya_simpan = total_nilai * TARIF_SIMPAN
total_akhir = total_nilai + biaya_simpan

# Keluaran
print(f"Nilai persediaan : Rp {total_nilai:.0f}")
print(f"Biaya penyimpanan: Rp {biaya_simpan:.0f}")
print(f"Total            : Rp {total_akhir:.0f}")