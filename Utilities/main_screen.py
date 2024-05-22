#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 5.22.24
#This is where you'll start when running the program... at least for now
cursor_position = 2
menu_items = ["All Artists", "All Albums", "All Songs", "Settings", "About"]

def print_menu():
    for i in range(0, 5):
        if(i == cursor_position):
            print(menu_items[i])
        else:
            print("  " + menu_items[i])


print_menu()