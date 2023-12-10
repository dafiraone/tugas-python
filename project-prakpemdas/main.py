import mysql.connector
from getpass import getpass
from admin import *
from dosen import *
from datasource import *

def login(role):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        username = input('Masukkan username : ')
        password = getpass('Masukkan password : ')

        cursor.execute(f"SELECT * FROM user WHERE username='{username}' AND password='{password}' AND role='{role}'")
        cred = cursor.fetchall()
        if len(cred) > 0:
            print('---- Selamat anda berhasil login ----')
            print()
            return cred[0]
        else:
            print('---- Akun yang anda masukkan tidak terdaftar ----')
            print()
            return None
    except mysql.connector.Error as e:
        print(f'Error connecting to database: {e}')
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    
print('Program Pengelolaan Nilai Mahasiswa')

while True:
    akses = input("""Login Sebagai:
M = Mahasiswa
D = Dosen
A = Admin
Pilihan anda -> """)

    match akses.lower():
        case 'm' | 'mhs' | 'mahasiswa':
            user = login('m')
        case 'd' | 'dsn' | 'dosen':
            user = login('d')
            dosen() if user != None else None
        case 'a' | 'adm' | 'admin':
            user = login('a')
            admin() if user != None else None
        case _:
            print("----- Pilihan yang anda ketikan tidak sesuai! -----")
            print()
            continue