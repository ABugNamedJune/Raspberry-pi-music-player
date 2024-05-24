#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.24.24

import song_index
import os
import keyboard

ui_columns = 5

#This is the main UI element, it takes a menu type (e.g. "artist", "album") and a value (e.g. "Starfucker", "Jupiter")
#And populates a navigable menu with the values from that data set
def generate_menu(type, value):
    #menu_items = parse_values(type, value)
    menu_items = ["item 0", "item 1", "item 2", "item 3", "item 4", "item 5", "item 6"]
    cursor_position = 6

    #trap the user in a recursive loop to generate sub menus
    while(True):
        print_menu_windows_console(cursor_position, menu_items)
        parse_user_input(cursor_position, menu_items)
    


#determines what objects to place into the menu based on type
def parse_values(type, value):
    if type == "All Artists":
        return song_index.get_all_artists()
    elif type == "All Albums":
        return song_index.get_all_albums()
    elif type == "All Songs":
        pass    #I gotta think about this more
    elif type == "artist":
        return song_index.get_albums_by_artist(value)
    elif type == "album":
        return song_index.get_songs_by_album(value)
    elif type == "main":
        return ["All Artists", "All Albums", "All Songs", "Settings", "About"]
    
#writes the menu to the screen for windows
def print_menu_windows_console(cursor, menu_items):
    os.system('cls')
    menu_display_start = 0
    display_list = []

    #keeps the cursor in the center of the display screen unless it's approaching the extremes
    #This needs to be de-hardcoded eventually
    if(cursor > 2 and cursor < len(menu_items) - 2):
        menu_display_start = cursor - 2
    elif(cursor >= len(menu_items) - 2):
        menu_display_start = len(menu_items) - 5
    
    #print the menu
    for i in range(menu_display_start, menu_display_start + 5):
        if i == cursor:
            print(menu_items[i])
        else:
            print("  " + menu_items[i])

#takes user input and determines what actions to take
def parse_user_input(cursor, menu_items):
    while True:
        if keyboard.is_pressed('down'):
            return cursor + 1

generate_menu(5, 5)