from youtube_dl import YoutubeDL


# Sample 1: Download a single youtube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4']) # Remember to put your video in a list, eventhough one video is downloaded



# # Sample 2: Download multiple youtube videos
# dl = YoutubeDL()
# # # Put list of song urls in download function to download them, one by one
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=RBumgq5yVrA','https://www.youtube.com/watch?v=RywCvt5JHyw'])



# # Sample 3: Download audio
# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])



# # Sample 4: Search and then download the first video
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['havana'])

# de dang co format thi khi tai video ve khong co hinh con k de thi lai co vi format kia la dang audio

# # Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio' # vi chi la dang audio nen k co hinh
}
dl = YoutubeDL(options)
dl.download(['đáp án'])