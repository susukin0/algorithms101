# Başlangıç değeri
baslangic = 10

# Bitiş değeri
bitis = 110

# Döngü başlat
for i in range(baslangic, bitis + 1):
    # Karekökü al
    karekok = i ** 0.5

    # Eğer karekök tam sayıysa, bu bir tam karedir.
    if karekok.is_integer():
        print(i)
