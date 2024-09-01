#BELAJAR PYTHON PART8 LATIHAN PERHITUNGAN SEDERHANA
#LATIHAN KONVERSI SATUAN TEMPERATURE

#program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")
celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah ",input, 'celcius')

#reamur (4/5c)
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "reamur")

#fahrenheit (9/5*c+32)
fahrenheit = ((9/5)*celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#kelvin (c+273)
kelvin = celcius+273
print("suhu dalam kelvin adalah", kelvin, "kelvin")