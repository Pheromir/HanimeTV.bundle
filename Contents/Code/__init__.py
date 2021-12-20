import re  # import time def Log(dbgline): Log("\n\n\n----------\n\n" + time.strftime("%H:%M:%S - ") + dbgline + "\n\n---------\n\n\n")
import sys

import htv_api as hanimetv
from datetime import datetime


def Start():
    HTTP.CacheTime = CACHE_1DAY
    HTTP.Headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)'


class HanimeTV(Agent.Movies):
    name, primary_provider, fallback_agent, contributes_to, languages, accepts_from = (
        'HanimeTV', True, False, None, [Locale.Language.English], ['com.plexapp.agents.localmedia'])

    def search(self, results, media, lang, manual=False):
        Log("".ljust(157, '-'))
        slug = media.name.replace(" ", "-").lower()
        Log("Fetching infos for " + slug)
        try:
            vid = hanimetv.get(slug)
        except KeyError:
            Log("Error getting HTV metadata for " + slug)
            return

        if vid is not None:
            results.Append(MetadataSearchResult(
                id=slug,
                name=vid.title,
                year=datetime.utcfromtimestamp(vid.release_unix),
                lang='en',
                score=100
            ))

    def update(self, metadata, media, lang):
        Log("".ljust(157, '='))
        Log("update() - metadata.id: '%s', metadata.title: '%s'" % (metadata.id, metadata.title))
        vid = hanimetv.get(metadata.id)
        metadata.title = vid.title
        metadata.summary = vid.description
        metadata.studio = vid.brand
        metadata.genres = vid.tags
        metadata.original_title = vid.slug
        metadata.collections.clear()
        metadata.collections.add(vid.franchise_name)
        poster = HTTP.Request(vid.cover, timeout=120, sleep=2.0).content
        metadata.posters[vid.cover] = Proxy.Media(poster)
        art = HTTP.Request(vid.thumb, timeout=120, sleep=2.0).content
        metadata.art[vid.thumb] = Proxy.Media(art)
        metadata.originally_available_at = datetime.utcfromtimestamp(vid.release_unix)
        Log('update() ended')
