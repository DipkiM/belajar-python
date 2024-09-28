#belajar python part27
#latihan perulangan membuat segitiga

sisi = 10
count = 1
#1.Menggunakan FOR
print("awal dari for")
for i in range(sisi):
    print("*"*count)
    count+=1#ini logika nya jadi kan bintang * dngn count itu karena pertama kali count nya satu maka bintang kali satu, nah stelah di print kan count nya ditambah 1 ke ata tuh nahh jadi bgitu trus.
print("akhir dari for")
print("\n")

#2.Menggunakan WHILE
print("awal dari while")
count=1
while True:
    print("*"*count)
    count+=1
    if count > sisi:
        break
print("akhir dari while")

#3.hanya ganjil saja
print("awal dari while")
count=1
while True:
    if (count%2):
        #print jika ganjil
        print("*"*count)
        count+=1
    else:
        #akan kembali keatas jika ganjil
        count+=1
        continue
    if count > sisi:
        #akan break ketika melebihi sisi
        break
print("akhir dari while")
print('\n')


print("awal dari while")
count=1
spasi = int(sisi/2)
while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -=1
        count+=1
    else:
        #akan kembali keatas jika ganjil
        count+=1
        continue
    if count > sisi:
        #akan break ketika melebihi sisi
        break
    
print("akhir dari while")




for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()




