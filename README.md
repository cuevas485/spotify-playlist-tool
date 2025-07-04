**\# Spotify Playlist Builder (Python Project)**

This is a Python-based CLI (command-line interface) application that allows users to search for songs using Spotify track metadata, build custom playlists, and receive tailored feedback based on audio features.

\---

**\#\# Dataset**

This project uses the \[Spotify Tracks Dataset from Kaggle\](https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db), specifically the \`SpotifyFeatures.csv\` file. The dataset includes the following audio features:

\- \`genre\`, \`artist\_name\`, \`track\_name\`, \`popularity\`  
\- \`acousticness\`, \`danceability\`, \`duration\_ms\`, \`energy\`  
\- \`instrumentalness\`, \`liveness\`, \`loudness\`, \`speechiness\`  
\- \`tempo\`, \`valence\`, \`key\`, \`mode\`, \`time\_signature\`

\---

**\#\# Features**

\- \*\*Search by Song or Artist:\*\* Find songs that match user input and display results.  
\- \*\*Shuffle by Genre:\*\* Select a genre and return 15 randomly selected songs.  
\- \*\*Add to Playlist:\*\* Users can add individual songs to their personal playlist.  
\- \*\*Tailored Song Description:\*\* Songs are described based on their popularity and audio features.  
\- \*\*Runtime Calculation:\*\* Total playlist duration is calculated and displayed in minutes.  
\- \*\*Planned Feature:\*\* Playlist summary that averages features and provides insights about the user’s taste.

\---

**\#\# How to Run**

1\. Clone the repository:  
   \`\`\`bash  
   git clone https://github.com/cuevas485/spotify-playlist-builder.git  
   cd spotify-playlist-builder  
2\. Make sure you have Python 3.7+ installed.

3\. Install any required packages (standard library only — no external dependencies needed).

4\. Place `SpotifyFeatures.csv` in the root of the project directory.

5\. Run the script:  
python spotify\_playlist.py

**\#\# Example Output**

\================================  
What would you like to do?  
1\. Search by Artist  
2\. Search by Song  
3\. Shuffle by Genre  
4\. Current Playlist  
Reply with a number or 'quit' to stop  
Enter here: 1

Enter Artist: Drake  
1\. Drake \- God's Plan  
2\. Drake \- Hotline Bling  
...  
Add a song to your playlist:  
Reply with the song number: 1  
Added song to playlist: God's Plan by Drake is classified as hip-hop. This song is considered popular with a high number of plays.
