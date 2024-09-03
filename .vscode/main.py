#BELAJAR PYTHON PART10
#OPERASI LOGIKA ATAU BOOLEAN

#not, or , and, xor

#NOT
print('======NOT======')
a = True
c = not a

print('data a =',a)
print('--------------- NOT')
print('data c =',c)
# knpa data c=false? krena dia not a, dan a = trus berarti not true = false


#OR
print('======OR======')
#kalau or kita harus punya dua buah nilai, contoh disini kita akan tambahkan b, dimana dia akan menjadi false

#kalau OR jika salah satu pilihan nya TRUE, maka hasilnya akan TRUE
a = False
b = False
c = a or b
print(a,"or",b,"=",c)
a = True
b = True
c = a or b
print(a,"or",b,"  =",c)
a = True
b = False
c = a or b
print(a,"or",b," =",c)
a = True
b = True
c = a or b
print(a,"or",b,"  =",c)

#AND
#jika salah satunya ada yang FALSE, maka akan hasilnya false, dan jika kduanya bernilai sama maka nilainya akan sama juga
print("========AND=========")
a = False
b = False
c = a and b
print(a,"and",b,"=",c)
a = True
b = False
c = a and b
print(a,"and",b,"  =",c)
a = True
b = False
c = a and b
print(a,"and",b," =",c)
a = True
b = True
c = a and b
print(a,"and",b,"  =",c)

#XOR
#dia akan TRUE jika hanya salah satu saja yang TRUE, sisanya false, jika dia ada dua TRUE maka hasilnya FALSE
print("========XOR=========")
a = False
b = False
c = a ^ b
print(a,"xor",b,"=",c)
a = True
b = False
c = a ^ b
print(a,"xor",b,"  =",c)
a = True
b = False
c = a ^ b
print(a,"xor",b," =",c)
a = True
b = True
c = a ^ b
print(a,"xor",b,"  =",c)

#dan aturan ini akan berlaku dngn 3 variabel, dngn syarat dan aturan yang sama