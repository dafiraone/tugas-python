from time import sleep
from art import *
from random import randrange
from getpass import getpass
from sys import exit as exit_os
from datetime import datetime

class console_colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

COMMAND = {
    'help' : 'Dokumentasi setiap perintah',
    'os' : 'Melihat informasi sistem operasi',
    'os name' : 'Melihat nama sistem operasi',
    'os fancyname' : 'Melihat nama sistem operasi dengan ASCII Art',
    'os changename' : 'Mengubah nama sistem operasi',
    'os changepass' : 'Mengubah password login',
    'os pcinfo' : 'Menampilkan informasi spesifikasi komputer',
    'datetime' : 'Menampilkan waktu sekarang',
    'cls' : 'Membersihkan layar',
    'reboot' : 'Boot ulang komputer',
    'shutdown' : 'Mematikan komputer',
    'author' : 'Menampilkan informasi pengembang',
}

PC_INFO = {
    'Motherboard' : {'name': 'MSI PRO B660M-A WIFI DDR4'},
    'CPU' : {'name': 'Intel i5-12400F'},
    'Memory' : {'name': 'Corsair Vengeance LPX 16GB (2x8GB)'},
    'SSD': {'name': 'TEAM MP33 M.2 PCIE 512GB'}, 
    'HDD': {'name' : 'Seagate Barracuda 1TB'},
    'Graphic Card' : {'name': 'Gigabyte Eagle Nvidia RTX 3060 OC 12G (rev 2.0)'},
    'Power Supply' : {'name': 'FSP HV PRO 650W 80+ Bronze'},
    'Keyboard' : {'name': 'Rexus Legionare MX5.2 FINALE TKL'},
    'Display' : {'name': 'Lenovo L24i-30'},
    'Mouse' : {'name': 'Rexus ARKA II RX-107'},
}


def loading(message):
    for i in range(101):
        print(f'{message}'.ljust(40), end='')
        print(f'{i}'.rjust(10), end='')
        print('%', end='')
        if i < 10:
            print('\b\b', end='\r')
        elif i > 99:
            print(f'\b\b\b\b  {console_colors.GREEN}{console_colors.BOLD}{console_colors.UNDERLINE}OK{console_colors.ENDC}'.rjust(10))
        else:
            print('\b\b\b', end='\r')
        sleep(randrange(1, 8)/100)

def list_to_string(lst):
    new_string = ''
    for c in lst:
        new_string += c + ' '
    return new_string[:-1]


def os_booting():
    global OS_NAME
    with open('credentials.txt') as f:
        OS_NAME = f.read().split(',')[2]
    tprint(OS_NAME, 'larry3d')
    sleep(0.3)
    print('Starting Power-On Self-Test (POST)')
    loading('RAM Test')
    loading('Storage Drive Test')
    loading('Graphic Card Test')
    loading('USB Port Test')

    for _ in range(randrange(1, 7)):
        print('Booting OS |', end='\r')
        sleep(0.1)
        print('Booting OS /', end='\r')
        sleep(0.1)
        print('Booting OS -', end='\r')
        sleep(0.1)
        print('Booting OS \\', end='\r')
        sleep(0.1)
        pass
    else:
        print(f'{console_colors.GREEN}{console_colors.BOLD}{console_colors.UNDERLINE}Booting Success!{console_colors.ENDC}'.rjust(10))
        sleep(0.5)

        with open('credentials.txt') as f:
            cred = f.read()
            cred = cred.split(',')
            cred_username = cred[0]
            cred_password = cred[1]

            for login_chance in range(3, 0, -1):
                global USERNAME
                global PASSWORD
                USERNAME = input('Username : ')
                PASSWORD = getpass('Password : ')
                login_chance -= 1
                if cred_username != USERNAME or cred_password != PASSWORD:
                    print('Username / Password Salah')
                    print('Kesempatan login : ' + str(login_chance))
                else:
                    print('\nLogin berhasil')
                    print(f'Halo, {console_colors.BOLD}{USERNAME}{console_colors.ENDC}')
                    break
                if login_chance == 0:
                    print('Login gagal. mematikan komputer')
                    exit_os()

        print('\nKetik help untuk melihat perintah yang tersedia\n')

