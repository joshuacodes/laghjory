#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import curses
import argparse
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler
import main_menu

def main(log_file, log_level):

    # Configure the logging module
    handler = logging.handlers.RotatingFileHandler(filename=log_file, maxBytes=1*1024*1024, backupCount=10)
    logging.basicConfig(handlers=[handler], level=log_level, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug("")
    logging.debug("NEW GAME SESSION STARTED")
    logging.debug("")

    # Initialize curses and start the main menu loop
    curses.wrapper(main_menu.main)

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

    # Call the main function
    main(args.log_file, log_level)
