def asal_mi(X):
    if X <= 1:
        return False
    elif X == 2:
        return True
    else:
        for i in range(2, X):
            if X % i == 0:
                return False
        return True

X = int(input("Bir sayı girin: "))
if asal_mi(X):
    print(X, "asal bir sayıdır.")
else:
    print(X, "asal bir sayı değildir.")