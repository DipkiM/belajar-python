#belajar python part21
#membuat kalkulator sederhana (LATIHAN)

#pertama kita ambil data user, yaitu angka pertama, angka kedua dan operasinya
#kedua kita ambil cabang nya, misal dia milih operasi satu trus ya dia akan menjalankan operasi satu

print(20*"=")
print("MEMBUAT KALKULATOR SEDERHANA")
print(20*"="+"\n")

angka1 = float(input("masukan angka pertama anda\n"))#knpa kita pakai float? karena ini bisa membuat kita menggunakan angka yang memiliki koma koma an, kalau int nnti dia error
angka2 = float(input("masukan angka kedua anda\n"))
operasi = input("masukan operasi anda (+,-,*,/,**)\n")

#PERCABANGAN NYA
if operasi == "+":
    hasil=(angka1 + angka2)
    print(f"nilai dari perhitungan anda ialah = {hasil}")
elif operasi == "-":
    hasil=(angka1 - angka2)
    print(f"nilai dari perhitungan anda ialah = {hasil}")
elif operasi == "*":
    hasil = (angka1 * angka2)
    print(f"nilai dari perhitungan anda ialah = {hasil}")
elif operasi == "/":
    hasil = (angka1 / angka2)
    print(f"nilai dari perhitungan anda ialah = {hasil}")
elif operasi == "**":
    hasil = (angka1 ** angka2)
    print(f"nilai dari perhitungan anda ialah = {hasil}")
else:
    print("masukan operasi yang jelas")