####################################################################
# Created by Christopher Primerano on 05-03-2012.                  #
# Copyright (c) 2012 Christopher Primerano. All rights reserved.   #
#                                                                  #
####################################################################

class Queue:
	
	def __init__(self):
		self.queue = []
	
	def enqueue(self, obj):
		self.queue.append(obj)
		
	def front(self):
		return self.queue[0]
	
	def is_empty(self):
		return True if len(self.queue) == 0 else False
	
	def dequeue(self):
		return self.queue.pop(0)
