# Get all url from a YouTube playlist
# Version: 1.0

# 1. Import the necessary libraries
from pytube import Playlist

# 2. Get the playlist url from the user
playlist_user = input("Enter the playlist url (YouTube): ")

# 3. Create a Playlist object
playlist = Playlist(playlist_user)

# 4. Get the number of videos in the playlist
playlist_len = len(playlist.video_urls)

# 5. Print the number of videos in the playlist
print(f"Number of videos in the playlist: {playlist_len}")
for i, url in enumerate(playlist.video_urls):
    print(f"{i + 1}. {url}")

# 6. Save the urls in a file
output_file = "playlist_urls.txt"
with open(output_file, "w") as file:
    for url in playlist.video_urls:
        file.write(url + "\n")

print(f"Urls saved in {output_file}")
