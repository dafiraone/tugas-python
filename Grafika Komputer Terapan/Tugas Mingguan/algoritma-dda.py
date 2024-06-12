'''library math diimport agar bisa menggunakan fungsi math.floor() dan math.ceil()'''
import math

#fungsi untuk memutlakan sebuah bilangan
def mutlak(bilangan):
    #bilangan yang akan dimutlakan dijadikan parameter
    #variabel bilangan_mutlak untuk menampung hasil pemutlakan
    bilangan_mutlak = bilangan

    #jika bilangan adalah bilangan negatif
    if bilangan<0:
        #maka jadikan bilangan tersebut menjadi bilangan positif
        bilangan_mutlak = bilangan_mutlak * (-1)
    #jika bilangan adalah bilangan positif
    else:
        #maka biarkan saja
        pass

    #kembalikan bilangan yang sudah dimutlakan
    return bilangan_mutlak

#fungsi untuk membulatkan bilangan menjadi lima angka dibelakag koma
def limaAngkaDibelakangKoma(bilangan):
    #bilangan yang akan dibulatkan dijadikan parameter
    #bulatkan kebawah bilangan menjadi enam angka dibelakang koma
    bilangan = float(f'{bilangan:.6f}')
    '''bulatkan kebawah bilangan menjadi lima angka dibelakang koma dan tampung ke dalam variabel bulat_kebawah'''
    bulat_kebawah = float(f'{bilangan:.5f}')
    '''variabel hasil_pembulatan untuk menampung hasil akhir pembulatan'''
    '''hasil_pembulatan diberi nilai awal dengan bilangan yang dibulatkan menggunakan fungsi round()'''
    '''namun kesalahannya fungsi round() ini membulatkan ke bawah jika angka dibelakang komanya adalah angka 5'''
    #misal 1.5 malah dibulatkan menjadi 1 bukannya 2
    hasil_pembulatan = round(bilangan, 5)

    '''oleh karena itu kita buat modifikasi supaya jika angka dibelakang komanya adalah angka 5 maka pembulatannya ke atas'''
    '''jika angka keenam di belakang koma dari bilangan adalah 5'''
    if (bilangan-0.000004) >= bulat_kebawah:
        '''maka tambahkan angka keenam di belakang koma tersebut dengan 1'''
        '''kemudian bulatkan menggunakan fungsi round()'''
        hasil_pembulatan = round(bilangan+0.000001, 5)
    else:
        '''jika angka keenam di belakang koma dari bilangan bukan 5'''
        '''maka biarkan nilai awal hasil_pembulatan'''
        pass

    #kembalikan nilai dari hasil_pembulatan
    return hasil_pembulatan

#fungsi untuk membulatkan bilangan menjadi empat angka dibelakag koma
def empatAngkaDibelakangKoma(bilangan):
    #bilangan yang akan dibulatkan dijadikan parameter
    #bulatkan kebawah bilangan menjadi lima angka dibelakang koma
    bilangan = float(f'{bilangan:.5f}')
    '''bulatkan kebawah bilangan menjadi empat angka dibelakang koma dan tampung ke dalam variabel bulat_kebawah'''
    bulat_kebawah = float(f'{bilangan:.4f}')
    '''variabel hasil_pembulatan untuk menampung hasil akhir pembulatan'''
    '''hasil_pembulatan diberi nilai awal dengan bilangan yang dibulatkan menggunakan fungsi round()'''
    '''namun kesalahannya fungsi round() ini membulatkan ke bawah jika angka dibelakang komanya adalah angka 5'''
    #misal 1.5 malah dibulatkan menjadi 1 bukannya 2
    hasil_pembulatan = round(bilangan, 4)

    '''oleh karena itu kita buat modifikasi supaya jika angka dibelakang komanya adalah angka 5 maka pembulatannya ke atas'''
    '''jika angka kelima di belakang koma dari bilangan adalah 5'''
    if (bilangan-0.00004) >= bulat_kebawah:
        '''maka tambahkan angka kelima di belakang koma tersebut dengan 1'''
        '''kemudian bulatkan menggunakan fungsi round()'''
        hasil_pembulatan = round(bilangan+0.00001, 4)
    else:
        '''jika angka kelima di belakang koma dari bilangan bukan 5'''
        '''maka biarkan nilai awal hasil_pembulatan'''
        pass

    #kembalikan nilai dari hasil_pembulatan
    return hasil_pembulatan

