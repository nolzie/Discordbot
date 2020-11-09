from bs4 import  BeautifulSoup
import urllib3


def usrRating(id):
    quote_page = "https://lichess.org/@/"+id
    http = urllib3.PoolManager()
    response = http.request('GET', quote_page)
    soup = BeautifulSoup(response.data, "html.parser")
    rating_box = soup.find("a", {"data-icon":")"})
    ratingshtml = rating_box.text.strip()
    rating = ratingshtml[5:9]
    print(rating)


usrRating('Nolzie123')

