#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.31.24
#This handles importing all songs into an indexed series of dictionaries

import os
import json
import time

#   -----
#   Chapter 1:
#   There and back again, snagging the data
#   -----

#returns all objects of a given type along with an identifier denoting that type.
#shouldn't be used for songs honestly, and frankly, I should find a better way of doing this in the future in case there are multiple albums / artists/ whatever with the same name
def get_all_x(identifier):
    x_return_list = []
    #songs have to be handled differently since they require a unique identifier to prevent culling duplicates
    if identifier == "song":
        for i in import_song_list():
            x_return_list.append({"type": "song", "name": i["song"], "number": i["number"]})
    else:
        #scan the entire song list and put together all objects of x-type, removing duplicates
        x_set = set()
        for i in import_song_list():
            x_set.add(i[identifier])
        for i in x_set:
            #number is superfluous but included just in case
            x_return_list.append({"type": identifier, "name": i, "number": 0})
    return(x_return_list)

#returns all albums by a specific artist
def get_albums_by_artist(artist_name):
    albums_by_artist = set()
    for i in import_song_list():
        if i["artist"] == artist_name:
            albums_by_artist.add(i["album"])
    album_list = []
    for i in albums_by_artist:
        album_list.append({"type": "album", "name": i, "number": 0})
    return album_list

#returns all songs in a given album
def get_songs_by_album(album_name):
    songs_by_album = list()
    for i in import_song_list():
        if i["album"] == album_name:
            songs_by_album.append({"type": "song", "name": i["song"], "number": i["number"]})
    return songs_by_album


#   -----
#   Chapter 2:
#   The great data exchange
#   -----

#Walks the directory where the songs are held and generates an array of dictionaries containing all their information
#oh god, don't look! If this made it to release I'm going to kms
def generate_song_list():
    master_song_list = []
    for (root,_,files) in os.walk(os.getcwd() + '\\Test Library\\'):
        count = 0
        for i in files:
            if(i != ""):
                current_song_path = os.path.abspath(os.path.join(root, i))
                tmp_path = current_song_path.split('\\')
                master_song_list.append({"song": i, "album": tmp_path[len(tmp_path) - 2], "artist": tmp_path[len(tmp_path) - 3], "path": current_song_path, "number": count})
                count = count + 1
    return(master_song_list)

#Saves the song list to a json file
#Should be run on startup or whenever changes are applied to the file structure.
def export_song_list():
    with open((os.getcwd() + '\\song_list.json'), 'w') as fout:
        json.dump(generate_song_list(), fout)

#imports the song list from a json file and returns a list of dictionaries.
def import_song_list():
    if not os.path.exists(os.getcwd() + '\\song_list.json'):
        export_song_list()
    with open((os.getcwd() + '\\song_list.json')) as fin:
        return(json.load(fin))