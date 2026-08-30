import requests
from bs4 import BeautifulSoup

def get_gleam_giveaways():
    url = "https://giveawaylisting.com/category/gleam-giveaways/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    offers = []
    for post in soup.select(".post-title a"):
        title = post.text.strip()
        link = post.get("href")
        offers.append({"source": "Gleam.io", "title": title, "url": link})
    return offers
