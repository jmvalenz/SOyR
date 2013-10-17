# coding=utf-8
# Parses all the actions to be excecuted
from Process import *
from operator import attrgetter
class Parser(object):
  
  def __init__(self):
    self.eventsList = []

  def GenerateListFromPath(self, path):
    print "----Generando Lista----"
    f = open(path, 'r')
    for line in f:
      self.eventsList.append(self.ParseLine(line))
    self.SortList()
    # for s in self.eventsList:
    #   print str(s.fecha)
    print "----Lista Generada----"

  def SortList(self):
    self.eventsList.sort(key=attrgetter('fecha'))

  def GetTipo(self, text):
    opciones = { "Hacer Llamada": 1, \
                 "Recibir Llamada": 2, \
                 "Enviar Mensaje": 3, \
                 "Recibir Mensaje": 4, \
                 "Agregar Contacto": 5, \
                 "Proceso Cualquiera": 6, \
                 "Enviar Ubicacion": 7, \
                 "Ver Ubicacion": 8, \
                 "Jugar": 9, \
                 "Escuchar Musica": 10, \
               }
    try:
      return opciones[text]
    except KeyError:
      return -1

  def ParseLine(self,line):
    accion = line.split(";")
    tipo = int(float(accion[2]))
    if len(accion) < 4:
      raise Exception("El formato del archivo no es válido")
    if tipo == 1 or tipo == 2:
      return Llamada(tipo,accion[0],int(accion[1]),accion[3],accion[4],int(accion[5]))
    if tipo == 3 or tipo == 4:
      return Mensaje(tipo,accion[0],int(accion[1]),accion[3],accion[4],accion[5])
    if tipo == 5:
      return Contacto(accion[0],int(accion[1]),accion[3],accion[4],accion[5])
    if tipo == 6:
      return Cualquiera(accion[0],int(accion[1]),accion[3],int(accion[4]))
    if tipo == 7:
      return MUbicacion(accion[0],int(accion[1]),accion[3])
    if tipo == 8:
      return VUbicacion(accion[0],int(accion[1]),accion[3],int(accion[4]))
    if tipo == 9: 
      return Jugar(accion[0],int(accion[1]),accion[3],int(accion[4]))
    if tipo == 10:
      return EscucharM(accion[0],int(accion[1]),accion[3],int(accion[4]))
    return None

  def CheckCommand(self, command, time):
    splitted = command.split(";")
    accion = [x.strip() for x in splitted]
    tipo = self.GetTipo(accion[0])
    if tipo == -1:
      return False
    return self.ParseCommand(accion, tipo, time)
    

  def ParseCommand(self, accion, tipo, time):
    if tipo == 1 or tipo == 2:
      return Llamada(tipo,accion[0], time, accion[2], accion[3], int(accion[4]))
    if tipo == 3 or tipo == 4:
      return Mensaje(tipo,accion[0], time, accion[2], accion[3], accion[4])
    if tipo == 5:
      return Contacto(accion[0], time, accion[2], accion[3],accion[4])
    if tipo == 6:
      return Cualquiera(accion[0], time, accion[2], int(accion[3]))
    if tipo == 7:
      return MUbicacion(accion[0], time, accion[2]) 
    if tipo == 8:
      return VUbicacion(accion[0], time, accion[2], int(accion[3]))
    if tipo == 9: 
      return Jugar(accion[0], time, accion[2], int(accion[3]))
    if tipo == 10:
      return EscucharM(accion[0], time, accion[2], int(accion[3]))
    return None