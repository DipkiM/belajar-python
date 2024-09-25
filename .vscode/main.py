#belajar python part25
#continue pass

#PASS fungsinya sbagai dummy (tidak akan dieksekusi)

#cntoh
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass#ini tidak akan dieksekusi (hanya lewat aja)
        # print("whatsup brow")
    print(angka)

#CONTINUE

angka = 0
print(f"angka sekarang adalah {angka}")

while angka < 5:
    angka+=1
    print(f"angka sekarang ialah {angka}")#ini aksi 1
#lalu continue fungsiny gmn?
#misal kita ingin buat kondisi saat dia sedang ngeloop, jadi cntoh saat selesai aksi 1 trus dikasih kondisi yng akan jadi pengecek, ketika dia blm memenuhi kondisi maka dia akan nge loop lagi
    if angka == 3:
        print("niceee!!!")
        continue #ini akan membuat  loop mlompat ke step slnjutny, jadi setiap ada di loop kalok ketemu continue dia akan balik lagi keatas, jadi intinya smua looping yang ada di bawah nya di skip dan loncat ke step slanjutnya
    print("whassupp")#ini aksi 2
print("finish")

