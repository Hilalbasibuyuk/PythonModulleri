"""
import json # cihazlar arasında ortak bir veri taşıma objesidir.
person_dict = {
    "name": "Hilal",
    "language": "java"
}
person_string = '{"name":"Ali", "languages": ["C#", "C++","Python"]}'

#stringe çevirme ve alt alta yazdırma yöntemi
person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent = 2, sort_keys= True)#sortkeys sıralama için,indent boşluk için
print(person_dict)
print(result)



#dict yapısı ile benzerdir. Dict yapısını hatırlayalım 
person_string = '{"name": "Ali", "languages": ["C#", "C++"," Python"]}'

result = person ["name"]
result = person ["languages"][0]

#json yapısı
#person = '{"name": "Ali", "languages": ["C#", "C++"," Python"]}'#yukarıdaki dict'i tırnak işaretine alınca json şeklinde yazılmış olur.


# Json'dan dict'e çevirme
result = json.loads(person_string) #dict formatı haline geldi.
result = result["name"] #name diyince Ali bilgisini verebiliyor artık
print(result)


# json formatındaki dosyayı okuruz 
with open("person.json") as f:
    data = json.load(f)
    print(data["name"])


#dict'ten json'a çevirme
person_dict = {
    "name": "Hilal",
    "language": "java"
}
result = json.dumps(person_dict)
print(result)

with open("person.json","w") as file:
    json.dump(person_dict, file)

"""

