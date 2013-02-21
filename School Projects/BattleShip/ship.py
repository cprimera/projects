from PIL import Image, ImageDraw

class Ship:
    def __init__(self, start=None, size=0, orientation=None, points=[]):
        self._start = start
        self._size = int(size)
        if orientation == 0 or orientation == 1:
            self._orientation = orientation
        else:
            self._orientation = None
        self._hits = [0] * self._size
        self._points = points
        
    def get_points(self):
        return self._points
        
    def set_points(self, points):
        if len(points) == self._size and type(points) == list:
            self._points = points
            return True
        return False
    
    def get_hits(self):
        return self._hits
    
    def set_hits(self, hits):
        if len(hits) == self._size and type(hits) == list:
            self._hits = hits
            return True
        return False
        
    def get_orientation(self):
        return self._orientation
        
    def set_orientation(self, orientation):
        if orientation >= 0 and orientation <= 1:
            self._orientation = orientation
            return True
        return False
    
    def get_size(self):
        return self._size   
    
    def set_size(self, size=0):
        if size >= 2 and size <= 5:
            self._size = size
            return True
        else:
            self._size = 0
            return False
        
    def get_start(self):
        return self._start
        
    def set_start(self, start):
        self._start = start
        return True
    
    def is_hit(self, point):
        # check if a point is a hit on the ship, if the ship is sunk no point can be a hit
        if self.is_sunk():
            return False
        #check to see if point is under the ship if so mark point as hit
        for p in self._points:
            if point == p:
                p.set_state(2)
                index = self._points.index(p)
                self._hits[index] = 1
                if enhancements and self.is_sunk():
                    print "You sunk my ship\n"
                return True
        return False
                
    def is_sunk(self):
        # check if a ship has been sunk
        if self._hits == [1] * self._size:
            # if the ship has been hit at all points it is sunk and mark the state of the points
            for point in self._points:
                point._state = 3
        return self._hits == [1] * self._size
    
    def draw_ship(self, image, draw):
        # draw a ship on image
        for p in self._points:
            p.draw_point(image, draw, True)
        
        return image
        
    def __str__(self):
        output = "["
        for point in self._points:
            output += str(point) + " "
        output += "]"
        return output
