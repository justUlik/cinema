import requests
from bs4 import BeautifulSoup

class CinemaParser:
    def __init__(self, city):
        self.city = city
        self.content = ""

    def extract_raw_content(self, url):
        response = requests.get(url)
        try:
            self.content = response.content.decode("utf-8",errors='ignore')
        except:
            self.content = response.content.decode("cp1251",errors='ignore')
        return self.content

    def print_raw_content(self):
        soup = BeautifulSoup(''.join(self.content))
        print(soup.prettify())


cinema = CinemaParser("msk")
cinema.extract_raw_content("https://vk.com")
cinema.print_raw_content()
