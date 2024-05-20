#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.15.24
#This handles importing all songs into an indexed series of dictionaries
#I think doing it this way will save resources at runtime... but may cause issues on systems where RAM is severely limited.
#asdflkjalksdfj
#Should I just be using SQL? Is this a bullshit way of doing this?

import os
import json

#   -----
#   The great return block
#   Are you supposed to do this in Python? I remember when studying C# and Java my teachers and professors always wanted me to
#   do this within the classes I wrote, but I'm self-taught with Python... this seems like good practice tho, yeah?
#   -----

#returns all albums by a specific artist
def get_albums_by_artist(artist_name):
    albums_by_artist = set()
    for i in import_song_list():
        if i["artist"] == artist_name:
            albums_by_artist.add(i["album"])
    return sorted(albums_by_artist)


#returns all albums
def get_all_albums():
    albums = set()
    for i in import_song_list():
        albums.add(i["album"])
    return sorted(albums)

#returns all songs
#this is a little jank.  There are going to be songs with the same name, so this needs some way to identify songs with the same name
#I'll try to find a way to get a better identifyer... maybe assign each song a number?
def get_all_songs():
    songs = list()
    for i in import_song_list():
        songs.append(i["title"])
    return sorted(songs)

#returns all artists
def get_all_artists():
    artists = set()
    for i in (import_song_list()):
        artists.add(i["artist"])
    return sorted(artists)

#returns all songs in a given album
def get_songs_by_album(album_name):
    songs_by_album = set()
    for i in import_song_list():
        if i["album"] == album_name:
            songs_by_album.add(i["album"])
    return songs_by_album


#   -----
#   The actual meat and potatoes
#   -----

#Walks the directory where the songs are held and generates an array of dictionaries containing all their information
#oh god, don't look! If this made it to release I'm going to kms
def generate_song_list():
    master_song_list = []
    for (root,_,files) in os.walk(os.getcwd() + '\\Test Library\\'):
        for i in files:
            if(i != ""):
                current_song_path = os.path.abspath(os.path.join(root, i))
                tmp_path = current_song_path.split('\\')
                master_song_list.append({"title": i, "album": tmp_path[len(tmp_path) - 2], "artist": tmp_path[len(tmp_path) - 3], "path": current_song_path})
    return(master_song_list)

#Saves the song list to a json file
#Should be run on startup or whenever changes are applied to the file structure.
def export_song_list():
    with open((os.getcwd() + '\\song_list.json'), 'w') as fout:
        json.dump(generate_song_list(), fout)

#imports the song list from a json file and returns a list of dictionaries.
def import_song_list():
    master_song_list = []
    #TODO: Write some shit to make sure this file actually exists.  I can do that later tho, 'cause I'm lazy and there's more exciting shit going on.
    with open((os.getcwd() + '\\song_list.json')) as fin:
        master_song_list = json.load(fin)
    return(master_song_list)