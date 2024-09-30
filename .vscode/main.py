#belajar python part28
#---LIST---

# angka = 1
# angka = 2
# angka = 3
# nah bisa gk kita menyatukan ini smua? bisa dengan mengumpulkan data nya dngn sebuah LIST

#kumpulan data NUMBERS
data_angka = [1,2,3]
print(data_angka)

#Kumpulan data STRINGS
data_string = ["ucup","otong","oda"]
print(data_string)

#Kumpulan data BOOLEAN
data_boolean = [True,False,True,False]
print(data_boolean)

#kumpulan data campuran
data_campuran = [1,'bala-bala',2,'cireng','ucup',True,'otong',False]
print(data_campuran)

#cara alternatif membuat list
data_range = range(0,10,2)#range(start,stop,step)
print(data_range)#ini tidak berbentuk didalam list
data_list = list(data_range)
print(data_list)

#kita bisa membuat list dengan for loop
#LIST COMPREHENSION
list_pake_for = [i**2 for i in range(0,10)]#ini kita ingin membuar didalam list i untuk i didalam range(0-10)
print(list_pake_for)

#membuat list pake for pake if
list_pake_for_pake_if = [i for i in range(0,10) if i!=5]
#(!= ini itu tidak sama dengan) 
print(list_pake_for_pake_if)
list_pake_for_pake_if = [i**2 for i in range(0,10) if i !=5]
print(list_pake_for_pake_if)

#membuat list genap
list_pake_for_pake_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_pake_if)
#membuat list ganjil
list_pake_for_pake_if = [i for i in range(0,10) if i%2 !=0]
print(list_pake_for_pake_if)