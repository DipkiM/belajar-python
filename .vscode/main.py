#belajar python part30
#operasi list
data_angka = [1,2,3,2,3,9,5,1,7,9,9,2,3,4,5,6,5,4,2,4,5,6]
print(f'data angka = \n{data_angka}')

#1. Count Data
#jadi kita bisa menghitung data ini muncul berapa kali di list data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3= data_angka.count(3)
print(f'jumlah angka 4 = {jumlah_data_4}')
print(f'jumlah angka 3 = {jumlah_data_3}')

#2.ambil posisi data
data = ['ucup','otong','ujeng','parno','dudung']
print(f'data = {data}')
index_dudung=data.index('dudung')
index_ujeng=data.index('ujeng')
print(f'index si dudung ialah = {index_dudung}')
print(f'index si ujeng ialah = {index_ujeng}')

#Mengurutkan list
print(f"ini adalah data angka seblum di urut = {data}")
data.sort()
print(f'data setelah diurut = {data}')
print(data_angka)
data_angka.sort()
print(f'data angka sort = {data_angka}')

#membalik list nya
data.reverse()
data_angka.reverse()
print(data)
print(data_angka)