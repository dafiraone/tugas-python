"""Palindrome"""
# kata = input("Masukan kata/kalimat : ")
# if kata == kata[::-1]:
#     print(f"{kata} adalah kalimat palindrome!")
# else:
#     print(f"{kata} bukan kalimat palindrome! ({kata[::-1]})")

"""2. tampilkan bilangan ganjil/genap dari 1 sampai angka yang diinput user"""
# angka = int(input("Masukan angka batas atas : "))
# jenis = input("Pilih jenis bilangan (ganjil/genap) : ")

# print(f"Bilangan {jenis} dari 1 hingga {angka} adalah : ")
# for i in range(1, angka+1):
#     if jenis.lower() == "genap":
#         if i % 2 == 0:
#             print(i)
#     elif jenis.lower() == "ganjil":
#         if i % 2 != 0:
#             print(i)

"""3. Membuat program kalkulator"""
hasil_operasi = ""
def kalkulator(operasi, angka1, angka2):
    if operasi == "1":
        return angka1+angka2
    elif operasi == "2":
        return angka1-angka2
    elif operasi == "3":
        return angka1*angka2
    elif operasi == "4":
        return angka1/angka2

print("""Pilih operasi:
1. Pertambahan
2. Pengurangan
3. Perkalian
4. Pembagian""")

a = input("Masukan nomor operasi (1/2/3/4) : ")
b = int(input("Masukkan angka pertama : "))
c = int(input("Masukkan angka kedua : "))

if a == "1":
    hasil_operasi = "Pertambahan"
elif a == "2":
    hasil_operasi = "Pengurangan"
elif a == "3":
    hasil_operasi = "Perkalian"
elif a == "4":
    hasil_operasi = "pembagian"

print(f"Hasil {hasil_operasi} : {kalkulator(a, b, c)}")