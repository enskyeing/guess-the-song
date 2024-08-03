from genius_brain import *
from data_managers import Artist, Song
import random

# TODO allow user to quit game at any time using "q"
# TODO Add error handling for finding artist
# TODO add confirmation for finding correct artist
# TODO add time limit functionality



class GTSGame:
    def __init__(self, time_limit: int = 60):
        self.time_limit = time_limit
        self.genius = GeniusAPI()
        self.artist = None
        self.song = None
        self.lyric = ""
        self.round = 1
        self.game_ongoing = True
        self.welcome()
        self.start()

    def welcome(self):
        """Sends heading and game instructions."""
        gts_caps_ascii = """   _____   _    _   ______    _____    _____       _______   _    _   ______        _____    ____    _   _    _____ 
          / ____| | |  | | |  ____|  / ____|  / ____|     |__   __| | |  | | |  ____|      / ____|  / __ \  | \ | |  / ____|
         | |  __  | |  | | | |__    | (___   | (___          | |    | |__| | | |__        | (___   | |  | | |  \| | | |  __ 
         | | |_ | | |  | | |  __|    \___ \   \___ \         | |    |  __  | |  __|        \___ \  | |  | | | . ` | | | |_ |
         | |__| | | |__| | | |____   ____) |  ____) |        | |    | |  | | | |____       ____) | | |__| | | |\  | | |__| |
          \_____|  \____/  |______| |_____/  |_____/         |_|    |_|  |_| |______|     |_____/   \____/  |_| \_|  \_____|"""
        welcome_text = (
            f"Welcome to Guess the Song; the game where you need to guess which song the lyric belongs to within "
            f"{self.time_limit} seconds!")

    def start(self):
        """Starts the game."""
        while self.game_ongoing:
            user_guessing = True
            self.choose_artist()
            self.choose_song()
            print(f"Round {self.round} starting in...")
            for i in range(0, 6):
                print(i)
            print(f"Artist: {self.artist.name}")
            print(f"Lyric: {self.choose_lyric()}")
            while user_guessing:
                guess = input("Guess: ").lower()
                if guess == self.song.title.lower():
                    print(f"You guessed correctly!\nThe song was {self.song.title} by {self.artist.name}.")
                    user_guessing = False
                else:
                    continue
            self.replay()
        self.end()

    def replay(self):
        """Checks if player wants to play again."""
        valid_answer = False
        while not valid_answer:
            play_again = input("Would you like to play again? (y/n) ").lower()
            if play_again == "y":
                valid_answer = True
                self.round += 1
                self.game_ongoing = True
            elif play_again == "n":
                valid_answer = True
                self.game_ongoing = False
            else:
                print("That was not a valid answer.")

    def end(self):
        print(f"You played {self.round} round(s).\nThanks for playing Guess the Song!")
        # TODO add game stats

    def choose_artist(self):
        """Uses LyricGenius to get artist information and songs."""
        user_input = input("What musician would you like to play for this round? ")
        print(f"Searching for {user_input}...")
        artist_info = self.genius.get_artist(name=user_input)
        artist_songs = self.genius.get_artist_songs(artist_id=artist_info["id"])

        # Create Artist class with all the information of the selected artist
        self.artist = Artist(
            name=artist_info['name'],
            genius_id=artist_info['id'],
            songs=artist_songs,
            image=artist_info['image_url'],
            genius_link=artist_info['url']
        )
        print(f"{self.artist.name} found!")

    def choose_song(self):
        print("Choosing lyric...")
        random_song = random.choice(self.artist.songs)
        lyrics = self.genius.get_lyrics(song_id=random_song["id"])

        # Format data in Song class
        self.song = Song(
            title=random_song["title"],
            lyrics=lyrics,
            cover=random_song['song_art_image_url'],
            genius_link=random_song['url'],
            genius_id=random_song['id']
        )

    def choose_lyric(self):
        lyric_list = [line for line in self.song.lyrics.splitlines() if len(line) > 25 and self.song.title not in line]
        return random.choice(lyric_list)
