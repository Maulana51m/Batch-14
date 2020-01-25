def membuatgaris():
    nama = input("Masukkan Nama Anda : ")
    nama_baru = ""
    nama_saya = " "

    print
    for tulis in nama:
        if tulis not in nama_saya:
            nama_baru += tulis
            print("Nama baru anda sudah dibuat : ", nama_baru)
    print("Nama baru anda adalah : ", nama_baru)
    print(" ")

membuatgaris()

def drawline():

    for i in range(1,10):
        print(' '*(i-1)+"D"*(1))
        print(' '*(2-1)+"U"*(1))
        print(' '*(3-1)+"M"*(1))
        print(' '*(4-1)+"B"*(1))
        print(' '*(5-1)+"W"*(1))
        print(' '*(6-1)+"A"*(1))
        print(' '*(7-1)+"Y"*(1))
        print(' '*(8-1)+"S"*(1))
        break

drawline()