#latihan looping akamulator dan pencacah

TARGET = 50
HARI = 10

total = 0 #akumultor
di_bawah = 0 #pencacah

for hari in range(1,HARI +1):
    produksi = int(input(f"produksi hari ke-{hari}:"))
    total = total + produksi
    if produksi < TARGET :
        di_bawah = di_bawah + 1

print("Total produksi", total)
print("rata - rata per hari", total / HARI)
print("Hari di bawah target :", di_bawah)