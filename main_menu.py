import time
import curses
import curses.textpad

import star_wars
import game_two

def clear_screen(stdscr):
    """Clears the console screen regardless of OS."""
    stdscr.clear()
    stdscr.refresh()

def print_intro(stdscr):
    """Prints the game's intro screen."""
    intro = """
    ################################################################################
    #                                                                              #
    # Welcome to Lucas's special game collection.                                  #
    #                                                                              #
    ################################################################################
    
"""
    stdscr.addstr(intro)
    stdscr.refresh()

def main_menu(stdscr):
    """Displays the main menu and processes user selection."""
    while True:
        print_intro(stdscr)

        stdscr.addstr("    Please select a game:\n")
        stdscr.addstr("    1. Star Wars\n")
        stdscr.addstr("    2. Game Two\n")
        stdscr.addstr("    3. Exit\n\n    ")

        stdscr.refresh()

        # Get the current cursor position
        y, x = stdscr.getyx()

        # Create a new window for the input field
        input_win = curses.newwin(1, 10, y+1, 0)

        # Create a Textbox in the new window
        textbox = curses.textpad.Textbox(input_win)

        # Let the user edit until Enter is struck
        choice = textbox.edit().strip()

        if choice.strip() == "1":
            star_wars.main(stdscr)
        elif choice.strip() == "2":
            game_two.main(stdscr)
        elif choice.strip() == "3":
            stdscr.addstr("Thanks for playing, goodbye!")
            stdscr.refresh()
            time.sleep(2)
            return 0
        else:
            stdscr.addstr("Invalid choice, please try again.")
            stdscr.refresh()
            time.sleep(2)
        clear_screen(stdscr)
