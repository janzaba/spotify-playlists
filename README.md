# Spotify Playlist Creator

This Python script creates a Spotify playlist from a CSV file using the Spotify Web API.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Spotify account.
* You have registered an application on the Spotify Developer Dashboard and have your Client ID, Client Secret, and Redirect URI.
* You have installed Python 3 and pip.

## Installing Spotify Playlist Creator

To install Spotify Playlist Creator, follow these steps:

1. Install the `spotipy` library by running the following command in your terminal:

```bash
pip install spotipy
```

2. Clone this repository or download the script to your local machine.

## Using Spotify Playlist Creator

To use Spotify Playlist Creator, follow these steps:

1. Copy `config.py.dist` into `config.py`
2. Open `config.py`
3. Replace `'your-spotify-client-id'`, `'your-spotify-client-secret'`, `'your-spotify-redirect-uri'`, and `'your-spotify-user-id'` with your actual Spotify Client ID, Client Secret, Redirect URI, and User ID.
4. Save and close the script.
5. Insert songs in `songs.csv` file (preferably use ChatGPT for recomendations)
5. Run the script in your terminal with the `--name` argument to specify the playlist name, like this:

```bash
python3 playlistFromCsv.py --name PLAYLIST_NAME
```

Replace `PLAYLIST_NAME` with the actual name you want for the playlist.

6. You'll be redirected to the Spotify website to log in and authorize the application. After authorizing the application, you'll be redirected to your Redirect URI. Copy the URL from your browser's address bar and paste it into your terminal.

7. The script will create a new playlist with the specified name and add the songs from the CSV file to the playlist.

## Authors

* ChatGPT-4
* Jan Żaba

## Contact

If you want to contact me, you can reach me at `janekzaba@gmail.com`.
