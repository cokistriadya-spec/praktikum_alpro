print("Bilangan ganjil dari 1 sampai 10 (Berhenti jika bertemu 8) ")
for i in range (1, 11):
    if i == 8:
        break
    if 1 % 2 == 1:
        continue
    print(i)
print("Perulangan Selesai")