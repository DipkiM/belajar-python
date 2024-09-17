#belajar python part18
#STRING WIDTH AND MULTILINE

#contoh kita punya DATA

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 160
data_nomor_sepatu = 40

#string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran sepatu = {data_nomor_sepatu}"
print(5*"="+"DATA STRING"+"="*5)
print(data_string)

#string multiline (dngn menggunakan enter, newline, \n)
data_string = f" nama = {data_nama}\n umur = {data_umur}\n tinggi = {data_tinggi}\n ukuran sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"DATA STRING"+"="*5)
print(data_string)

#string multiline (kutip triplets) caranya adalah dngn mnggunakan kutip tiga biji
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
ukuran sepatu = {data_nomor_sepatu}
"""
#dia akan mengeprint apa pun yang ada dalam kutip sesuai dngn posisi nya jadi misal umur berada disebelah nama, dia akan ngeprint sperti itu
print("\n"+5*"="+"DATA STRING"+"="*5)
print(data_string)

#mengatur lebar dngn cara menggunakan :>(nilai nya, jadi jarak nya mau brapa)cntoh
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama}
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
ukuran = {data_nomor_sepatu:>5}
"""
# maka data_nama yang diatur akan brada di posisi ke 7, yah kayak mengatur jarak lebar dll nya
print("\n"+5*"="+"DATA STRING"+"="*5)
print(data_string)

#NAH UNTUK NGEPRINT INI ITU BANYAK CARANY, NNTI BISA CARI SENDIRI DI WEB W3SCHOOLS ATAUPUN YANG LAIN KRENA BNYAK KONVENSI2NYA 
