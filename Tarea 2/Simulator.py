# encoding=utf-8
from OS import OS #Class OS from OS.py
from Parser import Parser
import time
from Process import *
from operator import attrgetter
import os
from CommandLineTools import CommandLineTools
try:
  # Win32
  from msvcrt import kbhit
except ImportError:
  def kbhit():
    import termios, fcntl, sys
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
      while True:
        try:
          c = sys.stdin.read(1)
          return True
        except IOError:
          return False
    finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
      fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)





#Simulator
class Simulator(object):
  #Constructor
  def __init__(self):
    self.simTime = 0 #Operating System 
    self.oSystem = OS() #Simulation time
    CommandLineTools.Cls()
    while True:
      print "Ingrese ruta archivo input..."
      path = raw_input()
      if CommandLineTools.FileExists(path):
        break
      print "Error: El archivo no existe. Por favor intente nuevamente...\n"
    self.eventsList =  CommandLineTools.GetInputFromPath(path) #Contains the processes that will arrive to the OS during the simulation
    self.StartSimulation()


  #Executes the simulation
  def StartSimulation(self):
    #Iterates until all processes are completed
    while(len(self.eventsList) != 0 or not self.oSystem.AllFinished()):
      self.oSystem.RunAQuantum() #Signal to execute next quantum
      self.oSystem.TopFunction(self.simTime) #Show the processes being executed
      while(True):
        if(len(self.eventsList) != 0 and self.eventsList[0].GetFecha() == self.simTime):
          aux = self.eventsList.pop(0)
          self.oSystem.ProcessRequest(aux)
        else:
          break
      time.sleep(0.1) #Pause
      self.simTime += 1 #Time advances
      if kbhit():
        self.AddNewEvent()



  def AddNewEvent(self):
    print "\n\n==SIMULACIÓN EN PAUSA==\n\n"
    CommandLineTools.ImprimirInstruccionesNuevoEvento()
    CommandLineTools.ImprimirComandos()
    print "\n"
    parser = Parser()
    while True:
      comando = raw_input()
      if comando.strip() == "":
        break
      success = parser.CheckCommand(comando, self.simTime)
      if not success:
        print "Error! Input incorrecto\n"
        CommandLineTools.ImprimirComandos()
        continue
      self.eventsList.insert(0, success)
      break



