#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.15.24
#This handles importing all songs into an indexed series of dictionaries
#I think doing it this way will save resources at runtime... but may cause issues on systems where RAM is severely limited.

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
    for (root,_,files) in os.walk(os.getcwd() + '\\Library\\'):
        for i in files:
            if(i != ""):
                current_song_path = os.path.abspath(os.path.join(root, i))
                tmp_path = current_song_path.split('\\')
                song_list.append({"title": i, "album": tmp_path[len(tmp_path) - 2], "artist": tmp_path[len(tmp_path) - 3], "path": current_song_path})
    return(song_list)

#Saves the song list to a json file
def export_song_list():
    with open((os.getcwd() + '\\song_list.json'), 'w') as fout:
        json.dump(generate_song_list(), fout)

#imports the song list from a json file
def import_song_list():
    #I'm writing this during my down time at work, and this function is going to be so easy to implement, but also I'm so tired and don't want to, so for now we'll just generate a new json file each time we need one.  k?
    pass