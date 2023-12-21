import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

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

        if 0 <= int(nilai) <= 100:
            cursor.execute(f"INSERT INTO nilai (nim, kode_matkul, nilai) VALUES ({nim}, {kode_matkul}, {nilai})")
            connection.commit()

            print('---- Nilai untuk nim '+ nim +' berhasil ditambahkan ----')
            print()
        else:
             print('---- Masukkan nilai 0-100 ----')
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
        

        # print('NIM'.ljust(13), end="")
        # print('Nama'.ljust(14), end="")
        # print('Kode Matkul'.ljust(21), end="")
        # print('Nama Matkul'.ljust(30), end="")
        # print('Nilai')

        nilai_mahasiswa = {
             'NIM': [],
             'Nama': [],
             'Kode Matkul': [],
             'Nama Matkul': [],
             'Nilai': [],
        }
        
        # for row in range(len(nilai)):
        #     print(f'{nilai[row][1]}'.ljust(13), end="")
        #     print(f'{nama}'.ljust(14), end="")
        #     print(f'{nilai[row][2]}'.ljust(21), end="")
        #     for r in matkul:
        #         if nilai[row][2] == r[0]:
        #             print(f'{r[1]}'.ljust(30), end="")
        #     print(f'{nilai[row][3]}')
        for row in range(len(nilai)):
            nilai_mahasiswa['NIM'].append(nilai[row][1])
            nilai_mahasiswa['Nama'].append(nama)
            nilai_mahasiswa['Kode Matkul'].append(nilai[row][2])
            for r in matkul:
                if nilai[row][2] == r[0]:
                    nilai_mahasiswa['Nama Matkul'].append(r[1])
            nilai_mahasiswa['Nilai'].append(nilai[row][3])
        
        df_nilai_mahasiswa = pd.DataFrame(nilai_mahasiswa)

        print(df_nilai_mahasiswa)
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

    if 0 <= int(nilai) <= 100:

        cursor.execute(f"UPDATE nilai SET nilai = {nilai} WHERE nim = {nim} AND kode_matkul={kode_matkul}")
        connection.commit()

        print(f'Mahasiswa dengan nim {nim} berhasil diubah')
        print()
    else:
        print('---- Masukkan nilai 0-100 ----')
        print()

def lihat_statistik_nilai(connection):
        cursor = connection.cursor()

        jumlah = input('Cek 1 atau semua mahasiswa? (1/s) : ')


        if jumlah == '1':
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

            rerata_nilai = np.array([c[3] for c in nilai])

            fungsi_statistik = input('Masukkan fungsi statistik (mean/median/min/max/sum) : ')

            try:
                df_nilai = pd.DataFrame({'nilai': rerata_nilai})
                nilai_statistik = df_nilai[['nilai']].agg([f'{fungsi_statistik}'])
            except:
                print('--- Error dalam melakukan perhitungan ---')
                print()
                return
            
            print(f"{fungsi_statistik} nilai dari {nama} untuk semua matkul adalah: {nilai_statistik['nilai'][fungsi_statistik]}")
            print()
        elif jumlah == 's':
            cursor.execute(f"SELECT * FROM nilai ORDER BY kode_matkul ASC")
            nilai = cursor.fetchall()
            cursor.execute(f"SELECT nama, nim FROM mahasiswa")
            nama = cursor.fetchall()

            nama_mahasiswa = [nama[0] for nama in nama]
            nilai_mahasiswa = {}

            for n in nilai:
                nim = n[1]
                if nim in nilai_mahasiswa:
                    nilai_mahasiswa[nim] += n[3]
                else:
                    nilai_mahasiswa[nim] = n[3]

            plt.bar(nama_mahasiswa, nilai_mahasiswa.values(), color='skyblue')
            plt.xlabel('Mahasiswa')
            plt.ylabel('Nilai')
            plt.title('Nilai Semua Mahasiswa')
            plt.show()
        else:
             print('--- Ketik 1 atau s ---')

def report_nilai(connection):
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM nilai ORDER BY kode_matkul ASC")
        nilai = cursor.fetchall()
        cursor.execute(f"SELECT nama, nim FROM mahasiswa")
        nama = cursor.fetchall()

        nim_mahasiswa = [nama[1] for nama in nama]
        nama_mahasiswa = [nama[0] for nama in nama]
        nilai_mahasiswa = {}
        hasil = []

        for n in nilai:
            nim = n[1]
            if nim in nilai_mahasiswa:
                nilai_mahasiswa[nim] += n[3]
            else:
                nilai_mahasiswa[nim] = n[3]
        nilai_mahasiswa = [nilai for nilai in nilai_mahasiswa.values()]

        for i in nilai_mahasiswa:
            if i >= 90:
                hasil.append('A')
            elif i >= 80:
                hasil.append('B')
            elif i >= 70:
                hasil.append('C')
            elif i >= 60:
                hasil.append('D')
            elif i >= 50:
                hasil.append('E')
            else:
             hasil.append('X')

        with open('report.csv', 'w', newline='\n') as File:
                writer = csv.writer(File)
                writer.writerow(['NIM','Nama','Nilai','Hasil'])
                for i in range(len(nama_mahasiswa)):
                    writer.writerow([nim_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i], hasil[i]])