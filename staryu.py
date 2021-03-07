from pokemon import Pokemon 
  #Definindo o tipo e os ataques do Pokemon Staryu
class Staryu(Pokemon):
  def __init__(self, treinador, tipo, identificacao):
    super().__init__(treinador, tipo, identificacao)
    self.__tipo = "Agua"
    self.__treinador = treinador
    self.__identificacao = identificacao
    self.__ataques = ["	Water Cannon", " Surf ", "	Bubble "]
    
  def getTipo(self):
      return self.__tipo
  
  def getTreinador(self):
    return self.__treinador

  def setTreinador(self,novoTreinador):
    self.__treinador = treinador

  def getAtaques(self):
    return self.__ataques

  def addNewAtaques(self, novoAtaque):
    self.__ataques = self.__ataques.append(novoAtaque)

