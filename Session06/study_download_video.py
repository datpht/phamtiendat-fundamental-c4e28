# DOWNLOAD video from Youtube 
from youtube_dl import YoutubeDL
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# DOWNLOAD multiple video from Youtube
from youtube_dl import YoutubeDL
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4','https://www.youtube.com/watch?v=8Qr9WW2bLAQ'])