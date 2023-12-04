from time import sleep
from art import *
from random import randrange
from getpass import getpass
from datasource import *
from directory_func import *
from datetime import datetime
import timeit
import os

def loading_ok(message):
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

def loading_rotate(message):
    for _ in range(randrange(3, 8)):
        print(f'{message} |', end='\r')
        sleep(0.1)
        print(f'{message} /', end='\r')
        sleep(0.1)
        print(f'{message} -', end='\r')
        sleep(0.1)
        print(f'{message} \\', end='\r')
        sleep(0.1)

def os_booting():
    os.system('cls' if os.name == 'nt' else 'clear')
    global OS_NAME
    sleep(0.3)
    print('Starting Power-On Self-Test (POST)')
    loading_ok('Verifying CPU')
    loading_ok('Motherboard Test')
    loading_ok('PCI Bus Test')
    loading_ok('RAM Test')
    loading_ok('Storage Drive Test')
    loading_ok('Graphic Card Test')
    loading_ok('I/O Port Test')

    loading_rotate('Booting OS')
    os.system('cls' if os.name == 'nt' else 'clear')

    tprint(OS_NAME, 'larry3d')
    loading_rotate('Booting OS')
    print(f'{console_colors.GREEN}{console_colors.BOLD}{console_colors.UNDERLINE}Booting Success!{console_colors.ENDC}'.rjust(10))
    sleep(0.5)

    for login_chance in range(2, -1, -1):
        global USERNAME
        global PASSWORD
        cred_username = input('Username : ')
        cred_password = getpass('Password : ')

        if cred_username != USERNAME or cred_password != PASSWORD:
            print('Username / Password Salah')
            print('Kesempatan login : ' + str(login_chance))
        else:
            print('\nLogin berhasil')
            print(f'Halo, {console_colors.BOLD}{USERNAME}{console_colors.ENDC}')
            break
        if login_chance == 0:
            global SYSTEM_ON
            SYSTEM_ON = False
            print('Login gagal. mematikan komputer')
            return

    print('\nKetik help untuk melihat perintah yang tersedia\n')



os_booting()

SYSTEM_DATETIME = None
SYSTEM_NEWDATETIME = datetime.now()
SYSTEM_ON = True
SYSTEM_UPTIME = timeit.default_timer()

