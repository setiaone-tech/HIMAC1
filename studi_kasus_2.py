import random, os, time

data_harga = [100000, 200000, 500000, 1000000]

def menu():
    print("+==================================================+")
    print("|                     M HOTEL                      |")
    print("+==================================================+")
    print("|1. Reservasi                                      |")
    print("|2. Keluar                                         |")
    print("+==================================================+")
    print("| Silahkan Pilih (1/2) :                           |")
    print("+==================================================+")

def jenishotel():
    print("+==================================================+")
    print("|                    JENIS KAMAR                   |")
    print("+==================================================+")
    print(f"|1. Standar   (Rp. {data_harga[0]}/malam)                   |")
    print(f"|2. Suite     (Rp. {data_harga[1]}/malam)                   |")
    print(f"|3. Deluxe    (Rp. {data_harga[2]}/malam)                   |")
    print(f"|4. Executive (Rp. {data_harga[3]}/malam)                  |")
    print("+==================================================+")

def order(nama_pemesan, jenis_kamar, nomor_kamar, lama, tanggal, total):
        print("+==================================================+")
        print("|                RESERVASI M HOTEL                 |")
        print("+==================================================+")
        print("|NAMA        :",nama_pemesan," "*(34-len(nama_pemesan)),"|")
        print("|JENIS KAMAR :",jenis_kamar," "*(34-len(str(jenis_kamar))),"|")
        print("|NOMOR KAMAR :",nomor_kamar," "*(34-len(str(nomor_kamar))),"|")
        print("|DURASI      :",lama," "*(34-len(str(lama))),"|")
        print("|TANGGAL     :",tanggal," "*(34-len(tanggal)),"|")
        print("|TOTAL HARGA : Rp. ",total," "*(29-len(str(total))),"|")
        print("+==================================================+")

ulang = "y"
while ulang == "y":
    os.system('cls')
    menu()
    pilih = int(input("Input : "))
    if(pilih == 1):
        jenishotel()
        nampes = input("Nama Pemesan : ")
        jeniskamar = input("Jenis Kamar (1/2/3/4) : ")
        nomkamar = input("Nomer Kamar : ")
        lama = input("Durasi (perhari) : ")
        tgl = input("Tanggal Pesanan (10 Juni 2023) : ")
   
        if jeniskamar.isdigit() != True or int(jeniskamar) < 1 or int(jeniskamar) > 5:
            print("JENIS KAMAR TIDAK TESEDIA!")
            time.sleep(2)
        else:
            if lama.isdigit() != True:
                print("HARAP MASUKAN DURASI BERUPA ANGKA!")
                time.sleep(2)
            else:
                total = data_harga[int(jeniskamar)-1] * int(lama)
                order(nampes, jeniskamar, nomkamar, lama, tgl, total)
                ulang = input("Ingin ulang lagi(y/t) : ")
                if ulang.lower() != "y":
                    print("TERIMA KASIH TELA MENGGUNAKAN PROGRAM:)")
    elif(pilih == 2):
        print("TERIMA KASIH TELA MENGGUNAKAN PROGRAM:)")
        ulang = "t"
    else:
        print("PILIHAN TIDAK TERSEDIA!")
           