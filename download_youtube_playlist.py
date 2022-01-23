from pytube import Playlist

done = [
    'https://www.youtube.com/watch?v=wg4dUKMjR1w&list=PLd1t7W2ShsB-EIJVyhaeRdgkO7Ax5Wr_8'
]
now = 'https://www.youtube.com/playlist?list=PLd1t7W2ShsB8A7PNrvvfaLhVJP-rdG_-l'

playlist = Playlist(now)
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
count = 1
for video in playlist.videos:
    streams = video.streams.filter(only_audio=True).first().download(output_path="/home/amit/Desktop/sounds-of-isha/damaru") # .get_highest_resolution().download()
    print(streams)
    print('done',count)
    count +=1
