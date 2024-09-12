#codingan aku
print("mari kita membuat operasi penghitungan nilai kelulusan siswa\ndengan poin 1-10")
nama_siswa = str(input("nama siswa = "))
nilai_math = int(input("nilai math = "))
nilai_kimia = int(input("nilai kimia = "))
nilai_fisika = int(input("nilai fisika = "))
jumlah_nilai = (nilai_math+nilai_fisika+nilai_kimia)/3
if jumlah_nilai>5:
    print("rata rata nilai siswa = ",jumlah_nilai)
    print(nama_siswa,"nilai kamu B\nkamu lulus.")
elif jumlah_nilai>8:
     print("rata rata nilai siswa = ",jumlah_nilai)
     print(nama_siswa,"nilai kamu A\nkamu lulus.")
elif jumlah_nilai<5:
    print("rata rata nilai siswa = ",jumlah_nilai)
    print(nama_siswa,"nilai kamu C\nmaaf kamu tidak lulus.")