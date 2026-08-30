from app.scraper import steam, reddit, itch
from app.database import SessionLocal
from app import crud, schemas

def main():
    db = SessionLocal()
    scrapers = [
        steam.get_steam_freebies,
        reddit.get_reddit_freebies,
        itch.get_itch_freebies,
    ]

    for scraper_func in scrapers:
        try:
            offers = scraper_func()
        except Exception as e:
            print(f"Błąd podczas uruchamiania {scraper_func.__name__}: {e}")
            continue

        for offer in offers:
            title = offer.get("title")
            url = offer.get("url") or offer.get("link")
            source = offer.get("source", "unknown")

            if not title or not url:
                print(f"Pominięto ofertę z powodu brakujących danych: {offer}")
                continue

            existing = crud.get_offer_by_url(db, url)
            if existing:
                print(f"Oferta już istnieje w bazie: {title}")
                continue

            schema = schemas.OfferCreate(
                title=title,
                url=url,
                source=source,
                description=offer.get("description", ""),
                expires=offer.get("expires"),
                tags=offer.get("tags"),
                requires_login=offer.get("requires_login", False),
                has_captcha=offer.get("has_captcha", False),
                has_adfly=offer.get("has_adfly", False),
                notes=offer.get("notes", ""),
            )

            crud.create_offer(db, schema)
            print(f"✔ Zapisano: {title}")

if __name__ == "__main__":
    main()
