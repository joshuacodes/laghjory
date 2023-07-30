#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import curses
import argparse
import logging
import main_menu

def main(stdscr, log_file, log_level):

    # Configure the logging module
    logging.basicConfig(filename=args.log_file, level=log_level, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    height, width = stdscr.getmaxyx()
    stdscr.addstr("The terminal is {}x{} characters".format(width, height))
    stdscr.refresh()

    main_menu.main_menu(stdscr)

# Call the main function if the script is run directly
if __name__ == "__main__":
    # Create the argument parser and add arguments
    parser = argparse.ArgumentParser(description="Start the game")
    parser.add_argument('--log-file', type=str, help='the name of the log file', default='testing.log')
    parser.add_argument('--log-level', type=str, help='the logging level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='DEBUG')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Convert log level to the corresponding logging level
    log_level = getattr(logging, args.log_level.upper())

    curses.wrapper(main, args.log_file, log_level)