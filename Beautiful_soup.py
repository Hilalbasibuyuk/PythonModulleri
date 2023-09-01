html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk Web Sayfam</title>
</head>
<body>
    <h1>Python Kursu</h1>
    <div class = "grup 1">

            <h2>kelebek</h2>
        
        <ul>    
            <li>C#</li>
            <li>Python</li>
            <li>Java</li>
        </ul>
  
         </div>
    <div class = "grup 2">

<h2>kanat</h2>
        
        <ul>    
            <li>C++</li>
            <li>css</li>
            <li>Javascript</li>
        </ul>
        <img src="kelebek.jpg" alt="">

    </div>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify() # prettify html_doc dosyasındaki bozduğumuz html kodlarını düzenleme işlemini yapar
result = soup.title # html_doc'teki kodun başlığını gösterir
result = soup.head # html_doc'teki kodun head kısmını gösterir
result = soup.body # html_doc'teki kodun body kısmını gösterir
result = soup.body.name # çıktı body olur. 
result = soup.body.string # çıktı body'nin içinde yazan şeyler olur
result = soup.title.name # çıktı title olur.
result = soup.find_all("h2") # Birden fazla h2 varsa hepsini gösterir h2'lerin
result = soup.div.findChildren() # Div etiketi altındakileri gösterir. Burada div parents altındaki etiketler children olur mantığı vardır.
result = soup.div.findNextSibling() # Bir sonraki divi gösterir. Diğer div bunun için siblings gibi olur aynı hizada(grupta) oldukları için
result = soup.div.findNextSibling().findNextSiblings() # Bir sonraki divden sonraki divi gösterir
result = soup.div.findNextSibling().findPreviousSibling() # önce bir sonraki div sonra bir önceki div yani başlangıca gider.

print(result)