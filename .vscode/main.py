#belajar python part31
#copy list
#teknik menduplikat list

#ini adalah teknik pass by reference (dengan address yang sama)
a = ['ucup','otong','dudung']
print(f"a={a}")
b=a
print(f"b={b}")

#kita akan merubah member dari a
a[1]="michael"
#maka akan merubah b juga pada indeks 1

b.sort()
#bahkan saat kita merubah b a juga ikut berubah

print(f"a={a}")
print(f"b={b}")

#address dari kedua list a dan b
print(f"address a={hex(id(a))}")
print(f"address b={hex(id(b))}")
#nah ini kita liat bahwasanya address a dan b sama, ini menjelaskan bahwa mereka itu sama. pengaruhnya apa?

#itu tadi bukan mengcopy karena dia berhubungan satu sama lain

#mari kita menduplikat dengan cara mengcopy
print("membuat list c, dengan a.copy")
c= a.copy() #ini cara dengan copy atau data baru address baru (full duplikat)
print(c)
print(f"address a={hex(id(a))}")
print(f"address b={hex(id(b))}")
print(f"address c={hex(id(c))}")

#nah sekarang kita punya address c yang beda, nah itu berarti kita membuat c list baru dengan address yang beda, shingga kita dapat data yang sama dengan si a, tapi ketika kita ingin merubah si c, si a dan b tidak akan berubah, karena address nya beda

c[1]= "suneo"
print(c)
print(b)
print(a)