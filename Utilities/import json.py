#exists for testing purposes.  Ignore for now.
import json

blah = []

for i in range(1, 1000):
    blah.append({"title": "average title", "artist": "artist name", "album": "album name"})

with open('test.json', 'w') as fout:
    json.dump(blah, fout)
