# for i in range(4):
#     print("Hello")

# print()

# i = 0
# while i < 4:
#     print("Hello")
#     i+=1

# print()

# i = 0
# while True:
#     print("Hello")
#     i+=1
#     if i >= 4:
#         break

banyak_nilai = int(input("Masukan Banyaknya Nilai Mahasiswa : "))
nilai_mahasiswa = 0
print(f"Masukkan {banyak_nilai} Nilai Mahasiswa : ")

for i in range(banyak_nilai):
    nilai = int(input(f"Nilai ke-{i+1} = "))
    nilai_mahasiswa += nilai

def hitung_rerata(banyak_nilai, nilai):
    return nilai / banyak_nilai

hasil = hitung_rerata(banyak_nilai, nilai_mahasiswa)
print()
print(f"Nilai rata-rata dari {banyak_nilai} inputan adalah : {hasil}")