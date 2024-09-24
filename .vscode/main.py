#belajar python part22
#FOR LOOP (perulangan)

#contohny kita membuat perulangan angka
# angka = 1
# print(angka)
# angka = angka + 1
# print(angka)
# angka = angka + 1#nah berarti jadi 3 kan
# print(angka)
# #tapi ini tidak efektif karena smkin bnyak perulangan line smkin bnyak dan panjang

#paling gampangnya ialah kita punya (FOR) lalu kita ada (KONDISI) dan juga (AKSI)
# for konidisi:#jadi misalkan kondisi nya apa akan mlakukan aksi apa gitu
#     aksi

# for i in range (5):#nah ini artinya untuk semua i didalam range 5, jadi istilahnya smua angka di range 5 ini akan dikasi nama i

# contoh

#INI DENGAN LIST
angka2_list = [1,2,3,4,5] #ini adalah angka yg berbentuk list

for i in angka2_list:#jadi nanti setiap brulang si i itu akan jadi 1, jadi 2, 3 dst
    print(f"angka i skrang --> {i}")
print("akhir program 1\n")

#INI DENGAN RANGE
angka2_range = range(5)

for i in angka2_range:
    print(f"angka i skrang --> {i}")
print("akhir program 2\n")

angka2_range = range(1,5)#ini artinya dia mulai dari 1 dan diakhiri sblum 5 (atau dia cuman ngeprint sampai 4)

for i in angka2_range:
    print(f"angka i sekarang ==> {i}")
print("akhir dari program 3\n")

#MENGGUNAKAN STRING
data_str = "saya ganteng abiesss"

for huruf in data_str:
    print(huruf)
print("akhir dari program 4\n")# jadi dia akan ngeprint per huruf nya sampai selesai secara brulang

