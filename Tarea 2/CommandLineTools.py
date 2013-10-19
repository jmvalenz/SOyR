# encoding=utf-8
import os
from Parser import Parser

class CommandLineTools(object):
  
  @staticmethod
  def ImprimirComandos():
    opciones = [ "Opciones Disponibles:\n"
               "\tHacer Llamada; Prioridad; Número; Tiempo de Duración",    \
               "\tRecibir Llamada; Prioridad; Número; Tiempo de Duración",  \
               "\tEnviar Mensaje; Prioridad; Número; Texto",                \
               "\tRecibir Mensaje; Prioridad; Número; Texto",               \
               "\tAgregar Contacto; Prioridad; Nombre; Numero ",            \
               "\tProceso Cualquiera; Prioridad; Tiempo de Duración",       \
               "\tEnviar Ubicación; Prioridad",                             \
               "\tVer Ubicación; Prioridad; Tiempo de Duración",            \
               "\tJugar; Prioridad; Tiempo de Duración",                    \
               "\tEscuchar Música; Prioridad; Tiempo de Duración",          \
               "\n\tEjemplo: Hacer Llamada; 0; 90353108; 20"
             ]
    for opcion in opciones:
      print opcion

  @staticmethod
  def ImprimirInstruccionesNuevoEvento():
    print "Introduzca el evento que quiere agregar luego presione ENTER. (Dejar en blanco para continuar ejecución)\n"

  @staticmethod
  def Cls():
    os.system(['clear','cls'][os.name == 'nt'])

  @staticmethod
  def FileExists(path):
    try:
      with open(path):
        return True
    except IOError:
      return False

  #Extracts the events from the file and appends them to the eventsList
  @staticmethod
  def GetInputFromPath(path):
    parser = Parser()
    parser.GenerateListFromPath(path)
    return parser.eventsList



  @staticmethod
  def TopFunction(time, first_level, second_level, third_level):
    CommandLineTools.Cls()
    print "Para interrumpir e ingresar evento manualmente, presione cualquier tecla"
    print "--------------------------------------------------"
    print "Tiempo transcurrido: ", time, " segundos"
    for p in first_level:
      p.printing()
    for p in second_level:
      p.printing()
    for p in third_level:
      p.printing()
    print "--------------------------------------------------"