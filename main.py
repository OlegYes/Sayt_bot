import requests
import bs4
from bs4 import BeautifulSoup as BS

#def print_hi(name):


if __name__ == '__main__':
    URL = "https://spaces.im/"
    r = requests.get(URL)
#    html = BS(r.content, 'html.parser')
    soup = BS(r.content, "lxml")
    menu = soup.find("div", class_="wrapper").find("a", class_="link darkblue").find_all("span", class_="m")
    print(menu)
    with open('temp.html', 'w') as f:
        text = f.write(menu)
        

