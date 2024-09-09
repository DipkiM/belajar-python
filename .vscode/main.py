#BELAJAR PYTHON PART13
#operator assignment (operasi yang dapat dilakukan dngan penyingkatan)
#operasi ditambah dngn assignment

a = 5 #ini adalah contoh assignment
print("nilai a =", a)

#contoh assignment yang disingkat
# a =a +1
# print('nilai a=', a)

#ini namanya OPERATOR TAMBAH
#nah contoh yang telah disingkat
a +=1 #ini adalah a = a+1
print('nilai a+=1, nilai a mnjadi', a) # tuh hasilnya akan sama sperti yang diatas (tetap berhasil 6)

#ini contoh OPERATOR KURANG
a -=2 #ini adalah a= a-2
print('nilai a-=2, nilai a mnjadi', a)
#kenapa hasilnya 4 bukan 3? krena diatas a sudah berubah jadi 6

#ini contoh OPERATOR PERKALIAN
a *=5 #ini adalah a= a*5
print('nilai a*=5, nilai a mnjadi', a)

#ini contoh OPERATOR PEMBAGIAN
a /=2 #ini adalah a= a/2
print('nilai a/=2, nilai a mnjadi', a)

#contoh baru
b=10
print('\n nilai b=',b)

#INI CONTOH OPERASI MODULUS dan FLOOR DIVISION
b %=3
print('nilai b%=3, nilai b menjadi', b)

b=10
print('\n nilai b=',b)

#INI CONTOH OPERASI LEFT DIVISION
b //=3 #ini nanti hasilnya adalah 3, krena 10/3 dibulatkan mnjadi 3
print('nilai b//=3, nilai b menjadi', b)

#CONTOH BARU
#INI ADALAH PERPANGKATAN atau EKSPONEN
a=5
print('nilai a=,',a)

a **=3
print('nilai a**3=, nilai a mnjadi', a)

#OPERASI BITWISE
#OR
c=True
print('nilai c=',c)
c |= False
print('nilai c|= false, maka nilai c =', c)# ini akan menjadi true, krena true dngn false akan mnjdi true

#contoh baru
c=False
c|=False
print('nilai c|=false, nilai c=',c)#ini akan menjadi false, karena false dengan false hasilny false

#AND
c=True
print('nilai c=',c)
c &= False
print('nilai c&= false, maka nilai c =', c)

#contoh baru
c=True
c&=True
print('nilai c&=true, nilai c=',c)

#XOR
c=True
print('nilai c=',c)
c ^= False
print('nilai c^= false, maka nilai c =', c)

#contoh baru
c=True
c^=True
print('nilai c^=true, nilai c=',c)

#geser geser
d = 0b0100
print('nilai d =',d)
print('nilai d=', format(d,'04b'))

d>>=2
#ini akan menggeser angka  nya kekanan sebanyak 2 kali
print('nilai d>>=2, maka nilai d menjadi', format(d, '04b'))

d<<=2
#ini akan menggeser angka nya kekiri sebanyak 1 kali
print('nilai d<<=2, maka nilai d menjadi', format(d, '04b'))
