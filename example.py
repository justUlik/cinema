from cinemaparse import CinemaParser

CINEMA = CinemaParser("msk")
CINEMA.extract_raw_content()
#CINEMA.print_raw_content()
print(CINEMA.get_film_list())
