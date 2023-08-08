import os
import time
import curses
import random
import logging

# Constants
SPEED = 0.20
DISTANCE = 10

# Utility to clear the screen regardless of OS
def clear_screen(window):
    window.clear()
    window.refresh()

def display_explosion(window, y, x):
    # Displays an explosion using slashes, dashes, and pipes around the cursor position.
    try:
        logging.debug("Displaying an explosion at {}, {}.".format(y, x))
        window.addch(int(y) - 1, int(x), '|', curses.color_pair(3))
        window.addch(int(y) + 1, int(x), '|', curses.color_pair(3))
        window.addch(int(y), int(x) - 1, '-', curses.color_pair(3))
        window.addch(int(y), int(x) + 1, '-', curses.color_pair(3))
        window.addch(int(y) - 1, int(x) - 1, '\\', curses.color_pair(3))
        window.addch(int(y) - 1, int(x) + 1, '/', curses.color_pair(3))
        window.addch(int(y) + 1, int(x) - 1, '/', curses.color_pair(3))
        window.addch(int(y) + 1, int(x) + 1, '\\', curses.color_pair(3))
    except curses.error:
        # Handle any errors caused by trying to print outside the screen boundaries
        pass

# TODO: Add a function to greet the player.
#def greet_player(star_wars_win):
#    # Greets the player.
#    star_wars_win.addstr(0, 0, "Luke, I am your father.")
#    star_wars_win.refresh()
#    time.sleep(2)
#    clear_screen()

# TODO: Add a function to print the X-wing fighter or other ASCII art.
#def print_animation(star_wars_win):
#    # Prints a simple ASCII art placeholder.
#    for i in range(DISTANCE):
#        star_wars_win.addstr(i, 0, "     #####     ")
#        star_wars_win.addstr(i+1, 0, "       #       ")
#        star_wars_win.addstr(i+2, 0, "     #####     ")
#        star_wars_win.refresh()
#        time.sleep(SPEED)
#        star_wars_win.clear()

# Randomly generate a number of stars
def generate_stars(star_wars_win):
    maxY, maxX = star_wars_win.getmaxyx()
    minY, minX = star_wars_win.getbegyx()
    logging.debug("Star Wars window size is {}x{}.".format(maxY, maxX))
    star_wars_win.border()
    star_wars_win.refresh()
    
    star_wars_win.keypad(1)
    star_wars_win.timeout(100)

    # Generate a list of stars
    stars = []
    for i in range(0, 10):
        star_x = random.randint(minX+1, maxX-1)
        star_y = random.randint(minY+1, maxY-1)
        stars.append([star_y, star_x])

    # Print the stars
    for star in stars:
        star_wars_win.addch(int(star[0]), int(star[1]), '*', curses.color_pair(2))

    return stars

def interactive_game(star_wars_win):
    # Handles user input and moving the X-wing fighter.
    maxY, maxX = star_wars_win.getmaxyx()
    minY, minX = star_wars_win.getbegyx()
    logging.debug("Star Wars window size is {}x{}.".format(maxY, maxX))
    logging.debug("Star Wars window position is {}x{}.".format(minY, minX))
    star_wars_win.border()
    star_wars_win.refresh()
    
    star_wars_win.keypad(1)
    star_wars_win.timeout(100)

    snk_x = maxX//4
    snk_y = maxY//2

    xwing = [
        [snk_y, snk_x],
    ]

    star_wars_win.addch(int(xwing[0][0]), int(xwing[0][1]), 'X', curses.color_pair(1))

    # Print the stars
    stars = generate_stars(star_wars_win)

    while True:
        next_key = star_wars_win.getch()
        if next_key == -1:
            pass
        else:
            if next_key == ord('h') or next_key == curses.KEY_LEFT:
                # Move the X-wing left but don't let it go off the screen
                if xwing[0][1] > minX+1:
                    logging.debug("X-wing is at {}.".format(xwing[0]))
                    xwing[0][1] -= 1
                    if xwing[0] in stars:
                        display_explosion(star_wars_win, xwing[0][0], xwing[0][1])
                        star_wars_win.addstr(xwing[0][0], xwing[0][1]+3, "You burned up in a star!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        return 1
                elif xwing[0][1] <= minX+1:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('j') or next_key == curses.KEY_DOWN:
                # Move the X-wing down but don't let it go off the screen
                if xwing[0][0] < maxY-2:
                    logging.debug("X-wing is at {}.".format(xwing[0]))
                    xwing[0][0] += 1
                    if xwing[0] in stars:
                        display_explosion(star_wars_win, xwing[0][0], xwing[0][1])
                        star_wars_win.addstr(xwing[0][0], xwing[0][1]+3, "You burned up in a star!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        return 1
                elif xwing[0][0] >= maxY-2:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('k') or next_key == curses.KEY_UP:
                # Move the X-wing up but don't let it go off the screen
                if xwing[0][0] > minY+1:
                    logging.debug("X-wing is at {}.".format(xwing[0]))
                    xwing[0][0] -= 1
                    if xwing[0] in stars:
                        display_explosion(star_wars_win, xwing[0][0], xwing[0][1])
                        star_wars_win.addstr(xwing[0][0], xwing[0][1]+3, "You burned up in a star!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        return 1
                elif xwing[0][0] <= minY+1:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('l') or next_key == curses.KEY_RIGHT:
                # Move the X-wing right but don't let it go off the screen
                if xwing[0][1] < maxX-2:
                    xwing[0][1] += 1
                    if xwing[0] in stars:
                        display_explosion(star_wars_win, xwing[0][0], xwing[0][1])
                        star_wars_win.addstr(xwing[0][0], xwing[0][1]+3, "You burned up in a star!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        return 1
                elif xwing[0][1] >= maxX-2:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('x'): # Exit the game if the user presses 'x'
                return 1

        star_wars_win.addch(int(xwing[0][0]), int(xwing[0][1]), 'X', curses.color_pair(1))
        star_wars_win.refresh()

def main(stdscr):
    # Main function to run the game.

    logging.debug("Main Star Wars function has started.")
    
    # Initialize the new window
    stdscr_maxY, stdscr_maxX = stdscr.getmaxyx()
    stdscr_minY, stdscr_minX = stdscr.getbegyx()
    logging.debug("Main window size is {}x{}.".format(stdscr_maxY, stdscr_maxX))
    logging.debug("Main window position is {}x{}.".format(stdscr_minY, stdscr_minX))

    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # X-Wing
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) # Path and Stars
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)   # Explosion

    # Create a new window to display the game.
    star_wars_win = stdscr.derwin(stdscr_maxY, stdscr_maxX, 0, 0)
    logging.debug("Created the Star Wars window.")

#    greet_player(star_wars_win)
#    print_animation(star_wars_win)
    interactive_game(star_wars_win)

if __name__ == "__main__":
    curses.wrapper(main)
