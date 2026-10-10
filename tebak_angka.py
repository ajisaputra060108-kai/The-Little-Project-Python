jawab = 86

print("===AYO MAIN TEBAK ANGKA===")
print("Cluenya adalah :")
print("1. Angka puluhan")
print("2. Akar dari 64")
print("3. Bulan kelahiran kaisa")


while (True):
    tebak = int(input("Masukkan tebakan anda : "))

    if tebak == jawab:
        print("Yeay.. selamat kamu berhasil nebak angkanya\n")
        break
    elif 1 <= tebak <= 20:
        print("Waduh, angkanya masih jauh banget bang\n")
    elif 21 <= tebak <= 40:
        print("Hmm, masih lumayan jauh bang\n")
    elif 41 <= tebak <= 60:
        print("Masih harus tambah lagi banh\n")
    elif 61 <= tebak <= 70:
        print("Nah ini udah lumayan deket nih\n")
    elif 71 <= tebak <= 80:
        print("Nah ini udah deket banget.. Ayo beberapa langkah lagi\n")
    elif 81 <= tebak <= 85:
        print("Wow wow wow\n")
    elif 87 <= tebak <= 90:
        print("Waduh, kelewat dikit banh..\n")
    elif 91 <= tebak <= 99:
        print("Udah banh jangan ngejauh lagi banhh\n")
    elif tebak > 100:
        print("Kan di cluenya cuman angka puluhan banh\n")
    else:
        print("Masukkin angka yang bener woii\n")