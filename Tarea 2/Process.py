import math
import Disc
class Process(object):

  def __init__(self, tipo, nombre, fecha, prioridad):
    self.tipo=tipo
    self.nombre=nombre
    self.fecha=fecha
    self.prioridad=prioridad
    self.tiempo = 0
    self.tiempoTotal = 0
    self.tiempoEnEjecucion = 0

  def PasarTiempo(self):
    self.tiempoEnEjecucion +=1

  def SetTiempo(self):
    self.tiempo -=1

  def GetTiempo(self):
    return self.tiempo

  def GetFecha(self):
    return self.fecha
  
  def calcTiempo(self,tiempo):
    self.tiempo = tiempo
    self.tiempoTotal = tiempo

  def BeforeFinish(self):
    pass


class Mensaje(Process):# dejare el tipo en el constructor. con el fin de usar esta clase tanto para recibir como enviar

  def __init__(self, tipo, nombre, fecha, prioridad, receptor, texto):
    super(Mensaje, self).__init__(tipo, nombre, fecha, prioridad)
    self.receptor=receptor
    self.texto = texto.strip()
    self.calcTiempo(texto)

  def BeforeFinish(self):
    if(self.tipo == 3):
      destino = "enviado"
      dePara = "para"
    else:
      destino = "recibido"
      dePara = "de"
    Disc.writeContentToDisc("Mensaje " + destino + " " + dePara + " " + self.receptor + ". Texto: " + self.texto + "\n", "mensajes")

  def calcTiempo(self, mensaje):
    self.tiempo = int(math.ceil(len(mensaje) * 0.2)) # ver  bien por cuento se multiplica
    self.tiempoTotal = self.tiempo


class Llamada(Process):# dejare el tipo en el constructor. con el fin de usar esta clase tanto para recibir como hacer
  
  def __init__(self, tipo, nombre, fecha, prioridad, numero, tiempo):
    super(Llamada, self).__init__(tipo, nombre, fecha, prioridad)
    self.numero = numero.strip()
    self.calcTiempo(tiempo)

  def BeforeFinish(self):
    if(self.tipo == 1):
      destino = "realizada"
      dePara = "para"
    else:
      destino = "recibida"
      dePara = "de"
    Disc.writeContentToDisc("Llamada " + destino + " " + dePara + " " + str(self.numero) + ". Duracion: " + str(self.tiempoTotal) + "\n", "historial")


class Contacto(Process):#Cuanto toma...
  
  def __init__(self, nombre, fecha, prioridad, nombreContacto, numero):
    super(Contacto, self).__init__(5, nombre, fecha, prioridad)
    self.numero = numero.strip()
    self.nombreContacto = nombreContacto

  def BeforeFinish(self):
    Disc.writeContentToDisc("Nombre: " + self.nombreContacto + ". Numero: " + str(self.numero) + "\n", "contactos")

class Cualquiera(Process):
  
  def __init__(self, nombre, fecha, prioridad, tiempo):
    super(Cualquiera, self).__init__(6, nombre, fecha, prioridad)
    self.calcTiempo(tiempo)


class MUbicacion(Process):
  
  def __init__(self, nombre, fecha, prioridad,):
    super(MUbicacion, self).__init__(7, nombre, fecha, prioridad)
    self.calcTiempo(2) #2 segundos


class VUbicacion(Process):
  
  def __init__(self, nombre, fecha, prioridad, tiempo):
    super(VUbicacion, self).__init__(8, nombre, fecha, prioridad)
    self.calcTiempo(tiempo)


class Jugar(Process):
  
  def __init__(self, nombre, fecha, prioridad, tiempo):
    super(Jugar, self).__init__(9, nombre, fecha, prioridad)
    self.calcTiempo(tiempo)


class EscucharM(Process):
  
  def __init__(self, nombre, fecha, prioridad, tiempo):
    super(EscucharM, self).__init__(10, nombre, fecha, prioridad)
    self.calcTiempo(tiempo)



