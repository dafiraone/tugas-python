class console_colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

class CommandNotValidError(Exception):
    pass

def list_to_string(lst):
    new_string = ''
    for c in lst: new_string += c + ' '
    return new_string[:-1]

COMMAND = {
    'help' : 'Dokumentasi setiap perintah',
    'os' : 'Melihat informasi sistem operasi',
    'os name' : 'Melihat nama sistem operasi',
    'os fancyname' : 'Melihat nama sistem operasi dengan ASCII Art',
    'os changename' : 'Mengubah nama sistem operasi',
    'os user' : 'Melihat username yang telah login',
    'os changeuser' : 'Mengubah username user',
    'os changepass' : 'Mengubah password login',
    'os pcinfo' : 'Menampilkan informasi spesifikasi komputer',
    'time' : 'Menampilkan waktu sekarang',
    'time usename' : 'Menampilkan waktu sekarang dengan nama waktu',
    'time uptime' : 'Menampilkan waktu nyala sistem',
    'time set date' : 'Mengubah tanggal sistem',
    'time set time' : 'Mengubah waktu sistem',
    'cls' : 'Membersihkan layar',
    'reboot' : 'Boot ulang komputer',
    'shutdown' : 'Mematikan komputer',
    'author' : 'Menampilkan informasi pengembang',
    'dir' : 'Menampilkan direktori',
    'dir make file' : 'Membuat file di direktori yang dituju',
    'dir make folder' : 'Membuat folder di direktori yang dituju',
    'dir {directory}' : 'Lihat direktori yang dituju. contoh: folder1/folder2',
    'dir del {directory}' : 'Menghapus direktori yang dituju',
}

HARDWARE = {
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

DIRECTORY = {
    'FD-root': {
        'FD-folder1': {
            'FD-folder11': {
                'F-tes.py': {}
            }
        },
        'FD-folder2': {
            'F-wow.py': {}
        },
    }
}

### Kredensial program
USERNAME = 'root'
PASSWORD = 'toor'
OS_NAME = 'PY.OS'