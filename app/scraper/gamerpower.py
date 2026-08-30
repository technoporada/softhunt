import requests

def scrape():
    url = "https://www.gamerpower.com/api/giveaways"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        results = []
        for item in data:
            results.append({
                "title": item.get("title"),
                "url": item.get("open_giveaway_url"),
                "source": "GamerPower",
                "description": item.get("description"),
                "tags": item.get("platforms"),
                "expires": item.get("end_date"),
                "requires_login": False,
                "has_captcha": False,
                "has_adfly": False,
                "notes": ""
            })
        return results
    except Exception as e:
        print("❌ GamerPower error:", e)
        return []
