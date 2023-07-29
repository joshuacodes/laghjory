#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import time

SPEED = 0.20
DISTANCE = 80
i = 0
SPACES = ""
LINES = ""

print("""\
################################################################################
#                                                                              #
# This is Lucas's special game.                                                #
#                                                                              #
#                       #                          #                           #
#                      ###                        ###                          #
#                       #                          #                           #
#                                                                              #
#                                    #                                         #
#                                   ###                                        #
#                                    #                                         #
#                       #                          #                           #
#                        ##                      ##                            #
#                        #                        #                            #
#                         #                      #                             #
#                          #                    #                              #
#                           ####################                               #
#                                                                              #
################################################################################
""")

print("Hello, Luke.")
print("I am your father")
time.sleep(5)
os.system('cls')

for i in range(0, DISTANCE):
    print(LINES)
    print(SPACES + "        #     #       ")
    print(SPACES + "         #   #        ")
    print(SPACES + "          # #         ")
    print(SPACES + "           #          ")
    print(SPACES + "          # #         ")
    print(SPACES + "         #   #        ")
    print(SPACES + "        #     #       ")

    time.sleep(SPEED)
    os.system('cls')
    SPACES = SPACES + " "
    LINES = LINES + "\n"
