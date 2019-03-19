#SEARCH and DOWNLOAD audio
from youtube_dl import YoutubeDL

option = {
    'default_search':'ytsearch',
    'download':1,
    'format':'bestaudio/audio'
}
dl = YoutubeDL(option)
dl.download(['Một đêm say'])