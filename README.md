
# Spotify Playlist

A Python script that scrapes Billboard’s Hot 100 chart for top songs from a specified date and automatically adds them to a Spotify playlist. This project is ideal for creating "throwback" playlists based on historical top songs.

## Features
- **Web Scraping**: Extracts song names from Billboard's Hot 100 chart for a specified date.
- **Spotify Integration**: Searches for songs on Spotify and adds them to a playlist using the Spotify API.

## Prerequisites

To run this project, you need the following:

1. **Python 3.x**
2. **Spotify Developer Account** (for API credentials)
3. **Python Libraries**:
   - Spotipy (for Spotify API interactions)
   - BeautifulSoup (for web scraping)
   - Requests (for sending HTTP requests)
   - dotenv (for environment variable management)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/zangrjol/spotify_playlist.git
   ```
2. Navigate into the project directory:
   ```
   cd spotify_playlist
   ```
3. Install the required Python packages:
   ```
   pip install spotipy beautifulsoup4 requests python-dotenv
   ```

## Setup

1. **Spotify API Credentials**:  
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
   - Note your `client_id` and `client_secret` from your Spotify app settings.
   - Set up a redirect URI in Spotify (e.g., `http://example.com`).

2. **Environment Variables**:  
   - Create a `.env` file in the root of the project folder with the following content:
     ```
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     ```
   - Replace `your_client_id` and `your_client_secret` with your actual Spotify credentials.

3. **Set Up `.gitignore`**:  
   Ensure `.env`, `token.txt`, and `.cache` files are ignored by adding them to `.gitignore`:
   ```
   # Ignore environment and sensitive files
   .env
   token.txt
   .cache
   ```

## Usage

1. Open `main.py` in your code editor.
2. Update the `year` variable in the script to specify the year for which you want to retrieve songs.
3. Run the main script:
   ```
   python main.py
   ```

The script will:
1. Scrape the Billboard Hot 100 chart for the specified date.
2. Retrieve the top song names.
3. Search for these songs on Spotify.
4. Add the songs to a predefined Spotify playlist.

## Code Overview

### main.py
- **Scrapes Billboard** for song names from a specific date.
- **Fetches Spotify URIs** for the top 5 songs.
- **Adds these songs** to an existing Spotify playlist.

### spotify_connect.py
- **SpotifyConnect Class**: Manages Spotify authentication and playlist manipulation.
  - `find_track_uri(track_name)`: Finds the URI of a specified track on Spotify.
  - `add_to_playlist(items_list)`: Adds a list of track URIs to a specified playlist.

## Notes

- Make sure your Spotify API credentials are correct and that your Spotify app has the necessary permissions for playlist modification.
- Modify the playlist ID in `add_to_playlist()` if you want to add songs to a different playlist.

## License

This project is licensed under the MIT License. Feel free to modify and use it as you like.
