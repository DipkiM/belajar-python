#belajar python part16
#operasi dan manipulasi string part2

#beberapa operator method

# 1. merubah case dari string
#merubah semua ke uppercase, misal
salam = "bro"
print("kabarnya baik kah?",salam)
salam = salam.upper()
print("upper =","kabarnya baik kah?",salam)#mau copy code = alt+shift, kalau pindahin tahan alt plus arrow

# merubah semua ke lowercase
aku = "Hai, APa KABar"
print(aku,"amel")
aku = aku.lower()
print("lower =",aku,"amel")

# 2. pengecekan isX method
#contoh untuk pengecekan lowercase
salam = "sis"#nah skrg kita mau ngecek apakah sis ini lower smua
apakah_lower = salam.islower()#nah dngn mnggunakan islower akan mngecek apakah dia lower, dan hasilnya adalah boolean
print(salam,"apakah dia lower ?",apakah_lower)
apakah_upper = salam.isupper()
print(salam,"apakah dia lower ?",apakah_upper)#kalau misalnya terjadi errror dan gk mau dia memunculkan bool nya, maka kita bisa mengubah tipe data dari apakah mnjdi str

#isalpha() <--- untuk mengecek smuanya huruf
#isalnum() <--- untuk mengecek smuanya huruf dan angka
#isdecimal() <--- untuk mengecek smuanya ialah angka
#isspace() <--- untuk mengecek isinya adalah kolom kosong, sperti spasi, tab, newline, \n
#istitle() <--- untuk mengecek smua kata dimulai dengan huruf besar

judul = "The Walking Death"
apakah_title = judul.istitle()
print(judul,"judulnya smua huruf brawal dari huruf besar ?",apakah_title)#nah karena benar jadi akan di print (true)

#ngecek komponen startswith() endwith() <--- ini keren
cek_start = "Hai guru".startswith("hai guru")#nah ini ialah untuk mengecek apakah kalimat cek_start itu dimulai dengan kalimat yang sama dngn value dari STARTSWITH, jadi disini kita tidak usah buat variabel lain dlu, karena bisa langsung taruh (.startswith) diblakangny

print("start = ",cek_start)#ini akan menjadi FALSE, karena "hai guru" yang benar berawalan dari huruf H kapital "Hai guru"

cek_end = "Hai guru".endswith("guru")
print("end = ",cek_end)

# 3. penggabunggan komponen join() split(), jelas sesuai nama si join akan menggabunggkan dan split akan memisahkan, ini termasuk salah satu komponen list (kumpulna data)

pisah = ["aku","sayang","kamu"] #nah untuk list dia pakai kurung siku ( [] )
print(pisah)#nah skrang kita ingin gabungkan smua

gabungan = ",".join(pisah)#nah ini untuk menggabungkan, value nya ialah hal yang ingin digabungkan, nah sedangkan str koma disini adalah hal yang kita pakai ketika menggabungkan, jadi ini akan menjadi seperti aku,sayang,kamu
print(gabungan)

gabungan = " ".join(pisah)#nah dngan ini kita akan menggabungkan keduanya dngan spasi
print(gabungan)

gabungan = " ehm ".join(pisah)#jadi yang digunakan bukan hanya koma dll, tapi juga bisa kalimat 
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))#nah ini akan membuat kita memisahkan nilai dari gabungan dengan ehm, artinya kita menghilangkan smua ehm didalamnya dan akan membuat dia menjadi sbuah list lagi. jadi ini kebalikan dari join

# 4. alokasi karakter rjust(), ljust(), center()
#rjust() atau right justify, rata kanan
kanan = "kanan".rjust(10)
print("'"+kanan+"'")#nah ini dia akan mengambil space 10 dan rata kanan tulisan nya, jadi karena kanan ini 5 karakter maka space ke kirinya akan bersisa 5

kiri = "kiri".ljust(7)
print("'"+kiri+"'")#nah ini dia akan mengambil space 7 dan rata kiri tulisan nya, jadi karena kiri ini 4 karakter jadi space ke kanan nya akan bersisa 3

tengah = "tengah".center(10)
print("'"+tengah+"'")#nah ini dia akan mengambil space 10 dan di tengah jadi kanan karena tengah itu 6 karakter maka kanan kiri akan bersisa 2 2 jadi 4

tengah = "tengah".center(18,"=")#nah tambahan (str =)disini ialah untuk mengubah jaraknya itu tidak ditandai dengan spasi, jadi jaraknya ditandai dengn value str yg kita masukan, contoh disini kan value nya =
print("'"+tengah+"'")

tengah = "tengah".center(18,"*")#ini kalian mau pakai tanda yang aneh juga bisa
print("'"+tengah+"'")

#kebalikan nya -> strip()
tengah = tengah.strip("*")
print("'"+tengah+"'")#nah jadi strip itu fungsinya untuk menghilangkan nilai dari value nya, cnth disini kita ingin menghilangan (*), maka kita gunakan .strip("*")

#NAH SEKIAN, JADI MASIH BANYAK LAGI METHOD YG LAIN DAN PENJELASAN NYA APA SAJA, CARINYA BISA DI W3SCHOOLS DAN LAIN LAIN