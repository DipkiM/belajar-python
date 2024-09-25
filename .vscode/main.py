#belajar python part26
#break
print("=====CONTOH FUNGSI BREAK KEREN=====")
data_int = int(input("hitung sampai = "))
angka = 0
while True:
    angka +=1
    print(f"count = {angka}")
        
    if angka == data_int:
        print("niceee")
        break#jadi yang 4 dan 5 nya gk di print dia langsung ke end (cukupppp)

        #NAH JADI DENGAN INI KITA BISA MENGEPRINT SBERAPA BNYAK MAU NYA
    print("wassuppp bebeh!!!")

print("cukupppp finishh!!")

print("=====CONTOH SEDERHANA=====")
angka = 0
while angka <5:
    angka +=1
    print(f"angka sekarang ialah {angka}")
        
    if angka == 3:
        print("niceee")
        break #jadi dia langsung ke end gk lanjut ke 4 dan 5
    print("wassuppp bebeh!!!")
print("cukupp")