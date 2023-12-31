# algorithms start!

 ![96308083](https://github.com/susukin0/algorithms101/assets/70662829/4c96aac3-35a3-459f-8d24-0b4cb176d42a) a little bit homework of pseudocode diagrams for SkyLab BootCamp :)

____________________________________________
### Sayı asal mı diye kontrol eden algoritma
metinsel ifadesi:
```sh
1.adim: basla
2.adim: "Bir sayı girin:", X

3.adim: eger X <= 1 ise
    3.1: X "asal bir sayı değildir."
    3.2: bitir
    3.3: Degilse devam et
    
4.adım: eger X == 2 ise
    4.1: X "asal bir sayidir."
    4.2: bitir
    4.3: Degilse devam et

5.adim: Döngü(for loop) başlangıcı İ=2
    5.1: 2'den X'e kadar (X dahil degil) olan her İ sayısı için:
    5.2: X'in İ'ye olan bölümünden kalan 0:
    5.3: Doğru ise X "asal bir sayidir."
    5.4: bitir.
    5.5: Yanlış ise X "asal bir sayı değildir."
    5.6: bitir.
```
Diagram ise aşağıdaki şekildedir (python kodu icin bkz. https://github.com/susukin0/algorithms101/blob/main/primenumber.py):

![primenumber](https://github.com/susukin0/algorithms101/assets/70662829/d3cf0955-8999-4957-a137-e43b34a7413a)


_____________________________________________________
### Girilen sayının faktöriyelini bulan algoritma
metinsel ifadesi:
```sh
   1.adim: başla.
   2.adim: n adlı bir değişken belirlenir.
   3.adim: faktoriyel değişkeni 1 e eşitlenir.
   4.adim: 1den n+1 e kadar olan her i sayisi icin
   5.adim: faktoriyel değeri her döngü adımında i ile çarpılır.
   6.adim: faktoriyelin yazdirilmasi.
   7.adim: bitir.
```
Diagram ise aşağıdaki şekildedir (python kodu icin bkz. https://github.com/susukin0/algorithms101/blob/main/faktoriyel.py):
![faktoriyel-1](https://github.com/susukin0/algorithms101/assets/70662829/11eb547b-fa27-4a51-ba73-30341a8a8dc4)

_____________________________________________________________
### 10 ile 110 arasındaki tam kare sayıları yazdıran algoritma
metinsel ifadesi:
```sh
1.adim: basla
2.adim: baslangic(10) ve bitis(110) aralıklarını tanımla.
3.adim: (döngü başlat) baslangic ve bitis+1 arasındaki her i sayısı için
4.adim: i nin karekökünü al.
5.adim: Eğer karekök tam sayıysa, bu bir tam karedir.
6.adim: dogruysa ekrana yaz.
7.adim: yanlissa aralik sonuna kadar dongu.
8.adim: bitir.
```
Diagram ise aşağıdaki şekildedir (python kodu icin bkz. https://github.com/susukin0/algorithms101/blob/main/10square110.py):
![10square110](https://github.com/susukin0/algorithms101/assets/70662829/7161b1b2-ba04-441a-8596-84ae71f2875d)
stop!

