# Volume Tabung = pi * jari-jari * jari-jari * tinggi

print(10*'=',"LUAS Lingkaran",10*'=')

pi = float(22/7)
r = int(input("Masukkan Nilai Jari - Jari Lingkaran Sebagai Alas (r) = "))
t = int(input("Masukkan Nilai Tinggi Lingkaran (t) = "))

volume = 22/7*((r*r)*t)

print("Volume Tabung = ",volume)
