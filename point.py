""" Docstring:
Description: 
    This file is about every individual point, which will form the mine_sweeping grid.
Author: 
Latest Update: May 20, 2019
"""
from all_enums import point_status, point_type

# NOTE: I changed point() to Point for naming convension.
class Point():
    def __init__( self, p_x, p_y, status=point_status.UNPRESSED, p_type=point_type.BLANK):
        self.status = status  # the status, e.g. pressed, marked, etc.
        self.p_type = p_type  # what is in the point, e.g. mine, blank, etc.
        self.p_x = p_x  # the horizental position
        self.p_y = p_y  # the vertical position
        self.surround_mine_num = 0

    def set_status( self, status):
        self.status = status
    
    def get_status( self):
        return self.status
    
    def set_p_type( self, p_type):
        self.p_type = p_type

    def get_p_type( self):
        return self.p_type
    
    @classmethod
    def create_empty_board( cls, x_lim, y_lim):
        board = []
        for i in range( x_lim):
            column = [] # x is horizontal, so each x is a column
            for j in range( y_lim):
                column.append( cls( i, j))
            board.append(column)
        return board

    
    
    

    