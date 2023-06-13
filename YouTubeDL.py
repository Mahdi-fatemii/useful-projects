from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("title of the video:", yt.title)
print("length of the video:", yt.length)
print("views of the video:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('\Users\MT1ShotYT\Desktop\VS\dl')
