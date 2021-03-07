class Pokemon:
# Dados que todos pokemons vão possuir como base
  def __init__(self, treinador, tipo,identificacao):
    self.__hp = 100
    self.__mp = 100
    self.__treinador = treinador
    self.__tipo = tipo 
    self.__identificacao = identificacao
    
  def getTipo(self):
      return self.__tipo
  
  def getHp(self):
    return self.__hp
    
  def getMp(self):
    return self.__mp
    
  def getTreinador(self):
    return self.__treinador
    
  def getIdentificacao(self):
    return self.__identificacao

  def __setHP(self, novoHP):
    self.__hp = novoHP
  
  def __setMP (self, novoMP):
    self.__mp = novoMP
    
  def showStatus(self):
    print('Status do pokemon de {} \n tipo:{} \n Hp: {} \n Mp:{}'.format(self.getTreinador(),self.getTipo(),self.getHp(),self.getMp()))
    
  def receberDano(self, valorDoDano):
    self.__setHP((self.getHP()-valorDoDano))
    print("Pokemon de {} recebe {} de dano".format(self.getTreinador(), valorDoDano))
    if ((self.getHP()-valorDoDano)) <= 0:
      print("Pokemon de {} esta fora de combate.".format(self.getTreinador()))
      
  