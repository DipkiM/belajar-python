#BELAJAR PYTHON PART12
#operator bitwise

a = 9
b = 5

#bitwise or (|)
c = a|b
print("\n ==========or=========")
print("nilai :",a,', binary :', format(a,"08b"))
#untuk format nnti di pelajari di string, ini cuman agar contoh aj dia diubah ke binary
print("\n ===============|")
print("nilai :",b,', binary :', format(b,"08b"))
print("nilai :",c,', binary :', format(c,"08b"))

#bitwise and (&)
c = a & b
print("\n ==========and=========")
print("nilai :",a,', binary :', format(a,"08b"))
print("\n ===============&")
print("nilai :",b,', binary :', format(b,"08b"))
print("nilai :",c,', binary :', format(c,"08b"))


#bitwise XOR (^)
c = a ^ b
print("\n ==========XOR=========")
print("nilai :",a,', binary :', format(a,"08b"))
print("\n ===============^")
print("nilai :",b,', binary :', format(b,"08b"))
print("nilai :",c,', binary :', format(c,"08b"))

#bitwise not (~)
c = ~a
#ini adalah operator yang membalikan, jadi misal si a nilainya 9, maka nannti di c akan menjadi -10 dia akan dibalikan dan plus satu
print("\n ==========not=========")
print("nilai :",a,', binary :', format(a,"08b"))
print("\n ===============(~)")
print("nilai :",c,', binary :', format(c,"08b"))

#shifting (pergeseran)

#shift right (>>)
c=a>>2
#iini berarti kita membuat a bergeser 2 kali ke kanan
print("\n ==========>>=========")
print("nilai :",a,', binary :', format(a,"08b"))
print("\n ===============(>>)")
print("nilai :",c,', binary :', format(c,"08b"))

#shift left (<<)
c=a<<2
#iini berarti kita membuat a bergeser 2 kali ke kiri
print("\n =========<<=========")
print("nilai :",a,', binary :', format(a,"08b"))
print("\n ===============<<)")
print("nilai :",c,', binary :', format(c,"08b"))




