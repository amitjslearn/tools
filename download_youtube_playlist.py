from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=wg4dUKMjR1w&list=PLd1t7W2ShsB-EIJVyhaeRdgkO7Ax5Wr_8')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
count = 1
for video in playlist.videos:
    video.streams.get_highest_resolution().download()
    print('done',count)
    count +=1
