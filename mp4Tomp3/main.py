from moviepy.editor import VideoFileClip

video_route_entrance = 'Ruta del video mp4'
video_route_exit = 'Ruta del audio mp3'

video_clip = VideoFileClip(video_route_entrance)
audio_clip = video_clip.audio
audio_clip.write_audiofile(video_route_exit)

audio_clip.close()
video_clip.close()