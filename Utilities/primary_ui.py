#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.24.24

import song_index
import os
import keyboard
import time

ui_columns = 5

#This is the main UI element, it takes a menu type (e.g. "artist", "album") and a value (e.g. "Starfucker", "Jupiter")
#And populates a navigable menu with the values from that data set
def generate_menu(menu_items):
    cursor_position = 0

    #trap the user in a recursive loop to generate sub menus
    while(True):
        print_menu_windows_console(cursor_position, menu_items)
        #ugh, I hate doing this, but sleep for a little bit 'cause it's going too quick
        time.sleep(.1)
        cursor_position = parse_user_input(cursor_position, menu_items)
        if cursor_position == -5:
            break
        cursor_position = constrain_cursor(cursor_position, menu_items)
    
#writes the menu to the screen for windows
#this is a fucking mess, but this will be deprecated when ported to rpi
def print_menu_windows_console(cursor, menu_items):
    os.system('cls')
    menu_display_start = 0

    #keeps the cursor in the center of the display screen unless it's approaching the extremes
    #This needs to be de-hardcoded eventually
    if(len(menu_items) > 5):
        if(cursor > 2 and cursor < len(menu_items) - 2):
            menu_display_start = cursor - 2
        elif(cursor >= len(menu_items) - 2):
            menu_display_start = len(menu_items) - 5

    #determines how long the list should be
    if len(menu_items) < 5:
        menu_display_end = len(menu_items)
    else:
        menu_display_end = menu_display_start + 5
    
    #print the menu
    for i in range(menu_display_start, menu_display_end):
        if i == cursor:
            print(menu_items[i]["name"])
        else:
            print("  " + menu_items[i]["name"])

#takes user input and determines what actions to take
def parse_user_input(cursor, menu_items):
    while True:
        if keyboard.is_pressed('down'):
            return cursor + 1
        elif keyboard.is_pressed('up'):
            return cursor - 1
        elif keyboard.is_pressed('left'):
            return -5
        elif keyboard.is_pressed('right'):
            parse_sub_menu(menu_items[cursor])

#parses what sub-menu to create based on current menu
def parse_sub_menu(menu_item):
    type = menu_item["type"]
    if type == "all artists":
        generate_menu(song_index.get_all_x("artist"))
    elif type == "all albums":
        generate_menu(song_index.get_all_x("album"))
    elif type == "artist":
        generate_menu(song_index.get_albums_by_artist(menu_item["name"]))
    elif type == "album":
        generate_menu(song_index.get_songs_by_album(menu_item["album"]))
        
        
#keeps the cursor from going off of the list
def constrain_cursor(cursor, menu_items):
    if cursor > len(menu_items) - 1:
        cursor = len(menu_items) - 1
    elif cursor < 0:
        cursor = 0
    return cursor