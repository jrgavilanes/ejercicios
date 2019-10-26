from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple("Episode", "title link pubDate show_id")
episode_data = {}


def download_info():
    url = "https://talkpython.fm/episodes/rss"
    response = requests.get(url)
    dom = ElementTree.fromstring(response.text)

    items = dom.findall("channel/item")
    count_episode = len(items)
    for idx, item in enumerate(items):
        episode = Episode(
            item.find("title").text,
            item.find("link").text,
            item.find("pubDate").text,
            count_episode - idx,
        )
        episode_data[episode.show_id] = episode


def get_episodio(item_id: int) -> Episode:
    return episode_data.get(item_id)
