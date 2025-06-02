import numpy as np

class Game():

    button_size: tuple[int, int] = (120,60)
    button_relative_position: tuple[float, float] = (0.5,0.5)
    
    def choose_next_position(self):
        x: float = np.random.random() 
        y: float = np.random.random() 

        self.button_relative_position= (x,y)

