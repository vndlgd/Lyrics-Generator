import pyfiglet
import os

# Generate banner and print
ascii_banner = pyfiglet.figlet_format("Lyrics Generator")
print(ascii_banner)

# User selection Menu
print(
    "Welcome to Lyrics Generator, select a genre of music you'd like to generate lyrics for: "
)

# Print list of available genres
genres = ["COUNTRY", "POP", "RAP", "ROCK", "METAL"]
for genre in genres:
    print(genre)
print('Type "quit" to exit.\n')

# Get user input
user_input = input("Genre: ")

# Generate lyrics, exit, or user-friendly error message when genre not found
while user_input.lower() != "quit":
    # Make user input case insensitive
    if user_input.upper() in genres:
        message = f"python3 generate.py {user_input}"
        os.system(message)
        print("\n")
        print(
            'Select a genre of music you\'d like to generate lyrics for or type "quit" to exit: '
        )
        for genre in genres:
            print(genre)
        user_input = input("\nGenre: ")
    else:
        user_input = input("Genre not found. Please choose a genre on the list: ")

