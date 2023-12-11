import mysql.connector
from datasource import *
from nilai_func import *
from mahasiswa_func import daftar_mahasiswa, data_mahasiswa

def dosen():
    while True:
        akses = input("""Daftar Operasi Dosen:
1: Lihat daftar Mahasiswa
2: Lihat data Mahasiswa
3: Tambah nilai Mahasiswa
4: Lihat nilai Mahasiswa
5: Lihat statistik nilai Mahasiswa
exit: Keluar
Pilihan anda -> """)
        try:
            connection = mysql.connector.connect(**DB_CONFIG)

            match akses:
                case '1':
                    daftar_mahasiswa(connection)
                case '2':
                    data_mahasiswa(connection)
                case '3':
                    tambah_nilai(connection)
                case '4':
                    lihat_nilai(connection)
                case '5':
                    lihat_statistik_nilai(connection)
                case _:
                    print("----- Pilihan yang anda ketikan tidak sesuai! -----")
                    print()
                    continue

        except mysql.connector.Error as e:
            print(e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()