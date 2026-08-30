# SoftHunt

Agregator darmowych gier i okazji — **zbiera oferty gratisów** z kilku źródeł
i pokazuje je w jednym miejscu. Napisane po to, żeby nie sprawdzać ręcznie
Steam, Epic, Itch i Reddita osobno.

## Źródła

| Źródło | Co zbiera |
|---|---|
| Steam | darmowe gry (`/search/?specials=1&maxprice=free`) |
| Epic Games | sekcja „Free Games” |
| itch.io | darmowe tytuły |
| gamerpower / gleam | givawaye |
| Reddit (`r/FreeGamesOnSteam`, `r/FreeEBOOKS`, `r/opensourcegames`, `r/software`, `r/opengaming`) | oferty z linkami, z filtrem plików wykonywalnych (.exe/.bat/...) |

Wyniki trafiają do bazy SQLite, z deduplikacją po URL.

## Struktura

```
app/
├─ main.py            # FastAPI (web UI)
├─ models.py          # model Offer (SQLAlchemy)
├─ crud.py            # operacje na bazie
├─ schemas.py         # pydantic
├─ scraper/           # scrapery źródeł
│  ├─ base.py         # fetch_html (User-Agent + Referer)
│  ├─ steam.py          ├─ reddit.py (PRAW)
│  ├─ epic.py           ├─ itch.py
│  ├─ gleam.py
│  └─ gamerpower.py
scripts/
├─ run_scrapers.py    # pobiera z: steam, reddit, itch → baza
├─ init_db.py         # tworzenie bazy
scraper_main.py       # CLI do scraperów
templates/ · static/  # frontend
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env   # wpisz własne REDDIT_CLIENT_ID/SECRET
python scripts/init_db.py
python scripts/run_scrapers.py     # zbierz oferty
uvicorn app.main:app --reload      # web UI na :8000
```

## Uwagi bezpieczeństwa

- Klucze Reddit tylko w `.env` (nie w repo). Bez nich scrapery webowe nadal działają;
  Reddit (PRAW) wymaga własnych danych API.
- Filtr odrzuca linki do plików wykonywalnych (anty-malware sanity-check).

## Licencja

MIT — patrz `LICENSE`.