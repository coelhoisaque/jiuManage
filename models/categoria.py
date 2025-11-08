class Categoria:
  """define as regras de peso, faixa e idade para uma divisao"""
  def __init__(self, nome, faixa_min, peso_max_kg, idade_min=18, idade_max=99):
    #o id da categoria pode ser um contador ou um nome simplificado
    self.categoria_id = nome.replace(" ", "_").lower()
    self.nome = nome
    self.faixa_min = faixa_min
    self.peso_max_kg = peso_max_kg
    self.idade_min = idade_min
    self.idade_max = idade_max
  def __str__(self):

    return f"Categoria: {self.nome} ({self.faixa_min} | até {self.peso_max_kg}kg)"