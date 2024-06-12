import matplotlib.pyplot as plt
x1 = int(input("Masukan nilai x1: "))
x2 = int(input("Masukan nilai x2: "))
y1 = int(input("Masukan nilai y1: "))
y2 = int(input("Masukan nilai y2: "))

m = (y2-y1)/(x2-x1)

if 0 < m < 1:
    dx = x2-x1
    dy = y2-y1
    d1 = 2*dy
    d2 = 2*(dx-dy)
    p = d1-dx
elif m > 1:
    dx = x2-x1
    dy = y2-y1
    d1 = 2*dx
    d2 = 2*(dx-dy)
    p = d1-dy

x = []
y = []

x.append(x1)
y.append(y1)
print("p\t\tx\t\ty")
print(f"{p}\t\t{x[-1]}\t\t{y[-1]}")
while x[-1]<x2 or y[-1]<y2:
    if 0 < m < 1:
        if p >= 0:
            p-=d2
            y.append(y[-1]+1)
        elif p < 0:
            p+=d1
            y.append(y[-1])
        x.append(x[-1]+1)
    elif m > 1:
        if p >= 0:
            p+=d2
            x.append(x[-1]+1)
        elif p < 0:
            p+=d1
            x.append(x[-1])
        y.append(y[-1]+1)
    print(f"{p}\t\t{x[-1]}\t\t{y[-1]}")

plt.plot(x, y,marker="s")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Bresenham Algorithm")
plt.show()