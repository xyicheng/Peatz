# common.py
# Created by Sofiane Taleb on 16/09/2015.

from core.core import Object

class Status(Object):
	
	def __init__(self, code=0, error=''):
		self.code = code
		self.error = error
		
class Event(Object):
	pass;