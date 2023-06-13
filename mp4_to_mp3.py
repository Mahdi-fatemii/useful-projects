from moviepy.editor import *

video_file = "ukelele.mp4" #here goes youur mp4 file name
audio_file = "your_mp3_audio.mp3" #this is the name of the mp3 file you will create

video = VideoFileClip(video_file)
your_audio = video.audio
print("please wait!")
your_audio.write_audiofile(audio_file)

video.close()
your_audio.close()
print("done")