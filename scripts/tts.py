#!/usr/bin/env python3
"""SoftHunt - Text-to-Speech module (darmowy, offline, zero kosztów API)

Używa pyttsx3 – nie potrzebuje kluczy API, nie płacisz za każde słowo,
działa lokalnie na espeak. Idealne do pokazać: "buduję z AI, ale bez funduszy".
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal
from app import crud, models
import pyttsx3


def speak_games(limit: int = 5, voice_index: int = None):
    """Odtwarza kolejno tytuły gier z bazy danych."""
    db = SessionLocal()
    try:
        games = db.query(models.Offer).limit(limit).all()
        if not games:
            print("Brak gier w bazie – najpierw uruchom: python scripts/run_scrapers.py")
            return

        engine = pyttsx3.init()
        # Opcjonalnie ustaw głos (indeks z listy dostępnych głosów)
        if voice_index is not None:
            voices = engine.getProperty('voices')
            if voice_index < len(voices):
                engine.setProperty('voice', voices[voice_index].id)

        engine.setProperty('rate', 150)    # szybsze/słabsze czytanie
        engine.setProperty('volume', 0.9)  # głośność 0-1

        for i, game in enumerate(games, 1):
            title = game.title or "Bez tytułu"
            print(f"[{i}] {title}")
            engine.say(f"Oferta numer {i}: {title}")

        engine.runAndWait()
        print("✅ TTS zakończone – gry odczytane głośno (lub do głowy).")
    finally:
        db.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Odtwarzaj tytuły gier z SoftHunt")
    parser.add_argument("limit", nargs="?", type=int, default=5, help="Ile gier odczytać")
    parser.add_argument("voice_index", nargs="?", type=int, default=None, help="Indeks głosu z systemu")
    args = parser.parse_args()
    speak_games(limit=args.limit, voice_index=args.voice_index)