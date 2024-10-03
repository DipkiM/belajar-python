#belajar python part29
#manipulasi list

data = ['dudung','otong','sabar']#ini sebenernya ada index yang dimulai dari 0, dan kita juga bisa menggunakan index bernilai (-) jika kita mau mulai dari belakang, 0(-3), 1(-2), 2(-1)

#1. cara mengambil data dari list tersebut
data_0=data[0]#0 sama value atau indexnya
print(f"data pertama = {data_0}")

data_trakhir=data[-1]
print(f"data terakhir = {data_trakhir}")

#mengambil info jumlah data
panjang_data = len(data)
print(f"panjang data = {panjang_data}") 

#manipulasi data list

#1.menambahkan item pada list sesuai posisi yang diinginkan
print(f"data sebelum ditambah = \n{data}")
data.insert(0,"ario")#nah pakai INSERT dimana (0 sebagai posisi yang ingin ditaruh, dan ario sebagai value yang ditambahkan)
print(f'data setlah ditambhakan = \n{data}')

#2.menambh di akhir list
data.append("jajang")
print(f'ini menambahkan data di akhir = {data}')

#3. menambakan list dengan list
data_baru = ['ujang','usep','dedeng']
data.extend(data_baru)#jadi misal data baru mau ditambah ke data itu gunaakan EXTEND
print(f'data gabungan = {data}')

#4. merubah data
#misal kita ingin ubah data ke dua , akan diganti dngn michael

data[2]='michael'
print(f'data rubah = {data}')#maka dari itu otong

#meremove data
data.remove('michael')
print(f'ujang di remove = {data}')

#meremove data paling blkang
data.pop()#data pop ialah yang paling blkang
print(f'data terakhir hilang = {data}')#nah skarang dedeng ilang, tapi misalkan kita taruh data.pop() kedalam variabel nnti yang ada ialah kita mengambil data terakhirny
data_terakir=data.pop()
print(data_terakir)#nah karena yang terakhir kali di run itu urutan nya usep, maka pas di print usep ikutin 