#fungsi untuk membulatkan bilangan menjadi tiga angka dibelakag koma
def tigaAngkaDibelakangKoma(bilangan):
    #bilangan yang akan dibulatkan dijadikan parameter
    #bulatkan kebawah bilangan menjadi empat angka dibelakang koma
    bilangan = float(f'{bilangan:.4f}')
    '''bulatkan kebawah bilangan menjadi tiga angka dibelakang koma dan tampung ke dalam variabel bulat_kebawah'''
    bulat_kebawah = float(f'{bilangan:.3f}')
    '''variabel hasil_pembulatan untuk menampung hasil akhir pembulatan'''
    '''hasil_pembulatan diberi nilai awal dengan bilangan yang dibulatkan menggunakan fungsi round()'''
    '''namun kesalahannya fungsi round() ini membulatkan ke bawah jika angka dibelakang komanya adalah angka 5'''
    #misal 1.5 malah dibulatkan menjadi 1 bukannya 2
    hasil_pembulatan = round(bilangan, 3)

    '''oleh karena itu kita buat modifikasi supaya jika angka dibelakang komanya adalah angka 5 maka pembulatannya ke atas'''
    '''jika angka keempat di belakang koma dari bilangan adalah 5'''
    if (bilangan-0.0004) >= bulat_kebawah:
        '''maka tambahkan angka keempat di belakang koma tersebut dengan 1'''
        '''kemudian bulatkan menggunakan fungsi round()'''
        hasil_pembulatan = round(bilangan+0.0001, 3)
    else:
        '''jika angka keempat di belakang koma dari bilangan bukan 5'''
        '''maka biarkan nilai awal hasil_pembulatan'''
        pass

    #kembalikan nilai dari hasil_pembulatan
    return hasil_pembulatan

#fungsi untuk membulatkan bilangan menjadi dua angka dibelakag koma
def duaAngkaDibelakangKoma(bilangan):
    #bilangan yang akan dibulatkan dijadikan parameter
    #bulatkan kebawah bilangan menjadi tiga angka dibelakang koma
    bilangan = float(f'{bilangan:.3f}')
    '''bulatkan kebawah bilangan menjadi dua angka dibelakang koma dan tampung ke dalam variabel bulat_kebawah'''
    bulat_kebawah = float(f'{bilangan:.2f}')
    '''variabel hasil_pembulatan untuk menampung hasil akhir pembulatan'''
    '''hasil_pembulatan diberi nilai awal dengan bilangan yang dibulatkan menggunakan fungsi round()'''
    '''namun kesalahannya fungsi round() ini membulatkan ke bawah jika angka dibelakang komanya adalah angka 5'''
    #misal 1.5 malah dibulatkan menjadi 1 bukannya 2
    hasil_pembulatan = round(bilangan, 2)

    '''oleh karena itu kita buat modifikasi supaya jika angka dibelakang komanya adalah angka 5 maka pembulatannya ke atas'''
    '''jika angka ketiga di belakang koma dari bilangan adalah 5'''
    if (bilangan-0.004) >= bulat_kebawah:
        '''maka tambahkan angka ketiga di belakang koma tersebut dengan 1'''
        '''kemudian bulatkan menggunakan fungsi round()'''
        hasil_pembulatan = round(bilangan+0.001, 2)
    else:
        '''jika angka ketiga di belakang koma dari bilangan bukan 5'''
        '''maka biarkan nilai awal hasil_pembulatan'''
        pass

    #kembalikan nilai dari hasil_pembulatan
    return hasil_pembulatan

#fungsi untuk membulatkan bilangan menjadi satu angka dibelakag koma
def satuAngkaDibelakangKoma(bilangan):
    #bilangan yang akan dibulatkan dijadikan parameter
    #bulatkan kebawah bilangan menjadi dua angka dibelakang koma
    bilangan = float(f'{bilangan:.2f}')
    '''bulatkan kebawah bilangan menjadi satu angka dibelakang koma dan tampung ke dalam variabel bulat_kebawah'''
    bulat_kebawah = float(f'{bilangan:.1f}')
    '''variabel hasil_pembulatan untuk menampung hasil akhir pembulatan'''
    '''hasil_pembulatan diberi nilai awal dengan bilangan yang dibulatkan menggunakan fungsi round()'''
    '''namun kesalahannya fungsi round() ini membulatkan ke bawah jika angka dibelakang komanya adalah angka 5'''
    #misal 1.5 malah dibulatkan menjadi 1 bukannya 2
    hasil_pembulatan = round(bilangan, 1)

    '''oleh karena itu kita buat modifikasi supaya jika angka dibelakang komanya adalah angka 5 maka pembulatannya ke atas'''
    '''jika angka kedua di belakang koma dari bilangan adalah 5'''
    if (bilangan-0.04) >= bulat_kebawah:
        '''maka tambahkan angka kedua di belakang koma tersebut dengan 1'''
        '''kemudian bulatkan menggunakan fungsi round()'''
        hasil_pembulatan = round(bilangan+0.01, 1)
    else:
        '''jika angka kedua di belakang koma dari bilangan bukan 5'''
        '''maka biarkan nilai awal hasil_pembulatan'''
        pass

    #kembalikan nilai dari hasil_pembulatan
    return hasil_pembulatan

#fungsi untuk membulatkan bilangan menjadi bilangan bulat
def pembulatan(bilangan):
    #bilangan yang akan dibulatkan dijadikan parameter
    '''bulatkan bilangan menjadi satu angka di belakang koma menggunakan fungsi satuAngkaDibelakangKoma()'''
    bilangan = satuAngkaDibelakangKoma(bilangan)
    '''bulatkan ke bawah bilangan kemudian tampung ke dalam variabel hasil_pembulatan'''
    hasil_pembulatan = math.floor(bilangan)
    '''jika satu angka dibelakang koma adalah 5 ke atas'''
    if (bilangan-0.5) >= int(bilangan):
        #maka bulatkan ke atas bilangan tersebut
        hasil_pembulatan = math.ceil(bilangan)
    else:
        '''jika satu angka dibelakang koma di bawah 5'''
        #maka biarkan nilai awal hasil_pembulatan
        pass
    
    #kembalikan nilai dari hasil_pembulatan
    return hasil_pembulatan

