from PIL import Image, ImageDraw

class Point:
    def __init__(self, state, point):
        if state >=0 and state <= 4:
            self._state = state
        else:
            self._state = -1
        self._point = point
        
    def get_point(self):
        return self._point
        
    def set_point(self, point):
        if type(point) == tuple:
            self._point = point
            return True
        return False
            
    def get_state(self):
        # State meanings:
        # 0 -> the point has neither been hit nor missed
        # 1 -> the point has a miss
        # 2 -> the point has a hit
        # 3 -> the ship at this point has been sunk
        # 4 -> there is an unhit ship here
        return self._state
        
    def set_state(self, state):
        if state >= 0 and state <= 4:
            self._state = state
            return True
        return False
        
    def draw_point(self, image, draw, draw_ships):
        # draw the point onto image, colors are set differently depending on the state of the point
        # draw_ships determines whether the ships should be shown or not
        # blue for a state of 0 (water)
        # white for a state of 1 (miss)
        # red for a state of 2 (hit)
        # black for a state of 3 (sunk)
        # grey for a state of 4 (ship) Note: only if ships are being drawn, otherwise blue like state 0
        p1 = (self._point[0] * 11, self._point[1] * 11)
        p2 = ((self._point[0] * 11) + 10, (self._point[1] * 11) + 10)
        box = [p1,p2]
        if self._state == 0:
            color = "#00f"
        elif self._state == 1:
            color = "#fff"
        elif self._state == 2:
            color = "#f00"
        elif self._state == 3:
            color = "#000"
        elif self._state == 4 and draw_ships:
            color = "#ccc"
        else:
            color = "#00f"
        draw.rectangle(box, color)
        
    def __eq__(self, other):
        return self._point == other.get_point()
        
    def __str__(self):
        if self._state == 0:
            return "0"
        elif self._state == 1:
            return "."
        elif self._state == 2:
            return "X"
        elif self._state == 3:
            return "_"
        elif self._state == 4:
            return "0"
        else:
            return "!"
