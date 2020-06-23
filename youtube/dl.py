"""

author: @endormi

Automated YouTube audio downloader

"""


import youtube_dl


url = input("Please enter the URL for the video you wish to download: ")
ytdl = youtube_dl.YoutubeDL().extract_info(url=url, download=False)

file = f"{ytdl['title']}.mp3"

options = {
    'format': 'bestaudio/best',
    'outtmpl': file,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([ytdl['webpage_url']])
