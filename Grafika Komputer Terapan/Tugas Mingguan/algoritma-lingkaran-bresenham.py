p = []
x = []
y = []
i = 0

r = int(input('Masukkan jari-jari: '))

p.append(1-r)
x.append(0)
y.append(r)

while x[i]<y[i]:
    if p[i]<0:
        x.append(x[i] + 1)
        y.append(y[i])
        p.append(p[i] + 2*x[i+1] + 1)
    else:
        x.append(x[i] + 1)
        y.append(y[i] - 1)
        p.append(p[i] + 2*x[i+1] + 1 - 2*y[i+1])
    
    i += 1

i = len(x)-1
while i>=0:
    x.append(y[i])
    y.append(x[i])
    i -= 1

#print tabel
i = 0
print(f'x    y    p')
while i<len(p):
    print(f'{x[i]}    {y[i]}    {p[i]}')
    i += 1
while i<len(x):
    print(f'{x[i]}    {y[i]}')
    i += 1

panjang_awal = len(x)
#kuadran 2 ditambah ke list x dan y
i = 0
while i<panjang_awal:
    x.append(x[i])
    y.append(y[i]*(-1))
    i += 1

#kuadran 3 ditambah ke list x dan y
i = 0
while i<panjang_awal:
    x.append(x[i]*(-1))
    y.append(y[i]*(-1))
    i += 1

#kuadran 3 ditambah ke list x dan y
i = 0
while i<panjang_awal:
    x.append(x[i]*(-1))
    y.append(y[i])
    i += 1

#gambar lingkaran menggunakan matplotlib
import matplotlib.pyplot as plt
  
plt.plot(x, y, color='red', marker='o')
plt.title('Lingkaran Bresenham', fontsize=14)
plt.grid(True)
plt.show()