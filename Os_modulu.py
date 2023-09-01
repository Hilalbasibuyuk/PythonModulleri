
"""
import os

result=dir(os)

result = os.name #işletim sistemi hakkında bilgi verir.(nt, windows işletim sistemi demektir.)
result = os.getcwd() #şu anda olduğumuz dizini bize verir.
print(result)

os.mkdir("new_folder") #olduğumuz dizinde "new_folder" isimli dosya oluşturur.
os.makedirs("new_folder/second_folder") #iç içe klasörler oluşturur.

os.chdir("C:\\") #belirttiğimiz dosya konumuna geçiş yaparız.
os.chdir("..") #bir üst dizine geçeriz.
os.chdir("../..") #iki üst dizine geçeriz.


os.system("mavproxy") #bilgisayarımızda ismini girdiğimiz dosyayı çalıştırır. 

os.rename("newdirectory","yeniklasor") #newdirectory isimli klasörün ismini yeniklasor ismi ile yeniden adlandırır.

os.rmdir("newdirectory") #ismini girdiğimiz dosyayı siler.
result = os.listdir() #dizin içerisindeki dosyaları listeler. İçine başka biz dizin belirtirsek onun içindekileri listeler.



for file in os.listdir():
    if file.endswith('.py'):
        print(file)# sonu .py ile biten dosyaları gösterir



#path
result =os.path.dirname(os.path.abspath("Os_modulu.py")) #girdiğimiz dosyanın tam yolunun dizin ismini (konumunu) verir
result =os.path.exists("Moduller") #girdiğimiz dosya var mı varsa True yoksa False döndürür
result =os.path.join("C:\\","deneme","deneme1") #bunları dizin haline getirir.
result =os.path.split("C:\\deneme") #dizinleri birbirinden ayırır.
result =os.path.splitext("_os.py") #dosya uzantısını ve dosya ismini birbirinden ayırır
print(result)

"""