os_booting()

while True:
    command_input = input('Insert Command> ')

    command_input = command_input.split(' ')

    if command_input[len(command_input)-1].lower() == '-h' or command_input[len(command_input)-1].lower() == '--help':
        if command_input[0] == '-h' or command_input[0] == '--help':
            print('Butuh parameter dari perintah yang ada, ketik help untuk melihat perintah yang ada') 
            continue

        command_input.pop(len(command_input)-1)

        str_command = list_to_string(command_input)

        if str_command in [c for c in COMMAND]:
            print(COMMAND[str_command])
            continue
        else:
            print(f'{str_command} bukan perintah yang valid!')
            continue
    
    if list_to_string(command_input) in [c for c in COMMAND]:
        if command_input[0].lower() == 'help':
            for c in COMMAND:
                print(f'{c}'.ljust(30), end='')
                print(COMMAND[c].rjust(10))
        elif command_input[0].lower() == '':
            continue
        elif command_input[0].lower() == 'datetime':
            print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        elif command_input[0].lower() == 'os':
            if len(command_input) > 1:
                if command_input[1].lower() == 'name':
                    print(OS_NAME)
                elif command_input[1].lower() == 'changename':
                    new_osname = input("Masukkan nama baru untuk sistem operasi ini : ")
                    cred = []
                    with open('credentials.txt') as f:
                        cred = f.read().split(',')
                    cred[2] = new_osname
                    with open('credentials.txt', 'w') as f:
                        f.write(list_to_string(cred).replace(' ', ','))
                        OS_NAME = new_osname
                    print(f'Sistem Operasi berubah nama menjadi {console_colors.BOLD}{new_osname}{console_colors.ENDC}')
                elif command_input[1].lower() == 'fancyname':
                    tprint(OS_NAME, 'random')
                elif command_input[1].lower() == 'changepass':
                    login_cred = []
                    with open('credentials.txt') as f:
                        login_cred = f.read().split(',')

                    password = getpass('Masukkan password : ')
                    if password == login_cred[1]:
                        new_password = getpass('Masukkan password baru : ')
                        if new_password == getpass('Masukkan password baru lagi : '):
                            login_cred[1] = new_password

                            new_cred = ''
                            for i in login_cred:
                                    new_cred += i + ','
                            with open('credentials.txt', 'w') as f:
                                f.write(new_cred[:-1])
                            print('Ganti password berhasil')
                        else:
                            print('Password tidak sesuai')
                    else:
                        print('Password Salah')
                elif command_input[1].lower() == 'pcinfo':
                    for spec in PC_INFO:
                        print(f'{spec}'.ljust(30), end='')
                        print(PC_INFO[spec]['name'].rjust(10))
            else:
                print('SIMULASI SISTEM OPERASI')
                print('By: Kelompok E1')
                print('Dibuat menggunakan Bahasa Python dengan tambahan library art ')
        elif command_input[0].lower() == 'cls':
            print('\033[H\033[2J', end="")
        elif command_input[0].lower() == 'reboot':
            os_booting()
        elif command_input[0].lower() == 'shutdown':
            print(f'Goodbye {console_colors.BOLD}{USERNAME}{console_colors.ENDC}')
            break
        elif command_input[0].lower() == 'author':
            print('Authored By')
            print(f'{console_colors.BOLD}{console_colors.YELLOW}Muhammad Daffa Deli Junior Irawan - 152022003{console_colors.ENDC}')
            print(f'{console_colors.BOLD}{console_colors.YELLOW}Katon Rinantomo - 152022012{console_colors.ENDC}')
    else:
        
        print(f'{list_to_string(command_input)} bukan perintah yang valid!')