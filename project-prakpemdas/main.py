import mysql.connector
from getpass import getpass
from admin import *
from dosen import *
from mahasiswa import *
from datasource import *

def login(role):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if role == 'm':
            username = input('Masukkan nim : ')
            if not username.isnumeric():
                print('---- NIM hanya terdiri dari angka ----')
                return
            db_query = f"SELECT * FROM mahasiswa WHERE nim={username}"
        else:
            username = input('Masukkan username : ')
            db_query = f"SELECT * FROM user WHERE username='{username}'  AND role='{role}'"
        password = getpass('Masukkan password : ')

        cursor.execute(db_query + f" AND password='{password}'")
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
            mahasiswa(user) if user != None else None
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