import requests


API_URL = "http://localhost:80"


def get_articles(title=None, tags=None, user=None, date=None):
    params = {}
    if title:
        params["title"] = title
    if tags:
        params["tags"] = ", ".join(tags)
    if user:
        params["user"] = user
    if date:
        params["date"] = date.isoformat()

    try:
        r = requests.get(f"{API_URL}/articles/", params=params, timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return []


def create_article(title, content, tags, user):
    try:
        r = requests.post(f"{API_URL}/articles/", json={
            "title": title,
            "content": content,
            "tags": [{"name": t} for t in tags],
            "user_id": user
        })
        r.raise_for_status()
        return r.ok
    except requests.exceptions.RequestException as e:
        return False


def delete_article(article_id: int):
    try:
        r = requests.delete(f"{API_URL}/articles/{article_id}")
        r.raise_for_status()
        return r.ok
    except requests.exceptions.RequestException as e:
        return False