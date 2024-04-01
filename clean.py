import re

genres = ["country", "metal", "pop", "rap", "rock"]

# Clean lyrics for all text files
for genre in genres:
    f = open(f"lyrics/{genre}.txt", "r")
    lyrics = f.read()

    # Define the first regex pattern to match sequences of digits followed by "Embed"
    pattern1 = r"\b\d+Embed\b|\d+Embed"

    # Define the second regex pattern to match lines containing square brackets []
    pattern2 = r"\[.*?\]"

    # Define the regex pattern to match lines containing "Contributors"
    pattern3 = r".*Contributors.*\n"

    # Remove the first pattern from lyrics
    clean_lyrics = re.sub(pattern1, "", lyrics)

    # Remove the second pattern from lyrics
    clean_lyrics = re.sub(pattern2, "", clean_lyrics)

    # Remove the second pattern from lyrics
    clean_lyrics = re.sub(pattern3, "", clean_lyrics)

    f2 = open(f"lyrics/{genre}.txt", "w")
    f2.write(clean_lyrics)

