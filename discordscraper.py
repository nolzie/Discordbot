from bs4 import  BeautifulSoup
import urllib3

quote_page = "https://lichess.org/@/nolzie123"
http = urllib3.PoolManager()

response = http.request('GET', quote_page)
soup = BeautifulSoup(response.data)

rating_box = soup.find("div", attrs={"class": "side sub-ratings"})
ratings = rating_box.text.strip()

print(ratings)