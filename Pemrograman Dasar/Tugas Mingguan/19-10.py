# kalitambah = lambda a,b,c: a*b+c
# print(kalitambah(3,2,3))

# Latihan 1
"""Program hitung kalori dengan rumus Harris Benedict"""

# kalori_pria = lambda bb, tb, u : 66 + (13.7*bb) + (5*tb) - (6.8*u)
# kalori_wanita = lambda bb, tb, u : 655 + (9.6*bb) + (1.8*tb) - (4.7*u)

# print("""Keterangan
# BB: Berat Badan (kg)
# TB: Tinggi Badan (cm)
# U: Usia (thn)
# """)

# jenis_kelamin = input("Masukan Jenis Kelamin (p/w) : ")
# bb = float(input("Masukan Berat Badan : "))
# tb = float(input("Masukan Tinggi Badan : "))
# u = int(input("Masukan Umur : "))

# if jenis_kelamin == "p":
#     print(f"Kalori anda : {kalori_pria(bb, tb, u)}")
# elif jenis_kelamin == "w":
#     print(f"Kalori anda : {kalori_wanita(bb, tb, u)}")
# else:
#     print("Masukan Jenis kelamin sesuai perintah!")


# Latihan 2
"""Program Supplier"""

jumlah_pelanggan = int(input("Masukkan jumlah pelanggan yang akan dimasukkan : "))
pelanggan = []
supplier = []
barang = []

for i in range(jumlah_pelanggan):
    print("Input pelanggan ke-" + str(i+1))
    kode_pelanggan = input("Masukkan Kode Pelanggan : ")
    nama_pelanggan = input("Masukkan Nama Pelanggan : ")
    alamat_pelanggan = input("Masukkan Alamat : ")
    pelanggan.append({"kode": kode_pelanggan, "nama": nama_pelanggan, "alamat": alamat_pelanggan, "banyak_barang": 0, "total_transaksi": 0})

    jumlah_supplier = int(input("Masukkan jumlah supplier yang akan dimasukkan : "))
    list_supplier = []
    list_barang = []
    for j in range(jumlah_supplier):
        print("Input Supplier ke-" + str(j+1))
        kode_supplier = input("Masukkan Supplier Code : ")
        nama_supplier = input("Masukkan Nama Supplier : ")
        status_supplier = input("Status? tersedia/kosong : ")
        if status_supplier.lower() == "kosong":
            continue
        kota_supplier = input("Masukkan Kota : ")
        list_supplier.append({"kode": kode_supplier, "nama": nama_supplier, "status": status_supplier, "kota": kota_supplier})

        jumlah_barang = int(input("Masukkan jumlah barang yang akan dimasukkan : "))
        temp_barang = []
        for k in range(jumlah_barang):
            print("Input barang ke-" + str(k+1))
            kode_barang = input("Masukkan Kode Barang : ")
            nama_barang = input("Masukkan Nama barang : ")
            harga_barang = int(input("Masukkan harga : "))
            qty_barang = int(input("Masukkan jumlah : "))
            temp_barang.append({"kode": kode_barang, "nama": nama_barang, "harga": harga_barang, "qty": qty_barang})
            pelanggan[i]["banyak_barang"] += qty_barang
            pelanggan[i]["total_transaksi"] += harga_barang * qty_barang
        list_barang.append(temp_barang)
    
    supplier.append(list_supplier)
    barang.append(list_barang)

print(pelanggan)
print(supplier)
print(barang)

print()

pelanggan_jumlah_terbanyak = pelanggan[0]
pelanggan_transaksi_terbanyak = pelanggan[0]
print("Data Pelanggan:")
for i in range(len(pelanggan)):
    print(f'Kode Pelanggan: {pelanggan[i]["kode"]}')
    print(f'Nama Pelanggan: {pelanggan[i]["nama"]}')
    print(f'Alamat Pelanggan: {pelanggan[i]["alamat"]}')
    if pelanggan[i]["banyak_barang"] >= pelanggan_jumlah_terbanyak["banyak_barang"]:
        pelanggan_jumlah_terbanyak = pelanggan[i]
    if pelanggan[i]["total_transaksi"] >= pelanggan_transaksi_terbanyak["total_transaksi"]:
        pelanggan_transaksi_terbanyak = pelanggan[i]
    print(pelanggan_jumlah_terbanyak)
    print(pelanggan_transaksi_terbanyak)

    print("Supplier yang disediakan:")
    for j in range(len(supplier[i])):
        print(f'Kode Supplier: {supplier[i][j]["kode"]}')
        print(f'Nama Supplier: {supplier[i][j]["nama"]}')
        print(f'Status Supplier: {supplier[i][j]["status"]}')
        print(f'Kota Supplier: {supplier[i][j]["status"]}')

        for k in range(len(barang[i][j])):
            print(f'Kode Barang: {barang[i][j][k]["kode"]}')
            print(f'Nama Barang: {barang[i][j][k]["nama"]}')
            print(f'Harga Barang: {barang[i][j][k]["harga"]}')
            print(f'Jumlah Barang: {barang[i][j][k]["qty"]}')

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