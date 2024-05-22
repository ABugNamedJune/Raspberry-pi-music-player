#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.22.24

import song_index

#This is the main UI element, it takes a menu type (e.g. "artist", "album") and a value (e.g. "Starfucker", "Jupiter")
#And populates a navigable menu with the values from that data set
def generate_menu(type, value):
    parse_values(type, value)


#god this is jank, but whatever, for now it's fine.
def parse_values(type, value):
    if type == "all_artists":
        return song_index.get_all_artists()
    elif type == "all_albums":
        return song_index.get_all_albums()
    elif type == "all_songs":
        pass    #I gotta think about this more
    elif type == "album_by_artist":
        return song_index.get_albums_by_artist(value)
    elif type == "song_by_album":
        return song_index.get_songs_by_album(value)