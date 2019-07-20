#! python3
# A simple stopwatch program.

# Chapter 15
# Keeping Time, Scheduling Tasks, and Launching Programs
# Automating the Boring Stuff

# Project: Super Stopwatch

import time, sys

print("Press ENTER to begin.\nAfterwards, press ENTER to \"click\" the stopwatch.\nEnter any text to quit.")

a = input()
# press enter to begin.
print("Started!")

start_time = round(time.time(), 2)
# get the first lap's start time.
last_time = start_time

lap_num = 1

# Start tracking the lap times.
while True:
    b = input()

    if b != a:
        print('\nDone.')
        break

    else:
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)  # Add a RegEx to show minutes when goes further than 59.99 sec.
        print("Lap #%s, time: %s ... Total time: %s" % (lap_num, lap_time, total_time), end='')
        lap_num += 1
        last_time = time.time()  # Reset the last lap time.
