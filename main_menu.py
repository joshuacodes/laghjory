import time
import curses
import curses.textpad
import logging

import star_wars
import game_two
import game_three

# Utility function to clear the screen regardless of OS
def clear_screen(window):

    window.clear()
    window.refresh()

# Utility function to print a centered string
def center_text(window, text, row):

    # Get the height and width of the console
#    height, width = win.getmaxyx()

    # Calculate the center position and print the text
    x = int((window.getmaxyx()[1] - len(text)) / 2)
    logging.debug("Centered line: {}.".format(text))
    window.addstr(row, x, text)
    window.refresh()

# Utility to process array of strings
def center_text_block(window, text_array):
    for i, text in enumerate(text_array):
        center_text(window, text, i)

def main(stdscr):

    logging.debug("Main menu function has started.")
    
    # Initialize the main screen with border
    maxY, maxX = stdscr.getmaxyx()
    minY, minX = stdscr.getbegyx()
    logging.debug("Main window size is {}x{}.".format(maxY, maxX))
    logging.debug("Main window position is {}x{}.".format(minY, minX))
    stdscr.border()
    stdscr.refresh()

    # Create a new window to display the menu
    menu_win = stdscr.derwin(maxY-4, maxX-4, 2, 2)
    logging.debug("Created the menu window.")

    # Array for text to display in the menu
    menu_heading = ["#######################################",
                 "#                                     #",
                 "# Welcome to Lucas's game collection. #",
                 "#                                     #",
                 "#######################################",
                 "",
                 "  Please select a game:                ",
                 ""]
    
    menu_options = ["  1. Star Wars                         ",
                 "  2. Game Two                          ",
                 "  3. Game Three                        ",
                 "  4. Exit                              ",
                 ""]

    menu_text = menu_heading + menu_options

    center_text_block(menu_win, menu_text)
    logging.debug("Added the menu text.")

    # Handle user selection of menu items
    ## TODO: Add highlighting of the selected menu item
    ## TODO: Add support for number keys to select menu items
    current_row = 11

    while True:
        key = menu_win.getch()
        logging.debug("User pressed {}.".format(key))
        logging.debug("Attempted conversion: {}.".format(chr(key)))
        if chr(key) == "1":
                logging.debug("User selected Star Wars.")
                clear_screen(stdscr)
                star_wars.main(stdscr)
                clear_screen(stdscr)
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
        elif chr(key) == "2":
                logging.debug("User selected Game Two.")
                clear_screen(stdscr)
                game_two.main(stdscr)
                clear_screen(menu_win)
                center_text_block(menu_win, menu_text)
        elif chr(key) == "3":
                logging.debug("User selected Game Three.")
                clear_screen(stdscr)
                game_three.main(stdscr)
                clear_screen(menu_win)
                center_text_block(menu_win, menu_text)
        elif chr(key) == "4":
                logging.debug("User selected Exit.")
                break 
        elif key == curses.KEY_UP and current_row > 11:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 13:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 11:
                logging.debug("User selected Star Wars.")
                clear_screen(stdscr)
                star_wars.main(stdscr)
                clear_screen(stdscr)
                center_text_block(menu_win, menu_text)
            elif current_row == 12:
                logging.debug("User selected Game Two.")
                clear_screen(stdscr)
                game_two.main(stdscr)
                clear_screen(stdscr)
                center_text_block(menu_win, menu_text)
            elif current_row == 13:
                logging.debug("User selected Exit.")
                break

        ## TODO: Add a loop to handle resizing of the main window
#        if stdscr.getch() == curses.KEY_RESIZE:
#            maxY, maxX = stdscr.getmaxyx()
#            logging.debug("Main window size changed to {}x{}.".format(maxY, maxX))
#            menu_win.erase()
#            menu_win.refresh()
#        if key == ord("q"):
#            break
