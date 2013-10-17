# encoding=utf-8
import os
from Parser import Parser

class CommandLineTools(object):
  
  @staticmethod
  def ImprimirComandos():
    opciones = [ "Opciones Disponibles:\n"
               "\tHacer Llamada; Fecha Entrada; Prioridad; Número; Tiempo de Duración",    \
               "\tRecibir Llamada; Fecha Entrada; Prioridad; Número; Tiempo de Duración",  \
               "\tEnviar Mensaje; Fecha Entrada; Prioridad; Número; Texto",                \
               "\tRecibir Mensaje; Fecha Entrada; Prioridad; Número; Texto",               \
               "\tAgregar Contacto; Fecha Entrada; Prioridad; Nombre; Numero ",            \
               "\tProceso Cualquiera; Fecha Entrada; Prioridad; Tiempo de Duración",       \
               "\tEnviar Ubicación; Fecha Entrada; Prioridad",                             \
               "\tVer Ubicación; Fecha Entrada; Prioridad; Tiempo de Duración",            \
               "\tJugar; Prioridad; Fecha Entrada; Tiempo de Duración",                    \
               "\tEscuchar Música; Fecha Entrada; Prioridad; Tiempo de Duración",          \
               "\n\tEjemplo: Hacer Llamada; 20; 0; 90353108; 20"
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
    print "-------------------------"
    print "Tiempo transcurrido: ", time, " segundos"
    for p in first_level:
      p.printing()
    for p in second_level:
      p.printing()
    for p in third_level:
      p.printing()
    print "-------------------------"