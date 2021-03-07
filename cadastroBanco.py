from replit import db as banco
#classe para realizar os cadastros no banco de dados.

class CadastroBanco:
  def __init__(self):
    self.banco = banco
    
  def cadastrarPokemon(self, objetoPidgeot):
    self.informacaoPidgeot = {'tipo' : objetoPidgeot.getTipo(),'treinador' : objetoPidgeot.getTreinador(),'hp': objetoPidgeot.getHp(), 'mp': objetoPidgeot.getMp(), 'ataques': objetoPidgeot.getAtaques()}
    self.banco[objetoPidgeot.getIdentificacao()] = self.informacaoPikachu
    print("\nPokemon de {} cadastrado!".format(objetoPidgeot.getTreinador()))
   


  def cadastrarPokemon(self, objetoStaryu):
    self.informacaoCharmander = {'tipo' : objetoStaryu.getTipo(),'treinador' : objetoStaryu.getTreinador(),'hp': objetoStaryu.getHp(), 'mp': objetoStaryu.getMp(), 'ataques': objetoStaryu.getAtaques()}
    self.banco[objetoStaryu.getIdentificacao()] = self.informacaoCharmander
    print("\nPokemon de {} cadastrado!".format(objetoStaryu.getTreinador()))
