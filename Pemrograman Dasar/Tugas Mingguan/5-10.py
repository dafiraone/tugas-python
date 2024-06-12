# angka = int(input("Masukkan angka: "))

# if angka % 2 == 0:
#     print(angka, "adalah angka Genap")
# else:
#     print(angka, "adalah angka Ganjil")

while True:
    print("="*30)

    print("""
    Operasi Matematika

    1. Penjumlahan (+)
    2. Pengurangan (-)
    3. Perkalian (*)
    4. Pembagian (/)
    """)
    print("="*30)

    operasi = int(input("Pilih operasi (1/2/3/4): "))

    if operasi == 1 or operasi == 2 or operasi == 3 or operasi == 4:
        bil_pertama = int(input("Masukkan bilangan pertama: "))
        bil_kedua = int(input("Masukkan bilangan kedua: "))
        print("="*30)
        if operasi == 1:
            print(f"Hasil operasi dari {bil_pertama} + {bil_kedua} = {bil_pertama+bil_kedua}")
        elif operasi == 2:
            print(f"Hasil operasi dari {bil_pertama} - {bil_kedua} = {bil_pertama-bil_kedua}")
        elif operasi == 3:
            print(f"Hasil operasi dari {bil_pertama} * {bil_kedua} = {bil_pertama*bil_kedua}")
        elif operasi == 4:
            print(f"Hasil operasi dari {bil_pertama} / {bil_kedua} = {bil_pertama/bil_kedua}")
    else:
        print("Pilih operasi sesuai pilihan angka diatas")
        continue