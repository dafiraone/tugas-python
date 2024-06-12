import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
last_df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for index, row in df.iterrows():
        df.at[index, 'Gaji_meningkat'] = (lambda x: x + (x*0.05))(row['Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print('Sebelum peningkatan 5%')
print(last_df)
print('Setelah peningkatan 5%')
print(df)

last_df = df.copy()

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for index, row in df.iterrows():
        if row['Usia'] > 30:
                df.at[index, 'Gaji_tambahan_diatas_30'] = (lambda x: x + (x*0.02))(row['Gaji_meningkat'])
        else:
                df.at[index, 'Gaji_tambahan_diatas_30'] = (lambda x: x)(row['Gaji_meningkat'])



# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print('Sebelum peningkatan 2% untuk usia > 30')
print(last_df)
print('Setelah peningkatan 2% untuk usia > 30')
print(df)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.