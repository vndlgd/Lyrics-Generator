import markovify
import sys


def generate_lyrics():
    lyrics = []

    genre = sys.argv[1]
    textfile = f"lyrics/{genre}.txt"
    # Get raw text as string.
    f = open(textfile, "r")
    text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(3):
        print(text_model.make_short_sentence(80))

    f.close()


generate_lyrics()

