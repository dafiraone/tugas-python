import mysql.connector
from datasource import *
from nilai_func import lihat_nilai
from mahasiswa_func import daftar_mahasiswa

def mahasiswa(mahasiswa):
    while True:
        akses = input("""Daftar Operasi Mahasiswa:
1: Lihat daftar nilai
2: Lihat data diri
exit: Keluar
Pilihan anda -> """)
        try:
            connection = mysql.connector.connect(**DB_CONFIG)

            match akses:
                case '1':
                    lihat_nilai(connection, mahasiswa[0])
                case '2':
                    daftar_mahasiswa(connection, mahasiswa[0])
                case 'exit':
                    print()
                    break
                case _:
                    print("----- Pilihan yang anda ketikan tidak sesuai! -----")
                    print()
                    continue

        except mysql.connector.Error as e:
            print(e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()