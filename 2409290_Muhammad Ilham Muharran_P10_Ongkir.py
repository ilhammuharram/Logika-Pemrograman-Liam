
TARIF = 9000

berat = float(input("Berat paket (kg): "))

if berat > 0:
    ongkir = berat * TARIF
    print(f"Ongkir: Rp {ongkir:.0f}")
else:
    print("Berat paket harus lebih dari 0 kg.")
