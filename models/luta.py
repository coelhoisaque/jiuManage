import uuid
import datetime

class Luta:
  """representa o confronto entre dois atletas"""
  def __init__(self, categoria, atleta1, atleta2, fase="rodada"):
    self.luta_id = str(uuid.uuid4())[:8]
    self.categoria = categoria # --> luta recebe uma categotia . agregação. idependencia ciclo de vida
    self.atleta1 = atleta1  # Usa os atletas mas não cria - associação. Uma classe usa objetos de outra classe como parte de suas operações. REFERENCIA OS ATLETA NO CASO OUTRO OBJETO
    self.atleta2 = atleta2
    self.fase = fase
    self.data_hora = datetime.datetime.now()

    #resultado
    self.vencedor = None
    self.perdedor = None
    self.empate = False
    self.tempo_vitoria = "em andamento"
    self.tempo_luta_minutos = 0.0
    self.metodo_vitoria = "Em andamento" 

  def registrar_ponto(self, atleta_id_arg, pontos=2, tipo='Ponto'): 
    """metodo para registrar pontos, vantagens ou puniçoes. """
    # Lógica para registrar pontos (implementação pendente)

    if atleta_id_arg == self.atleta1.id_atleta:
      if tipo == 'Ponto':
        self.atleta1.pontuacao += pontos
      elif tipo == 'Vantagem':
        self.atleta1.vantagens += 1
      elif tipo == 'Punicao':
        self.atleta1.punicoes += 1
    elif atleta_id_arg == self.atleta2.id_atleta:
      if tipo == 'Ponto':
        self.atleta2.pontuacao += pontos
      elif tipo == 'Vantagem':
        self.atleta2.vantagens += 1
      elif tipo == 'Punicao':
        self.atleta2.punicoes += 1
    else:
      print("Atleta não encontrado na luta.")

  def finalizar_luta(self, vencedor_obj, metodo, tempo_min):
    """Define o vencedor e o método de vitória."""
    self.vencedor = vencedor_obj
    self.metodo_vitoria = metodo
    self.tempo_luta_minutos = tempo_min

    print(f"\n--- LUTA FINALIZADA ({self.fase}) ---")
    print(f"Vencedor: {self.vencedor.nome} por {metodo}")
    print(f"Placar: {self.atleta1.nome} ({self.atleta1.pontuacao}) vs {self.atleta2.nome} ({self.atleta2.pontuacao})")

  def __str__(self):
    vencedor_nome = self.vencedor.nome if self.vencedor else "N/A"
    return (
        f"Luta ID: {self.luta_id[:4]}... | Categoria: {self.categoria.nome}\n"
        f"Fase: {self.fase} | Data: {self.data_hora.strftime('%d/%m %H:%M')}\n"
        f"Atletas: {self.atleta1.nome} vs {self.atleta2.nome}\n"
        f"Resultado: {vencedor_nome} | Método: {self.metodo_vitoria}"
    )
