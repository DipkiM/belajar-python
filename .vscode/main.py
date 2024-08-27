#belajar python part7
#operasi aritmetika

#pertama kita buat sbuah variabel

a=10
b=3

#operasi tambah +
hasil = a+b
print(a,"+",b,"=",hasil)

#operasi pengurangan -
hasil = a-b
print(a,"-",b,"=",hasil)

#operasi perkalian *
hasil = a*b
print(a,"*",b,"=",hasil)

#operasi pembagian /
hasil = a/b
print(a,"/",b,"=",hasil)

#operasi eksponen (pangkat) **
hasil = a**b
print(a,"**",b,"=",hasil)

#BEBERAPA OPERATOR YG SERING DIPAKAI DI BAHASA LAIN

#operasi modulus % (sisa pembagian)

hasil=a%b
print(a,'%',b,"=",hasil)

#operasi floor division //
# ini adalah hasil pembagian yg dibulatkan, krna 10/3 = 3,33333 dia akan dibulatkan hanya menjadi 3
hasil= a//b
print(a,"//",b,"=",hasil)

#PRIORITAS OPERASI (OPERASI MANA YG AKAN DIDLUANKAN)

'''
1.() operasi didalam kurung akan didluankan
2.eksponen **
3.perkalian dan kawan kawan * / % //
4.pertambahan dan pengurangn + -
'''
x=3
y=2
z=4

hasil = x ** z * y + x / y - x % z // y
print(x,'**',z,'*',y,'+',x,'/',y,'-',x,'%',z,'//',y,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z)

hasil = (x+y) * z
print('(',x,'+',y,")",'*',z)
