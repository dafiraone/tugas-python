# tahun = int(input("Masukkan tahun: "))

# if tahun % 30 == 0:
#     print(f"{tahun} adalah tahun kabisat dalam kalender hijriah")
# else:
#     print(f"{tahun} bukan tahun kabisat dalam kalender hijriah")

# jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
# nilai_mahasiswa = []

# for mhs in range(jumlah_mahasiswa):
#     nama = input("Masukkan nama mahasiswa ke-" + str(mhs+1) + ": ")
#     nilai_pg = int(input("Masukkan nilai pilihan ganda: "))
#     nilai_essay = int(input("Masukkan nilai essay: "))
#     # nilai_mahasiswa.append({"nama": nama, "nilai_pg": nilai_pg, "nilai_essay": nilai_essay})
#     nilai_ujian = nilai_pg * 0.4 + nilai_essay * 0.6
#     nilai_mahasiswa.append({"nama": nama, "nilai_ujian": nilai_ujian})

# print()


# for i in nilai_mahasiswa:
#     print(f"Mahasiswa: {i['nama']}")
#     print(f"Nilai ujian Mahasiswa: {i['nilai_ujian']}")

# import matplotlib.pyplot as plt

# plt.bar([kamus['nama'] for kamus in nilai_mahasiswa], [kamus['nilai_ujian'] for kamus in nilai_mahasiswa])
# plt.title("Diagram Nilai Ujian Mahasiswa")
# plt.show()

# def kalkulator(operator, input1, input2):
#     fungsi = {
#         "+": input1+input2,
#         "-": input1-input2,
#         "*": input1*input2,
#         "/": input1/input2
#     }
#     # return fungsi.get(operator)
#     return fungsi[operator]

# a = int(input("Masukkan angka pertama : "))
# b = int(input("Masukkan angka kedua : "))
# c = input("Masukan operator (+/-/*//) : ")
# print(kalkulator(c, a, b))

# angka = int(input("Masukkan angka asal: "))

# for i in range(angka, -1, -1):
#     print(f"Sisa angka: {i}")

# username = input("Masukkan username: ")
# password = input("Masukkan password: ")

# kesempatan = 3

# while kesempatan >= 0:
#     print()
#     check_username = input("Masukkan username: ")
#     check_password = input("Masukkan password: ")
#     if check_username == username and check_password == password:
#         print("Selamat, akses diberikan")
#         break
#     elif kesempatan > 0:
#         print("Username atau password salah. sisa kesempatan", kesempatan)
#     kesempatan -= 1
# else:
#     print("Username atau password salah. Akses terblokir")

# angka = int(input("Masukkan angka: "))
# for i in range(1, angka+1):
#     show = ""
#     for j in range(1, i+1):
#         show += (str(j) + " ")
#     print(show.strip())

array1 = ["A", "B", "C", "D", "E"]
array2 = ["E", "A", "F", "C", "G"]
import numpy as np

array1 = np.array(array1)
array2 = np.array(array2)
array3 = np.concatenate((array1,array2))

x = 15
is_prima = True
for i in range(2, x):
    if (x % i) == 0:
        is_prima = False
        break

print(is_prima)



# def Fibonacci(n):

# 	# Check if input is 0 then it will
# 	# print incorrect input
# 	if n < 0:
# 		print("Incorrect input")

# 	# Check if n is 0
# 	# then it will return 0
# 	elif n == 0:
# 		return 0

# 	# Check if n is 1,2
# 	# it will return 1
# 	elif n == 1 or n == 2:
# 		return 1

# 	else:
# 		return Fibonacci(n-1) + Fibonacci(n-2)


# # Driver Program
# print(Fibonacci(9))
