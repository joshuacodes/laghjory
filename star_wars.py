import os
import time
import curses
import logging

# Constants
SPEED = 0.20
DISTANCE = 10

def clear_screen():
    # Clears the console screen regardless of OS.
    os.system('cls' if os.name == 'nt' else 'clear')

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
        
def interactive_game(star_wars_win):
    # Handles user input and moving the X-wing fighter.
    maxY, maxX = star_wars_win.getmaxyx()
    minY, minX = star_wars_win.getbegyx()
    logging.debug("Star Wars window size is {}x{}.".format(maxY, maxX))
    star_wars_win.border()
    star_wars_win.refresh()
    
    star_wars_win = curses.newwin(maxY, maxX, 0, 0)

    star_wars_win.keypad(1)
    star_wars_win.timeout(100)

    snk_x = maxX//4
    snk_y = maxY//2

    xwing = [
        [snk_y, snk_x],
    ]

    star_wars_win.addch(int(xwing[0][0]), int(xwing[0][1]), '^')

    while True:
        next_key = star_wars_win.getch()
        if next_key == -1:
            pass
        else:
            if next_key == ord('h') or next_key == curses.KEY_LEFT:
                # Move the X-wing left but don't let it go off the screen
                if xwing[0][1] > minX+1:
                    xwing[0][1] -= 1
                elif xwing[0][1] <= minX+1:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('j') or next_key == curses.KEY_DOWN:
                # Move the X-wing down but don't let it go off the screen
                if xwing[0][0] < maxY-1:
                    xwing[0][0] += 1
                elif xwing[0][0] >= maxY-1:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('k') or next_key == curses.KEY_UP:
                # Move the X-wing up but don't let it go off the screen
                if xwing[0][0] > minY+1:
                    xwing[0][0] -= 1
                elif xwing[0][0] <= minY+1:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('l') or next_key == curses.KEY_RIGHT:
                # Move the X-wing right but don't let it go off the screen
                if xwing[0][1] < maxX-1:
                    xwing[0][1] += 1
                elif xwing[0][1] >= maxX-1:
                    star_wars_win.addstr(maxY//2, maxX//2, "You have reached the edge of the galaxy!")
                    star_wars_win.refresh()
                    time.sleep(2)
                    return 1
            elif next_key == ord('x'): # Exit the game if the user presses 'x'
                return 1

        star_wars_win.addch(int(xwing[0][0]), int(xwing[0][1]), '^')
        star_wars_win.refresh()

def main(stdscr):
    # Main function to run the game.

    logging.debug("Main Star Wars function has started.")
    
    # Initialize the new window
    maxY, maxX = stdscr.getmaxyx()
    minY, minX = stdscr.getbegyx()
    logging.debug("Main window size is {}x{}.".format(maxY, maxX))
    logging.debug("Main window position is {}x{}.".format(minY, minX))
#    stdscr.border()
#    stdscr.refresh()

    # Create a new window to display the game.
    star_wars_win = stdscr.derwin(maxY, maxX, 0, 0)
    logging.debug("Created the Star Wars window.")

#    greet_player(star_wars_win)
#    print_animation(star_wars_win)
    interactive_game(star_wars_win)

if __name__ == "__main__":
    curses.wrapper(main)
