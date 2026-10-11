import calendar

year = int(input("Masukkan tahun kelahiranmu : "))
month = int(input("Masukkan bulan kelahiranmu : "))

kalender = calendar.month(year,month)

print("\nINI ADALAH KALENDER DI BULAN KELAHIRANMU")
print("\n",kalender)