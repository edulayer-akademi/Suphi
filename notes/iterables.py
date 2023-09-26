# Kavramlar

## Iterable: 
metin = "Kahramanmaraş" # Iterable 
harf_notu = "F" # Iterable

# 1.5 float
# 99 int
# 2e5 float
# True bool
# "" str




### TUPLES (DEMETLER) ###

t = (1, 1, 4, 8, "panter", True, True)

# sabit gezilebilir ifadeler

harf_notlari = ("AA", "BB", "BC", "CD", "FF")

# readonly variable - constant

isim = "Mert"


isim = "Ahmet"

t2 = ("Ata", )
t3 = "Ata"

### LISTS (LISTELER) ###

# Iterable bir tür


# meyve_listesi = meyve_listesi[::-1]
# meyve_listesi[::] = ["Ananas", "Muz"][::-1]

# list.append fonksiyonu
# l = [a, b, c]
# l[3] = d
# l.append(d)
# [a, b, c, d]

meyve_listesi = ["Elma", "Çilek", "Kivi", "Muz", "Karpuz"]


meyve_listesi.append("Avokado")
meyve_listesi.append("Kiraz")
meyve_listesi.append("Portakal")

# meyve_listesi = meyve_listesi + ["Avokado", "Kiraz", "Portakal"]
# meyve_listesi += ["Avokado", "Kiraz", "Portakal"]
# print(meyve_listesi)

meyve_listesi.extend(["Ananas"])

# print(meyve_listesi)


m1 = meyve_listesi.copy() # meyve_listesi[:], meyve_listesi[::]

# m1.clear()
# print(m1.index("Muz"))
m1.insert(-1, "Ejder Meyvesi")

# print(m1)

m2 = m1.copy()
m2.pop(m2.index("Muz"))
m1.remove("Muz")

m1.reverse()

x = [1, False, 0, 234, .234, 3e5]
x1 = x.copy()
x1.sort(key=int, reverse=True)

# print(sorted((1,2,3,-3,-23), key=int))

notlar = [45, 73, 78, 90]

notlar.sort(reverse=True)

# print(notlar)

### SETS (KÜMELER) ###

kume = {1,1,2,3,4,5,6,6,7,7,7,8,9}

# kume.add(11)
# print(kume)

# kume.clear()
# kume.copy()
# kume.pop() ilk elemanı siler
# kume.remove(4) 4'ü siler

# kume.discard(3) # 3'ü siler

# kume.update((1,5,7,14,12))

ustkume = {"Fenerbahçe", "Galatasaray", "Beşiktaş"}

altkume = {"Fenerbahçe", "Galatasaray"}

# print(altkume.issubset(ustkume)) # True
# print(ustkume.issuperset(altkume)) # True

# issubset - alt küme kontrolü
# issuperset - üst küme kontrolü
# union - birleşim alma
# intersection - kesişim alma



# print(altkume.intersection(ustkume))

# symmetric_difference - örneklendirme 

a = {1,2,3,4}
b = {1,3,5,7,9}

sonuc = a.symmetric_difference(b)

# print(sonuc)

# dict 

bilgiler = {"adet": 1} # key: value / anahtar: değer

bilgiler["adet"] = 2

# print(bilgiler, bilgiler["adet"])

bilgiler = dict(adet=1, yas=20, ogrenci_mi=True)
# {'adet': 1, 'yas': 20, 'ogrenci_mi': True}

# dict sınıfı key ve value ile değer alır
# dict sınıfına işaret eder
# dict sınıfı iterable bir türdür fakat kendi özel fonksiyonlarıyla gezilebilir hale gelir

adet, yas, ogrenci_mi = bilgiler.items() 
# sozluk yapısını doner [(key, value), (key, value), (key, value)]

bilgiler.keys() # anahtarları döndürür [key, key, key]
bilgiler.values() # değerleri döndürür [value, value, value]

key, value = adet

# print("key='%s', value=%s" % (key, value))

c = {
    "path": "/",
    "sleep": 5,
    "config_file": "./config.json"
}

config = c.copy() # sözlüğü kopyalar

config.pop("sleep") # sleep keyine sahip değeri siler
config.popitem() # son ekleneni siler
config.clear()


c.get("sleep") # bulabilirse değeri döner, bulamazsa None 
c.get("path")

# dict.get default value
c.pop("sleep")
# print(c.get("sleep")) # None
# print(c.get("sleep", 5)) # 5

# c[key]
c.get(key) # daha güvenilir, hatanın önüne geçmek için

# c.update({"path2": "./worker/main.py"})
# print(c)

# c.setdefault("sleep", 5)

# print(c["sleep"] == c.get("sleep")) # c.get('sleep', 5)

# print(c.fromkeys(["data", "table", "dir"], None))
# istenen anhtar kelimeler ve varsayılan değerle yeni sözlük oluşturma

tumu = list(c.items())

# iterator ve generator

### iterator

liste = [1,2,3,4]

liste = iter(liste)

# print(liste.__next__())
# print(liste.__next__())
# print(liste.__next__())
# print(liste.__next__())

# print(next(liste)) # 1
# print(next(liste)) # 2
# print(next(liste)) # 3
# print(next(liste)) # 4

# generator

# yield keyword, yielding

def foo():
     yield 1

a = (foo())

i = iter(a)

# print(i, next(i))
