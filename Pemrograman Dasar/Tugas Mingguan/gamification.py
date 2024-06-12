fitur = input("Masukkan daftar fitur untuk diterapkan konsep gamification: ")

statusAplikasi = input("Aplikasi e-learning sudah ada? ya/tidak: ")
if statusAplikasi == "ya":
    statusAplikasi = True
elif statusAplikasi == "tidak":
    statusAplikasi = False

if statusAplikasi:
    print("Loading... sedang menerapkan fitur  gamification......")
else:
    print("Sedang membuat aplikasi dengan penerapan konsep gamification.....")

print("E-learning sudah menerapkan konsep:", fitur)