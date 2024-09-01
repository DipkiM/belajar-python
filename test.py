# print("apa kabar my friend?")
# a=12
# print(a)

# kita bisa mengcompile python ke yang namanya BYTECODE
# cara mengcompile, buka terminal dan tuliskan
# python -m py_compile (nama file)
# bedanya apa yg di compile dan interpreted? bedanya ialah yang di compile akan lebih cepat dari pada interpreted.
# mungkin karena ini masih sedikit program yang kita buat maka perbedaanya sedikit, tapi smkin banyak program yang kita buat maka akan terasa waktu perbedaan antara program yang compile dengan interpreted waktu hasilnya keluar, jadi terbukti bahwa compile akan lebih cepat dengan interpreted
# maka dari itu krna python bahasa interpreted maka hasilnya akan lebih lambat daripada bahasa compiled tapi itu bisa ditanggulangi dengan cara mengcompile file nya terlebih dahulu, sperti yang diajarkan diataas

#program fahrenheit ke kelvin
celcius = float(input("masukan suhu dalam fahrenheit = "))
print("suhu adalah ",input,"fahrenheit")

celcius = 5/9 * (celcius-32)
print("suhu dalam celcius ialah ", celcius, "celcius")
kelvin = celcius+273
print("suhu dalam kelvin ialah ",kelvin, "kelvin")

#program kelvin ke fahrenheit
celcius = kelvin-273
print("suhu dalam celcius adalah ", celcius,"celcius")
fahrenheit = (9/5)*celcius+32
print("suhu dalam fahrenheit ",fahrenheit,"fahrenheit")
