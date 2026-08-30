from app.scraper.base import fetch_html
from bs4 import BeautifulSoup

def get_steam_freebies():
    url = "https://store.steampowered.com/search/?specials=1&maxprice=free"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    offers = []
    for item in soup.select(".search_result_row"):
        title_el = item.select_one(".title")
        if not title_el:
            continue
        title = title_el.text.strip()
        url = item.get("href")
        offers.append({"source": "Steam", "title": title, "url": url})
    return offers
