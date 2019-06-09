""" Docstring:
Description: 
    This file is about every individual point, which will form the mine_sweeping grid.
Author: 
Latest Update: May 20, 2019
"""


class point():
    def __init__(self, status, p_type, p_x, p_y):
        self.status = status  # the status, e.g. pressed, marked, etc.
        self.p_type = p_type  # what is in the point, e.g. mine, blank, etc.
        self.p_x = p_x  # the horizental position
        self.p_y = p_y  # the vertical position

    def set_status(self, status):
        self.status = status
    
    def get_status(self):
        return self.status
    
    def set_p_type(self, p_type):
        self.p_type = p_type

    def get_p_type(self):
        return self.p_type
    
    
    

    