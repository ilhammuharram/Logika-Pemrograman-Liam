
# Konstanta
HARGA_SATUAN = 9000
TARIF_PAJAK = 0.11

# Masukan
jumlah_barang = float(input("Masukkan jumlah barang: "))

# Proses
total_harga = jumlah_barang * HARGA_SATUAN
biaya_pajak = total_harga * TARIF_PAJAK
total_bayar = total_harga + biaya_pajak

# Keluaran
print("Total harga:", total_harga)
print("Biaya pajak:", biaya_pajak)
print("Total bayar:", total_bayar)