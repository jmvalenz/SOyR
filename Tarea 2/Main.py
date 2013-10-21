# encoding=utf-8
from Simulator import Simulator
from CommandLineTools import CommandLineTools

def Main():
  CommandLineTools.PrintBootScreen()
  simulador = Simulator()

if __name__ == '__main__':
  Main()