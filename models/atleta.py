import uuid

class Atleta:
  def __init__(self, nome, faixa, peso_kg, equipe="sem equipe"):
    self.id_atleta = str(uuid.uuid4())
    self._nome = nome.strip()
    self._faixa = faixa.strip()
    self._peso_kg = float(peso_kg)
    self._equipe = equipe.strip()
    self.pontuacao = 0
    self.vantagens = 0
    self.punicoes = 0

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, value):
    self._nome = value.strip()

  @property
  def faixa(self):
    return self._faixa

  @faixa.setter
  def faixa(self, value):
    self._faixa = value.strip()

  @property
  def peso_kg(self):
    return self._peso_kg

  @peso_kg.setter
  def peso_kg(self, value):
    v = float(value)
    if v <= 0:
      raise ValueError("peso_kg deve ser positivo")
    self._peso_kg = v

  @property
  def equipe(self):
    return self._equipe

  @equipe.setter
  def equipe(self, value):
    self._equipe = value.strip()