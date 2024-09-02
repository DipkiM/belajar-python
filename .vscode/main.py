#BELAJAR JAVASCRIPT PART9
#OPERASI KOMPARASI

#setiap hasil komparasi bernilai boolean (true or false)
#operator operatornya antara lain: >,<,>=,<=,==,!=,is,is not

#cntoh
a=2
b=5

#lebih besar dari (>)
print('========== lebih besar dari (>)')
hasil = a>7
print(a,">",7,"=",hasil)
hasil = a>1
print(a,">",1,"=",hasil)
hasil = a>2
print(a,">",2,"=",hasil)

#kurang dari (<)
print('========== kurang dari (<)')
hasil = b<4
print(b,"<",4,"=",hasil)
hasil = b<6
print(b,"<",6,"=",hasil)
hasil = b<6.1
print(b,"<",6.1,"=",hasil)
hasil = b<2
print(b,"<",2,"=",hasil)

#lebih besar sama dengan (>=)
print('========== lebih besar sama dengan (>=)')
hasil = a>=2
print(a,">=",2,"=",hasil)
hasil = a>=4
print(a,">=",4,"=",hasil)
hasil = a>=1
print(a,">=",1,"=",hasil)

#kurang dari sama dengan (<=)
print('========== kurang dari sama dengan (<=)')
hasil = b<=4
print(b,"<=",4,"=",hasil)
hasil = b<6
print(b,"<=",6,"=",hasil)
hasil = b<=5
print(b,"<=",5,"=",hasil)

#sama dengan sama dengan (==)
print('========== sama dengan sama dengan (==)')
#nah kalau bgini dia akan mengecek, misal a=5, lalu kita buat program a==5, maka jawabn yang akan keluar adalah TRUE, karena 5=5, misal a==3, jawabny akan FALSE, jadi sama dengan sama dengan ini adalah untuk mengecek suatu data

hasil = a==2
print(a,"==",2,"=",hasil)#jawaban ini nanti akan TRUE
hasil = a==1
print(a,"==",1,"=",hasil)#dan jawaban ini akan FALSE

#tidak sama dengan (!=)
#ini adalah kebalikan dari sama dengan sama dengan, ini akan mengecek, bila perbandingan nya sama maka jawaban yang dihasilkan ialah FALSE, dan jika perbandingan nya hasil berbeda maka jawabn akan menjadi TRUE
print('========== tidak sama dengan (!=)')
hasil = a!=2
print(a,"!=",2,"=",hasil)#jawaban ini nanti akan TRUE
hasil = a!=1
print(a,"!=",1,"=",hasil)#dan jawaban ini akan FALSE

# "is" sebagai komparasi objek
print('========== object identity (is)')
x=5 #ini adalah assignment membuat objek
y=6
print('nilai x =',x,'id=',hex(id(x)))
print('nilai x =',y,'id=',hex(id(y)))
hasil = x is y
print(x,"is",y,"=",hasil)#nah ini hasilnya akan TRUE, krena nilai x dan y sama, dan juga dia bukan literal
hasil = x is 5
print(x,"is",5,"=",hasil)#nah kalau ini akan menjadi peringatan, krna nilai x dan y walaupun sama tapi dia itu sebuah literal makanya nnti akan ada peringatan dari python ny

# "is not" ini mirip dengan tidak sama dengan, jadi yang beda akan bernilai TRUE
hasil = x is not y
print("nilai x =",x,"id=",hex(id(x)))
print("nilai x =",y,"id=",hex(id(y)))
print (x,"is not",y,"=",hasil)