import time
import curses
import logging

def main(stdscr):
    # A placeholder for a second game.
    logging.debug("Game Three function has started.")
    maxY, maxX = stdscr.getmaxyx()
    # Put message in middle of screen.
    stdscr.addstr(maxY//2, maxX//2, "Game Three is still under development!")
    stdscr.refresh()
    time.sleep(2)
    return 1

# Call the main function if the script is run directly
if __name__ == "__main__":
    curses.wrapper(main)
