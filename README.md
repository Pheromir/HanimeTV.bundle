# HanimeTV.bundle
A Plex Metadata Agent for Hanime.TV.
Please don't expect too much of this plugin, it might be full of bugs and throw some errors.

## Filenames
Currently the agent uses the name given by Plex to search for the metadata. As it tries to translate the given name to the slug used by hanimetv internally (lowercase and dashes), 
you should be able to use the official Hanime.TV title, but I recommend to use the slug (visible in the url of the video)


Example: `Uchi no Otouto Maji de Dekain Dakedo Mi ni Konai? 2` -> `uchi-no-otouto-maji-de-dekain-dakedo-mi-ni-konai-2`


Please just use the slug, I'm bad at matching stuff. Really.

## Installation
1. Download the latest code from this repository: "Code" -> "Download ZIP"
2. Unzip the downloaded file
3. Rename "HanimeTV.bundle-main" to "HanimeTV.bundle"
4. Drop the folder into your [Plug-ins](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/) directory

## Todo
- Filter/Ignore quality tags used by [rxqv's Hanime.TV downloader](https://github.com/rxqv/htv) (`[...]-v1x-1080`)