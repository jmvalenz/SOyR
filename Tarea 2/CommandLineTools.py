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
    print "Procesos: ", (len(first_level) + len(second_level) + len(third_level)), " en total\n"
    list_of_processes = [("NIVEL", "NOMBRE", "FECHA INGRESO", "DURACION", "TIEMPO EN EJECUCION", "TIEMPO RESTANTE", "PRIORIDAD")]
    for p in first_level:
      list_of_processes.append(("1", str(p.nombre), str(p.fecha), str(p.tiempoTotal), str(p.tiempoEnEjecucion), str(p.tiempo), str(p.prioridad)))
    for p in second_level:
      list_of_processes.append(("2", str(p.nombre), str(p.fecha), str(p.tiempoTotal), str(p.tiempoEnEjecucion), str(p.tiempo), str(p.prioridad)))
    for p in third_level:
      list_of_processes.append(("3", str(p.nombre), str(p.fecha), str(p.tiempoTotal), str(p.tiempoEnEjecucion), str(p.tiempo), str(p.prioridad)))
    CommandLineTools.PrintTableWithProcesses(list_of_processes)
    print "--------------------------------------------------"

  @staticmethod
  def PrintTableWithProcesses(processes):
    longg = dict.fromkeys((0,1,2,3,4,5,6),0)
    for tu in processes:
      for i,el in enumerate(tu):
        longg[i] = max(longg[i],len(str(el)))
    fofo = '  '.join('%'+str(longg[i])+'s' for i in xrange(0,7))
    print '\n'.join(fofo % (a,b,c,d,e,f,g) for (a,b,c,d,e,f,g) in processes)