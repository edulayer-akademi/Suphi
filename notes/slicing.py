# slicing

slice



# indexing - indeksleme

isim = "Mert" # 0, 3

# print(isim[4]) # hata: IndexError

# negative indexing
# print(isim[-4])


# string slicing 

# start : stop : step

metin = "Afyonkarahisar"

# print(metin[:len(metin):1])
# print(metin[:len(metin)])
# print(metin[0:])

# start kolonundan önce değer yazılmasa da sıfır kabul edilir
# stop kolonundan önce değer yazılmasa da bir kabul edilir

# print(metin[0:4] == "") # slice

# m1 = (metin[0: 14: 4])
# m2 = (metin[slice(5, 14)])

# print(m1)
# print(m2)

# print(m1 == m2)


print(metin[::2])


metin[0:len(metin)] # Afyonkarahisa

# [0, 14) # 13 

metin[0:-1]

# son karakter 13. index iken 14. karakterdir
# len(metin) = 14
# 0: 14: 1 = metin
# 0: 13 : 1 != metin

