#belajar python part15
#operasi dan manipulasi string part1

# 1. menyambung string (concatenate)
#misal kita buat yang simple
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir  = "Fame"

nama_lengkap = nama_pertama+" "+nama_tengah+"'"+nama_akhir
print(nama_lengkap)#ini akan jadi aneh karena kita menempelkan smua string nya, gimana kalau kita ingin menambahkan spasi? dngn cara memnambhkan petik dua dngan value spasi di antara string nya

# 2. menghitung panjang dari string (len=length)
panjang = len(nama_lengkap)
print("panjang dari"+nama_lengkap+"="+str(panjang))#ini untuk mngukur panjang dri string dengan menggunakan len(variabel) dngn value variabel yang ingin kita hitung.
#kenapa itu ditambah str, krena kalau tidak itu akan jadi masalah karena itu angka, jadi harus diubah terlebih dahulu tipe nya menjadi string

# 3. operator untuk string
#mengecek apakah ada komponen character atau string di string
#misal kita buat d adalah sbuah d string

d = "D"
status = d in nama_lengkap#nah ini untuk mengecek apakah d ada di komponen nama_lengkap
print("string "+d+" ada di "+nama_lengkap +" "+ str(status))#ini akan menjadi false karena variabel d yang kita miliki bernilai d lowercase, sdngkan yang di nama_lengkap itu uppercase, nah coba kita ganti jadi uppercase

d = "d"
status = d in nama_lengkap#nah ini untuk mengecek apakah d ada di komponen nama_lengkap
print("string "+d+" ada di "+nama_lengkap +" "+ str(status))

#ada satu lagi cara nya untuk mengecek yaitu dngn menggunakan (not in) tidak ada

d = "D"
status = d not in nama_lengkap#nah ini untuk mengecek apakah d ada di komponen nama_lengkap
print("string "+d+"tidak ada di "+nama_lengkap +" "+ str(status))#ini akan bernilai false, krena variabel d itu ada di dalam nama_lengkap

# 4. mengulang string
print("wk"*10)
print(10*"wk")

# 5.indexing (mengambil data dari string)
#cntoh
print("index ke-0 = "+nama_lengkap[0])#nah karena ucup D'Fame itu 11, dan index slalu dimulai dari 0, berarti e sbagai index trakhir akan terhitung sbagai index 10
print("index ke-1 = "+nama_lengkap[1])
print("index ke-10 = "+nama_lengkap[10])
print("index ke-4 = "+nama_lengkap[4])
#gimana kalau index nya mines?
print("index ke-(-1) = "+nama_lengkap[-1])#nah ini e yg akan muncul, nah kesimpulan nya kolom mines akan mengambil nilai dari belakang
print("index ke-(-2) = "+nama_lengkap[-2])#nah jadi intinya kalau mulai dri belkang, itu mulai dari nilai mines

#nah skrang gimana kita mau ambil range?
print("index ke-(0-3) = "+nama_lengkap[0:3])#nah jadi aturan nya kalau kita hitung mau ambil 0-3, kita tidak bisa membuat value nya itu [0-3]nanti akan error, tpi kita harus membuat value nya[0:3]titik dua yang artinya (sampai).
#nah tapi kalau gini dia hanya akan print "ucu" atau bisa diblg 0-2 doang, knpa? karena python emg begitu jadi jikalau kita ingin sampai index tiga, maka kalian harus membuat dia menjadi 0:4 agar p nya ikut terbaca
print("index ke-(0-3) = "+nama_lengkap[0:4])#nah begini dia akan ngeprint index 0-3
#kita juga bisa mengambil pakai jeda
print("index ke-[0,2,4,6,8,10]:"+nama_lengkap[0:10:2])

# 6. item paling kecil (min)
print("paling kecil :"+min(nama_lengkap))#nah nanti akan keluar paling kecil adalah (gadak) atau spasi

# 7.item paling besar (max)
print("paling besar :"+max(nama_lengkap))#nanti akan mengeprint (u)sesuai abjad karena u yang paling besar, maksudnya ialah kita mengambil ascii_code contoh

ascii_code = ord(" ")
print("ascii code untuk spasi adalah "+str(ascii_code))
data = 117
print("char untuk ascii 117 adalah "+ chr(data))
#nah disini u=117 dan spasi =32, maka dari itu ketika kita ngeprint yang paling besar akan keluar u dan yang paling kecil akan keluar spasi

# 8. operator dalam bentuk method
data = "otong surotong markontong"
jumlah = data.count("u")#nah ini count salah satu bentuk method, dia menempel ke si data, disini kita bisa itung, contoh kita ingin itung jumlah U
print("jumlah u pada data = "+data+" = "+str(jumlah))