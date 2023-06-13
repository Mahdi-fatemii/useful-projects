from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link) #you'll have to give the link in windows 
#terminal with this command: 'python YoutubeDL.py "your youtube video"'

print("title of the video:", yt.title)
print("length of the video:", yt.length)
print("views of the video:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('\Users\MT1ShotYT\Desktop\VS\dl')
#and this is the download location you should 
#change this according to your address