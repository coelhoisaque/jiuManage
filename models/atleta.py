import uuid

class Atleta:
  """representa um competidor no campeonato"""
  def __init__(self, nome, faixa, peso_kg, equipe="sem equipe"):
    #gerar um id unico para o atleta
    self.id_atleta = str(uuid.uuid4())
    self.nome = nome
    self.faixa = faixa
    self.peso_kg = peso_kg
    self.equipe = equipe
    # Adicionando atributos de pontuação ao atleta
    self.pontuacao = 0
    self.vantagens = 0
    self.puniçoes = 0
