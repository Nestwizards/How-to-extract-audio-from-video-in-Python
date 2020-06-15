

from moviepy import editor
# Replace the parameter with the file location of the video
video = editor.VideoFileClip("sample.mkv")

audio = video.audio

# Replace the parameter with the file location
audio.write_audiofile("sample.mp3")