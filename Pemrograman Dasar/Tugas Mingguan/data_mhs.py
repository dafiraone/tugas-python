data_mahasiswa = ["Diash", "Firdaus", "Lisa", "Kristiana", "Yusup", "Miftahuddin"]
mahasiswa_aktif = []

for i in range(3):
    mahasiswa_aktif.append(data_mahasiswa[0])
    del data_mahasiswa[0]

print("Mahasiswa aktif:", mahasiswa_aktif)
print("Mahasiswa tidak aktif:", data_mahasiswa)