import pandas as pd

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

def daftar_mahasiswa(connection, mhs=None):
    cursor = connection.cursor()

    if mhs == None:
        cursor.execute("SELECT * FROM mahasiswa")
        rows = cursor.fetchall()

        daftar_mahasiswa = {
            'NIM': [],
            'Nama': [],
            'Alamat': [],
            'No. Telp': [],
            'Email': [],
            'Tanggal Lahir': [],
            'Password': [],
        }

        for mhs in rows:
            daftar_mahasiswa['NIM'].append(mhs[0])
            daftar_mahasiswa['Nama'].append(mhs[1])
            daftar_mahasiswa['Alamat'].append(mhs[2])
            daftar_mahasiswa['No. Telp'].append(mhs[3])
            daftar_mahasiswa['Email'].append(mhs[4])
            daftar_mahasiswa['Tanggal Lahir'].append(mhs[5])
            daftar_mahasiswa['Password'].append(mhs[6])
        
        df_daftar_mahasiswa = pd.DataFrame(daftar_mahasiswa)

        print(df_daftar_mahasiswa)
        print()
    else:
        cursor.execute(f"SELECT * FROM mahasiswa where nim={mhs}")
        rows = cursor.fetchall()[0]

        data_diri = {
            'NIM': [],
            'Nama': [],
            'Alamat': [],
            'No. Telp': [],
            'Email': [],
            'Tanggal Lahir': [],
            'Password': [],
        }

        data_diri['NIM'].append(rows[0])
        data_diri['Nama'].append(rows[1])
        data_diri['Alamat'].append(rows[2])
        data_diri['No. Telp'].append(rows[3])
        data_diri['Email'].append(rows[4])
        data_diri['Tanggal Lahir'].append(rows[5])
        data_diri['Password'].append(rows[6])
        
        
        df_data_diri = pd.DataFrame(data_diri)

        print(df_data_diri)
        print()


def data_mahasiswa(connection):
    cursor = connection.cursor()

    input_search = input('Masukkan nim/nama/alamat/no. telp/email mahasiswa : ')

    cursor.execute(f"SELECT * FROM mahasiswa WHERE nim LIKE '%{input_search}%' OR nama LIKE '%{input_search}%' OR alamat LIKE '%{input_search}%' OR no_telp LIKE '%{input_search}%' OR email LIKE '%{input_search}%'")
    rows = cursor.fetchall()

    data_mahasiswa = {
        'NIM': [],
        'Nama': [],
        'Alamat': [],
        'No. Telp': [],
        'Email': [],
        'Tanggal Lahir': [],
        'Password': [],
    }
    
    for mhs in rows:
        data_mahasiswa['NIM'].append(mhs[0])
        data_mahasiswa['Nama'].append(mhs[1])
        data_mahasiswa['Alamat'].append(mhs[2])
        data_mahasiswa['No. Telp'].append(mhs[3])
        data_mahasiswa['Email'].append(mhs[4])
        data_mahasiswa['Tanggal Lahir'].append(mhs[5])
        data_mahasiswa['Password'].append(mhs[6])
    
    df_data_mahasiswa = pd.DataFrame(data_mahasiswa)

    print(df_data_mahasiswa)
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
