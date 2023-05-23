import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
import argparse

# Spotify app credentials
SPOTIPY_CLIENT_ID = 'app_client_id'
SPOTIPY_CLIENT_SECRET = 'app_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'

# User ID
USER_ID = 'janzaba'

# CSV file name
CSV_FILE_NAME = 'songs.csv'

# Create argument parser
parser = argparse.ArgumentParser(description='Create a Spotify playlist from a CSV file.')
parser.add_argument('--name', required=True, help='The name of the playlist to create.')

# Parse arguments
args = parser.parse_args()

# Playlist name
PLAYLIST_NAME = args.name

# Create Spotify object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-public'))

# Create playlist
playlist = sp.user_playlist_create(USER_ID, PLAYLIST_NAME)

# Read CSV file
with open(CSV_FILE_NAME, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        artist_name = row[0]
        song_title = row[1]

        # Search for song
        results = sp.search(q=f'artist:{artist_name} track:{song_title}', type='track')

        # Check if song was found
        if results['tracks']['items']:
            # Get song ID
            song_id = results['tracks']['items'][0]['id']

            # Add song to playlist
            sp.playlist_add_items(playlist['id'], [song_id])

print(f'Playlist {PLAYLIST_NAME} created successfully.')
