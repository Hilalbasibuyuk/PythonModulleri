

"""
import re

result=dir(re)

#re modülü
str = "Python öğrenmek isteyenler Python kursumuza bakabilir |40 saat"
result = re.findall("Python",str) #str'de Python kelimelerini bulur. Büyük küçük harfe duyarlı. Liste halinde verir.
result = len(result) #kaç kere tekrar ettiğinin sayısı

result = re.split(" ",str) #boşluklardan ayırır
result = re.split("\s",str) #bu da aynıdır boşluklardan ayırır

result = re.sub(" ","-", str) #boşluklar yerine tire(-) işareti koyar.
result = re.search("Python",str) #kelimenin yerini söyler, mesela(0,6) aralığı
result = result.span() #direkt aralığı söyler.
result = result.group() #aradığımız kelimeyi yazar.
result = result.string #yazdığımız stringi karşımıza getirir.
print(result)




#regular expression

str = "Python öğrenmek isteyenler Python kursumuza bakabilir |40 saat"

result = re.findall("[abc]",str) #abc harflerini tek tek arar.
result = re.findall("[^abc]",str) #abs harfleri dışındaki her şeyi tek tek arar.
result = re.findall("[012]",str) #012 sayılarını arar. Mesela str'de 0 vardır, onu bulur ve yazdırır.
result = re.findall("[1-9]",str) #1'den 9'a kadar olan rakamları arar(str içerisinde)
result = re.findall("[^1-9]",str) #1'den 9'a kadar olan rakamlar dışındakileri arar.
result = re.findall("[a-z]",str) #a'dan z'ye kadar olan harfleri arar

result = re.findall("...",str) #üçerli üçerli kelimeleri listeler. Nokta sayısını değiştirebiliriz veya
#başka bir kelimenin ortasına vs de nokta koyarak o kelimeyi aratabiliriz.

result = re.findall("^P",str) #str P ile mi başlıyor
result = re.findall("t$",str) #str t ile mi bitiyor

print(result)

"""
