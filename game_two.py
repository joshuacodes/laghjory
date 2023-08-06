import time
import curses
import logging

# New function to get the time in human readable format and print it to the screen in the upper right corner.
def get_time(stdscr):
    maxY, maxX = stdscr.getmaxyx()
    minY, minX = stdscr.getbegyx()
    stdscr.addstr(minY+1, maxX-20, time.strftime("%H:%M:%S"))
    stdscr.refresh()

def main(stdscr):
    # A placeholder for a second game.
    logging.debug("Game Two function has started.")
    maxY, maxX = stdscr.getmaxyx()
    # Put message in middle of screen.
    stdscr.addstr(maxY//2, maxX//2, "Game Two is still under development!")
    # Print the time on the screen.
    get_time(stdscr)
    stdscr.refresh()
    time.sleep(2)
    return 1

# Call the main function if the script is run directly
if __name__ == "__main__":
    curses.wrapper(main)
