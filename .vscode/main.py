#BELAJAR PYTHON PART13
#pengenalan string

# 1. cara membuat string
#contoh kita punya variabel data
data = "ini adalah string"#string ialah kumpulan dari karakter
print(data, type(data))#ini adalah cara pemanggilan nya

#cara membuat string

'''
    1. dengan cara menggunakan single quote ('.....')
    2. dengan menggunakan double quote (".....")
'''
data = 'menggunakan single quote'
print(data, type(data))

data = "menggunakan double quote"
print(data, type(data))

#kita juga bisa menggabungkan dua tadi
print("'halo apa kabar?'")
print('"halo apa kabar?"')
print("ini adalah hari jum'at")

    # 2. menggunakan tanda \
#BISA MEMBUAT (') MENJADI STRING
#print('mari kita sholat jum'at') nah ini akan error karena dikira kode telah ditutup di bagian(jum)
# maka dari itu kita bisa menggunakan tanda \ sperti ini:
print('mari kita sholat jum\'at')

#BISA MENJADI BACKSLASH
#print("c:\user\ucup") nah ini akan eror karena dia akan bingung backslash gk bisa dibaca, gimana cara agar backslash dapat dibaca sbgai string backslash? dngn cara menambahkan backslash lagi (\\)
print("c:\\user\\ucup")

#BISA MENJADI TAB (\t)
print("ucup\t otong, jauhan")#nah ini akan membuat space setelah ucup akan menjadi jarak ketika kita memakai tab
print("ucup\t\t\t\t otong, semakin jauh")#kita bisa menambahkan (\t) terus menerus dan akan membuat space nya smakin lebar atau smakin jauh

#BISA MENJADI BACKSPACE (\b)
print("ucup otong, ini jarak normal")#nah ini kan jarak normal, gimana kalau kita tambahkan (\b)
print("ucup \botong, jadi deketan")#jarak dari ucup ke otong akan menjadi lebih dekat

#BISA MENJADI NEWLINE (\n) (BARIS BARU)
print("baris pertama.\n baris kedua.")#ini yg kita kenal sbagai LF (line feed), ini biasany di mac os atau di linux dipakai nya LF (lihat kebawah kanan di samping {}python, nah ini biasanya newline menggunakan (\n))
print("baris pertama.\r baris kedua.")#ini kita kenal sbagai CR (carriage return), ini biasanya dipakai sama yg dulu sperti commodore, acorn dll
print("baris pertama.\r\n baris kedua.")#ini kita kenal sbagai CRLF (line feed carriage return), ini dipakai oleh windows, makanya terkadang suka beda ketika kita mau mendeteksi enter pada program windows dngn macos atau linux beda, krna yg windows pake CRLF sdngkan mereka menggunakan LF

    # 3. STRING LITERAL ATAU RAW (r".......")
#misalkan kalian suka bikin kata (hati-hati)
print("c:\new folder")#nah ini akan eror dong n nya akan menjadi LF. gimana caranya kita bikin dia tidak begitu?
print("c:\\new folder")#ini bisa, cuman bgaimana kalau kita punya banyak yg begituan? nah ini bisa dipermudah dngn memakai RAW STRING

#menggunakan RAW STRING
print(r'c:\new folder')#nah ini akan dianggap sbagai raw string (semuanya akan di print apa yg kita taruh disitu )

#multiline untuk LITERAL STRING (sama sperti membuat command)(""".....""")
print("""
    Nama : Ucup
    Kelas : 4SD
    Umur : 10 tahun
      """)
#maka nanti akan di print sesuai yang kita tulis disini, mau enter nya dan sbagainya

#kita juga bisa menggabungkan MULTILINE LITERAL STRING DAN RAW
print(r"""
    Nama : Ucup
    Kelas : 4SD
    Umur : 10 tahun
    Zodiac : Piesces
    Agama : islam
    website : www.ucup.com\newID
      """)
