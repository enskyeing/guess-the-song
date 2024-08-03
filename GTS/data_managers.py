class Artist:
    """Contains name, id, songs, image, and genius link for an Artist."""

    def __init__(self, name: str, genius_id: int, songs: list, image: str, genius_link: str):
        self.name = name
        self.id = genius_id
        self.songs = songs
        self.image = image
        self.genius_link = genius_link

    def __str__(self):
        return self.name


class Song:
    """Contains the title, lyrics, cover, genius link, and genius ID for a song."""

    def __init__(self, title: str, lyrics: str, cover: str, genius_link: str, genius_id: int):
        self.title = title
        self.lyrics = lyrics
        self.cover = cover
        self.genius_link = genius_link
        self.id = genius_id

    def __str__(self):
        return self.title
