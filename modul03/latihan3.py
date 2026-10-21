total = 0
banyak = 0

#
durasi = int(input("waktu proses(menit, -1 selesai) :"))
while durasi != -1 :
    total = total + durasi
    banyak = banyak + 1
    durasi = int(input("waktu proses(menit, -1 selesai) :"))
    
if banyak == 0:
   print("Belum ada data yang dimasukkan")
else :
    print("Banyak data", banyak)
    print("Rata-Rata", round (total /banyak,2), "menit")

    #waktu proses (menit, -1 selesai) :10 (true)
    #waktu proses (menit, -1 selesai) :15 (true)
    #waktu proses (menit, -1 selesai) :-1 (false) karena ditandai -1 itu false di while
    #Banyak data 2 (menghitung berdasarkan true)
#rata-rata 12.5 menit (hasil dari pembagian 10 + 15 = 25 : 2 = 12,5 menit)