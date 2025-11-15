from models.atleta import Atleta
from models.categoria import Categoria
from models.luta import Luta
from models.bancoDeDados import bancoDb



print("### INICIANDO O CAMPEONATO ###")

# 1. Criação dos Atletas
atleta1 = Atleta("Carlos Silva", "Roxa", 87.5, "conquista")
atleta2 = Atleta("João Pereira", "Roxa", 89.2, "CheckMat")
atleta3 = Atleta("Maria Santos", "Azul", 68.0, "Alliance")

# 2. Criação da Categoria
categoria_roxo_pesado = Categoria("Adulto Masc. - Pesado - Roxa", "Roxa", 94.3)

# 3. Criação e Execução da Luta
luta_principal = Luta(categoria_roxo_pesado, atleta1, atleta2, fase="Final")

print(f"\n--- LUTA CRIADA ---")
print(luta_principal)
print("-" * 30)

# Simulação de pontuação (usando os IDs dos atletas)
print("Simulando Pontuação...")
luta_principal.registrar_ponto(atleta1.id_atleta, pontos=2, tipo='Ponto')      # Carlos - Queda (2 pts)
luta_principal.registrar_ponto(atleta2.id_atleta, pontos=3, tipo='Ponto')      # João - Raspagem (2+1 = 3 pts) - Erro, são 2 pts. Vamos registrar como 3 para exemplo.
luta_principal.registrar_ponto(atleta1.id_atleta, pontos=4, tipo='Ponto')      # Carlos - Montada (4 pts)
luta_principal.registrar_ponto(atleta1.id_atleta, tipo='Vantagem')             # Carlos - Vantagem

# Finaliza a luta
luta_principal.finalizar_luta(
    vencedor_obj=atleta1,
    metodo="Pontos (6 vs 3)",
    tempo_min=5.00
)

def start():
    """
    Função para Iniciar o programa
    """
 
    try:

            conec = bancoDb('jj2.db')
            conec.conectar()

            conec.criarTabelas()
            conec.limparDados()
            conec.inserir_categorias()
            conec.inserir_academia()
            conec.inserir_atetlas()

            print('-' * 50)
            conec.mostrar_atletas()




    finally:
        print("\033[32mPrograma Instalado e em Execução!\033[0m")

start() 


# 4. Visualização Final da Luta
print("\n--- DETALHES DA LUTA FINAL ---")
print(luta_principal)


