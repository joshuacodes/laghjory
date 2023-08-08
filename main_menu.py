import time
import curses
import curses.textpad
import logging

import star_wars
import game_two
import game_three

# Utility to clear the screen regardless of OS
def clear_screen(window):
    window.clear()
    window.refresh()

# Utility center a string
def center_text(window, text, row):
    x = int((window.getmaxyx()[1] - len(text)) / 2)
    logging.debug("Centered line: {}.".format(text))
    window.addstr(row, x, text)
    window.refresh()

# Utility to center an array of strings
def center_text_block(window, text_array):
    logging.debug("Centering a block of text.")
    for i, text in enumerate(text_array):
        center_text(window, text, i)

def main(stdscr):
    logging.debug("Main menu function has started.")

    # Initialize the main screen with border and get the size
    maxY, maxX = stdscr.getmaxyx()
    stdscr.border()
    stdscr.refresh()
    logging.debug("Main window initialized with {}x{} border.".format(maxY, maxX))

    # Create a new window to display the menu
    menu_win = stdscr.derwin(maxY-4, maxX-4, 2, 2)
    logging.debug("Created the menu window.")

    # Array for menu heading
    menu_heading = ["#######################################",
                 "#                                     #",
                 "# Welcome to Lucas's game collection. #",
                 "#                                     #",
                 "#######################################",
                 "",
                 "  Please select a game:                ",
                 ""]

    # Array for menu options    
    menu_options = ["  1. Star Wars                         ",
                 "  2. Game Two                          ",
                 "  3. Game Three                        ",
                 "  4. Exit                              ",
                 ""]

    menu_text = menu_heading + menu_options

    # Define styles used in menu display and selection
    normal_style = curses.A_NORMAL
    highlighted_style = curses.A_REVERSE

#    center_text_block(menu_win, menu_text)
#    logging.debug("Added the menu text.")

    # Handle user selection of menu items
    current_row = 8 # Start at the first menu item
    while True:

        menu_win.clear()
        # Display each option, highlighting the current_row
        for idx, option in enumerate(menu_text, start=0):
            if idx == current_row:
                menu_win.attron(highlighted_style)
                center_text(menu_win, option, idx)
                menu_win.attroff(highlighted_style)
            else:
                center_text(menu_win, option, idx)
        menu_win.refresh()
        logging.debug("Menu text printed and highlighted.")
    
        key = menu_win.getch()
        logging.debug("User pressed key with ASCII value: {} and representation: {}.".format(key, chr(key)))
        logging.debug("Current row is: {}.".format(current_row))

        if chr(key) in ["1", "2", "3", "4"]:
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
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
            elif chr(key) == "3":
                logging.debug("User selected Game Three.")
                clear_screen(stdscr)
                game_three.main(stdscr)
                clear_screen(menu_win)
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
            elif chr(key) == "4":
                logging.debug("User selected Exit.")
                clear_screen(stdscr)
                center_text(stdscr, "Thanks for playing!", maxY//2)
                stdscr.refresh()
                time.sleep(2)
                logging.debug("Exiting program.")
                break 
        elif key == curses.KEY_UP and current_row > 8:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 11:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 8:
                logging.debug("User selected Star Wars.")
                clear_screen(stdscr)
                star_wars.main(stdscr)
                clear_screen(stdscr)
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
            elif current_row == 9:
                logging.debug("User selected Game Two.")
                clear_screen(stdscr)
                game_two.main(stdscr)
                clear_screen(menu_win)
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
            elif current_row == 10:
                logging.debug("User selected Game Three.")
                clear_screen(stdscr)
                game_three.main(stdscr)
                clear_screen(menu_win)
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
            elif current_row == 11:
                logging.debug("User selected Exit.")
                clear_screen(stdscr)
                center_text(stdscr, "Thanks for playing!", maxY//2)
                stdscr.refresh()
                time.sleep(2)
                logging.debug("Exiting program.")
                break 

"""
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
                stdscr.border()
                stdscr.refresh()
                center_text_block(menu_win, menu_text)
        elif chr(key) == "3":
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
"""
        ## TODO: Add a loop to handle resizing of the main window
#        if stdscr.getch() == curses.KEY_RESIZE:
#            maxY, maxX = stdscr.getmaxyx()
#            logging.debug("Main window size changed to {}x{}.".format(maxY, maxX))
#            menu_win.erase()
#            menu_win.refresh()
#        if key == ord("q"):
#            break
