from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    # 'format': 'bestaudio/audio' # co cai nay thi video lai k co hinh vi chi la dang audio
}
dl = YoutubeDL(options)
dl.download(['Thunder Imagin Dragons'])