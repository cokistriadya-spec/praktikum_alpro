nama = input("Masukkan nama: ") 
input_nilai = int(input("Masukkan nilai: "))

if input_nilai >= 60:
    print (nama, "anda dinyatakan lulus")
    status = "Lulus"
else:
    print (nama, "anda dinyatakan tidak lulus")
    status = "Tidak Lulus"

if input_nilai >= 90:
    grade = "A"
elif input_nilai >= 80:
    grade = "B"
elif input_nilai >= 70:
    grade = "C"
elif input_nilai >= 60:
    grade = "D"
elif input_nilai < 60:
    grade = "E"

print (nama, "mendapatkan grade", grade, "dengan status", status)