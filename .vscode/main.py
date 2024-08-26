#belajar python part5
#CASTING TIPE DATA
#merubah satu tipe ke tipe lainya

#data int
data_int=9
print("data = ",data_int, "type = ",type(data_int))
#nah kalau ingin merubah itu semua ada namanya operator casting

data_float=float(data_int)
data_str=str(data_int)
data_bool=bool(data_int) #bool akan false jika nilai int = 0 
#nah ini akan merubah si data_int menjadi float
print("data = ",data_float, "type = ",type(data_float))
print("data = ",data_str, "type = ",type(data_str))
print("data = ",data_bool, "type = ",type(data_bool))

#data float
data_float=9.5

data_int=int(data_float)
data_str=str(data_float)
data_bool=bool(data_float)
print("data = ",data_int, "type = ",type(data_int))
print("data = ",data_str, "type = ",type(data_str))
print("data = ",data_bool, "type = ",type(data_bool))
