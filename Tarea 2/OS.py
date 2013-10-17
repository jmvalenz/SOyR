#Represents the Operating System

class OS:

  #Constructor
  def __init__(self):

    #Instantiation of multilevel queues
    self.__firstLevelProc = [] #will contain the processes with the highest priority
    self.__secondLevelProc = [] #will contain the processes with middle priority
    self.__thirdLevelProc = [] #will contain the processes with the lowest priority


  #Receives a process and puts it into the corresponding queue depending on its priority
  def ProcessRequest(self, newProcess):
    if(newProcess.tipo == "1" or newProcess.tipo == "2"):
      self.__firstLevelProc.append(newProcess)
    elif(newProcess.tipo == "3" or newProcess.tipo == "4"):
      self.__secondLevelProc.append(newProcess)
    else:
      self.__thirdLevelProc.append(newProcess)

  def EliminarProcesosFinalizados(self):
    if(len(self.__firstLevelProc) != 0 and self.__firstLevelProc[0].GetTiempo() == 0):
      finished_process = self.__firstLevelProc.pop(0)
      finished_process.BeforeFinish()

    if(len(self.__secondLevelProc) != 0 and self.__secondLevelProc[0].GetTiempo() == 0):
      finished_process = self.__secondLevelProc.pop(0)
      finished_process.BeforeFinish()

    if(len(self.__thirdLevelProc)!= 0):
      ultimo = self.__thirdLevelProc.pop()
      ultimo.BeforeFinish()
      if(ultimo.GetTiempo() != 0):
        self.__thirdLevelProc.append(ultimo)

  #Executes a quantum
  def RunAQuantum(self):
    self.EliminarProcesosFinalizados()
    if(len(self.__firstLevelProc) != 0):
      self.__RunProccess(self.__firstLevelProc[0])
    elif(len(self.__secondLevelProc) != 0):
      self.__RunProccess(self.__secondLevelProc[0])
    elif(len(self.__thirdLevelProc)!=0):
      actual = self.__thirdLevelProc.pop(0)
      self.__RunProccess(actual)
      self.__thirdLevelProc.append(actual)

  #Shows a list with the information of the proceses that are being executed
  def TopFunction(self):
    for p in self.__firstLevelProc:
      p.printing()
    for p in self.__secondLevelProc:
      p.printing()
    for p in self.__thirdLevelProc:
      p.printing()

  #Returns true if the three queues are empty
  def AllFinished(self):
    return len(self.__firstLevelProc) == 0 and len(self.__secondLevelProc) == 0 and len(self.__thirdLevelProc) == 0 

  #Runs a process
  def __RunProccess(self, process):
    process.SetTiempo()