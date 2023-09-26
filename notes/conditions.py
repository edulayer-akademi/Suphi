# ŞART KOŞUL YAPILARI

### IF KEYWORD ###


if 1 == 2: # false
    print("if bloğuna girdi")

a = 1
b = 1
kosul = (a == b)
kosul2 = a > b
kosul3 = a >= b
kosul4 = a!=b

kosul5 = bool(a / b) # kalan varsa bool türden true olacak, kalansız bölünüyorsa bool türden false olacak
a = 10
b = 10

a # int

a = 0

liste = [1,2,3,4]
liste2 = []

if liste:
    # bloğa girer
    pass
if liste2:
    ...
    ab = 4
    # bloğa girmez
if a: 
    print("bloğa girmeyecek çünkü sıfır = false")
if a:
    print(kosul)
    print("if bloğu çalışıyor")

[]
(1,)
{}
""
0
0.0

bos_liste = []
if bos_liste != []: # aynı
    if bos_liste: # aynı
        ...

if not bos_liste: # true
    ... #print("ben boşum")

# a != b 
# == ve not operatörü kullanarak yazın

if not (a == b):
    ...
if a != b:
    ...


a = 100
b = 98
if a > b:
    ... # print("100 > 98")

if not (a <= b):
    ... # print("100 >= 98 yanlıştır")

### ELIF KEYWORD (ELSE-IF KEYWORD)

if a == 101:
    ab = a + 3
    print("a=100")
elif b == 99:
    ab = b - 40
    print("b=99")
elif b == 99:
    ab = b - 40
    print("b=99")
### ELSE KEYWORD
else: 
    ab = 50
    ... #print("hiçbir durum karşılanmadı")

if True:
    ...
elif kosul:
    ...
elif kosul2:
    ...
elif kosul3:
    ...
if True:
    ...
else:
    ...


if kosul: 
    ...

if kosul:
    ...
else:
    ...

if kosul:
    ...
elif kosul:
    ...

if kosul:
    ...
elif kosul:
    ...
else:
    ...

# sayi = int(input("bir sayı giriniz: ").strip())

# int('567          ') # int('567')


# if sayi == 567:
#     print(sayi)
# else:
#     sayi = input("bir sayı giriniz: ")
#     print(sayi)

# notlar = input("notlarınızı giriniz: ") # '60 65 70 75'

# notlar = (notlar.split()) # ['60', '65', '70', '75']

# if len(notlar) == 4:
#     turkce, ingilizce, tarih, felsefe = notlar
#     print("ingilizce=%s"%ingilizce)
# elif len(notlar) > 4:
#     turkce, ingilizce, tarih, felsefe = notlar[:4]
#     print("elif bloğu")
#     print("ingilizce=%s"%ingilizce)
# else:
#     print("yeterli argüman yok")
#     print(notlar)
#     if len(notlar) == 3:
#         turkce, ingilizce, tarih = notlar
#         felsefe = 50
#         print(tarih)
#     elif len(notlar) == 2:
#         turkce, ingilizce = notlar
#         tarih = 50
#         felsefe = 50
#         print(tarih)
#     else:
#         print("En az bir argüman girmelisiniz.")
    


ders_notu = -7
match (ders_notu):
    case 0:
        print("sınavlara girmediniz")
    case (10 | 20 | 30 | 40):
        print("kaldınız")
    case (50 | 60 | 70 | 80 | 90 | 100):
        print("geçtiniz")
    case _:
        ... #print("kaldınız mı geçtiniz mi belirsiz")

# bitwise or (bitsel veya opr. |)

### short if / ternary opertor / ternary if

yas = 19

resit = True if yas >= 18 else False

# fstringlerde short-if kullanımı


selamlama = f"Merhaba Mert, siz {'reşitsiniz' if resit else 'reşit değilsiniz'}"

# print(selamlama)

sozluk = {
    "resit": int(resit)
}

# print(sozluk)

# >=  greater than
# <=  less than
# < greater
# > less
