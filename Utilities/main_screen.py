#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.31.24
#This is where you'll start when running the program... at least for now
#import primary_ui

import song_index
import primary_ui

while True:
    menu_items = [{"type": "all artists", "name": "All Artists", "number": 0}, {"type": "all albums", "name": "All Albums", "number": 0}, {"type": "all songs", "name": "All Songs", "number": 0},{"type": "settings", "name": "Settings", "number": 0}, {"type": "about", "name": "About", "number": 0},]
    primary_ui.generate_menu(menu_items)
