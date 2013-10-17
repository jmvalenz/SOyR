from OS import OS #Class OS from OS.py
from Parser import Parser
import time
from Process import *
from operator import attrgetter
import os

#Simulator
class Simulator:
	#Constructor
	def __init__(self, eventsList):
		self.simTime = 0 #Operating System 
		self.oSystem = OS() #Simulation time
		self.eventsList =  eventsList #Contains the processes that will arrive to the OS during the simulation

	def Cls(self):
		os.system(['clear','cls'][os.name == 'nt'])

	#Executes the simulation
	def StartSimulation(self):
		#Iterates until all processes are completed
		while(len(self.eventsList) != 0 or not self.oSystem.AllFinished()):
			self.oSystem.RunAQuantum() #Signal to execute next quantum
			# self.Cls()
			print "--------------------------"
			self.oSystem.TopFunction() #Show the processes being executed
			while(True):
				if(len(self.eventsList) != 0 and self.eventsList[0].GetFecha() == self.simTime):
					aux = self.eventsList.pop(0)
					self.oSystem.ProcessRequest(aux)
				else:
					break
			time.sleep(0.1) #Pause
			self.simTime += 1 #Time advances
