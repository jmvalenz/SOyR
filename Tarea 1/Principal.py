from OS import OS #Class OS from OS.py
import time

#Simulator

simTime = 0 #Simulation time
eventList = [] #Contains the proccesses that will arrive to the OS during the simulation
oSystem = OS() #Operating System 

#Appends the events to the eventList
def GetInput():
	global eventList
	#Completar!!

#Executes the simulation
def StartSimulation():
	global oSystem
	global simTime
	global eventList

	#Iterates until all proccesses are completed
	while(len(eventList) != 0 or not oSystem.AllFinished()):
		simTime += 1 #Time advances
		#Agregar iterador para obtener eventos que llegan al sistema en el tiempo actual de simulacion
		oSystem.RunAQuantum() #Signal to execute next quantum
		oSystem.TopFunction() #Show the proccesses being executed
		time.sleep(0.4) #Pause

if __name__ == '__main__':
	GetInput()
	StartSimulation()