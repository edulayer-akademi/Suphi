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