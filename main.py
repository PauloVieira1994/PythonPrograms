#importando as classes pokemons e cada pokemon criado, e pelo Show Status mostrando seus atributos em comum
from pidgeot import Pidgeot 
from staryu import Staryu
from cadastroBanco import CadastroBanco
banco = CadastroBanco

objetoPidgeot = Pidgeot('Ash','Voador', '001')

cadastro = CadastroBanco()

cadastro.cadastrarPokemon(objetoPidgeot)

objetoPidgeot.showStatus()

objetoStaryu = Staryu('Mist','Agua','002')

cadastro.cadastrarPokemon(objetoStaryu)

objetoStaryu.showStatus()