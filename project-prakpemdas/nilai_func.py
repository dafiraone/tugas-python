import numpy

def tambah_nilai(connection):
        cursor = connection.cursor()
        nim = input('Masukkan nim mahasiswa : ')
        cursor.execute(f"SELECT nim from mahasiswa")
        if int(nim) not in [c[0] for c in cursor.fetchall()]:
            print(f'Tidak ada mahasiswa dengan nim {nim}')
            print()
            return
        kode_matkul = input('Masukkan kode matakuliah : ')
        cursor.execute(f"SELECT kode from matkul")
        if int(kode_matkul) not in [c[0] for c in cursor.fetchall()]:
            print(f'Tidak ada matkul dengan kode {kode_matkul}')
            print()
            return
        cursor.execute(f"SELECT kode_matkul, nim FROM nilai")
        if tuple([int(kode_matkul), int(nim)]) in cursor.fetchall():
            print('Matkul sudah diberi nilai untuk nim '+ str(nim))
            print()
            return
        nilai = input('Masukkan nilai 0-100 : ')

        cursor.execute(f"INSERT INTO nilai (nim, kode_matkul, nilai) VALUES ({nim}, {kode_matkul}, {nilai})")
        connection.commit()

        print('---- Nilai untuk nim '+ nim +' berhasil ditambahkan ----')
        print()

def lihat_nilai(connection, nim=None):
        cursor = connection.cursor()

        if nim == None:
            nim = input('Masukkan nim mahasiswa yang akan dicek nilainya : ')
        cursor.execute(f"SELECT nim FROM mahasiswa")
        nim_mahasiswa = [c[0] for c in cursor.fetchall()]

        if int(nim) not in nim_mahasiswa:
             print(f'---- Tidak ada mahasiswa dengan nim {nim} ----')
             return

        cursor.execute(f"SELECT * FROM nilai WHERE NIM={nim} ORDER BY nim ASC, kode_matkul ASC")
        nilai = cursor.fetchall()
        cursor.execute(f"SELECT nama FROM mahasiswa WHERE NIM={nim}")
        nama = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT kode, nama FROM matkul")
        matkul = cursor.fetchall()
        
        print('NIM'.ljust(13), end="")
        print('Nama'.ljust(14), end="")
        print('Kode Matkul'.ljust(21), end="")
        print('Nama Matkul'.ljust(30), end="")
        print('Nilai')
        for row in range(len(nilai)):
            print(f'{nilai[row][1]}'.ljust(13), end="")
            print(f'{nama}'.ljust(14), end="")
            print(f'{nilai[row][2]}'.ljust(21), end="")
            for r in matkul:
                if nilai[row][2] == r[0]:
                    print(f'{r[1]}'.ljust(30), end="")
            print(f'{nilai[row][3]}')
        print()

def ubah_nilai(connection):
    cursor = connection.cursor()

    nim = input('Masukkan nim yang akan diubah nilainya : ')
    cursor.execute(f"SELECT nim from nilai")
    if int(nim) not in [c[0] for c in cursor.fetchall()]:
        print(f'Tidak ada nilai mahasiswa dengan nim {nim}')
        print()
        return
    kode_matkul = input('Masukkan kode matakuliah : ')
    cursor.execute(f"SELECT kode_matkul from nilai")
    if int(kode_matkul) not in [c[0] for c in cursor.fetchall()]:
        print(f'Tidak ada nilai matkul dengan kode {kode_matkul}')
        print()
        return
    nilai = input('Masukkan nilai 0-100 : ')
    cursor.execute(f"UPDATE nilai SET nilai = {nilai} WHERE nim = {nim} AND kode_matkul={kode_matkul}")
    connection.commit()

    print(f'Mahasiswa dengan nim {nim} berhasil diubah')
    print()

def lihat_statistik_nilai(connection, nim=None):
        cursor = connection.cursor()

        nim = input('Masukkan nim mahasiswa yang akan dicek nilainya : ')
        cursor.execute(f"SELECT nim FROM mahasiswa")
        nim_mahasiswa = [c[0] for c in cursor.fetchall()]


        if int(nim) not in nim_mahasiswa:
             print(f'---- Tidak ada mahasiswa dengan nim {nim} ----')
             return

        cursor.execute(f"SELECT * FROM nilai WHERE NIM={nim} ORDER BY nim ASC, kode_matkul ASC")
        nilai = cursor.fetchall()

        if len(nilai) < 1:
             print(f'---- Belum ada nilai untuk mahasiswa dengan nim {nim} ----')
             return

        cursor.execute(f"SELECT nama FROM mahasiswa WHERE NIM={nim}")
        nama = cursor.fetchall()[0][0]
        # cursor.execute(f"SELECT kode, nama FROM matkul")
        # matkul = cursor.fetchall()

        rerata_nilai = numpy.array([c[3] for c in nilai])
        rerata_nilai = numpy.mean(rerata_nilai)
        
        print(f'Rerata nilai dari {nama} untuk semua matkul adalah: {rerata_nilai}')

        
        print()