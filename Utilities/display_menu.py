#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 6.4.24
#This class is fed a list and allows the user to choose from them and returns the selection
#Either returns the object code or a status code
#status codes:
#0 - Cancel (return to previous screen with no selection)
#1 - go to player

import os
import config
import keyboard
import time

cursor_position = 0

last_time = 0
tick_number = 0
tick_time = .5
tick_delay = 5

#create a selectable menu base on a list fed to the function
def generate_menu(menu_items, display_entry):
    global last_time
    last_time = time.time()
    global tick_number
    global tick_time
    global tick_delay
    global cursor_position
    return_value = False

    #trap the user in a recursive loop to display the menu until a selection is made
    while(return_value == False):
        #increment the tick counter - not using a delta operation because who cares
        if time.time() - last_time > tick_time:
            tick_number = tick_number + 1
            if tick_number > tick_delay + config.columns:
                tick_number = 0
            print_menu_windows_console(menu_items, display_entry)
            last_time = time.time()

        #run through the printing and user input
        #parse user input
        if keyboard.is_pressed('down'):
            print("blah blah")
            cursor_position = cursor_position + 1
            tick_number = 0
            break
        elif keyboard.is_pressed('up'):
            cursor_position = cursor_position - 1
            tick_number = 0
            break
        elif keyboard.is_pressed('left'):
            return 0
        elif keyboard.is_pressed('right'):
            return 1
        elif keyboard.is_pressed('enter'):
            return(menu_items[cursor_position])

#writes the menu to the screen for windows
#this is a fucking mess, but this will be deprecated when ported to rpi
def print_menu_windows_console(menu, display_entry):
    global tick_delay
    global tick_number
    os.system('cls')

    #define variables
    menu_start = 0
    lines = config.lines
    if(lines > len(menu)):
        lines = len(menu)
    lines_half = lines / 2
    columns = config.columns


    #constrain the list to only the entries that can fit on screen at any given time
    if cursor_position > lines_half and cursor_position < len(menu) - lines_half:
        menu_start = cursor_position - lines_half
    elif cursor_position > len(menu) - lines_half:
        menu_start = len(menu) - lines

    #build the display
    for i in range(int(menu_start), int(menu_start + lines)):
        if(i == cursor_position):
            menu[i].ljust(columns, ' ')
            if(tick_number > tick_delay):
                #the fun cycle-ey bit
                menu[i] = menu[i][tick_number - tick_delay:] + menu[i][:tick_number - tick_delay]
                #add padding if the entry is less than the column width and append three spaces just for funsies
                menu[i] = ">" + menu[i].ljust(columns, ' ') + "   "
                #reset the tick number if it becomes greater than the length of the entry
                if(tick_number - tick_delay > len(menu_items)):
                    tick_number = 0
        else:
            menu_items[i] = " " + menu[i]

        #truncate the entry down to the column width
        if len(menu_items[i]) > columns:
            menu_items[i] = menu_items[i][:columns]



    #print the menu
    for i in menu_items:
        print(i)