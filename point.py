""" Docstring:
Description: 
    This file is about every individual point, which will form the mine_sweeping grid.
Author: 
Latest Update: May 20, 2019
"""


class point():
    def __init__(self, status, p_x, p_y, p_type):
        self.status = status  # The status, e.g. pressed, marked, etc.
        self.p_x = p_x  # The horizental position
        self.p_y = p_y  # The vertical position
        self.p_type = p_type  # What is in the point, e.g. mine, blank, etc.
    
    def change_status(self, click_type): # ! Code structure to be determined
        if click_type == 'Left':  # If the left button of the mouse is pressed ! value & data type to be determined
            # Code here #
        if click_type == 'Right': # If the right button of the mouse is pressed ! value & data type to be determined
            # Code here #

        """if status == ''  #
            pass"""


    

