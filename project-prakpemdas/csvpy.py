import csv

def data_csv():
    data = []

    with open(f'report.csv', 'r') as File:
        csv_reader = csv.reader(File, delimiter=',')
        for row in csv_reader:
            data.append({'username': row[0], 'password': row[1], 'role': row[2]})
    return data

def register():
    username = input('Masukkan username baru : ')
    password = input('Masukkan password baru : ')
        
    data = data_csv()

    username_ada = False

    for akun in data:
        if username == akun['username']:
            print('---- Username sudah terdaftar!!, silahkan masukan ulang username----')
            username_ada = True
            break
    
    if username_ada == False:
        databaru = {'username': username, 'password': password}
        with open('login.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=databaru.keys())
            writer.writerow(databaru)

def login():
    username = input('Masukkan username : ')
    password = input('Masukkan password : ')

    data = data_csv()

    datalogin = []

    for i in data:
        if username == i['username'] and password == i['password']:
            datalogin.append(i)
            print('---- Selamat anda berhasil login ----')
            print('List Username & Password: ')
            print('Username'.ljust(20), end='')
            print('Password'.ljust(0))
            for d in data:
                print(f"{d['username']}", end='')
                print(f"{d['password']}".rjust(20))
            break
    
    if len(datalogin) == 0:
        print('---- Akun yang anda masukkan tidak terdaftar ----')

def delete():
    username = input('Masukkan username yang ingin dihapus : ')

    data = data_csv()
    data_exist = False

    for i in range(len(data)):
        if username == data[i]['username']:
            data_exist = True
            del data[i]
            print(f'---- {username} sudah dihapus ----')
            with open('login.csv', 'w', newline='\n') as file:
                for i in data:
                    writer = csv.DictWriter(file, fieldnames=i.keys())
                    writer.writerow(i)
            break

    if data_exist != True:
        print('---- Akun yang anda masukkan tidak terdaftar ----')

def update():
    username = input('Masukkan username yang ingin diubah : ')

    data = data_csv()
    data_exist = False

    for i in range(len(data)):
        if username == data[i]['username']:
            data_exist = True
            username_baru = None
            password_baru = None

            if input('Ubah username? (y/n): ').lower() == 'y':
                username_baru = input('Masukkan username baru: ')
            
            if username_baru in [j['username'] for j in data]:
                print(f'{username_baru} sudah ada')
                break

            if input('Ubah password? (y/n): ').lower() == 'y':
                password_baru = input('Masukkan password baru: ')

            if username_baru != None:
                data[i]['username'] = username_baru
            if password_baru != None:
                data[i]['password'] = password_baru

            with open('report.csv', 'w', newline='\n') as file:
                for i in data:
                    print(i)
                    writer = csv.DictWriter(file, fieldnames=i.keys())
                    writer.writerow(i)
                print(f'---- {username} sudah berhasil diupdate ----')
            break

    if data_exist != True:
        print('---- Akun yang anda masukkan tidak terdaftar ----')

while True:
    akses = input("""
    Jika anda sudah memiliki akun silahkan ketik 'login'
    Jika anda belum memiliki akun silahkan ketik 'regis'
    Jika anda ingin hapus akun silahkan ketik 'delete'
    Jika anda ingin ubah akun silahkan ketik 'update'
    -> """)

    if akses == 'login':
        login()
    elif akses == 'regis':
        register()
    elif akses == 'update':
        update()
    elif akses == 'delete':
        delete()
    else:
        print("----- Pilihan yang anda ketikan tidak sesuai ! -----")
        continue