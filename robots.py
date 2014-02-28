#!/usr/bin/env python

# base algorithm class, extend to have custom algorithms
class Algorithm:

	# TODO: implement something like enums for states
	def __init__(self, robot):
		# algo initialization code
		self.robot = # robot needed to access state and position values

	# perform a single round worth of actions
	# return a tuple including new state and position if movement is made
	def run(self, position, local_view, state):

class BotManager:
	def __init__(self, sim_options):
		self.global_view # create new global view
		self.bots # list of bots
		self.logger
	
	# return bot config data from bot file
	def parseBotInitFile(file_name):

	# use sim_options to do this
	def initBots():
	def getRandStartPos():
	def getRandShape():
	def initRandStartPos():
	def initRandShape():
	def updateGlobalView():
	def drawBots():
	# boolean, indicates all bots are done moving
	def done(): 
	# runs robot actions for one tick of time
	def tick(): 
	def setLoggerLevel():

# contains config info for a bot
# initialized from input file
# TODO: maybe pass string to botconfig, and have it parse the input?
class BotConfig:
	def __init__(self, string)
		# data fields are: move_delta, compute_delta and others as needed

	# return a tuple with parsed input
	def parseOptions(self, string):

class Robot:
	# NOTE: algorithm is a class name, Robot must instantiate it
	def __init__(self, algorithm, bot_config, position, target_shape):
		self.algorithm, bot_data = algorithm(), bot_data
		self.target_shape,
		# initialize local view and algorithm
		
	def tickOccurred():
	def drawBot():
	def GlobalPosition(): # return the global position, should we have this?

	# used by BotManager to notify robot of a collision. Method updates
	# position and sets state to 'Collision'
	def collisionOccurred(position):

		

