class Categoria:
  def __init__(self, nome, faixa_min, peso_max_kg, idade_min=18, idade_max=99):
    self.categoria_id = nome.replace(" ", "_").lower()
    self._nome = nome.strip()
    self._faixa_min = faixa_min.strip()
    self._peso_max_kg = float(peso_max_kg)
    self._idade_min = int(idade_min)
    self._idade_max = int(idade_max)

  @property
  def nome(self):
    return self._nome

  @property
  def faixa_min(self):
    return self._faixa_min

  @property
  def peso_max_kg(self):
    return self._peso_max_kg

  @property
  def idade_min(self):
    return self._idade_min

  @property
  def idade_max(self):
    return self._idade_max

  def __str__(self):
    return f"Categoria: {self.nome} ({self.faixa_min} | até {self.peso_max_kg}kg)"