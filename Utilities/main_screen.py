#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.22.24
#This is where you'll start when running the program... at least for now
#This is going to get folded into primary_ui.py soon
import os
import primary_ui

cursor_position = 0
menu_items = ["All Artists", "All Albums", "All Songs", "Settings", "About"]

def print_menu(menu):
    for i in range(0, 5):
        if(i == cursor_position):
            print(menu[i])
        else:
            print("  " + menu[i])

def read_input(menu):
    global cursor_position
    blah = input("")
    if(blah == "w"):
        cursor_position -= 1
    elif(blah == "s"):
        cursor_position += 1
    elif(blah == "d"):
        primary_ui.generate_menu(menu[cursor_position], "")
    else:
        read_input()
    
    if(cursor_position > 4):
        cursor_position = 4
    elif(cursor_position < 0):
        cursor_position = 0

def clear_scn():
    os.system('cls')

print (int(5/2))