#latihan looping nilai ekstrem dan jebakan inisialisasi

tertinggi = None
bulan_tertinggi = 0

for bulan in range (1,7) :
    laba = int(input (f"laba bulan {bulan} (juta)"))

    if tertinggi is None or laba > tertinggi :
        tertinggi = laba
        bulan_tertinggi = bulan

print(f"laba tertinggi: {tertinggi} juta (bulan ke - {bulan_tertinggi})")