import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    # 'outtmpl': r'D:\newfolder',
    'postprocessors': [
        {
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
        },
    ],
}

files = [2, 3, 4]

for x in files:
    f = open('final_links/final_links'+str(x)+'.txt')
    links = f.readlines()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for x in links:
            try:
                ydl.download([x])
            except:
                continue




