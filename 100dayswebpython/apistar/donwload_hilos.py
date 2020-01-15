import requests
import bs4

import threading

def get_title(html, episode_number):
    print(f"Obteniendo titulo para el episodio {episode_number}")
    soup = bs4.BeautifulSoup(html, "html.parser")
    header = soup.select_one("h1")
    if not header:
        print("NO ENCONTRADO")
    
    print(header.text.strip())

def get_html(episode_number):
    url = f"https://talkpython.fm/{episode_number}"
    resp =requests.get(url)
    resp.raise_for_status()

    get_title(resp.text, episode_number)



threads = []

for i in range(150,155):
    threads.append(threading.Thread(target=get_html, args=([i]), daemon=True))

[t.start() for t in threads]

[t.join() for t in threads]



