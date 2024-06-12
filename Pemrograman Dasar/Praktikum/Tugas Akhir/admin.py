import mysql.connector
from datasource import *
from mahasiswa_func import *
from nilai_func import *
from matkul_func import *

def admin():
    while True:
        akses = input("""Daftar Operasi Admin:
1: Tambah Mahasiswa
2: Lihat daftar Mahasiswa
3: Lihat data Mahasiswa
4: Ubah data Mahasiswa
5: Hapus Mahasiswa
6: Tambah nilai Mahasiswa
7: Ubah nilai Mahasiswa
8: Lihat nilai Mahasiswa
9: Hapus nilai Mahasiswa
10: Tambah matkul
11: Lihat matkul
12: Ubah matkul
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
                    tambah_nilai(connection)
                case '7':
                    ubah_nilai(connection)
                case '8':
                    lihat_nilai(connection)
                case '9':
                    hapus_nilai(connection)
                case '10':
                    tambah_matkul(connection)
                case '11':
                    lihat_matkul(connection)
                case '12':
                    ubah_matkul(connection)
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