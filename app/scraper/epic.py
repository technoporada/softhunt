from app.scraper.base import fetch_html
from bs4 import BeautifulSoup

def get_epic_freebies():
    url = "https://store.epicgames.com/en-US/free-games"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    offers = []
    for section in soup.select("section[data-component='FreeGamesCollection'] a"):
        title = section.select_one("span[data-component='OfferTitleInfo']")
        if not title:
            continue
        title_text = title.get_text(strip=True)
        link = "https://store.epicgames.com" + section.get("href")
        offers.append({"source": "Epic Games", "title": title_text, "url": link})
    return offers
