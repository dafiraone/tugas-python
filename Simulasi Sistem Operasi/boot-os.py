# from time import sleep
# from art import *
# from random import randrange
# from getpass import getpass

# class console_colors:
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     ENDC = '\033[0m'

# COMMAND = {
#     'help' : {'deskripsi' : 'Dokumentasi setiap perintah'},
#     'os' : {'deskripsi' : 'Melihat informasi sistem operasi'},
#     'os name' : {'deskripsi' : 'Melihat nama sistem operasi'},
#     'os fancyname' : {'deskripsi' : 'Melihat nama sistem operasi dengan ASCII Art'},
#     'reboot' : {'deskripsi' : 'Boot ulang komputer'},
#     'shutdown' : {'deskripsi' : 'Mematikan komputer'},
#     'author' : {'deskripsi' : 'Menampilkan informasi pengembang'},
#     'exit' : {'deskripsi' : 'Matikan komputer'},
# }

# def loading(message):
#     for i in range(101):
#         print(f'{message}'.ljust(40), end='')
#         print(f'{i}'.rjust(10), end='')
#         print('%', end='')
#         if i < 10:
#             print('\b\b', end='\r')
#         elif i > 99:
#             print(f'\b\b\b\b  {console_colors.OKGREEN}{console_colors.BOLD}{console_colors.UNDERLINE}OK{console_colors.ENDC}'.rjust(10))
#         else:
#             print('\b\b\b', end='\r')
#         sleep(randrange(1, 8)/100)

# def os_booting():
#     tprint(os_name, 'larry3d')
#     sleep(0.3)
#     print('Starting Power-On Self-Test (POST)')
#     # loading('RAM Test')
#     # loading('Storage Drive Test')
#     # loading('Graphic Card Test')
#     # loading('USB Port Test')

#     for _ in range(randrange(1, 7)):
#         print('Booting OS |', end='\r')
#         sleep(0.1)
#         print('Booting OS /', end='\r')
#         sleep(0.1)
#         print('Booting OS -', end='\r')
#         sleep(0.1)
#         print('Booting OS \\', end='\r')
#         sleep(0.1)
#     else:
#         print(f'{console_colors.OKGREEN}{console_colors.BOLD}{console_colors.UNDERLINE}Booting Success!{console_colors.ENDC}'.rjust(10))
#         sleep(0.5)
#         print('\nKetik help untuk melihat perintah yang tersedia\n')

# os_name = 'PY.OS'

# os_booting()

# username = input('Username : ')
# password = getpass('Password : ')


# while True:
#     print('\nKetik help untuk melihat perintah yang tersedia\n')
#     command_input = input('Insert Command> ')

#     if command_input in [c for c in COMMAND]:
#         command_input = command_input.split(' ')

#         if command_input[len(command_input)-1].lower() == '-h' or command_input[len(command_input)-1].lower() == '--help':
#             print(COMMAND[command_input[len(command_input)-2].lower()]['deskripsi'])
#         elif command_input[0].lower() == 'help':
#             for c in COMMAND:
#                 print(f'{c}'.ljust(30), end='')
#                 print(COMMAND[c]['deskripsi'].rjust(10))
#         elif command_input[0].lower() == '':
#             continue
#         elif command_input[0].lower() == 'os':
#             if len(command_input) > 1:
#                 if command_input[1].lower() == 'name':
#                     print(os_name)
#                 elif command_input[1].lower() == 'fancyname':
#                     tprint(os_name, 'random')
#             else:
#                 print('SIMULASI SISTEM OPERASI')
#                 print('By: Kelompok E1')
#                 print('Dibuat menggunakan Bahasa Python dengan tambahan library art ')
#         elif command_input[0].lower() == 'reboot':
#             os_booting()
#         elif command_input[0].lower() == 'shutdown':
#             print(f'Goodbye {username}')
#             break
#         elif command_input[0].lower() == 'author':
#             tprint(os_name, 'random')
#             print('Authored By')
#             print('Muhammad Daffa Deli Junior Irawan - 152022003')
#             print('Katon Rinantomo - 152022012')
#         elif command_input[0].lower() == 'exit':
#             break
#     else:
#         print(f'{command_input} bukan perintah yang valid!')