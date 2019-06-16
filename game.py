""" Docstring:
Description: Game class
Author: 
Date:April 01, 2019
"""

# module


# parameters


# classes
class Game():
    def __init__(self):
        """ game init """
        pass
    
    def start(self):
        """ start the game """
        while self.status():
            self.run_once()
            
    
    def status(self):
        """ decide if the game ends """
        pass
    
    def run_once(self):
        """ one round of the game """
        self.visualize()
    
    def visualize(self):
        """ visualize the game """
        pass




# functions
def test_init():
    """ test initialization of a mine """
    pass

def test_game():
    """ test of the game """
    test_init()
    pass

# main
if __name__ == "__main__":
    test_game()
