def add(song, playlist):
    """TODO: Add song to playlist"""
    playlist.append(song)

def remove(song, playlist):
    """TODO: Remove song from playlist (if there)"""

def play(playlist):
    playlist.pop(0)
    """TODO: Print the first song in the playlist (if any) and remove"""

def show_all(playlist):
    for song in playlist:
        for key, value in song.items():
            print(f"\t{key}: {value}")
    print(f"\n")

    """TODO: Print all contents in the playlist"""

def save(playlist, filepath):
    """Challenge: TODO: Save current playlist to filepath"""

def load(filepath):
    """Challenge: TODO: Load a new playlist from filepath and return it"""

def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
        then do the task requested
    """

    playlist = []
    end = False

    while not end:
        user_choice = input("Select command: ")

        # Ask all inputs in the playlist_app() function to make functions simple
        if user_choice == "add":
            title= input("Enter song title: ")
            artist = input("Enter artist name: ")
            new_song = {"Title": title, "Artist": artist}
            add(new_song, playlist)
        if user_choice == "show":
            show_all(playlist)
        if user_choice == "play":
            play(playlist)
        if user_choice == "exit":
            end = True

playlist_app()