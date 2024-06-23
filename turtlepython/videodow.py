from pytube import YouTube
link=YouTube("https://youtu.be/lFml8NrHoeo")
video=link.streams.get_highest_resolution()
video.download("Desktop")