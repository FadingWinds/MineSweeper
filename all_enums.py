""" Docstring:
Description: 
    This file is about all the enums that would be used in the game.
Author: 
Latest Update: May 20, 2019
"""

from enum import Enum

class game_type(Enum): 
    # The overall difficulty of the game (easy/normal/hard/etc.)
    # details

class point_type(Enum):
    NUMBER = 1 # ? Should 1-9 be listed in the enum?
    BLANK = 2
    MINE = 3

class point_status(Enum):
    UNPRESSED = 1
    PRESSED = 2
    MARKED = 3
    QUESTIONED = 4
