import re

class Video:
    def __init__(self, jo): 
        self.title = jo["hentai_video"]["name"]
        self.slug = jo["hentai_video"]["slug"]
        self.brand = jo["hentai_video"]["brand"]
        self.tags = list(map(lambda i: i["text"], jo["hentai_video"]["hentai_tags"]))
        self.thumb = jo["hentai_video"]["poster_url"]
        self.cover = jo["hentai_video"]["cover_url"]
        self.description = re.compile(r'<[^>]+>').sub("", jo["hentai_video"]["description"])
        self.franchise_name = jo["hentai_franchise"]["title"]
        self.release_unix = jo["hentai_video"]["released_at_unix"]
    
    def __str__(self):
        return "<Video " + self.slug + ">"


def get(slug):
    jo = JSON.ObjectFromURL("https://hanime.tv/api/v8/video?id=" + slug,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
        }
    )
    return Video(jo)