#fungsi untuk print tabel titik-titik (x,y)
def printTabel(x, y, round_x, round_y):
    #print header tabel
    print('k      x        y      round(x),round(y)')
    
    '''lakukan perulangan untuk membaca titik-titik yang didapat dari list argument'''
    #pembacaan data dimulai dari index ke-0
    i = 0
    while i<len(round_x):
        #jika yang dibaca adalah data pertama
        if i == 0:
            '''maka print titik (x,y) yang sudah dibulatkan'''
            print(f'                            ({round_x[0]},{round_y[0]})')
        else:#jika yang dibaca bukan data pertama
            #maka print nilai x dan y, dan print juga titik (x,y) yang sudah dibulatkan
            print(f'{i-1}    {(x[i]):.2f}    {(y[i]):.2f}         ({round_x[i]},{round_y[i]})')
        '''tambah i dengan 1 untuk melakukan pembacaan data di index berikutnya'''
        i += 1

'''fungsi untuk menampilkan garis berdasarkan nilai-nilai x dan y yang sudah diperoleh'''
def tampilkanGaris(list_x, list_y):
    #import matplotlib untuk melakukan plotting
    import matplotlib.pyplot as plt
    
    #plotkan nilai-nilai x dan y
    plt.plot(list_x, list_y, color='red', marker='o')
    #beri judul 'Garis DDA'
    plt.title('Garis DDA', fontsize=14)
    plt.grid(True)
    #tampilkan garis berdasarkan plot yang sudah dibuat
    plt.show()

#masukkan titik awal (x0,y0) dan titik akhir (x1,y1)
x0 = int(input('Masukkan x0: '))
y0 = int(input('Masukkan y0: '))
x1 = int(input('Masukkan x1: '))
y1 = int(input('Masukkan y1: '))
print()#untuk membuat baris baru

'''list x_awal untuk menampung titik-titik x sebelum dibulatkan'''
x_awal = []
'''list y_awal untuk menampung titik-titik y sebelum dibulatkan'''
y_awal = []
'''list x untuk menampung titik-titik x sesudah dibulatkan menjadi bilangan bulat'''
x = []
'''list y untuk menampung titik-titik y sesudah dibulatkan menjadi bilangan bulat'''
y = []

'''bulatkan nilai x0 dua angka di belakang koma, kemudian masukkan ke list x_awal'''
x_awal.append(duaAngkaDibelakangKoma(x0))
'''bulatkan nilai y0 dua angka di belakang koma, kemudian masukkan ke list y_awal'''
y_awal.append(duaAngkaDibelakangKoma(y0))
'''nilai x0 yang sudah dimasukkan ke list x_awal kemudian dibulatkan menjadi bilangan bulat, kemudian masukkan ke list x'''
x.append(pembulatan(x_awal[0]))
'''nilai y0 yang sudah dimasukkan ke list y_awal kemudian dibulatkan menjadi bilangan bulat, kemudian masukkan ke list y'''
y.append(pembulatan(y_awal[0]))

#hitung delta (selisih) x
dx = x1-x0
#hitung delta (selisih) y
dy = y1-y0

#jika |dx|>|dy|
if mutlak(dx) > mutlak(dy):
    #maka r = |dx|
    r = mutlak(dx)
else:
    #maka r = |dy|
    r = mutlak(dy)

#hitung xr
xr = dx/r
#hitung yr
yr = dy/r

i = 0
#lakukan perulangan selama x!=x1 dan y!=y1
while (x_awal[i] != x1) and y_awal[i] != y1:
    '''untuk x dan y selanjutnya tambah dengan xr dan yr sampai x=x1 dan y=y1'''
    '''tambah nilai x terbaru dengan xr kemudian masukkan hasilnya ke list x_awal'''
    x_awal.append(duaAngkaDibelakangKoma(x_awal[i]+xr))
    '''tambah nilai y terbaru dengan yr kemudian masukkan hasilnya ke list y_awal'''
    y_awal.append(duaAngkaDibelakangKoma(y_awal[i]+yr))
    '''nilai x yang sudah dimasukkan ke list x_awal kemudian dibulatkan menjadi bilangan bulat, kemudian masukkan ke list x'''
    x.append(pembulatan(x_awal[i+1]))
    '''nilai y yang sudah dimasukkan ke list y_awal kemudian dibulatkan menjadi bilangan bulat, kemudian masukkan ke list y'''
    y.append(pembulatan(y_awal[i+1]))

    i += 1

#print tabel yang menampilkan nilai-nilai x dan y
printTabel(x_awal, y_awal, x, y)

'''tampilkan garis menggunakan titik-titik (x,y) yang sudah dibulatkan menjadi bilangan bulat'''
tampilkanGaris(x, y)