while SYSTEM_ON is True:
    try:
        command_input = input('Masukkan Perintah> ')


        command_input = command_input.strip().split(' ')
        command_input = [c for c in command_input if len(c) > 0]

        if len(command_input) < 1:
            continue
        elif command_input[len(command_input)-1].lower() == '-h' or command_input[len(command_input)-1].lower() == '--help':
            if command_input[0] == '-h' or command_input[0] == '--help':
                print('Butuh parameter dari perintah yang ada, ketik help untuk melihat perintah yang ada') 
                continue

            command_input.pop(len(command_input)-1)

            str_command = list_to_string(command_input)

            if 'time set' in str_command:
                print('Mengubah tanggal/waktu sistem')
                continue
            elif 'dir make' in str_command:
                print('Membuat direktori ke path yang dituju')
                continue
            elif 'dir del' in str_command:
                print(COMMAND['dir del {directory}'])
                continue
            elif str_command in [c for c in COMMAND]:
                print(COMMAND[str_command])
                continue
            else:
                print(f'{str_command} bukan perintah yang valid!')
                continue
        elif command_input[0].lower() in [c for c in COMMAND]:
            match command_input[0].lower():
                case 'help':
                    for c in COMMAND:
                        print(f'{c}'.ljust(30), end='')
                        print(COMMAND[c].rjust(10))
                case 'os':
                    if len(command_input) < 2:
                        print('SIMULASI SISTEM OPERASI')
                        print(OS_NAME)
                        print(f'By: {console_colors.BOLD}{console_colors.YELLOW}Kelompok E1{console_colors.ENDC}')
                        print('Dibuat menggunakan Bahasa Python dengan tambahan library art')
                    else:
                        match command_input[1].lower():
                            case 'name':
                                print(OS_NAME)
                            case 'changename':
                                new_osname = input("Masukkan nama baru untuk sistem operasi ini (jangan pakai spasi) : ")
                                OS_NAME = new_osname
                                print(f'Sistem Operasi berubah nama menjadi {console_colors.BOLD}{OS_NAME}{console_colors.ENDC}')
                            case 'fancyname':
                                tprint(OS_NAME, 'random')
                            case 'user':
                                print(USERNAME)
                            case 'changeuser':
                                password = getpass('Masukkan password : ')
                                if password == PASSWORD:
                                    new_username = input('Masukkan username baru : ')
                                    USERNAME = new_username
                                    print('Ganti username berhasil')
                                else:
                                    print('Password Salah')
                            case 'changepass':
                                password = getpass('Masukkan password : ')
                                if password == PASSWORD:
                                    new_password = getpass('Masukkan password baru : ')
                                    if new_password == getpass('Masukkan password baru lagi : '):
                                        PASSWORD = new_password
                                        print('Ganti password berhasil')
                                    else:
                                        print('Password tidak sesuai')
                                else:
                                    print('Password Salah')
                            case 'pcinfo':
                                for spec in PC_INFO:
                                    print(f'{spec}'.ljust(30), end='')
                                    print(PC_INFO[spec]['name'].rjust(10))
                            case _:
                                raise CommandNotValidError(f'{list_to_string(command_input)} {console_colors.FAIL}bukan perintah yang valid!{console_colors.ENDC}')
                case 'time':
                    if len(command_input) > 1:
                        match command_input[1].lower():
                            case 'usename':
                                if SYSTEM_DATETIME is None:
                                    print(datetime.now().strftime('%A, %d %B %Y'))
                                    print(datetime.now().strftime('%H:%M:%S'))
                                else:
                                    print(SYSTEM_DATETIME.strftime('%A, %d %B %Y'))
                                    print(SYSTEM_DATETIME.strftime('%H:%M:%S'))
                            case 'uptime':
                                print(f'Sistem telah berjalan {(timeit.default_timer() - SYSTEM_UPTIME):.2f} detik yang lalu')
                            case 'set':
                                if len(command_input) > 2:
                                    match command_input[2].lower():
                                        case 'date':
                                            new_date = input('Masukkan tanggal baru (dd/mm/yyyy): ').split('/')
                                            if len(new_date) < 3:
                                                print("Gunakan '/' untuk membagi tanggal")
                                                continue
                                            current_time = datetime.now().time()
                                            if SYSTEM_DATETIME is None:
                                                SYSTEM_DATETIME = datetime(day=int(new_date[0]), month=int(new_date[1]), year=int(new_date[2]), second=current_time.second, minute=current_time.minute, hour=current_time.hour)
                                            else:
                                                SYSTEM_DATETIME = SYSTEM_DATETIME + (datetime.now() - SYSTEM_NEWDATETIME)
                                                SYSTEM_DATETIME = datetime(day=int(new_date[0]), month=int(new_date[1]), year=int(new_date[2]), second=SYSTEM_DATETIME.second, minute=SYSTEM_DATETIME.minute, hour=SYSTEM_DATETIME.hour)
                                            print(f"Tanggal telah diubah ke {SYSTEM_DATETIME.strftime('%d/%m/%Y')}")
                                            SYSTEM_NEWDATETIME = datetime.now()
                                        case 'time':
                                            new_time = input('Masukkan waktu baru (ss:mm:hh): ').split(':')
                                            if len(new_time) < 3:
                                                print("Gunakan ':' untuk membagi waktu")
                                                continue
                                            current_date = datetime.now().date()
                                            if SYSTEM_DATETIME is None:
                                                SYSTEM_DATETIME = datetime(day=current_date.day, month=current_date.month, year=current_date.year, second=int(new_time[0]), minute=int(new_time[1]), hour=int(new_time[2]))
                                            else:
                                                SYSTEM_DATETIME = SYSTEM_DATETIME + (datetime.now() - SYSTEM_NEWDATETIME)
                                                SYSTEM_DATETIME = datetime(day=SYSTEM_DATETIME.day, month=SYSTEM_DATETIME.month, year=SYSTEM_DATETIME.year, second=int(new_time[0]), minute=int(new_time[1]), hour=int(new_time[2]))
                                            print(f"Waktu telah diubah ke {SYSTEM_DATETIME.strftime('%H:%M:%S')}")
                                            SYSTEM_NEWDATETIME = datetime.now()
                                        case _:
                                            raise CommandNotValidError(f'{console_colors.FAIL}Hanya bisa melakukan operasi ke date/time!{console_colors.ENDC}')
                            case _:
                                raise CommandNotValidError(f'{list_to_string(command_input)} {console_colors.FAIL}bukan perintah yang valid!{console_colors.ENDC}')
                    else:
                        if SYSTEM_DATETIME is None:
                            print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                        else:
                            print((SYSTEM_DATETIME + (datetime.now() - SYSTEM_NEWDATETIME)).strftime('%d/%m/%Y %H:%M:%S'))
                case 'cls':
                    os.system('cls' if os.name == 'nt' else 'clear')
                case 'reboot':
                    os_booting()
                    SYSTEM_UPTIME = timeit.default_timer()
                    continue
                case 'shutdown':
                    loading_rotate('Shutting down')
                    print(f'Goodbye {console_colors.BOLD}{USERNAME}       {console_colors.ENDC}')
                    break
                case 'author':
                    print('Authored By')
                    print(f'{console_colors.BOLD}{console_colors.YELLOW}Kelompok E1{console_colors.ENDC}')
                    print(f'{console_colors.BOLD}{console_colors.YELLOW}Muhammad Daffa Deli Junior Irawan - 152022003{console_colors.ENDC}')
                    print(f'{console_colors.BOLD}{console_colors.YELLOW}Katon Rinantomo - 152022012{console_colors.ENDC}')
                case 'dir':
                    if len(command_input) == 2:
                        CURDIR = command_input[1].split('/')
                        show_dir(DIRECTORY['FD-root'], CURDIR)
                    elif len(command_input) > 2:
                        match command_input[1].lower():
                            case 'del':
                                CURDIR = command_input[2].split('/')
                                CURDIR = [elem for elem in CURDIR if len(elem) > 0] # jika pakai / diakhir tidak akan menambah string kosong
                                delete_dir(DIRECTORY['FD-root'], CURDIR)
                            case 'make':
                                match command_input[2]:
                                    case 'file':
                                        get_type_make_dir(DIRECTORY, 'file')
                                    case 'folder':
                                        get_type_make_dir(DIRECTORY, 'folder')
                                    case _:
                                        print('Hanya bisa melakukan operasi ke file/folder')
                                        continue
                    else:
                        show_dir(DIRECTORY['FD-root'])
        else:
            raise CommandNotValidError(f'{list_to_string(command_input)} {console_colors.FAIL}bukan perintah yang valid!{console_colors.ENDC}')
    except CommandNotValidError as Err:
        print(Err)