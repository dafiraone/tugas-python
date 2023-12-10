import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'pemdas_mysql',
}

while True:
    print()
    crud_input = input("""Menu
    1. Tambah Data
    2. Lihat Data
    3. Update Data
    4. Hapus Data
    5. Keluar
Pilih Menu (1-5): """)
    print()

    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        match crud_input:
            case '1':
                nama = input('Masukkan Nama: ')
                umur = input('Masukkan Umur: ')
                jenis_kelamin = input('Masukkan Jenis Kelamin (P/W): ')

                insert_query = f"INSERT INTO orang (nama, umur, jenis_kelamin) VALUES ('{nama}', {umur}, '{jenis_kelamin}')"

                cursor.execute(insert_query)

                connection.commit()

                this_data_id = cursor.lastrowid

                print(f'Data inserted successfully with ID: {this_data_id}')
            case '2':
                select_query = "SELECT * FROM orang"

                cursor.execute(select_query)

                rows = cursor.fetchall()

                for row in rows:
                    print(row)
            case '3':
                id = input('Masukkan id yang ingin diubah: ')

                cursor.execute("SHOW COLUMNS FROM orang")

                columns = cursor.fetchall()
                kolom = input(f'Masukkan kolom yang ingin diubah {[c[0] for c in columns]}: ')
                new_data = input('Masukkan data baru: ')

                update_query = f"UPDATE orang SET {kolom} = '{new_data}' WHERE id = {id}"

                cursor.execute(update_query)

                connection.commit()
                print(f'Data sucessfully updated') 
            case '4':
                id = input('Masukkan id yang ingin dihapus: ')
                delete_query = f"DELETE FROM orang WHERE id = {id}"

                cursor.execute(delete_query)

                connection.commit()
            case '5':
                break
        
    except mysql.connector.Error as e:
        print(f'Error connecting to database: {e}')
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()


# try:
#     connection = mysql.connector.connect(**DB_CONFIG)
#     if connection.is_connected():
#         print('Connected to MySQL Database')

#     cursor = connection.cursor()

#     insert_query = "INSERT INTO pasien (nama, tanggal_lahir, alamat, telepon, jenis_kelamin) VALUES (%s, %s, %s, %s, %s)"

#     values = ('Zaky', '2004-05-26', 'Tegal', '081476652656', 'P')

#     cursor.execute(insert_query, values)

#     connection.commit()

#     this_data_id = cursor.lastrowid

#     print(f'Data inserted successfully with ID: {this_data_id}')

#     # Read Data
#     select_query = "SELECT * FROM pasien"

#     cursor.execute(select_query)

#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

#     # Update Data
#     update_query = f"UPDATE pasien SET nama = 'Zacky' WHERE id = {this_data_id}"

#     cursor.execute(update_query)

#     connection.commit()
#     print(f'Data sucessfully updated') 

#     # Delete Data
#     delete_query = f"DELETE FROM pasien WHERE id = {this_data_id}"

#     cursor.execute(delete_query)

#     connection.commit()
    
# except mysql.connector.Error as e:
#     print(f'Error connecting to database: {e}')
# finally:
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print('Connection Closed')