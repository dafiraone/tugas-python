def tambah_mahasiswa(connection):
        cursor = connection.cursor()
        nama = input('Masukkan nama : ')
        alamat = input('Masukkan alamat : ')
        no_telp = input('Masukkan no telp : ')
        email = input('Masukkan email : ')
        tanggal_lahir = input('Masukkan tanggal lahir (YYYY-MM-DD) : ')
        password = input('Masukkan password: ')

        cursor.execute(f"INSERT INTO mahasiswa (nama, alamat, no_telp, email, tanggal_lahir, password) VALUES ('{nama}', '{alamat}', '{no_telp}', '{email}', '{tanggal_lahir}', '{password}')")
        connection.commit()

        print('---- Mahasiswa '+ nama +' berhasil ditambahkan ----')
        print()

def daftar_mahasiswa(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    rows = cursor.fetchall()

    print('NIM'.ljust(13), end="")
    print('Nama'.ljust(14), end="")
    print('Alamat'.ljust(16), end="")
    print('No. Telp'.ljust(18), end="")
    print('Email'.ljust(20), end="")
    print('Tanggal Lahir'.ljust(23), end="")
    print('Password')
    for mhs in rows:
        print(f'{mhs[0]}'.ljust(13), end="")
        print(f'{mhs[1]}'.ljust(14), end="")
        print(f'{mhs[2]}'.ljust(16), end="")
        print(f'{mhs[3]}'.ljust(18), end="")
        print(f'{mhs[4]}'.ljust(20), end="")
        print(f'{mhs[5]}'.ljust(23), end="")
        print(f'{mhs[6]}')
    print()

def data_mahasiswa(connection):
    cursor = connection.cursor()

    input_search = input('Masukkan nim/nama/alamat/no. telp/email mahasiswa : ')

    cursor.execute(f"SELECT * FROM mahasiswa WHERE nim LIKE '%{input_search}%' OR nama LIKE '%{input_search}%' OR alamat LIKE '%{input_search}%' OR no_telp LIKE '%{input_search}%' OR email LIKE '%{input_search}%'")
    rows = cursor.fetchall()

    print('NIM'.ljust(13), end="")
    print('Nama'.ljust(14), end="")
    print('Alamat'.ljust(16), end="")
    print('No. Telp'.ljust(18), end="")
    print('Email'.ljust(20), end="")
    print('Tanggal Lahir'.ljust(23), end="")
    print('Password')
    for mhs in rows:
        print(f'{mhs[0]}'.ljust(13), end="")
        print(f'{mhs[1]}'.ljust(14), end="")
        print(f'{mhs[2]}'.ljust(16), end="")
        print(f'{mhs[3]}'.ljust(18), end="")
        print(f'{mhs[4]}'.ljust(20), end="")
        print(f'{mhs[5]}'.ljust(23), end="")
        print(f'{mhs[6]}')
    print()

def ubah_mahasiswa(connection):
    cursor = connection.cursor()

    nim = input('Masukkan nim mahasiswa yang akan diubah: ')
    cursor.execute("SHOW COLUMNS FROM mahasiswa")
    columns = [c[0] for c in cursor.fetchall()]
    del columns[0]

    set_columns = ""

    for c in columns:
        confirm = input('Apakah ingin ubah kolom '+c+'? (y/n) ')
        if confirm.lower() == 'y':
            new_data = input('Masukkan data baru untuk kolom '+c+ ' : ')
            set_columns += f"{c}='{new_data}',"
    set_columns = set_columns[:-1]

    cursor.execute(f"UPDATE mahasiswa SET {set_columns} WHERE nim = {nim}")
    connection.commit()

    print(f'Mahasiswa dengan nim {nim} berhasil diubah')
    print()

def hapus_mahasiswa(connection):
    cursor = connection.cursor()

    nim = input('Masukkan nim mahasiswa yang akan dihapus: ')
    cursor.execute(f"DELETE FROM mahasiswa WHERE nim = {nim}")
    connection.commit()

    print(f'Mahasiswa dengan nim {nim} berhasil dihapus')
    print()