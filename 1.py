Burung=(int(input("Masukkan Jumlah Burung pada penangkarang : ")))
BurungMati=float(111/1000)
Mati=Burung*BurungMati
print("Jumlah burung yang mati sebelum melahirkan yaitu : ", Mati)
Lahir=Burung-Mati
print("Jumlah Burung yang Lahir adalah : ", Lahir)

Jumlah_hari=(int(input("Masukkan Jumlah Hari : ")))
if Jumlah_hari == 21:
    Total_hari=Jumlah_hari/21
    print("Banyak melahirkan adalah : ", Total_hari)
elif Jumlah_hari > 21:
    Total_hari = Jumlah_hari / 21
    print("Banyak melahirkan adalah : ", Total_hari)
else:
    print("Maaf Tidak dapat di proses")

Jumlah_burung=Lahir*Total_hari
print("Jumlah Burung pada hari ke" ,Jumlah_hari ,Jumlah_burung)