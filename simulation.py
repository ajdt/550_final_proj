#!/usr/bin/env python

class SimulationOptions:
	def __init__(self, num_bots, grid_size, algorithm, bot_init_file, log_level):
		
class Simulation:
	def __init__(self, sim_options, graphics):
		self.sim_options = sim_options
		self.timer = # new timer
		self.bot_manager = # new manager
		self.stop_sim = False # flag to stop simulation

	def initSim():
	def changeTick(new_delta):
	def changeLoggerLevel(new_level):
	def stopSimulation():
	def simulate():


class SimulationRunner:
	def __init__(self, sim_options, num_sims, use_gui=False):
		self.sim_options = sim_options
		self.num_sims = num_sims
		self.use_gui = use_gui
	
	# call only if graphics are required
	def initGraphics():
	# run simulations
	def runSims():
	# listen for user actions in gui
	def listenForUserInput(): 

class Tick:
	# timer class, delta is in seconds/tick
	def __init__(self, delta):

	def setTickDelta(new_delta):
	def nextTick():
		
		
	

		
