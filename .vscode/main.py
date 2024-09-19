#belajar python part20
#if dan else statement

#1. if ny
#2. kondisi nya
#3. aksi nya
nama = input("masukan nama kamu = ")

#RUMUS IF
#if kondisi: aksi
#program selanjutnya

#contohnya (1.PROGRAM IF INLINE)
if nama=="ucup": print("kamu ganteng abiezz")#nah disini kondisinya ialah (nama == ucup), akan melakukan aksi apa? print("kamu ganteng abiezzz")
print(f"Terima kasih {nama}")

# #CONTH
# if nama == "ucup":
#     print("kamu ganteng")
# else:
#     print(f"terima kasih {nama}")

#contohnya (2.PROGRAM IF DNGN INDENTATION)
if nama == "ucup":
    print("kamu ganteng abiezz")
    print("kamu juga keren banget")#nah ini dua adalah contoh indentation, atau apapun itu yang menjorok kedalam stelah sebuah kondisi, dimana berarti ini akan dijalankan ketika kondisi nya terpenuhi.
print(f"Terima kasih {nama}")#nah jika ingin keluar dari indentation maka kamu harus kembali ke posisi awal (gunakan backspace supaya tidak menjorok kedalam if, atau kamu harus sejajar dngn kondisi nya)

#NAH TADI KAN CUMAN AKSI KETIKA DIA TRUE ("ATAU NILAI NYA BENER", gmana kalau salah, apakah bisa menambhkan aksi? bisa dengn (ELSE STATEMENT))

nama = input("masukan nama kamu = ")

#contohnya (3. ELSE STATEMENT)
if nama == "otong":#jika ini benar, maka lakukan line33
    print("hai otoooong, si keren!!!")
else:#sejajar dngn kondisi sblmnya, nah jika line 32 tidak sesuai maka lakukan line 35
    print("ah kamu bukan otong, kamu gak keren")

print("akhir program")


