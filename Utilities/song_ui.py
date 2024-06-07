#PyPlayer - June Bush - June@JuneBush.com - GPL3.0 - Last updated 6.7.24

import time
import config

start_time = 0
last_time = 0
frame_time = 1
second_counter = 0

def initialize_player(song_duration, seconds_elapsed):
    last_time = time.time()

    while(True):
        current_time = time.time()

        #print the timeline
        #clunky bullshit alert!
        #wee-woo wee-woo, someone take away this chick's programming license.
        if(current_time - last_time > frame_time):
            timeline = int(round(seconds_elapsed / song_duration * config.columns, 0))
            print_timeline = ""
            for i in range(0, timeline):
                print_timeline = print_timeline + "#"
            print(print_timeline)

            seconds_elapsed = seconds_elapsed + 1
            last_time = current_time


initialize_player(195,120)