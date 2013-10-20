# encoding=utf-8
import os
from Parser import Parser

class CommandLineTools(object):
  
  @staticmethod
  def ImprimirComandos():
    opciones = [ "Opciones Disponibles:\n"
               "\tHacer Llamada; Prioridad; Numero; Tiempo de Duracion",    \
               "\tRecibir Llamada; Prioridad; Numero; Tiempo de Duracion",  \
               "\tEnviar Mensaje; Prioridad; Numero; Texto",                \
               "\tRecibir Mensaje; Prioridad; Numero; Texto",               \
               "\tAgregar Contacto; Prioridad; Nombre; Numero ",            \
               "\tProceso Cualquiera; Prioridad; Tiempo de Duracion",       \
               "\tEnviar Ubicacion; Prioridad",                             \
               "\tVer Ubicacion; Prioridad; Tiempo de Duracion",            \
               "\tJugar; Prioridad; Tiempo de Duracion",                    \
               "\tEscuchar Musica; Prioridad; Tiempo de Duracion",          \
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
  def TopFunction(time, first_level, second_level, third_level, os):
    CommandLineTools.Cls()

    number_of_running_processes = os.NumberOfRunningProcesses()
    number_of_sleeping_processes = os.NumberOfProcesses() - number_of_running_processes
    print "Para interrumpir e ingresar evento manualmente, presione cualquier tecla"
    print "------------------------------------------------------------------------------------------------------------------"
    print "Tiempo transcurrido: ", time, " segundos"
    print "Procesos: ", os.NumberOfProcesses(), " en total, ",  number_of_running_processes, " running,", number_of_sleeping_processes, " sleeping"
    list_of_processes = []
    state = "running"
    for p in first_level:
      list_of_processes.append(("1", str(p.nombre), state, str(p.fecha), str(p.tiempoTotal), str(p.tiempoEnEjecucion), str(p.tiempo), str(p.prioridad)))
      state = "sleeping"
    for p in second_level:
      list_of_processes.append(("2", str(p.nombre), state, str(p.fecha), str(p.tiempoTotal), str(p.tiempoEnEjecucion), str(p.tiempo), str(p.prioridad)))
      state = "sleeping"
    for p in third_level:
      list_of_processes.append(("3", str(p.nombre), state, str(p.fecha), str(p.tiempoTotal), str(p.tiempoEnEjecucion), str(p.tiempo), str(p.prioridad)))
      state = "sleeping"
    CommandLineTools.PrintTableWithProcesses(sorted(list_of_processes, key=lambda process: (process[0], process[1])))
    print "------------------------------------------------------------------------------------------------------------------"

  @staticmethod
  def PrintTableWithProcesses(processes):
    processes.insert(0, ("NIVEL", "NOMBRE", "ESTADO", "FECHA INGRESO", "DURACION", "TIEMPO EN EJECUCION", "TIEMPO RESTANTE", "PRIORIDAD"))
    longg = dict.fromkeys((0,1,2,3,4,5,6,7),0)
    for tu in processes:
      for i,el in enumerate(tu):
        longg[i] = max(longg[i],len(str(el)))
    fofo = '  '.join('%'+str(longg[i])+'s' for i in xrange(0,8))
    print '\n'.join(fofo % (a,b,c,d,e,f,g,h) for (a,b,c,d,e,f,g,h) in processes)