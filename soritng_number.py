angka_acak = []

for i in range(5):
    acak = int(input(f"Masukkan angka ke-{i+1} : "))
    angka_acak.append(acak)

print(f"\nAngka sebelum di urutkan : {angka_acak}")

n = len(angka_acak)

for i in range(n):
    for j in range(0, n - i - 1):
        if angka_acak[j] > angka_acak[j+1]:
            temp = angka_acak[j]
            angka_acak[j] = angka_acak[j+1]
            angka_acak[j+1] = temp

print(f"Angka setelah diurutkan\t : {angka_acak}")