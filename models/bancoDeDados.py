import sqlite3

class bancoDb:

    def __init__(self, dbPath: str = 'exemplo_bd.db'):
        self.dbPath = dbPath
        self.conn = None
    
    def conectar(self):
        if self.conn is None:
            # isolation_level=None ativa autocommit (cada operação é commitada automaticamente)
            self.conn = sqlite3.connect(self.dbPath, isolation_level=None)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")
            print('ok')
        return self.conn

    def fechar(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()
            self.conn = None
     
    def cursor(self):
        """Retorna um cursor para executar queries"""
        if self.conn is None:
            self.conectar()
        return self.conn.cursor()
    
    def criarTabelas(self):
        cur = self.cursor()
           #criar tabela atletas
        try:
            print('[Criando tabela Atletas]....')
            print('////....')
            cur.execute("""
                    CREATE TABLE "Atleta" (
                        "id_atleta"	INTEGER,
                        "nome"	TEXT NOT NULL,
                        "cpf"	TEXT NOT NULL,
                        "data_nascimento"	TEXT NOT NULL,
                        "equipe"	TEXT,
                        "faixa"	TEXT NOT NULL,
                        "peso"	INT,
                        "id_academia"	INT,
                        "data_inscricao"	TEXT,
                        UNIQUE("cpf"),
                        PRIMARY KEY("id_atleta" AUTOINCREMENT)
                    )

                        """)
        except sqlite3.Error as xy:
            print(f"\033[31mDeu erro mano: {xy}\033[0m")

        
        finally:
            print("Tabela Atleta Criada com Sucesso!")
            print("##################################")
        
        #criar tabela categoria
        try:
            print('[Criando tabela Categoria]....')
            print('////....')
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS Categoria ( 
                        id_peso INTEGER PRIMARY KEY AUTOINCREMENT,  
                        limite_peso INT NOT NULL,  
                        sexo VARCHAR(255),  
                        categoria_peso VARCHAR(255)  
                        ); 

                        """)
        except sqlite3.Error as xy:
            print(f"Deu erro mano: {xy}")
        finally:
            print("Tabela Categoria Criada com Sucesso!")
            print("##################################")


    #criar tabela lUTAS
        try:
            print('[Criando tabela Lutas]....')
            print('////....')
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS Lutas 
                        ( 
                        id_luta INTEGER PRIMARY KEY AUTOINCREMENT,  
                        atleta1 VARCHAR(255),  
                        atleta2 VARCHAR(255),  
                        resultado INT  
                        ); 

                    

                        """)
        except sqlite3.Error as xy:
            print(f"\033[31mDeu erro mano: {xy}\033[0m")
        finally:
            print("Tabela Lutas Criada com Sucesso!")
            print("##################################")
            
        
    #criar tabela Academia

        try:
            print('[Criando tabela Academia]....')
            print('////....')
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Academia (
                    id_academia INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_academia VARCHAR(100),
                    CNPJ VARCHAR(20),
                    telefone VARCHAR(20),
                    UNIQUE (CNPJ, telefone)
                )
                        """);
        except sqlite3.Error as e:
            print(f"\033[31mDeu erro mano: {e}\033[0m")
        finally:
            print("Tabela Academia Criada com Sucesso!")
            print("##################################")

    #criar tabela Inscrições
            try:
                print('[Criando tabela Inscricoes]....')
                print('////....')
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS Inscricoes (
                        id_inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_atleta INTEGER NOT NULL,
                        id_campeonato INTEGER,
                        id_categoria_peso INTEGER,
                        id_criterio_idade INTEGER,
                        status_pagamento VARCHAR(50),
                        FOREIGN KEY (id_atleta) REFERENCES Atleta(id_atleta),
                        FOREIGN KEY (id_categoria_peso) REFERENCES Categoria(id_peso)
                    )
                """)
            except sqlite3.Error as e:
                print(f"\033[31mDeu erro mano: {e}\033[0m")
            finally:
                print("Tabela Inscricoes Criada com Sucesso!")
                print("##################################")

    def inserir_categorias(self):
        cur = self.cursor()
        categorias = [
            ("Galo", 53.50, "Masculino"),
            ("Pena", 58.50, "Masculino"),
            ("Leve", 64.00, "Masculino"),
            ("Médio", 70.00, "Masculino"),
            ("Pesado", 76.00, "Masculino"),
            ("Super Pesado", 82.30, "Masculino"),
            ("Galo", 48.30, "Feminino"),
            ("Pena", 53.50, "Feminino"),
            ("Leve", 58.50, "Feminino"),
        ]
        
        sql_insert = """
        INSERT INTO Categoria (categoria_peso, limite_peso , sexo)
        VALUES (?,?,?);
        """
        cur.executemany(sql_insert, categorias)
        print('Cadastrando Categorias')
        self.conn.commit()

    def inserir_academia(self):
        cur = self.cursor()

        Academias = [('Leões Academy', '14.888.0001/15', '77998506765'),
                    ('Lobos Academy', '14.888.0001/15', '77998506764'),
                    ('Ferozes', '14.888.0001/15', '77998506767'),
                    ('Conquista', '14.888.0001/15', '77998506768'),
                    ('Lutadores do Cão', '14.888.0001/15', '77998506664'),
                    ('Dedicados', '14.888.0001/15', '77998506364'),
                    ('Rocha Rocha', '14.888.0001/15', '77998306764'),
                    ('Santos Academy', '14.888.0001/15', '77996506364'),
                    ('SP Academy', '14.888.0001/15', '77998503764'),
                    ('Brazil Academy', '14.888.0001/15', '77968506764'),
                    ('JJ Academy', '14.888.0001/15', '77998606764'),

                    ]
        
        sql_acd = """
                    INSERT INTO Academia (nome_academia, CNPJ, telefone) VALUES (?,?,?);
                """
        try:
            print('Cadastrando Academias....')
            cur.executemany(sql_acd , Academias)
            print('///////.....')
        except sqlite3.Error as xy:
                print(f"\033[31mErro ao Cadastrar Academias: {xy}\033[0m")
        finally:    
            self.conn.commit()
            print('Academias Cadastradas!')
           
    def inserir_atetlas(self):
        cur = self.cursor()
        Atletas = [
            ('Lucas', '060.287.275-80', '22/06/1995', 'Leão', 'Preta', 64, 1, '07/11/2025'),
            ('Marcos', '415.982.134-09', '10/03/1990', 'Peixes', 'Roxa', 72, 1, '06/11/2025'),
            ('Juliana', '289.654.871-22', '15/08/1998', 'Leão', 'Azul', 58, 2, '05/11/2025'),
            ('Rafael', '301.875.640-51', '09/11/1993', 'Escorpião', 'Marrom', 82, 1, '03/11/2025'),
            ('Ana', '852.647.190-74', '27/04/2001', 'Touro', 'Branca', 56, 2, '01/11/2025'),
            ('Carlos', '164.920.387-33', '11/09/1988', 'Virgem', 'Preta', 95, 1, '30/10/2025'),
            ('Beatriz', '598.741.236-47', '20/01/2000', 'Aquário', 'Roxa', 62, 2, '29/10/2025'),
            ('Pedro', '715.834.209-10', '14/05/1996', 'Touro', 'Azul', 69, 1, '27/10/2025'),
            ('Camila', '947.162.508-25', '05/12/1994', 'Sagitário', 'Marrom', 60, 2, '26/10/2025'),
            ('Thiago', '328.756.941-62', '03/07/1992', 'Câncer', 'Preta', 88, 1, '25/10/2025'),
            ('Larissa', '419.385.270-13', '22/02/1999', 'Peixes', 'Azul', 57, 2, '24/10/2025'),
            ('Gabriel', '593.701.846-90', '17/10/1991', 'Libra', 'Roxa', 77, 1, '22/10/2025'),
            ('Renata', '230.894.561-22', '09/09/2002', 'Virgem', 'Branca', 54, 2, '21/10/2025'),
            ('Felipe', '672.580.193-48', '02/02/1995', 'Aquário', 'Preta', 81, 1, '19/10/2025'),
            ('Bruna', '809.315.467-72', '11/06/1997', 'Gêmeos', 'Marrom', 63, 2, '18/10/2025'),
            ('Victor', '736.904.582-60', '29/03/1990', 'Áries', 'Roxa', 70, 1, '16/10/2025'),
            ('Carolina', '905.781.423-17', '01/12/1998', 'Sagitário', 'Azul', 59, 2, '15/10/2025'),
            ('André', '154.392.708-45', '25/05/1993', 'Gêmeos', 'Preta', 85, 1, '14/10/2025'),
            ('Luiza', '268.541.907-83', '06/08/1999', 'Leão', 'Roxa', 61, 2, '13/10/2025'),
            ('Matheus', '497.630.815-29', '17/11/1994', 'Escorpião', 'Marrom', 79, 1, '12/10/2025'),
        ]

        sql_atletas = """

                INSERT INTO Atleta (nome, cpf, data_nascimento, equipe, faixa, peso, id_academia, data_inscricao)
                VALUES (?,?,?,?,?,?,?,?);

               """
        try:
            print("Inserindo Atletas....")
            print("////////....")
            cur.executemany( sql_atletas, Atletas)
        except sqlite3.Error as xy:
             print(f"\033[31mErro ao Cadastrar Atletas: {xy}\033[0m")
        finally:

            self.conn.commit()    
            print("Atletas Cadastrados!")
                    
    def mostrar_atletas(self):
        cur = self.cursor()
        cur.execute("SELECT * FROM Atleta;")
        
        categorias = cur.fetchall()
        
        if not categorias:
            print("\033[93mNenhum Atleta encontrado.\033[0m")  # amarelo
        else:
            print("\033[92m=== ATLETAS CADASTRADOS ===\033[0m")  # verde
            for cat in categorias:
                print(f"ID: {cat['id_atleta']} | Nome: {cat['nome']} | CPF: {cat['cpf']} | Data de Nascimento: {cat['data_nascimento']} | Equipe: {cat['equipe']} | Faixa: {cat['faixa']} | Peso: {cat['peso']}Kg | Academia: {cat['id_academia']} | Data Inscrição: {cat['data_inscricao']}     ")


    
    def limparDados(self):
            cur = self.cursor()
            cur.execute("DELETE FROM Academia;")
            cur.execute("DELETE FROM Lutas;")
            cur.execute("DELETE FROM Inscricoes;")
            cur.execute("DELETE FROM Atleta;")
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('Atleta', 'Categoria', 'Lutas', 'Inscricoes');")

            print('DADOS LIMPOS')
        
