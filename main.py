from models.bancoDeDados import bancoDb


def solicitar_nao_vazio(msg):
    """
    Solicita uma entrada ao usuário e garante que não esteja vazia.
    Retorna a string digitada sem espaços nas extremidades.
    """
    while True:
        v = input(msg).strip()
        if v:
            return v
        print('Valor vazio não é permitido')


def solicitar_float_positivo(msg):
    """
    Solicita um número real positivo e repete até receber valor válido.
    Retorna o valor em float.
    """
    while True:
        s = solicitar_nao_vazio(msg)
        try:
            v = float(s)
            if v > 0:
                return v
        except Exception:
            pass
        print('Valor inválido')


def solicitar_int_opcao(msg, opcoes):
    """
    Solicita um número inteiro que esteja dentro das opções fornecidas.
    Retorna o inteiro escolhido.
    """
    cs = set(opcoes)
    while True:
        s = solicitar_nao_vazio(msg)
        try:
            v = int(s)
            if v in cs:
                return v
        except Exception:
            pass
        print('Opção inválida')


def _somente_digitos(s):
    """
    Extrai e retorna apenas os dígitos de uma string fornecida.
    """
    return ''.join(ch for ch in s if ch.isdigit())


def cpf_valido(cpf):
    """
    Valida um CPF brasileiro usando o algoritmo dos dígitos verificadores.
    Retorna True se for válido, caso contrário False.
    """
    n = _somente_digitos(cpf)
    if len(n) != 11 or n == n[0] * 11:
        return False
    nums = list(map(int, n))
    s1 = sum(nums[i] * (10 - i) for i in range(9))
    r1 = s1 % 11
    d1 = 0 if r1 < 2 else 11 - r1
    if nums[9] != d1:
        return False
    s2 = sum(nums[i] * (11 - i) for i in range(10))
    r2 = s2 % 11
    d2 = 0 if r2 < 2 else 11 - r2
    return nums[10] == d2


def start():
    """
    Inicializa o sistema: configura o banco de dados, autentica o usuário
    e apresenta o menu principal de operações.
    """
    db = bancoDb('jj2.db')
    db.conectar()
    db.criarTabelas()
    db.inserir_categorias()
    db.inserir_academia()
    db.criar_usuario('admin', 'admin')

    print('Login')
    usuario = solicitar_nao_vazio('Usuário: ')
    senha = solicitar_nao_vazio('Senha: ')
    if not db.autenticar_usuario(usuario, senha):
        print('\033[31mCredenciais inválidas\033[0m')
        return

    while True:
        print('\n=== Menu ===')
        print('1 - Cadastrar Atleta')
        print('2 - Listar Atletas')
        print('3 - Atualizar Atleta')
        print('4 - Remover Atleta')
        print('5 - Listar Categorias')
        print('6 - Listar Academias')
        print('0 - Sair')
        op = input('Escolha: ').strip()

        if op == '1':
            nome = solicitar_nao_vazio('Nome: ')
            cpf = solicitar_nao_vazio('CPF: ')
            while not cpf_valido(cpf):
                print('CPF inválido')
                cpf = solicitar_nao_vazio('CPF: ')
            nasc = solicitar_nao_vazio('Data nascimento (dd/mm/aaaa): ')
            equipe = solicitar_nao_vazio('Equipe: ')
            faixa = solicitar_nao_vazio('Faixa: ')
            peso = solicitar_float_positivo('Peso (kg): ')
            acads = db.obter_academias()
            if not acads:
                print('Nenhuma academia cadastrada')
                continue
            print('Academias:')
            for ac in acads:
                print(f"ID: {ac['id_academia']} | Nome: {ac['nome_academia']} | CNPJ: {ac['CNPJ']} | Tel: {ac['telefone']}")
            id_academia = solicitar_int_opcao('ID Academia: ', [ac['id_academia'] for ac in acads])
            db.criar_atleta(nome, cpf, nasc, equipe, faixa, peso, id_academia)
            print('Atleta cadastrado')

        elif op == '2':
            atletas = db.obter_atletas()
            if not atletas:
                print('Nenhum atleta cadastrado')
            else:
                for a in atletas:
                    print(f"ID: {a['id_atleta']} | Nome: {a['nome']} | CPF: {a['cpf']} | Faixa: {a['faixa']} | Peso: {a['peso']}Kg | Academia: {a['id_academia']}")

        elif op == '3':
            id_a = solicitar_nao_vazio('ID do atleta: ')
            try:
                id_a_int = int(id_a)
            except Exception:
                print('ID inválido')
                continue
            novo_nome = input('Novo nome (enter para manter): ').strip()
            nova_faixa = input('Nova faixa (enter para manter): ').strip()
            novo_peso = input('Novo peso (enter para manter): ').strip()
            nova_equipe = input('Nova equipe (enter para manter): ').strip()
            nova_academia = input('Novo id academia (enter para manter): ').strip()
            db.atualizar_atleta(
                id_a_int,
                nome=novo_nome or None,
                faixa=nova_faixa or None,
                peso=float(novo_peso) if novo_peso else None,
                equipe=nova_equipe or None,
                id_academia=int(nova_academia) if nova_academia else None,
            )
            print('Atleta atualizado')

        elif op == '4':
            atletas = db.obter_atletas()
            if not atletas:
                print('Nenhum atleta cadastrado')
                continue
            for a in atletas:
                print(f"ID: {a['id_atleta']} | Nome: {a['nome']} | CPF: {a['cpf']} | Faixa: {a['faixa']} | Peso: {a['peso']}Kg | Academia: {a['id_academia']}")
            id_a = solicitar_nao_vazio('ID do atleta: ')
            try:
                id_a_int = int(id_a)
            except Exception:
                print('ID inválido')
                continue
            db.remover_atleta(id_a_int)
            print('Atleta removido')

        elif op == '5':
            cur = db.cursor()
            cur.execute('SELECT * FROM Categoria')
            cats = cur.fetchall()
            for c in cats:
                print(f"ID: {c['id_peso']} | Categoria: {c['categoria_peso']} | Limite: {c['limite_peso']} | Sexo: {c['sexo']}")

        elif op == '6':
            acads = db.obter_academias()
            if not acads:
                print('Nenhuma academia cadastrada')
            else:
                for ac in acads:
                    print(f"ID: {ac['id_academia']} | Nome: {ac['nome_academia']} | CNPJ: {ac['CNPJ']} | Tel: {ac['telefone']}")

        elif op == '0':
            break
        else:
            print('Opção inválida')

    print('\033[32mPrograma Instalado e em Execução!\033[0m')


if __name__ == '__main__':
    start()


