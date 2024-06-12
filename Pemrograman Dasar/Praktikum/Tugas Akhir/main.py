import mysql.connector
from getpass import getpass
from admin import *
from dosen import *
from mahasiswa import *
from datasource import *
import re

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

pattern_mhs = r'\b(?:m|mhs|mahasiswa|\w*m\w*h\w*s\w*w\w*)\b'
pattern_dosen = r'\b(?:d|dsn|dosen|\w*d\w*s\w*n\w*)\b'
pattern_admin = r'\b(?:a|adm|admin|\w*a\w*d\w*m\w*)\b'

while True:
    akses = input("""Login Sebagai:
M = Mahasiswa
D = Dosen
A = Admin
exit: Keluar
Pilihan anda -> """)
    
    if len(re.findall(pattern_mhs, akses, flags=re.IGNORECASE)) > 0:
            user = login('m')
            mahasiswa(user) if user != None else None
    elif len(re.findall(pattern_dosen, akses, flags=re.IGNORECASE)) > 0:
            user = login('d')
            dosen() if user != None else None
    elif len(re.findall(pattern_admin, akses, flags=re.IGNORECASE)) > 0:
            user = login('a')
            admin() if user != None else None
    elif akses == 'exit':
        print()
        break
    else:
        print("----- Pilihan yang anda ketikan tidak sesuai! -----")
        print()
        continue