"""
importing requests for getting html-code and bs4 for printing this code in the
console pretty
"""
import requests
from bs4 import BeautifulSoup

class CinemaParser:
    """
    class for parsing cinema
    """
    def __init__(self, city):
        """
        initisalisation
        """
        self.city = city
        self.content = ""

    def extract_raw_content(self):
        """
        function for getting html code
        """
        if self.city == "msk":
            response = requests.get("https://msk.subscity.ru")
        elif self.city == "spb":
            response = requests.get("http://spb.subscity.ru")
        self.content = response.content.decode("utf-8", errors='ignore')
        return self.content

    def print_raw_content(self):
        """
        function for printing html code
        """
        soup = BeautifulSoup(''.join(self.content))
        print(soup.prettify())

    def get_film_list(self):
        """
        function for getting film list
        """
        film_list = []
        soup = BeautifulSoup(self.content, 'lxml')
        spans = soup.select('.movie-plates')
        for _ in spans:
            now = soup.select('.movie-plate')
            for nows in now:
                film_list.append(nows.get('attr-title'))

CINEMA = CinemaParser("msk")
CINEMA.extract_raw_content()
#CINEMA.print_raw_content()
print(CINEMA.get_film_list())
