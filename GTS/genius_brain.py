from lyricsgenius import Genius
from hidden import *


class GeniusAPI:
    """Talks to the LyricGenius API and handles information received."""

    def __init__(self):
        self.genius = Genius(access_token=GENIUS_CLIENT_ACCESS_TOKEN, verbose=False)
        self.artist = None
        self.song = None

    def get_artist(self, name: str) -> dict:
        """Get artist information and list of songs."""
        # Search Genius for artist and get the first result
        artist_info = self.genius.search_artists(search_term=name)['sections'][0]['hits'][0]['result']
        return artist_info

    def get_artist_songs(self, artist_id: int) -> list:
        """Gets top 100 songs from artist on Genius and returns them in a list."""
        # Combine 2 search result pages to get top 100 artist popular songs
        songs = self.genius.artist_songs(artist_id=artist_id, sort='popularity',
                                         per_page=50, page=1)['songs']
        songs.extend(self.genius.artist_songs(artist_id=artist_id, sort='popularity',
                                              per_page=50, page=2)['songs'])
        return songs

    def get_lyrics(self, song_id: int):
        song_lyrics = self.genius.lyrics(
            song_id=song_id,
            remove_section_headers=True
        )
        return song_lyrics
