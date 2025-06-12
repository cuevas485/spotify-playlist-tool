import csv
import random

currentPlaylist = []
totalRuntime = 0

CSV_FILE = 'SpotifyFeatures.csv'


def extract_song_details(row):
    return {
        "genre": row[0],
        "artist": row[1],
        "song": row[2],
        "trackId": row[3],
        "popularity": row[4],
        "acousticness": row[5],
        "danceability": row[6],
        "duration": row[7],
        "energy": row[8],
        "instrumentalness": row[9],
        "key": row[10],
        "liveness": row[11],
        "loudness": row[12],
        "mode": row[13],
        "speechiness": row[14],
        "tempo": row[15],
        "timeSignature": row[16],
        "valence": row[17]
    }


def phraseOne(popularity):
    popularity = int(popularity)
    if popularity >= 75:
        return "This song is considered popular with a high number of plays."
    elif popularity >= 50:
        return "This song seems to get an average number of plays."
    else:
        return "This song is not well known and gets minimal plays."


def search_csv(column_index, search_term):
    with open(CSV_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        return [row for row in csv_reader if search_term.strip().lower() in row[column_index].strip().lower()]


def shuffle_by_genre():
    genre = input("Enter genre: ").strip().lower()
    with open(CSV_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        songs = [row for row in csv_reader if genre == row[0].strip().lower()]
        random.shuffle(songs)
        for row in songs[:15]:
            print(f"{row[0]} | {row[1]} - {row[2]}")


def add_song_to_playlist(results):
    global totalRuntime
    for idx, row in enumerate(results, start=1):
        print(f"{idx}. {row[1]} - {row[2]}")

    choice = input("\nAdd a song to your playlist (enter number): ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(results)):
        print("Not a valid selection")
        return

    selected = results[int(choice) - 1]
    currentPlaylist.append(selected)
    details = extract_song_details(selected)
    totalRuntime += int(details["duration"])

    phrase = phraseOne(details["popularity"])
    print(f"Added song: {details['song']} by {details['artist']}, Genre: {details['genre']}. {phrase}")


def display_playlist():
    print("\nCurrent Playlist:")
    for row in currentPlaylist:
        print(f"{row[1]} - {row[2]}")
    minutes = totalRuntime / 60000
    print(f"Runtime Duration: {minutes:.2f} minutes")


# Start Program
while True:
    print("\n================================")
    print("What would you like to do?")
    print("1. Search by Artist")
    print("2. Search by Song")
    print("3. Shuffle by Genre")
    print("4. Current Playlist")
    print("Type 'quit' to stop")
    
    choice = input("Enter your choice: ").strip().lower()

    if choice == "quit":
        print("Program ended.")
        break

    elif choice == "1":
        artist = input("Enter Artist: ")
        results = search_csv(1, artist)
        if results:
            add_song_to_playlist(results)
        else:
            print("No songs found for that artist.")

    elif choice == "2":
        song = input("Enter Song: ")
        results = search_csv(2, song)
        if results:
            add_song_to_playlist(results)
        else:
            print("No songs found matching that title.")

    elif choice == "3":
        shuffle_by_genre()

    elif choice == "4":
        display_playlist()

    else:
        print("Invalid input. Try again.")
