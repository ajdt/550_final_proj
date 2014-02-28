import planar # 3rd party library to be obtained later
class LocalView:
	# rotation = 0-360 deg, translation is (x,y) coord, relfection is over y axis (True/False)
	def __init__(self, rotation, translation, reflection):
		self.transformations = [] # list of transformations based on inputs.

	# local view of a point or list of points
	def translateToLocal(points):
	def translateToGlobal(points):
	
	# udpate local view based on global view
	def updateView(global_view):

	# return (x,y) coord of other bots
	def getBotLocations():

	# return location of bot with this view
	def getLocalPosition():

	# methods to return what is visible by the robot?

class GlobalView:
	def __init__(self, start_position):
	
	# returns None if successful, or list of collisions if
	# they occur. Each collision specifies colliding objects
	# and the new positions for the bots involved
	# NOTE: old_pos and new_pos are position lists index i
	# refers to robot i for both lists
	def updatePosition( old_pos, new_pos):

	def collisionOccurred():
		
		
