#BELAJAR PYTHON PART11
#LATIHAN KOMPARASI DAN LOGIKA

#membuat gabungan area rentang dari angka

# ++++++++3---------10++++++++

inputuser = float(input("masukan angka yang bernilai kurang dari 3\n atau\n lebih besar dari 10\n"))

#++++++++3---------
#kurang dari

iskurangdari = (inputuser <3)
print("kurang dari 3=", iskurangdari)

#-----------10+++++++++
#lebih besar dari

islebihbesar = (inputuser >10)
print("lebih besar dari 10=", islebihbesar)

#jikalau ingin menggabungkan dua buah pers (lebih dari, kurang dari dll) itu kita gunakan or

iscorrect = iskurangdari or islebihbesar
print("angka yang anda masukan bernilai =", iscorrect)

# -----3++++++++10------
#ini adalah kasus irisan

inputuser=float(input("masukan angka yang bernilai lebih dari 3\n dan\n kurang dari 10\n"))

# ------3+++++++++++
#lebih dari 3
islebihbesar = inputuser >3
print("lebih besar = ",islebihbesar)

# +++++++++++10--------
#kurang dari 10
iskurangdari = inputuser <10
print("kurang dari 10 =", iskurangdari)

inputuser=float(input("masukan angka lebih besar dari 0\n dan\n kurang dari 5\n dan lebih besar dari 8\n dan kurang dari 11\n"))

#--------0+++++++
#lebih dari 0
islebihbesar = inputuser > 0
print("lebih besar dari 0 =", islebihbesar)

#++++++++5--------
#kurang dari 5
iskurangdari = inputuser < 5
print("kurang dari 5 =", iskurangdari)

#---------8+++++++
#lebih besar dari 8
islebihbesar = inputuser > 8
print("lebih besar dari 8 =", islebihbesar)

#++++++++11-------
#kurang dari 11
iskurangdari = inputuser < 11
print("kurang dari 11 =", iskurangdari)

inputuser=float(input("masukan angka kurang dari 0\n dan\n lebih besar dari 5\n dan kurang dari 8\n dan lebih besar dari 11\n"))

#+++++++0---------
#kurang dari 0
iskurangdari = inputuser < 0
print("lebih besar dari 0 =", iskurangdari)

#-------5+++++++
#lebih dari dari 5
islebihbesar = inputuser > 5
print("kurang dari 5 =", islebihbesar)

#+++++++8---------
#kurang dari 8
iskurangdari = inputuser < 8
print("lebih besar dari 8 =", iskurangdari)

#---------11++++++++
#lebih dari 11
islebihbesar = inputuser > 11
print("kurang dari 11 =", islebihbesar)