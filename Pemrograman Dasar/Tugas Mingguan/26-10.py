"""Numpy"""
import numpy as np

# print(np.zeros(10))
# print(np.ones(10))
# print(np.arange(1, 10, 2))
# print(np.linspace(1, 10, 2))
# print(np.logspace(1, 10, 2))

# myarray = np.array([1,2,3,4,5])

# print(myarray.min())
# print(myarray.max())
# print(myarray.mean())
# print(myarray.sum())
# print(myarray.std())

"""Matplotlib"""
# import matplotlib.pyplot as plt

# xpoints = np.array([0,6])
# ypoints = np.array([0,50])

# plt.plot(xpoints,ypoints)
# plt.xlabel("Label X")
# plt.ylabel("Label Y")

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y)

# plt.show()

"""Algoritma n adalah Happy Number"""

bilangan = input("Masukkan angka : ")
same_number = set()

def cek_happy_number(number):
    hasil = 0

    for angka in number:
        hasil += int(angka)**2
    
    message = ""
    for i in range(len(number)):
        if i == len(number)-1:
            message += number[i] + "^2"
        else:
            message += number[i] + "^2 + "
    print(f"{message} = {hasil}")

    if hasil == 1:
        print(f"{bilangan} adalah happy number")
    elif hasil in same_number:
        print(f"{bilangan} bukan happy number")
    else:
        same_number.add(hasil)
        return cek_happy_number(str(hasil))

cek_happy_number(bilangan)

"""Program jam kerja"""

# jam_kerja = input("Masukkan jam kerja karyawan (pisahkan dengan spasi): ")
# target_jam_kerja = int(input("Masukkan target jam kerja: "))

# import matplotlib.pyplot as plt


# target = [int(number) for number in jam_kerja if number != " "]
# karyawan_memenuhi_target = 0
# karyawan_tidak_memenuhi_target = 0

# for number in target:
#     if number >= target_jam_kerja:
#         karyawan_memenuhi_target += 1
#     else:
#         karyawan_tidak_memenuhi_target += 1

# print("Jumlah karyawan yang mencapai atau melebihi target: " + str(karyawan_memenuhi_target))

# x = np.array(["Mencapai/Melebihi Target", "Tidak Mencapai Target"])
# y = np.array([karyawan_memenuhi_target, karyawan_tidak_memenuhi_target])

# bars = plt.bar(x, y)
# bars[0].set_color("Green")
# bars[1].set_color("Red")
# plt.xlabel("Status Karyawan")
# plt.ylabel("Jumlah Karyawan")
# plt.title("Perbandingan Karyawan yang Mencapai/Melebihi Target dan Tidak")
# plt.show()