# 1 - Cek Kelipatan 3
# bilangan = int(input("Masukkan Bilangan : ")) # memasukkan nilai yang akan dicek
# print("Kelipatan 3") if bilangan % 3 == 0 else print("Bukan kelipatan 3") # print hasil cek

# 2 - Perulangan dari input user
# nama = input("Masukkan nama kamu : ")
# perulangan = int(input("Masukkan Banyak Perulangan : "))
# for i in range(perulangan): print(f"No {i}. {nama}")

# 3 - Menampilkan nilai beberapa mahasiswa
banyak_mahasiswa = int(input("Masukkan Banyak Mahasiswa : "))

for i in range(banyak_mahasiswa):
    nama = input(f"Masukkan Nama Mhs ke-{i} : ")
    jumlah_matkul = int(input("Jumlah Matkul : "))
    for j in range(jumlah_matkul):
        input(f"Nilai matkul ke-{i} : ")