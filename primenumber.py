#asal fonksiyon tanimi
def asal_mi(X):
    #girilen sayi 1'e kucuk veya esitse asal degildir
    if X <= 1:
        return False
    #girilen sayi 2 ise asaldir.
    elif X == 2:
        return True
    #2den buyukse 2'den X'e kadar olan her sayiya kalanli bolme yapilir ve 0'a esit olursa asal degildir. 
    else:
        for i in range(2, X):
            if X % i == 0:
                return False
        #0'a esit degilse asaldir.        
        return True
#kullanicidan input alimi
X = int(input("Bir sayı girin: "))
#eger dogruysa asal bir sayidir promptu, yanlissa degildir promptu
if asal_mi(X):
    print(X, "asal bir sayıdır.")
else:
    print(X, "asal bir sayı değildir.")
