# SEARCH and DOWNLOAD the first video from Youtube
from youtube_dl import YoutubeDL

option = {
    'default_search':'ytsearch',# SEARCHING before download
    'download':1
}
dl = YoutubeDL(option)
dl.download(['Một đêm say'])
