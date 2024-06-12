from graphics import *

import sys
sys.setrecursionlimit(1000000)

win = GraphWin("Boundary fill Algorithm", 500, 500)

#list untuk mengubah letak koordinat x yang dituju
dx=[0,1,0,-1,-1,1,1,-1]
#list untuk mengubah letak koordinat y yang dituju
dy=[-1,0,1,0,-1,-1,1,1]

a = 230
b = a
c = 280
d = c

#list ini berguna untuk menghentikan proses pewarnaan
#jika value putih "white" pada list sudah diganti menjadi kuning "yellow"
color = [["white" for j in range(d+1)] for i in range(c+1)]

#fungsi untuk melakukan pewarnaan pada titik yang dituju
def putPixel(win, x, y, fillColor):
    #tentukan titik yang dituju (mengikuti argumen x,y)
    pt = Point(x,y)
    #atur warna untuk titik yang dituju (dengan argumen fillColor)
    pt.setFill(fillColor)
    #lakukan pewarnaan pada titik yang dituju
    pt.draw(win)


#fungsi untuk membuat persegi
def drawSomeFigure(borderColor):
    #tentukan koordinat-koordinat sudut persegi:
    #sudut kiri bawah dengan titik (230,230)
    #sudut kanan bawah dengan titik (280,230)
    #sudut kanan atas dengan titik (280,280)
    #sudut kiri atas dengan titik (230,280)
    p=Polygon(Point(a,b), Point(c,b), Point(c,d), Point(a,d))
    #atur warna garis yang menyambungkan sudut-sudut tersebut (dengan argumen borderColor)
    p.setOutline(borderColor)
    #gambar sebuah persegi dengan sudut dan garis yang sudah ditentukan di atas
    p.draw(win)

#fungsi rekursif untuk melakukan pewarnaan pada sebuah bangun
def boundaryFill(x, y, fillColor, borderColor):
    #jika pewarnaan sudah dilakukan
    if x<=a or x>=c or y<=b or y>=d or color[x][y]==fillColor:
        #maka keluar dari fungsi
        return
    #lakukan pewarnaan di titik yang dituju (mengikuti argumen x,y) dengan warna fillColor (kuning)
    putPixel(win,x,y,fillColor)
    #ganti nilai putih "white" di list color dengan warna fillColor (kuning) pada index color[x][y]
    color[x][y] = fillColor
    
    #ganti koordinat titik pewarnaan dengan mengganti argumen (x,y)
    for i in range(4):
        boundaryFill(x+dx[i], y+dy[i], fillColor, borderColor)

#fungsi program utama
def main():
    
    borderColor = "blue"
    fillColor = "yellow"
    #gambar sebuah persegi dengan warna border biru
    drawSomeFigure(borderColor)
    
    #titik awal dilakukannya pewarnaan
    interior_x = 279
    interior_y = 231
    
    #pewarnaan dilakukan
    boundaryFill(interior_x, interior_y, fillColor, borderColor)
    win.getMouse()

#program utama dijalankan
main()
