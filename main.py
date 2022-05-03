from email import header
from encodings import utf_8
from wsgiref import headers
import requests
import bs4
from bs4 import BeautifulSoup as BS

def get_menu():
    URL = "https://spaces.im/"
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }

    req = requests.get(URL, headers=headers)
    src = req.text
    with open('index.html', 'w') as f:
         f.write(src)
    # тут я не доробив
    
    soup = BS(r.content, "lxml")
    
    with open('temp.html', 'wb') as f:
         f.write(soup.encode('utf-8'))
#отримуємо ссилки меню
    menu = soup.find("div", class_="wrapper").find_all("a", class_="link darkblue")
    for i in menu:
        print(i.text)
        lincs = i.get("href")
        print(lincs)
    return 0    


if __name__ == '__main__':
    get_menu()