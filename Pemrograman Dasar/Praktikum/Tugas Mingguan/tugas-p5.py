import numpy as np

"""Gaji[i] Karyawan"""
# gaji = input("Masukkan gaji karyawan (pisahkan dengan spasi): ")
# gaji = gaji.split(' ')
# gaji_matriks = np.array([int(gaji) for gaji in gaji])

# print("Gaji minimum: " + str(gaji_matriks.min()))
# gaji_matriks = gaji_matriks[gaji_matriks != gaji_matriks.min()]
# print("Gaji minimum: " + str(gaji_matriks.max()))
# gaji_matriks = gaji_matriks[gaji_matriks != gaji_matriks.max()]

# hasil = sum(gaji_matriks) / len(gaji_matriks)
# print(f"Gaji rata-rata tidak termasuk gaji minimum dan maksimum: {hasil}")

"""Matrikx m x n"""

# inputan_matriks = input('Masukkan Matriks : ')
# inputan_matriks = inputan_matriks.replace(' ', '')
# inputan_matriks = inputan_matriks.replace('[', '')
# inputan_matriks = inputan_matriks.split(',')

# list_input = []
# temp_list = []

# for elem in inputan_matriks:
#     try:
#         if ']' in elem:
#             elem = elem.replace(']', '')
#             temp_list.append(int(elem))
#             list_input.append(temp_list)
#             temp_list = []
#         else:
#             temp_list.append(int(elem))
#     except:
#         pass

# matriks = np.array(list_input)
# hasil = None

# for rows in range(len(matriks)):
#     row = matriks[rows]
#     min_row = [num for num in row]
#     min_row = min(min_row)
#     for i in range(len(row)):
#         max_col = [num for num in matriks[:, i]]
#         max_col = max(max_col)
#         if min_row == max_col:
#             hasil = max_col

# if hasil:
#     print(matriks)
#     print(f"{hasil} is the only lucky number since it is the minimum in its row and the maximum in its column")

# [[7,9,11], [4,8,7]]

"""Harga Saham"""
saham = input("Masukkan harga saham (pisahkan dengan spasi): ")
saham = saham.split(' ')

saham_matriks = np.array([int(saham) for saham in saham])

saham_min = (0, saham_matriks[0])
for i in range(1, len(saham_matriks)):
    if i+1 == len(saham_matriks)-1:
        if saham_matriks[i+1]< saham_min[1]:
            break
    elif i != len(saham_matriks):
        if saham_matriks[i] < saham_min[1]:
            saham_min = (i, saham_matriks[i])

saham_matriks = saham_matriks[saham_min[0]:len(saham_matriks)]

saham_max = (0, saham_matriks[0])
for i in range(1, len(saham_matriks)):
    if i != len(saham_matriks):
        if saham_matriks[i] > saham_max[1]:
            saham_max = (i, saham_matriks[i])

untung = saham_matriks[saham_max[0]] - saham_matriks[0]

if saham_matriks[saham_max[0]] > saham_matriks[0]:
    print(f"Keuntungan maksimum yang bisa didapat adalah: {saham_matriks[saham_max[0]]} - {saham_matriks[0]} = {untung}")
    import matplotlib.pyplot as plt
    plt.xlabel("Hari")
    plt.ylabel("Hari")
    plt.title("Grafik Harga Saham dan Titik Pembelian/Jualan")
    hari = np.array([i for i in range(1, len(saham_matriks)+1)])
    plt.plot(hari,saham_matriks, marker="o")
    plt.grid(True)
    plt.show()
else:
    print("No transaction are done because profit is 0 or lower")

# 45000 120000 46000 10000
# 5 4 1 3 2 9 1
# 7 1 5 3 6 4
# 3 2 4 3 5 7 5 4 1 2 1 3 7 6 4 8 4