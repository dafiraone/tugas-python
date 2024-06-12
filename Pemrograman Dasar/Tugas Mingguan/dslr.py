print("Muhammad Daffa Deli Junior Irawan")
print("152022003")

nilai_sebelumnya = 0

processing = True
while processing:
    nilai_ketajaman = int(input("Masukkan nilai ketajaman: "))

    if nilai_sebelumnya > nilai_ketajaman:
        print("Putar fokus ke kanan")
    elif nilai_sebelumnya < nilai_ketajaman:
        print("Putar fokus ke kiri")
    else:
        print("Ambil gambar📸")
        processing = False
    nilai_sebelumnya = nilai_ketajaman