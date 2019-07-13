#! python3
# A simple stopwatch program.

# Chapter 15
# Keeping Time, Scheduling Tasks, and Launching Programs
# Automating the Boring Stuff

# Project: Super Stopwatch

import time, sys

print("Press ENTER to begin.\nAfterwards, press ENTER to \"click\" the stopwatch.\nPress Ctrl-C to quit.")

input()
# press enter to begin.
print("Started!")

start_time = round(time.time(), 2)
# get the first lap's start time.
last_time = start_time

lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print("Lap #%s: Total time: %s ... Lap time: %s" % (lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = time.time() # Reset the last lap time.

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
