import os
from lyricsgenius import Genius

token = os.getenv("TOKEN")
genius = Genius(token)


def scrape_lyrics(song_name, artist_name, genre):
    try:
        song = genius.search_song(song_name, artist_name)
        if song is not None:
            f = open(f"lyrics/{genre}.txt", "a")
            f.write(song.lyrics)
            f.write("\n\n")
        else:
            print(f"Song '{song_name}' by '{artist_name}' not found.")
    except Exception as e:
        print(f"Error scraping lyrics: {e}")


# Rock
scrape_lyrics("Stairway to  Heaven", "Led Zeppelin", "rock")
scrape_lyrics("Bohemian Rhapsody", "Queen", "rock")
scrape_lyrics("Smells Like Teen Spirit", "Nirvana", "rock")

# Pop
scrape_lyrics("Shake It Off", "Taylor Swift", "pop")
scrape_lyrics("Sorry", "Justin Beiber", "pop")
scrape_lyrics("Hello", "Adele", "pop")

# Country
scrape_lyrics("Ring of Fire", "Johnny Cash", "country")
scrape_lyrics("Jolene", "Dolly Parton", "country")
scrape_lyrics("Friends in Low Places", "Garth Brooks", "country")

# Metal
scrape_lyrics("Enter Sandman", "Metallica", "metal")
scrape_lyrics("The Trooper", "Iron Maiden", "metal")
scrape_lyrics("Paranoid", "Black Sabbath", "metal")

# Rap
scrape_lyrics("Lose Yourself", "Eminem", "rap")
scrape_lyrics("Hotline Bling", "Drake", "rap")
scrape_lyrics("Empire State of Mind", "Jay-Z", "rap")
