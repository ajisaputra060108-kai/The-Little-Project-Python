def menu():
    print("=======MENU ATRIATH=======")
    print("1. Americano\t Rp5.000")
    print("2. Mico\t\t Rp10.000")
    print("3. Lattte\t Rp15.000")
    print("4. Nasgor\t Rp20.000")
    print("5. Lihat keranjang")
    print("-"*26)
    

pesanan = []
harga_pesanan = []
QTY = []

while True:
    print("\n")
    menu()
    try:
        pilihan = int(input("Silahkan pilih menu yang anda inginkan : "))
    except ValueError:
        print ("Mohon hanya pilih menu yang ada di atas")
        continue
    if pilihan == 1:
        harga = 5000
        qty = int(input("Pesan berapa Americano?: "))

        total = harga*qty

        pesanan.append("Americano")
        QTY.append(qty)
        harga_pesanan.append(total)

    elif pilihan == 2:
        harga = 10000
        qty = int(input("Pesan berapa Mico?: "))

        total = harga*qty

        pesanan.append("Mico")
        QTY.append(qty)
        harga_pesanan.append(total)
        

    elif pilihan == 3:
        harga = 15000
        qty = int(input("Ingin pesan berapa Latte?: "))

        total = harga*qty

        pesanan.append("Lattte")
        QTY.append(qty)
        harga_pesanan.append(total)
        

    elif pilihan == 4:
        harga = 20000
        qty = int(input("Ingin pesan berapa Nasgor?: "))

        total = harga*qty
        
        pesanan.append("Nasgor")
        QTY.append(qty)
        harga_pesanan.append(total)
        

    elif pilihan == 5:
        print("====KERANJANG ANDA====")

        no = 0
        if len(pesanan) > 0:
            print(f"{'No':<3} {'Nama':<11} {'Qty':<8} {'Harga':<7}")
            print("-"*31)
            while no < len(pesanan):
                print(no+1, ".", pesanan[no], "\t", QTY[no], "\t", f"Rp{harga_pesanan[no]}") #pesanan[no] memanggil index dari list pesanan dengan no index yang di sesuaikan dengan variabel no
                no += 1

        else:
            print("\n(Anda belum memasukkan apapun)")

    else:
        print("Pilihan tidak valid!")
        continue

    lanjut_tidak = input("\nApakah anda ingin memesan lagi? (y/n) : ")
    if lanjut_tidak == 'y':
        continue
    else:
        lanjut_tidak == 'n'
        break

print("\n")

#Tabel
print("==========ATRIATH COFFEE=========")
print("-"*33)
print(f"{'No':<3} {'Nama':<11} {'Qty':<8} {'Harga':<7}")
print("-"*33)

#Isi pesanan
no = 0
if len(pesanan) > 0:
    while no < len(pesanan):
        print(no+1, ".", pesanan[no], "\t", QTY[no], "\t", f"Rp{harga_pesanan[no]}") #pesanan[no] memanggil index dari list pesanan dengan no index yang di sesuaikan dengan variabel no
        no += 1
else:
    print("\nAnda belum memesan apapun")

#Total pesanan
print("-"*33)
total1 = sum(harga_pesanan)
print(f"Total harga\t\t Rp{total1}")

print("\nSilahkan tunjukkan bukti transaksi ini ke kasir untuk melakukan pembayaran")
print("\nTHANK YOU")

