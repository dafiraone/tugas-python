import numpy as np

array1d = np.array([[1,2], [5,6]])
array2d = np.array([[3,4], [7, 8]])

vgabungan = np.vstack((array1d, array2d))
print("vstack")
print(vgabungan)

hgabungan = np.hstack((array1d, array2d))
print("hstack")
print(hgabungan)

print("concatenate a0")
print(np.concatenate((array1d, array2d), axis=0))
print("concatenate a1")
print(np.concatenate((array1d, array2d), axis=1))

array1d = np.array([1,2,3])
array3 = np.array([[4,5,6], [7,8,9]])

gabungan = np.vstack((array1d, array3))
print("beda dimensi vstack")
print(gabungan)

my_array = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(my_array[1,:])
print(my_array[:,0])
print(my_array[1:3,0:3])

mylist = [1,2,3]
mylist.insert(0, 4)
print(mylist)
mylist.insert(2, 8)
print(mylist)
mylist[3] = 7
print(mylist)

import array as arr
a = arr.array("i", [1,2,3,4,5])
print(a)

b = np.array([1,2,3,4,5])
arr2d = np.array([["zaky", "agil", "rehan"], [1,2,3], [4,5,6]])
print(b)
print(arr2d[1,1])