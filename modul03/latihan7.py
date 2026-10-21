#latihan looping pengelompokan masalah

suhu_tertinggi = None
urutan_tertinggi = 0
count_lebih_80 = 0
total_suhu_lebih_80 = 0
count_suhu_80 = 0

for i in range(1,9):
    suhu = int(input(f"suhu pencatatan ke - {i}"))

    #pola nilai ekstrim
    if suhu_tertinggi is None or suhu > suhu_tertinggi:
        suhu_tertinggi = suhu
        urutan_tertinggi = i

        #pola penyaringan + pencacah + akumulator
        if suhu > 80 :
            count_lebih_80 += 1
            total_suhu_lebih_80 += 1
            count_suhu_80 += 1

print(f"suhu tertinggi: {suhu_tertinggi} (pencatatan ke+ {urutan_tertinggi})")

if count_lebih_80 == 0 :
   print("Tidak ada suhu yang melebihi 80")
else :
    print(f"Suhu melebihi 80 : {count_lebih_80} kali")
    print(f"Rata-rata suhu yang melebihi 80: {total_suhu_lebih_80 / count_suhu_80}") 