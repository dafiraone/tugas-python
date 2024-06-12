def upacara(x):
    if x =='senin':
        print('upacara')
    else:
        print('bukan upacara')

def upacara1(x):
    if x == 'senin':
        hasil='upacara'
    elif x != 'senin:':
        hasil='bukan upacara'
    return hasil


hari=input('Masukkan hari: ')
upacara(hari)
print(upacara1(hari))

def ucapkan(salutasi, nama):
    print(salutasi + ', ' + nama + '!')
ucapkan('Selamat pagi', 'Andi')
ucapkan(salutasi='Halo', nama='John')

def sapa(nama):
    pesan = f'halo {nama}!'
    return pesan
str1=input()
print(sapa(str1))


def hewan():
    def hewan1():
        jenis = 'angsa'
        return jenis
    def hewan2():
        nonlocal jenis
        jenis = 'harimau'
    def hewan3():
        global jenis
        jenis = 'gajah'

    jenis = 'ayam'
    hewan1()
    print(f'jenis hewan pertama {hewan1()}')
    hewan2()
    print(f'jenis hewan kedua {jenis}')
    hewan3()
    print(f'jenis hewan ketiga {jenis}')

hewan()
print(f'jenis hewan adalah {jenis}')