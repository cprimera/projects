#!/usr/local/bin/python 
from PIL import Image, ImageDraw
import random
import math
from Queue import *

class PathDetails:
    def __init__(self, dist=None, prev=None):
        self.dist = dist # the distance from this pixel back to source
        self.prev = prev # the coordinates of a previous pixel on a path back to source

class ObstacleAvoider:
    def __init__(self, source=None, dest=None, image=None):
        ''' An instance of this, determines whether there is a path from self._source to self._dest which avoids
        all white pixels. It uses the Breadth First Search algorithm to determine a path from any self._reachable pixel
        back to self._source. If no image is supplied, a random image is created, with random source and dest.'''
        if image!=None:
            self._source=source
            self._dest=dest
            self._image=image
        else:
            (self._source, self._dest, self._image)=self._create_random_obstacle_image()

        (self._width, self._height)=self._image.size
        self._pix=self._image.load() # for quicker access to the pixels in self._image

        self._reachable = {} # A dictionary of PathDetails. 
        # self._reachable[(x,y)] == None, if (x,y) is not reachable from self._source
        # self._reachable[(x,y)] is a PathDetails, otherwise

    def _create_random_obstacle_image(self, width=400, height=400, obstacle_dim=60, num_obstacles=140):
        ''' return (source, dest, image) where source and dest are (x,y) coordinates of a random source in 
        randomly generated obstacle image image. image has the specified width and height. It has 
        approximately num_obstacles obstacles in it. Each fit in a obstacle_dim by obstacle_dim box.
        '''
        image = Image.new ( "RGB", (width,height), "#000" )
        draw = ImageDraw.Draw ( image ) # use this to draw in an image 
        for i in range(num_obstacles/2):
            p1=(random.randint(0,width), random.randint(0,height))
            p2=(p1[0]+random.randint(0,obstacle_dim), p1[1]+random.randint(0,obstacle_dim))
            box=[p1,p2]
            draw.rectangle(box, "#fff")
        
        for i in range(num_obstacles/2):
            p1=(random.randint(0,width), random.randint(0,height))
            p2=(p1[0]+random.randint(0,obstacle_dim), p1[1]+random.randint(0,obstacle_dim))
            box=[p1,p2]
            draw.ellipse(box, "#fff")
        
        draw.rectangle([(0,0),(width-1,height-1)])
    
        source=(x,y)=(random.randint(0,width-1), random.randint(0,height-1))
        draw.rectangle([(x-5,y-5),(x+5,y+5)],"#0f0")
        
        dest=(x,y)=(random.randint(0,width-1), random.randint(0,height-1))
        draw.rectangle([(x-5,y-5),(x+5,y+5)],"#f00")
        return (source, dest, image)

    def _get_neighbours(self, (x,y)):
        '''  return (x,y)'s neighbouring pixels as determined by self._pix (same as self._image).
        A white pixel has no neighbours. A white pixel can not be a neighbour.
        '''
        
        neighbours=[] # a list of all neighbouring, non-white pixels, by (x,y) coordinate

        # A white pixel has no neighbours
        if self._pix[x, y]==(255,255,255):
            return neighbours

        ''' determine all of the neighbours of (x,y) 
        that is, of the 8 pixels immediately surrounding, (x,y) we return
        the coordinates of those that are not white. Of course, coordinates must be inside 
        the image.
        '''
        # YOUR CODE GOES HERE
        for y_val in range(-1, 2):
            for x_val in range(-1, 2):
                # make sure that the neighbour is inside of the image
                if x + x_val >= 0 and x + x_val <= self._image.getbbox()[2] and y + y_val >= 0 and y + y_val <= self._image.getbbox()[3]:
                    if self._pix[x + x_val, y + y_val] != (255, 255, 255):
                        neighbours.append((x + x_val, y + y_val))


        return neighbours

    def _get_snapshot(self, frontier, draw_reachable, draw_path):
        ''' return a snapshot of the bfs algorithm in progress.
        if frontier is supplied, we draw it in yellow.
        if draw_reachable is True, then we draw all of the points reachable from s so far in blue
        if draw_path is True, then we draw a path from self._dest back to self._source in green'''

        imc=self._image.copy()
        drawimc = ImageDraw.Draw ( imc )

        
        if draw_reachable:
            # YOUR CODE GOES HERE
            for values in self._reachable.keys():
                drawimc.point(values, "#00f")
            

        # YOUR CODE GOES HERE (Draw the frontier if given one)
        for pixel in frontier:
            drawimc.point(pixel, "#ff0")

        (x,y)=self._source
        drawimc.rectangle([(x-5,y-5),(x+5,y+5)],"#0f0")
        (x,y)=self._dest
        drawimc.rectangle([(x-5,y-5),(x+5,y+5)],"#f00")

        if draw_path:
            # YOUR CODE GOES HERE
            drawimc.point(self._dest, "#ccc")
            temp = self._reachable[self._dest].prev
            while temp != self._source:
                drawimc.point(temp, "#ccc")
                temp = self._reachable[temp].prev
            drawimc.point(self._source, "#ccc")

        return imc 

    def _save_snapshot(self, frontier, draw_reachable, draw_path, snap_count):
        ''' return a snapshot of the bfs algorithm in progress, also saving it to images/snapshot{snap_count}.gif '''
        imc = self._get_snapshot(frontier, draw_reachable, draw_path)
        imc.save("images/snapshot%03d.gif" % snap_count)
        return imc
        
    def bfs(self):
        ''' 
        perform a breadth first search of the image for self._dest, from self._source, filling in self._reachable on the way. 
        additionally, snapshots are taken and stored for later generation of a movie. Our convention is that white pixels
        in the image represent obstacles, so paths can not go over white pixels.
        '''

        self._reachable={} # if you are not in this dictionary, you are not yet known to be reachable from self._source
        self._reachable[self._source]=PathDetails(0, None)
    
        q=Queue()
        q.enqueue(self._source)

        min_dist=0
        snap_count = 0
        end = q.front()
        count = 0
    
        # YOUR CODE GOES HERE
        previous = self._source

        while not q.is_empty() and q.front() != self._dest:
            neighbours = self._get_neighbours(q.front())
            # set initial distance of previous neighbour
            distance = self._reachable[previous].dist + math.sqrt(((q.front()[0] - previous[0]) ** 2) + ((q.front()[1] - previous[1]) ** 2))
            for neighbour in neighbours:
                try:
                    # if the neighbour has already been visted, then update distance if needed
                    self._reachable[neighbour]
                    if distance >= self._reachable[neighbour].dist:
                        previous = neighbour
                        distance = self._reachable[neighbour].dist
                except KeyError:
                    # if the neighbour has not been visited and in not already in the queue,
                    # then add it to the queue
                    if neighbour not in q.queue:
                        q.enqueue(neighbour)
            # mark current pixel as visited and set its PathDetails
            self._reachable[q.front()] = PathDetails(self._reachable[previous].dist + math.sqrt(((q.front()[0] - previous[0]) ** 2) + ((q.front()[1] - previous[1]) ** 2)), previous)
            # if we have gone through the entire queue twice then we want to save a snapshot
            if end == q.front():
                if count % 2 == 0:
                     im = self._save_snapshot(q.queue, True, False, snap_count)
                     snap_count += 1
                count += 1
                end = q.queue[-1]
            q.dequeue()
        
        # if we have not finished the queue then we must have found the destination point
        # so we will save a snapshot with the path to the destination visible
        if not q.is_empty():
            self._reachable[q.front()] = PathDetails(self._reachable[previous].dist + math.sqrt(((q.front()[0] - previous[0]) ** 2) + ((q.front()[1] - previous[1]) ** 2)), previous)
            im = self._save_snapshot(q.queue, True, True, snap_count)
            snap_count += 1

       
oa=ObstacleAvoider()
oa.bfs()
