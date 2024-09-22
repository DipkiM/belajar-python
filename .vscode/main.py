#belajar python part20
#ELIF STATEMENT

nama = input("nama anda siapa? ")
# ini if else
# if kondisi:
#     aksi:
# else:
#     aksi false:

# ini elif
# if kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# elif kondisi:
#     aksi true. NAH JADI KITA BISA PAKAI ELIF INI SBNYAK APAPUN YANG KITA MAU

if nama == "ucup": #ini kondisi satu
    print("hai ganteng") #aksi true satu
elif nama == "otong": #ini kondisi satu
    print("hai si kece bingits") #aksi true dua
else:
    print("siapa lu, gua gak kenal")#nah ini akan menampilkan ketika kita menginput nama selain otong dan ucup
print("ini adalah hasil akhir dari program")

# NAH ITU DIA KONDISI ELIF, TAPI SI ELIF INI BISA DITAMBAH SBNYAK APAPUN