import praw
import os
from prawcore.exceptions import NotFound, Redirect, Forbidden

LAST_FULLNAME_FILE = "last_reddit_post.txt"

def read_last_fullname():
    if os.path.exists(LAST_FULLNAME_FILE):
        with open(LAST_FULLNAME_FILE, "r") as f:
            return f.read().strip()
    return None

def save_last_fullname(fullname):
    with open(LAST_FULLNAME_FILE, "w") as f:
        f.write(fullname)

def get_reddit_freebies():
    reddit = praw.Reddit(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent="script:h5n1:0.1 by /u/Alarming_Appeal_3211"
    )

    # Subreddity na których szukamy ofert
    # Z ogólnych giveaway (np. GameDeals, FreeGameFindings) tymczasowo wyłączone,
    # bo często wymagają logowania, captcha albo są mniej „czyste”.
    subreddits = [
        # "FreeGameFindings",
        "opensourcegames",
        # "GameDeals",
        "FreeGamesOnSteam",
        "FreeEBOOKS",
        "software",
        "opengaming",
    ]

    # Lista rozszerzeń plików do odrzucenia — tzw. „śmieci” do filtrowania
    bad_file_exts = ('.exe', '.bat', '.cmd', '.scr', '.dll', '.msi', '.com')

    offers = []
    newest_fullname = None
    last_fullname = read_last_fullname()

    for subreddit_name in subreddits:
        try:
            subreddit = reddit.subreddit(subreddit_name)

            params = {}
            if last_fullname:
                params['after'] = last_fullname

            posts = subreddit.new(limit=30, params=params)
            for post in posts:
                url = post.url.lower()

                # Filtrowanie ofert z linkami do niechcianych plików wykonywalnych
                if url.endswith(bad_file_exts):
                    # Pomijamy śmieciowe pliki
                    continue

                offers.append({
                    "title": post.title,
                    "url": post.url,
                    "source": f"reddit/{subreddit_name}",
                    "fullname": post.name
                })
                newest_fullname = post.name

        except (NotFound, Redirect, Forbidden) as e:
            print(f"Pominięto subreddit '{subreddit_name}' z powodu błędu: {e}")

    if newest_fullname and newest_fullname != last_fullname:
        save_last_fullname(newest_fullname)

    return offers

