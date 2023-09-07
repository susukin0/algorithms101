# Başlangıç Değerlerinin Tanımlanması
n = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
faktoriyel = 1

# Faktöriyel Hesaplama
for i in range(1, n + 1):
    faktoriyel *= i

# Sonucun Yazdırılması
print(f"{n}! = {faktoriyel}")
