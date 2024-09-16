#belajar python part17
#FORMAT STRING

#contoh generic
#STRING
nama = "marlene"
#untuk membuat lebih mudah kita bisa membuat formating
format_str = f"hello {nama}"#kita panggil value dngn menggunakan kurung kurawal {}

print(format_str)

#kita juga bisa nmpilin BOOLEAN
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

#angka
angka = 2005.5
format_str = "angka = " + str(angka)
print(format_str)#ini akan error karena tipe datanya tidak sesuai, kita harus menambahkan tipe data str. maknya lebih mudah memeakai formating

format_str = f"angka = {angka}"
print(format_str)#nah lebih mudah kan begini

#bilangan bulatnya saja
angka = 15
format_str = f"angka bil bulat = {angka:d}"# :d disini artinya kita ingin menampilkan si angka ini ialah bilangan bulat
print(format_str)#jika contoh kita membuat angka 15.5 ini akan error karena si tipe nya adalah float bukan lagi integer

#bilangan ribuan
angka = 1000
format_str = f"ribuan = {angka:,}"
print(format_str)#nah biasanya angka ini kan ada koma diblkang angka nya (disini contoh 2) maka kita tinggal masukin (titik dua koma di value angka yang di format)

#bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"#nah dngn bgini kita akan mngambil dua angka di blkang koma, 2 berarti bnyak angka yang diambil, nah f adalah tipe data float
print(format_str)#nah kalau begini kita akan menampilkan smuanya saat di print, tapi bisa gak kita ingin nampilin contoh nya dua angka doang diblkang koma? bisa, dngn cara menggunakan titik dua titik yang berarti itu akan menampilkan anka diblkang koma

#menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.2f}"#nah contoh karena kan ini dua angka yang diambil jadi, sharusnya jumlah angka dari depan smpai dua angka diblkang koma ialah 7 (koma nya juga diitung), lalu kita tambahin disini 7 yang brarti ialah jumlah angka, nah hasilnya akan tetap sama

#tapi bagaimana jika kita membuat angka yang akan ditampilkan berbeda dari jumlah angka dari depan hingga blkang koma yang dipanggil, cntoh disini kita akan membuat 10, maka angka nya akan bergeser hingga membuat sebuah tempat ksoong yang skiranya bisa diisi sisa angka dari jumlah angka yang dipanggil, lalu gimana kalau ingin mengisi daerah kosong tersebut? kita tinggal menulis angka lagi didepan banyak nya jumlah angka, contoh kita ingin mengisi nya dngn 0
print(format_str)

#menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.124
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus:+.2f}"#nah cara agar kita dapat mengeluarkan tanda nya, dngn cara menambahkan :+d yang berarti kita akan menampilkan tandanya 

print(format_minus)
print(format_plus) 

#memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.0%}"#nah cara agar menjadi persen ialah dengn memberikan titik dua lalu %, tapi apa yg akan terjadi ialah ada bnyak 0, nah cara agar tidak bnyak 0 adalah dngn mnggunakan titik dan ada brapa bnyak 0, disini kita contoh dngn gdk angka 0 sama sekali maka akan mnjadi ():.0%)
print(format_persen)

#info tambahan, didalam kurung kurawal kita dapat mlakukan operasi
#melakukan operasi aritmetika didalam kurung kurawal (placeholder)
#contoh
harga = 10000
jumlah = 5

format_string = f"harga total = Rp.{harga*jumlah:,}"
print("harga smuanya menjadi =",format_string)

#format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal =  f"octal = {oct(angka)}"
format_hexadecimal =  f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexadecimal)