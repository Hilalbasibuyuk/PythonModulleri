# file = open("YıldızlarlaResimler.py", "r",encoding= "utf-8")
# for i in file:
#     print(i,end="")

# content1=file.read()
# print(content1)
# file = open("YıldızlarlaResimler.py", "r",encoding= "utf-8")
# print(file.readline(),end=)
# print(file.readline())


# file.close()

# with open("YıldızlarlaResimler.py","r",encoding="utf-8") as file:
#     content=file.read(16)
#     print(content)
#     print(file.seek(8))
#     print(file.tell())

with open("YıldızlarlaResimler.py" , "r+",encoding='utf-8') as file:
    list=file.readlines()
    list.insert(1,"Hilal")
