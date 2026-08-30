from app.scraper.base import fetch_html
from bs4 import BeautifulSoup

def get_itch_freebies():
    html = fetch_html("https://itch.io/games/on-sale/free")
    soup = BeautifulSoup(html, "html.parser")
    offers = []
    for game in soup.select(".game_cell"):
        title = game.select_one(".game_title").text.strip()
        link = game.select_one("a.title_link").get("href")
        if not link.startswith("http"):
            link = "https://itch.io" + link
        offers.append({"source": "itch.io", "title": title, "url": link})
    return offers
