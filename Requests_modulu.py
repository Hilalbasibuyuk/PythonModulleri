import requests
import json
import pprint

result = requests.get("https://jsonplaceholder.typicode.com/todos") # verilerini almak istediğimiz internet sitesinin adresini kopyalıyoruz
result = result.text #verileri yazdırıyoruz çıktıya
result =json.loads(result) # string'ten dict'e çevirdik

print(result) # bilgiler string şeklinde gelir

for i in result: # böylece bilgiler satır satır gelmiş olur
    print(i)
    print(i["title"]) # başlıkların çıktısını alırız
# for döngüsü yerine pprint'i kullanarak da düzgün bir şekilde yazılmasını sağlayabiliriz.
pprint.pprint(result) #pprint kullanımı bu şekildedir ve for'daki gibi düzenli yazmayı sağlar



