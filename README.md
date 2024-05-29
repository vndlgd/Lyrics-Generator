# Lyrics Generator

This project, developed using Python for the San Diego State University Artificial Intelligence Club Hackathon, is designed to generate lyrics based on user-selected music genres using Markov chains.

![alt text](<Screenshot 2024-04-01 at 2.13.26 AM.png>)

## Project Structure

- **main.py:** Entry point of the program that presents the user with a menu to select a music genre and generates lyrics based on the chosen genre.
- **scrape.py:** Module to retrieve lyrics from various songs of different genres using the Genius.com API and store them in text files categorized by genre.
- **clean.py:** Module to preprocess the retrieved lyrics by removing unwanted patterns and metadata from the text files.
- **generate.py:** Module to generate new lyrics using Markov chains based on the preprocessed lyrics stored in text files.

## Dependencies

- [lyricsgenius](https://pypi.org/project/lyricsgenius/): A Python client for the Genius.com API, used for fetching song lyrics.
- [pyfiglet](https://pypi.org/project/pyfiglet/): A Python library for creating ASCII text banners, used for the project banner.
- [markovify](https://pypi.org/project/markovify/): A simple, extensible Markov chain generator, used for generating new lyrics.

## How It Works

1. **Retrieving Lyrics:** The `scrape.py` module retrieves lyrics from various songs of different genres using the Genius.com API and stores them in text files categorized by genre in the `lyrics/` directory.

2. **Preprocessing Lyrics:** The `clean.py` module preprocesses the retrieved lyrics by removing unwanted patterns, metadata, and formatting from the text files to prepare them for the Markov chain generation process.

3. **Generating Lyrics:** The `generate.py` module uses Markov chains to generate new lyrics based on the preprocessed lyrics stored in text files. It creates new lyrics by analyzing the patterns and structures of the existing lyrics.

4. **User Interaction:** The `main.py` script provides a user-friendly CLI interface where the user can select a music genre from a menu and view the generated lyrics based on their choice.

## Challenges and Considerations

- **Web Scraping:** One of the challenges faced was web scraping and cleaning the lyrics. The `lyricsgenius` library was used for scraping, but there were limitations and stability concerns due to infrequent updates.
- **Regex Patterns:** Another challenge was using regex patterns for text cleaning. Researching and learning regex patterns were necessary to effectively clean the retrieved lyrics.
- **Text Uniqueness:** A key consideration is that with a larger dataset of lyrics to work with, the generated text would be more unique and diverse.

## Future Improvements

- **API Integration:** Consider integrating with a dedicated API for fetching song lyrics to ensure stability and reliability in the lyrics retrieval process.
- **Enhanced Text Cleaning:** Implement more advanced text cleaning techniques using regex to handle a wider range of patterns and improve the quality of generated lyrics.
- **Advanced Generation Techniques:** Explore advanced generation techniques beyond Markov chains to enhance the quality and variability of generated lyrics.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the `main.py` script to start the Lyrics Generator.
4. Follow the on-screen instructions to select a music genre and view the generated lyrics.
