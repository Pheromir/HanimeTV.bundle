# HanimeTV.bundle
A Plex Metadata Agent for Hanime.TV.
Please don't expect too much of this plugin, it might be full of bugs and throw some errors.

## Filenames
The agent uses the direct filename (hentai-name.mp4) instead of the name provided by plex.
As the agent replaces spaces by dashes, you can use them, but I still recommend keeping it simple by using the hanime.tv id directly.
You can find the id in the URL of the video on hanime.tv.

URL Example: `https://hanime.tv/videos/hentai/shuumatsu-no-harem-6` -> `shuumatsu-no-harem-6`
File Example: `Shuumatsu no Harem 6` -> `shuumatsu-no-harem-6`

There isn't any magic title matching, so just use the htv id.

## Installation
1. Download the latest code from this repository: "Code" -> "Download ZIP"
2. Unzip the downloaded file
3. Rename "HanimeTV.bundle-main" to "HanimeTV.bundle"
4. Drop the folder into your [Plug-ins](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/) directory

## Todo
- Filter/Ignore quality tags used by [rxqv's Hanime.TV downloader](https://github.com/rxqv/htv) (`[...]-v1x-1080`)
