from bs4 import BeautifulSoup
# import lxml 
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_article_site = response.text
soup = BeautifulSoup(movies_article_site,'html.parser')
list_of_movies = [title.getText() for title in soup.find_all(name = "h3" , class_="title")]
list_of_movies = [title.replace("â\x80\x93",'-') for title in list_of_movies]
list_of_movies = list_of_movies[::-1]
with open('movies.txt', mode = 'w') as file:
    for movie in list_of_movies:
        file.write(f'{movie}\n')