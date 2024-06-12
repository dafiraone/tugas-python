switch = {
    1: "Satu",
    2: "Dua",
    3: "Tiga",
    4: "Empat"
}

x = int(input("Masukkan angka pertama : "))
y = int(input("Masukkan angka kedua: "))
z = x * y
print(switch.get(z))

def kalkulator(operator, input1, input2):
    fungsi = {
        "+": input1+input2,
        "-": input1-input2,
        "*": input1*input2,
        "/": input1/input2
    }
    return fungsi.get(operator)

a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))
c = input("Masukan operator (+/-/*//) : ")
print(kalkulator(c, a, b))

try:
    5/0
except:
    print("TIdak bisa membagi 0")

for i in range(10):
    print(f"Hello World! {i}x")

vokal= 'aiueo'
kata = "Sofwan Rinantomo"
jumlah_vokal = 0

for char in kata:
    if char.lower() in vokal:
        jumlah_vokal += 1

print("Jumlah Vokal.", jumlah_vokal)

tuple_a = 10, 20, 30
print(tuple_a[2])

