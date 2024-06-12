import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

def tambah_matkul(connection):
        cursor = connection.cursor()
        nama = input('Masukkan nama matkul : ')
        sks = int(input('Masukkan sks matkul : '))

        if sks < 1:
            print(f'---- Sks minimal 1 ----')
            print()
            return
             
        cursor.execute(f"SELECT nama from matkul")

        if nama.lower() in [c[0].lower() for c in cursor.fetchall()]:
            print(f'---- Matkul {nama} sudah ada ----')
            print()
            return
        
        cursor.execute(f"INSERT INTO matkul (nama, sks) VALUES ('{nama}', {sks})")
        connection.commit()

        print(f'---- Matkul {nama} berhasil ditambahkan ----')
        print()
             

def lihat_matkul(connection):
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM matkul")
        matkul = cursor.fetchall()
        
        daftar_matkul = {
             'Kode': [],
             'Nama': [],
             'SKS': [],
        }
        
        for row in matkul:
            daftar_matkul['Kode'].append(row[0])
            daftar_matkul['Nama'].append(row[1])
            daftar_matkul['SKS'].append(row[2])
        
        df_daftar_matkul = pd.DataFrame(daftar_matkul)

        print(df_daftar_matkul)
        print()

def ubah_matkul(connection):
    cursor = connection.cursor()

    kode = input('Masukkan kode yang akan diubah : ')
    cursor.execute(f"SELECT * from matkul WHERE kode={kode}")
    matkul = cursor.fetchall()


    if len(matkul) < 1:
        print('---- Tidak ada matkul dengan kode {kode} ----')
        print()
        return

    if int(kode) not in matkul[0]:
        print(f'---- Tidak ada matkul dengan kode {kode} ----')
        print()
        return
    
    cursor.execute("SHOW COLUMNS FROM matkul")
    columns = [c[0] for c in cursor.fetchall()]
    del columns[0]

    set_columns = ""

    for c in columns:
        confirm = input('Apakah ingin ubah kolom '+c+'? (y/n) ')
        if confirm.lower() == 'y':
            new_data = input('Masukkan data baru untuk kolom '+c+ ' : ')
            set_columns += f"{c}='{new_data}',"
    set_columns = set_columns[:-1]

    cursor.execute(f"UPDATE matkul SET {set_columns} WHERE kode = {kode}")
    connection.commit()

    print(f'Matkul dengan kode {kode} berhasil diubah')
    print()