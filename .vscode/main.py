#belajar python part19
#LATIHAN DATE AND TIME

#contoh ingin membuat kapan kita lahir, pertama tengok terlebih dahulu ke library python tentang date and time 

import datetime as dt
#jadi disini artinya sih datetime tadi akan kita import sbagai dt

# contoh
hari_ini = dt.date.today()#nah dengan bgini kita akan mengprint tanggal hari ini, dngn menggunakan datetime dan .date .today
print(hari_ini)

# cara manual
tanggal = dt.date(2024,9,18)#ini akan ngeprint secara manual
print(tanggal)  
print(f"hari ini adalah hari = {hari_ini:%A}")#nah dngn ini kita bisa memanggil hari dengan mnggunakan "format" (%A) ialah untuk mmgil hari

# NAH SKRNG KITA AKAN MENDETEKSI HARI LAHIR
print("silahkan masukan\n tanggal\n bulan dan\n tahun lahir anda\n")
bulan   = int(input("bulan \t\t:"))
tanggal = int(input("tanggal \t:"))
tahun   = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("tanggal lahir anda ialah =",tanggal_lahir)

hari_ini = dt.date.today()
print(f"hari ini tanggal = {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 # nah untuk penggunaan .days disini itu berarti kita ingin dia itu hari
umur_bulan_sisa = (umur_hari.days % 365)//30 #nah 30 disini itu ialah rata rata banyak hari perbulan nya 
print(f"hari lahir anda ialah = {tanggal_lahir:%A}")
print(f"umur anda ialah = {umur_tahun} tahun, {umur_bulan_sisa} bulan")