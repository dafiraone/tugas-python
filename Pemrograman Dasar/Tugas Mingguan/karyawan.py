karyawan = [
    {"nama": "Dani", "masa kerja": 2, "gaji": 4200000},
    {"nama": "Duki", "masa kerja": 1, "gaji": 4800000},
    {"nama": "Duke", "masa kerja": 1, "gaji": 5300000},
    {"nama": "Deni", "masa kerja": 5, "gaji": 5900000},
    {"nama": "Dena", "masa kerja": 6, "gaji": 6400000},
]

total_gaji = sum([item["gaji"] for item in karyawan])
print(f"Total Gaji : {total_gaji}")

total_gaji_ganjil = 0
banyak_karyawan = len(karyawan)
for i in range(banyak_karyawan):
    if i % 2 != 0:
        total_gaji_ganjil += karyawan[i]["gaji"]
print(f"Total Gaji Indeks Ganjil : {total_gaji_ganjil}")

rerata_gaji_karyawan = total_gaji_ganjil/banyak_karyawan
print(f"Rata-rata Gaji Seluruh Karyawan : {rerata_gaji_karyawan}")

if rerata_gaji_karyawan < 5000000:
    print("Rata-rata gaji karyawan tidak memenuhi UMR")
else:
    print("Rata-rata gaji karyawan memenuhi UMR")

total_gaji_dengan_kenaikan = 0
for i in range(banyak_karyawan):
    masa_kerja = karyawan[i]["masa kerja"]
    kenaikan_gaji = masa_kerja * 1250000 + karyawan[i]["gaji"]
    nama = karyawan[i]["nama"]
    print(f"Gaji {nama} setelah {masa_kerja} tahun = {kenaikan_gaji}")
    total_gaji_dengan_kenaikan += kenaikan_gaji

print(f"Total gaji setelah kenaikan : {total_gaji_dengan_kenaikan}")