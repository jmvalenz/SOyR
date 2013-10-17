# coding=utf-8
import os
from Simulator import Simulator
from Parser import Parser

def Cls():
  os.system(['clear','cls'][os.name == 'nt'])

def PedirModo():
  Cls()
  print "Seleccione Modo: \n1.- Input Archivo\n2.- Interactivo"
  entrada = raw_input()
  return entrada

def SimulacionPorArchivo():
  Cls()
  while True:
    print "Ingrese ruta archivo input"
    path = raw_input()
    if FileExists(path):
      break
    print "El archivo no existe!\n"

  simulador = Simulator(GetInputFromPath(path))
  simulador.StartSimulation()

def SimulacionInteractiva():
  Cls()
  parser = Parser()
  print "**Ingrese las acciones a ejecutar**\n"
  ImprimirComandos()
  while True:
    comando = raw_input()
    if comando == "Finish" or comando == "finish":
      break
    if not parser.CheckCommand(comando):
      print "Error! Input incorrecto\n"
      ImprimirComandos()
      continue
  parser.SortList()
  print "Iniciando Simulación: " + str(len(parser.eventsList)) + " eventos"
  simulador = Simulator(parser.eventsList)
  simulador.StartSimulation()


def FileExists(path):
    try:
      with open(path):
        return True
    except IOError:
      return False

#Extracts the events from the file and appends them to the eventsList
def GetInputFromPath(path):
  parser = Parser()
  parser.GenerateListFromPath(path)
  return parser.eventsList

def ImprimirComandos():
  opciones = [ "Opciones Disponibles:\n"
  						 "\tHacer Llamada; Fecha Entrada; Prioridad; Numero; Tiempo de Duracion", 	 \
               "\tRecibir Llamada; Fecha Entrada; Prioridad; Numero; Tiempo de Duracion",  \
               "\tEnviar Mensaje; Fecha Entrada; Prioridad; Numero; Texto",								 \
               "\tRecibir Mensaje; Fecha Entrada; Prioridad; Numero; Texto", 							 \
               "\tAgregar Contacto; Fecha Entrada; Prioridad; Nombre; Numero ", 					 \
               "\tProceso Cualquiera; Fecha Entrada; Prioridad; Tiempo de Duracion", 			 \
               "\tEnviar Ubicacion; Fecha Entrada; Prioridad", 														 \
               "\tVer Ubicacion; Fecha Entrada; Prioridad; Tiempo de Duracion", 					 \
               "\tJugar; Prioridad; Fecha Entrada; Tiempo de Duracion", 									 \
               "\tEscuchar Musica; Fecha Entrada; Prioridad; Tiempo de Duracion", 				 \
               "\n\tEjemplo: Hacer Llamada; 20; 0; 90353108; 20", 												 \
               "\n**Para terminar de escribir comandos, escriba Finish**" 								 \
             ]
  for opcion in opciones:
    print opcion


def Main():
  while True:
    modo = PedirModo()
    if (modo == "1" or modo == "2"):
      break

  if(modo == "1"):
    SimulacionPorArchivo()
  else:
    SimulacionInteractiva()
    
if __name__ == '__main__':
  Main()