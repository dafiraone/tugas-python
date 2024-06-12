alamat = "Bandung"
status_nikah = False
nama = input("masukan nama: ")
kelas = input("kelas: ")
prodi = input("prodi: ")
kampus = input("kampus: ")
umur = int(input("umur: "))
tinggibadan = float(input("tinggi_badan:"))

print("nama saya: ", nama)
print("kelas: ", kelas)
print("prodi: ", prodi)
print("hello {} selamat datang di kampus {}".format(nama, kampus))
print("nama saya %s, umur saya %d, tinggi saya %f" %(nama, umur, tinggibadan))
print(nama)
print(alamat)
if status_nikah == True:
    print("Sudah Menikah")
else:
    print("Belum Menikah")

for i in range(5):
    bintang = ""
    for j in range(i+1):
        bintang = bintang + "*"
    print(bintang)

for i in range(1, 5+1): print("*"*i)

list_angka = [3, 69, 20, 5, 10]

terkecil =  list_angka[0]
terbesar =  list_angka[0]

for i in list_angka:
    if i < terkecil:
        terkecil = i
    elif i > terbesar:
        terbesar = i

print("Terkecil: ", terkecil)
print("Terbesar: ", terbesar)