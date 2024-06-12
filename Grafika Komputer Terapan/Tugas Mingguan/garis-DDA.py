import matplotlib.pyplot as plt
# x1 = int(input("Masukan nilai x0: "))
# x2 = int(input("Masukan nilai x1: "))
# y1 = int(input("Masukan nilai y0: "))
# y2 = int(input("Masukan nilai y1: "))
x1 = 1
x2 = 5
y1 = 2
y2 = 9

dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy):
    r = abs(dx)
else:
    r = abs(dy)

xr = dx/r
yr = dy/r

i = 0

x = []
y = []

print("k\t\tx\t\ty\t\tround(x),round(y)")
print(f" \t\t \t\t \t\t{round(x1)},{round(y1)}")
x.append(round(x1))
y.append(round(y1))
while i < r:
    x1 = x1 + xr
    y1 = y1 + yr
    print(f"{i}\t\t{x1}\t\t{round(y1,2)}\t\t{round(x1)},{round(y1)}")
    x.append(round(x1))
    y.append(round(y1))
    i +=1

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("DDA Algorithm")
plt.plot(x, y, marker="o")
plt.grid(True)
plt.show()