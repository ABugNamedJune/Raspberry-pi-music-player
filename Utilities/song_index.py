#PyPlayer - June Bush - June@JuneBush.com - Last updated 5.16.24
#This handles importing all songs into an indexed series of dictionaries
#I think doing it this way will save resources at runtime...

import os
import json

#   -----
#   The great return block
#   Are you supposed to do this in Python? I remember when studying C# and Java my teachers and professors always wanted me to
#   do this within the classes I wrote, but I'm self-taught with Python... this seems like good practice tho, yeah?
#   -----

#returns all albums by a specific artist
def get_albums_by_artist(artist_name):
    pass

#returns all albums
def get_all_albums():
    pass

#returns all songs
def get_all_songs():
    pass

#returns all artists
def get_all_artists():
    pass

#returns all songs in a given album
def get_songs_by_album(album_name):
    pass


#   -----
#   The actual meat and potatoes
#   -----

#Walks the directory where the songs are held and generates an array of dictionaries containing all their information
#oh god, don't look! If this made it to release I'm going to kms
def generate_song_list():
    song_list = []
    for (root,_,files) in os.walk(os.getcwd() + '\\Test Library\\'):
        for i in files:
            if(i != ""):
                current_song_path = os.path.abspath(os.path.join(root, i))
                tmp_path = current_song_path.split('\\')
                song_list.append({"title": i, "album": tmp_path[len(tmp_path) - 2], "artist": tmp_path[len(tmp_path) - 3], "path": current_song_path})
    return(song_list)

#Saves the song list to a json file
#Should be run on startup or whenever changes are applied to the file structure.
def export_song_list():
    with open((os.getcwd() + '\\song_list.json'), 'w') as fout:
        json.dump(generate_song_list(), fout)

#imports the song list from a json file and returns a list of dictionaries.
def import_song_list():
    song_list = []
    #TODO: Write some shit to make sure this file actually exists.  I can do that later tho, 'cause I'm lazy and there's more exciting shit going on.
    with open((os.getcwd() + '\\song_list.json')) as fin:
        song_list = json.load(fin)
    return(song_list)

export_song_list()
print(import_song_list())
