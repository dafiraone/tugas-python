import re
import requests
from getpass import getpass

# Login

cred = {}
url_public = 'https://daffa-posttest.vercel.app/'

email_regex = r"^[\sa-zA-Z0-9_.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}+$"
password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$"

while True:
    menu = input("""Menu login:
1. Kirim email & password
2. Lihat email & password
3. Exit
Pilihan anda -> """)
    
    match menu:
        case '1':
            while True:
                email = input('Masukkan email : ')
                password = getpass('Masukkan password : ')

                if re.match(email_regex, email) and re.match(password_regex, password):
                    cred['email'] = email
                    cred['password'] = password
                    break
                else:
                    print('--- Email/password tidak valid! ---')
                
            response = requests.post(url_public + 'kirim/', json=cred)
            print(response.json()['message'])
        case '2':
            response_get = requests.get(url_public + 'terima')
            data_get = response_get.json()
            print('Email: ', data_get['cred']['email'])
            print('Password: ', data_get['cred']['password'])
        case '3':
            print('Bye!')
            break
        case _:
            print('Menu tidak ada')