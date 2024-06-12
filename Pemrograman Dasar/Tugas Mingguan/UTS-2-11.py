print("Program Index Massa Tubuh")
print()


tinggi = int(input("Masukkan tinggi: ")) # menginput tinggi
berat = int(input("Masukkan berat: ")) # menginput berat

bmi = berat / (tinggi/100)**2 # menghitung bmi
hasil = None # inisialisasi variabel hasil

# menghitung batas ambang bmi
if bmi < 17:
    hasil = ("Kurus", "Kekurangan berat badan tingkat berat")
elif 17 <= bmi < 18.5:
    hasil = ("Kurus", "Kekurangan berat badan tingkat rendah")
elif 18.5 <= bmi < 25:
    hasil = ("Normal", "Normal")
elif 25 <= bmi <= 27:
    hasil = ("Gemuk", "Kelebihan berat badan tingkat ringan")
elif bmi > 27:
    hasil = ("Gemuk", "Kelebihan berat badan tingkat berat")

# output hasil
print("Hasil:")
print(f"Kelompok: {hasil[0]}")
print(f"Kategori: {hasil[1]}")