#belajar python part4
#MENGENAL TIPE DATA

#cntoh: a=10, maka a adalah variabel dngn nilai 10

#tipe data apa saja yang ada di python?
#1.tipe data:angka (integer)
data_integer=1
print("data :", data_integer, ", bertipe : ", type(data_integer))
#2.tipe data float (angka dngn koma, tpi kita menggunakan titik)
data_float=1.5
print("data :", data_float, ", bertipe : ", type(data_float))
#3.tipe data string (kumpulan karakter)
data_string="ucup"
#disini ucup mnjdi str (string)
print("data :", data_string, ", bertipe : ", type(data_string))
#4.tipe data biner (true / false, boolean)
data_bool=False
print("data :", data_bool, ", bertipe : ", type(data_bool))
#5.tipe data khusus
#tipe data kompleks, atau memiliki bil ril dan imajiner
data_kompleks=complex(5,6)
#ini berarti 5=bil ril dan 6 sbagai bil imajiner, krna ril slalu diawal atau depan dan imajiner diblkang
print("data :", data_kompleks, ", bertipe : ", type(data_kompleks))
#tipe data dari bahasa c
from ctypes import c_double, c_char, c_long
#adaaa c_char,c_double,c_long dll
data_c_double=c_double(10.6)
#ini akan menjadi data c_double
print("data :", data_c_double, ", bertipe : ", type(data_c_double))
#maka saat di print dia akan menampilkan data c_double
