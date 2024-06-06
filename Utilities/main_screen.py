#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.31.24
#This is where you'll start when running the program... at least for now
#import primary_ui

import song_index
import primary_ui
import display_menu
import time

#while True:
#    print("heck")
#    menu_items = [{"type": "all artists", "name": "All Artists", "number": 0}, {"type": "all albums", "name": "All Albums", "number": 0}, {"type": "all songs", "name": "All Songs", "number": 0},{"type": "settings", "name": "Settings", "number": 0}, {"type": "about", "name": "About", "number": 0},]
#    primary_ui.generate_menu(menu_items)

test_menu = ["Juniper Bush is rlly cool", "This is a long list entry", "blegh", "ugh", "heck", "jeez", "dang", "shoot"]
while True:
    display_menu.generate_menu(test_menu, 2)
