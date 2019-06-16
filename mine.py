""" Docstring:
Description: mine class
Author: 
Date:April 01, 2019
"""

# module
import numpy as np

from point import Point
from all_enums import point_type, point_status
# parameters


# classes
class Settings(object):
    def __init__(self):
        self.level = None
        self.x_lim = None
        self.y_lim = None
        self.mine_num = None


class Mine(object):
    def __init__( self, level='easy'):
        """ Mine init """
        self.level = level
        level_settings = self.load_settings( self.level)
        self.mine_num = level_settings.mine_num
        self.mine_left = self.mine_num
        self.x_lim = level_settings.x_lim
        self.y_lim = level_settings.y_lim
        # TODO at June 15, 2019: how are we going to store user defined settings of the level
        # is there a design pattern of saving a setting file and load it?
        self.board = Point.create_empty_board(self.x_lim, self.y_lim)
        self.mine_poses = []
        self.generate_mines()
        
        
    def load_settings( self, level):
        filehandler = open( './settings.txt', 'r')
        lines = filehandler.readlines()
        started = False
        settings = Settings()
        settings.level = level
        for line in lines:
            chars = line.split()
            if chars[0] == 'level:':
                if False == started and chars[1] == level:
                    started = True
                else:
                    break
            if True == started:
                if chars[0] == 'x_lim:':
                    settings.x_lim = int(chars[1])
                elif chars[0] == 'y_lim:':
                    settings.y_lim = int(chars[1])
                elif chars[0] == 'mine_num:':
                    settings.mine_num = int(chars[1])
        return settings

    def generate_mines( self):
        """ create random mines and assign the point numbers """
        mine_ids = np.random.permutation(np.arange(self.x_lim*self.y_lim))[0:self.mine_num]
        for mine_id in mine_ids:
            rol = mine_id % self.y_lim
            col = int(mine_id / self.y_lim)
            self.board[col][rol].p_type = point_type.MINE
            self.mine_poses.append([col, rol])
        
        for mine_pos in self.mine_poses:
            print(mine_pos[0], mine_pos[1])
            for i in range(max(mine_pos[0]-1, 0), min(mine_pos[0]+2, self.x_lim)):
                for j in range(max(mine_pos[1]-1, 0), min(mine_pos[1]+2, self.y_lim)):
                    self.board[i][j].surround_mine_num += 1
                    if not (i == mine_pos[0] and j == mine_pos[1]) and self.board[i][j].p_type == point_type.BLANK:
                        self.board[i][j].p_type = point_type.NUMBER

    
    def vis_debug( self, displayType='All'):
        """ visualization tools, with mine position, thus only for debugging """
        if displayType == 'All':
            print("******* Mine *********")
            for j in range(self.y_lim):
                print('*', end=' ')
                for i in range(self.x_lim):
                    if self.board[i][j].p_type == point_type.BLANK:
                        print(' ', end=' ')
                    elif self.board[i][j].p_type == point_type.MINE:
                        print('B', end=' ')
                    elif self.board[i][j].p_type == point_type.NUMBER:
                        print(self.board[i][j].surround_mine_num, end=' ')
                print('*')
            print("***********************")
        elif displayType == 'mine':
            print("******* Mine *********")
            for j in range(self.y_lim):
                print('*', end=' ')
                for i in range(self.x_lim):
                    if self.board[i][j].p_type == point_type.MINE:
                        print('B', end=' ')
                    else:
                        print(' ', end=' ')
                print('*')
            print("***********************")
        elif displayType == 'number':
            print("******* Mine *********")
            for j in range(self.y_lim):
                print('*', end=' ')
                for i in range(self.x_lim):
                    if self.board[i][j].p_type == point_type.NUMBER:
                        print(self.board[i][j].surround_mine_num, end=' ')
                    else:
                        print(' ', end=' ')
                print('*')
            print("***********************")
    
    def vis( self):
        """ visualization tools for playing """
        print("********* Mine *********")
        for j in range(self.y_lim):
            print('*', end=' ')
            for i in range(self.x_lim):
                if self.board[i][j].status == point_status.UNPRESSED:
                    print('-', end=' ')
                elif self.board[i][j].status == point_status.MARKED:
                    print('M', end=' ')
                elif self.board[i][j].status == point_status.QUESTIONED:
                    print('?', end=' ')
                else:
                    if 0 == self.board[i][j].surround_mine_num:
                        print('-', end=' ')
                    else:
                        print(self.board[i][j].surround_mine_num, end=' ')
            print('*')
        print("***********************")



# functions


def mine_test():
    """ testing of mine """
    mine = Mine()
    mine.vis()
    mine.vis_debug()
    mine.vis_debug('mine')
    mine.vis_debug('number')
    pass


# main
if __name__ == "__main__":
    mine_test()
