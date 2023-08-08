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

def display_shield(window, y, x):
    # Displays a shield around the X-Wing at the motherhsip.
    try:
        logging.debug("Displaying the shield at {}, {}.".format(y, x))
        window.addch(int(y) - 1, int(x), '-', curses.color_pair(6))
        window.addch(int(y) + 1, int(x), '-', curses.color_pair(6))
        window.addch(int(y), int(x) - 1, '(', curses.color_pair(6))
        window.addch(int(y), int(x) + 1, ')', curses.color_pair(6))
        window.addch(int(y) - 1, int(x) - 1, '0', curses.color_pair(6))
        window.addch(int(y) - 1, int(x) + 1, '0', curses.color_pair(6))
        window.addch(int(y) + 1, int(x) - 1, '0', curses.color_pair(6))
        window.addch(int(y) + 1, int(x) + 1, '0', curses.color_pair(6))
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

    while True:

        # Handles user input and moving the X-wing fighter.
        maxY, maxX = star_wars_win.getmaxyx()
        minY, minX = star_wars_win.getbegyx()
        logging.debug("Star Wars window size is {}x{}.".format(maxY, maxX))
        logging.debug("Star Wars window position is {}x{}.".format(minY, minX))
        star_wars_win.border()
        star_wars_win.refresh()
        
        star_wars_win.keypad(1)
        star_wars_win.timeout(100)

        # Initialize starting positions
        xwing = [[(maxY//4), (maxX//4)]]
        tie = [[maxY*3//4, maxX*3//4]]
        mothership = [[random.randint(minY+1, maxY-1), random.randint(minX+1, maxX-1)]]
        
        star_wars_win.addch(int(xwing[0][0]), int(xwing[0][1]), 'X', curses.color_pair(1))
        star_wars_win.addch(int(tie[0][0]), int(tie[0][1]), '8', curses.color_pair(4))
        star_wars_win.addch(int(mothership[0][0]), int(mothership[0][1]), 'M', curses.color_pair(5))

        # Print the stars
        stars = generate_stars(star_wars_win)

        exit_key = star_wars_win.getch()

        while True:

            # Move the TIE fighter closer to the X-wing
            if tie[0][0] > xwing[0][0]:
                tie[0][0] -= 1
            elif tie[0][0] < xwing[0][0]:
                tie[0][0] += 1
            if tie[0][1] > xwing[0][1]:
                tie[0][1] -= 1
            elif tie[0][1] < xwing[0][1]:
                tie[0][1] += 1

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
                            break
                    elif xwing[0][1] <= minX+1:
                        star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        break
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
                            break
                    elif xwing[0][0] >= maxY-2:
                        star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        break
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
                            break
                    elif xwing[0][0] <= minY+1:
                        star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        break
                elif next_key == ord('l') or next_key == curses.KEY_RIGHT:
                    # Move the X-wing right but don't let it go off the screen
                    if xwing[0][1] < maxX-2:
                        xwing[0][1] += 1
                        if xwing[0] in stars:
                            display_explosion(star_wars_win, xwing[0][0], xwing[0][1])
                            star_wars_win.addstr(xwing[0][0], xwing[0][1]+3, "You burned up in a star!")
                            star_wars_win.refresh()
                            time.sleep(2)
                            break
                    elif xwing[0][1] >= maxX-2:
                        star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                        star_wars_win.refresh()
                        time.sleep(2)
                        break
                elif next_key == ord('x'): # Exit the game if the user presses 'x'
                    break

            star_wars_win.addch(int(xwing[0][0]), int(xwing[0][1]), 'X', curses.color_pair(1))
            star_wars_win.addch(int(tie[0][0]), int(tie[0][1]), '8', curses.color_pair(4))
            star_wars_win.refresh()
            
            # Check for a collision between the TIE fighter and a star
            if tie[0] in stars:
                display_explosion(star_wars_win, tie[0][0], tie[0][1])
                star_wars_win.addstr(tie[0][0], tie[0][1]+3, "The TIE fighter crashed into a star!")
                star_wars_win.refresh()
                time.sleep(2)
                star_wars_win.clear()
                break

            # Check for a collision between the X-wing and the TIE fighter
            if xwing[0] == tie[0]:
                display_explosion(star_wars_win, xwing[0][0], xwing[0][1])
                star_wars_win.addstr(xwing[0][0], xwing[0][1]+3, "You were shot down by a TIE fighter!")
                star_wars_win.refresh()
                time.sleep(2)
                star_wars_win.clear()
                break

            # Check for a collision between the X-wing and the Mothership
            if xwing[0] == mothership[0]:
                display_shield(star_wars_win, xwing[0][0], xwing[0][1])
                star_wars_win.addstr(maxY // 2, (maxX // 2) - 10, "You reached safety!")
                star_wars_win.refresh()
                time.sleep(2)
                star_wars_win.clear()
                break

            star_wars_win.refresh()

        if exit_key == ord('X') or next_key == ord('x'):
            return 1

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
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # X-Wing
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Path and Stars
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_YELLOW)    # Explosion
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_GREEN) # TIE Fighter
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)    # Mothership
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_CYAN)   # Shield

    # Create a new window to display the game.
    star_wars_win = stdscr.derwin(stdscr_maxY-4, stdscr_maxX, 0, 0)
    logging.debug("Created the Star Wars window.")

    # Create an instructions window below the main game window
    instructions_win = stdscr.derwin(3, stdscr_maxX, stdscr_maxY-4, stdscr_minX)
    logging.debug("Created the instructions window.")
    instructions_win.border(0)
    instructions_win.addstr(1, 2, "Move with arrow keys or hjkl. Press 'X' to exit.")
    instructions_win.refresh()

#    greet_player(star_wars_win)
#    print_animation(star_wars_win)
    interactive_game(star_wars_win)

if __name__ == "__main__":
    curses.wrapper(main)
