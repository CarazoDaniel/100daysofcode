from bs4 import BeautifulSoup
# import lxml 
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,'html.parser')
articles = soup.find_all(class_="titleline")
article_titles = []
article_links = []

for title in articles:
    title = title.find(name='a')
    name = title.getText()
    link = title.get('href')
    article_titles.append(name)
    article_links.append(link)
    
article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_="score")]

top_score = article_scores.index(max(article_scores))
print(article_titles[top_score])
print(article_links[top_score])
print(article_scores[top_score])




#with open("bs-start/website.html") as file:
    #contents = file.read()

#soup = BeautifulSoup(contents, 'html.parser')
#print(soup.title)
#print(soup.title.name)
#print(soup.prettify())


#all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#   print(tag.getText())
#   print(tag.get('href'))

#heading = soup.find(name="h1", id="name")

#section_heading = soup.find(name="h3", class_="heading")

#company_url = soup.select_one(selector="p a")

#name = soup.select_one("#name")

#headings = soup.select(".heading")