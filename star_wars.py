import os
import time
import curses

# Constants
SPEED = 0.20
DISTANCE = 10

def clear_screen():
    """Clears the console screen regardless of OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def greet_player(stdscr):
    """Greets the player."""
    stdscr.addstr(0, 0, "Luke, I am your father.")
    stdscr.refresh()
    time.sleep(2)
    clear_screen()

def print_animation(stdscr):
    """Prints a simple ASCII art placeholder."""
    for i in range(DISTANCE):
        stdscr.addstr(i, 0, "     #####     ")
        stdscr.addstr(i+1, 0, "       #       ")
        stdscr.addstr(i+2, 0, "     #####     ")
        stdscr.refresh()
        time.sleep(SPEED)
        stdscr.clear()
        
def interactive_game(stdscr):
    """Handles user input and moving the X-wing fighter."""
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    w.keypad(1)
    w.timeout(100)

    snk_x = sw//4
    snk_y = sh//2

    xwing = [
        [snk_y, snk_x],
    ]

    w.addch(int(xwing[0][0]), int(xwing[0][1]), '^')

    while True:
        next_key = w.getch()
        if next_key == -1:
            pass
        else:
            if next_key == ord('h'):
                xwing[0][1] -= 1
            elif next_key == ord('j'):
                xwing[0][0] += 1
            elif next_key == ord('k'):
                xwing[0][0] -= 1
            elif next_key == ord('l'):
                xwing[0][1] += 1
            elif next_key == ord('x'): # Exit the game if the user presses 'x'
                return 1

        w.addch(int(xwing[0][0]), int(xwing[0][1]), '^')
        w.refresh()

def main(stdscr):
    """Main function to run the game."""
    greet_player(stdscr)
    print_animation(stdscr)
    interactive_game(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
