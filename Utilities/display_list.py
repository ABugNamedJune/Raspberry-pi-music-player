#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 6.7.24

import song_index
import os
import keyboard
import time
import config

menu_items = []
display_item = ""

cursor_position = 0

last_time = time.time()
tick_rate = .1
timer_text_scroll = 0
frame_counter = 0

columns = config.columns
lines = config.lines

#This is the main UI element, it's fed a list and allows the user to pick an entry from that list which it then returns
def generate_menu(menu, display):
    print("creating menu...")
    #yank them global variables into this here function
    global cursor_position
    global timer_text_scroll
    global last_time
    global tick_rate
    global frame_counter
    global menu_items
    menu_items = menu
    global display_item
    display_item = display


    print("imported variables")

    #loop until a selection is made
    while(True):
        current_time = time.time()

        #logic on the tick clock
        if(current_time - last_time > tick_rate):
            render()

            #parse user input
            if keyboard.is_pressed('down'):
                cursor_position = cursor_position + 1
                timer_text_scroll = 0
            elif keyboard.is_pressed('up'):
                cursor_position = cursor_position - 1
                timer_text_scroll = 0
            elif keyboard.is_pressed('left'):
                return 0
            elif keyboard.is_pressed('right'):
                return 1
            elif keyboard.is_pressed('enter'):
                return(menu_items[cursor_position])

            frame_counter = frame_counter + 1
            last_time = time.time()




#I mean the functionality is in the name, what do you want from me?
def render():
    global timer_text_scroll
    global cursor_position

    menu_start = 0
    lines = config.lines
    if(lines > len(menu_items)):
        lines = len(menu_items)

    #constrain the list to only the entries that can fit on screen at any given time
    if cursor_position > lines / 2 and cursor_position < len(menu_items) - lines / 2:
        menu_start = cursor_position - lines / 2
    elif cursor_position > len(menu_items) - lines / 2:
        menu_start = len(menu_items) - lines

    #constrain the cursor to the bounds of the menu
    if(cursor_position > len(menu_items) - 1):
        cursor_position = len(menu_items) - 1
    if(cursor_position < 0):
        cursor_position = 0

    os.system("cls")

    #Render the display
    for index, i in enumerate(menu_items):
        #print only the elements within the bounds of the display
        if(index >= menu_start and index < menu_start + config.lines):
            #scroll the active element if it's longer than the column width
            if(len(i[display_item]) > columns and cursor_position == index):
                print(">" + (i[display_item][timer_text_scroll:] + " " + i[display_item][:timer_text_scroll])[:columns - 1] + "<")
                timer_text_scroll = timer_text_scroll + 1
                if(timer_text_scroll > len(i[display_item])):
                    timer_text_scroll = 0
            #just select it if not
            elif(cursor_position == index):
                print(">" + i[display_item].ljust(columns, " ") +"<")
            elif(len(i[display_item]) > columns):
                print(" " + i[display_item][:columns] + " ")
            else:
                print(" " + i[display_item] + " ")
        

#generate_menu(["something went wrong -_-", "whoops", "uh oh", "try restarting this application"],1)
