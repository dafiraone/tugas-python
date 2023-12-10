import mysql.connector
from datasource import *
from mahasiswa_func import *
from nilai_func import *

def admin():
    while True:
        akses = input("""Daftar Operasi Admin:
1: Tambah Mahasiswa
2: Lihat daftar Mahasiswa
3: Lihat data Mahasiswa
4: Ubah data Mahasiswa
5: Hapus Mahasiswa
6: Ubah nilai Mahasiswa
exit: Keluar
Pilihan anda -> """)
        try:
            connection = mysql.connector.connect(**DB_CONFIG)

            match akses:
                case '1':
                    tambah_mahasiswa(connection)
                case '2':
                    daftar_mahasiswa(connection)
                case '3':
                    data_mahasiswa(connection)
                case '4':
                    ubah_mahasiswa(connection)
                case '5':
                    hapus_mahasiswa(connection)
                case '6':
                    ubah_nilai(connection)
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