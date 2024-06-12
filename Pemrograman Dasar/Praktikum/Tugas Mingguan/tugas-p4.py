"""Jumlah angka dalam list (ganjil&genap)"""
# list_angka = [23, 93, 56, 233, 23, 6, 47, 11, 93]

# jumlah_ganjil = sum([angka for angka in list_angka if angka % 2 != 0])
# jumlah_genap = sum([angka for angka in list_angka if angka % 2 == 0])
# print(list_angka)
# print(f"SUM angka ganjil: {jumlah_ganjil}")
# print(f"SUM angka genap: {jumlah_genap}")

# """Program Index Massa Tubuh"""
# tinggi = float(input("Masukkan tinggi: "))
# berat = float(input("Masukkan berat: "))
# def BMI(tinggi, berat):
#     IMT = berat / (tinggi/100)**2
#     print(IMT)
#     if IMT < 17:
#         return ("Kurus", "Kekurangan berat badan tingkat berat")
#     elif 17 <= IMT < 18.5:
#         return ("Kurus", "Kekurangan berat badan tingkat rendah")
#     elif 18.5 <= IMT <= 25:
#         return ("Normal", "Normal")
#     elif 25 < IMT <= 27:
#         return ("Gemuk", "Kelebihan berat badan tingkat ringan")
#     elif IMT > 27:
#         return ("Gemuk", "Kelebihan berat badan tingkat berat")


# print("Hasil:")
# kelompok, kategori = BMI(tinggi, berat)
# print("Kelompok: " + kelompok)
# print("Kategori: " + kategori)

"""Program Supplier"""
jumlah_pelanggan = int(input("Masukkan jumlah pelanggan yang akan dimasukkan : "))
pelanggan = []
supplier = []
barang = []

for i in range(jumlah_pelanggan):
    print("Input pelanggan ke-" + str(i+1))
    kode_pelanggan = f"P{i+1}"
    print("Masukkan Kode Pelanggan : " + kode_pelanggan)
    nama_pelanggan = input("Masukkan Nama Pelanggan : ")
    alamat_pelanggan = input("Masukkan Alamat : ")
    pelanggan.append({"kode": kode_pelanggan, "nama": nama_pelanggan, "alamat": alamat_pelanggan, "banyak_barang": 0, "total_transaksi": 0})

    jumlah_supplier = int(input("Masukkan jumlah supplier yang akan dimasukkan : "))
    list_supplier = []
    list_barang = []
    for j in range(jumlah_supplier):
        print("Input Supplier ke-" + str(j+1))
        kode_supplier = f"S{j+1}P{i+1}"
        print("Masukkan Supplier Code : " + kode_supplier)
        nama_supplier = input("Masukkan Nama Supplier : ")
        status_supplier = input("Status? : (tersedia/tidak tersedia): ")
        if status_supplier.lower() == "tersedia":
            pass
        else: continue
        kota_supplier = input("Masukkan Kota : ")
        list_supplier.append({"kode": kode_supplier, "nama": nama_supplier, "status": status_supplier, "kota": kota_supplier})

        jumlah_barang = int(input("Masukkan jumlah barang yang akan dimasukkan : "))
        temp_barang = []
        for k in range(jumlah_barang):
            print("Input barang ke-" + str(k+1))
            kode_barang = f"B{k+1}S{j+1}P{i+1}"
            print("Masukkan Kode Barang : " + kode_barang)
            nama_barang = input("Masukkan Nama barang : ")
            harga_barang = int(input("Masukkan harga : "))
            qty_barang = int(input("Masukkan jumlah : "))
            temp_barang.append({"kode": kode_barang, "nama": nama_barang, "harga": harga_barang, "qty": qty_barang})
            pelanggan[i]["banyak_barang"] += qty_barang
            pelanggan[i]["total_transaksi"] += harga_barang * qty_barang
        list_barang.append(temp_barang)
    
    supplier.append(list_supplier)
    barang.append(list_barang)

print()

pelanggan_jumlah_terbanyak = pelanggan[0]
pelanggan_transaksi_terbanyak = pelanggan[0]
print("Data Pelanggan:")
for i in range(len(pelanggan)):
    print(f'Kode Pelanggan: {pelanggan[i]["kode"]}')
    print(f'Nama Pelanggan: {pelanggan[i]["nama"]}')
    print(f'Alamat: {pelanggan[i]["alamat"]}')
    if pelanggan[i]["banyak_barang"] >= pelanggan_jumlah_terbanyak["banyak_barang"]:
        pelanggan_jumlah_terbanyak = pelanggan[i]
    if pelanggan[i]["total_transaksi"] >= pelanggan_transaksi_terbanyak["total_transaksi"]:
        pelanggan_transaksi_terbanyak = pelanggan[i]

    print("Supplier yang disediakan:")
    for j in range(len(supplier[i])):
        print(f'Supplier Code: {supplier[i][j]["kode"]}')
        print(f'Nama Supplier: {supplier[i][j]["nama"]}')
        print(f'Status: {supplier[i][j]["status"]}')
        print(f'Kota: {supplier[i][j]["kota"]}')

        print("Barang yang Dibeli:")
        for k in range(len(barang[i][j])):
            print(f'Kode Barang: {barang[i][j][k]["kode"]}')
            print(f'Nama Barang: {barang[i][j][k]["nama"]}')
            print(f'Harga: {barang[i][j][k]["harga"]}')
            print(f'Jumlah: {barang[i][j][k]["qty"]}')

print("Pelanggan dengan jumlah barang terbanyak:")
print(pelanggan_jumlah_terbanyak)
print(pelanggan_transaksi_terbanyak)
print(f'Kode pelanggan: {pelanggan_jumlah_terbanyak["kode"]}')
print(f'Nama pelanggan: {pelanggan_jumlah_terbanyak["nama"]}')
print(f'Jumlah Barang: {pelanggan_jumlah_terbanyak["banyak_barang"]}')
print()
print("Pelanggan dengan transaksi terbanyak:")
print(f'Kode pelanggan: {pelanggan_transaksi_terbanyak["kode"]}')
print(f'Nama pelanggan: {pelanggan_transaksi_terbanyak["nama"]}')
print(f'Total transaksi: {pelanggan_transaksi_terbanyak["total_transaksi"]}')