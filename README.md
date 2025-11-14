# 🥋  Jiu-Manage – Sistema de Gerenciamento

Sistema completo para cadastro, gerenciamento e simulação de um campeonato de Jiu-Jitsu, incluindo **atletas, academias, categorias, inscrições e lutas**, com banco de dados SQLite e classes Python orientadas a objetos.

---

##  **Descrição do Projeto**

Este projeto tem como objetivo fornecer uma aplicação simples, modular e extensível para gerenciamento de campeonatos de Jiu-Jitsu.
O sistema inclui:

* Cadastro automático de **academias**, **atletas** e **categorias**;
* Simulação estruturada de lutas com pontuação;
* Registro de resultados no banco de dados;
* Exibição de todos os dados cadastrados;
* Criação automática do banco SQLite com todas as tabelas necessárias.

Toda a estrutura foi projetada com **classes separadas** (Atleta, Categoria, Luta, bancoDb), facilitando manutenção e expansão.

---

##  **Estrutura de Arquivos**

```
jiuManage
├── main.py
├── models
│   ├── atleta.py
│   ├── bancoDeDados.py
│   ├── categoria.py
│   └── luta.py
└── README.md
``` 


---

##  **Banco de Dados**

O sistema utiliza **SQLite**, criando automaticamente as seguintes tabelas:

* **Atleta**
* **Categoria**
* **Lutas**
* **Academia**
* **Inscricoes**

Cada tabela contém campos essenciais para organização do campeonato.

---

## ⚙️ **Funcionalidades Principais**

### Cadastro automático inicial:

* Categorias por peso, faixa e sexo
* Academias com CNPJ e telefone
* Atletas iniciais (exemplo)

### CRUD básico (implícito nas classes):

* Inserir Atletas
* Inserir Categorias
* Registrar Lutas
* Mostrar dados completos do banco

### Simulação de Lutas

* Registro de pontos
* Registro de vantagens
* Registro de punições
* Definição de vencedor e método
* Salvamento do resultado

---

## **Como Executar o Projeto**

### 1. Clone este repositório:

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Execute o arquivo principal:

```bash
python3 main.py
```

O sistema irá:

1. Criar o banco SQLite se ele ainda não existir
2. Criar atletas, categorias, academias e lutas de exemplo
3. Simular uma luta
4. Exibir resultados no console

---

##  **Requisitos**

```bash
# Nenhuma dependência externa
# Python 3.8+
python3 --version

# SQLite (já incluído no Python)
python3 -c "import sqlite3; print('SQLite OK')"
```

---

## **Classes Principais**

### 🥋 `Atleta`

Representa um competidor:

* Nome
* Faixa
* Peso
* Equipe
* Pontuação da luta

### 🧮 `Categoria`

* Nome
* Faixa mínima
* Peso limite
* Sexo

### ⚔️ `Luta`

* Atleta 1
* Atleta 2
* Pontos / Vantagens / Punições
* Método de vitória
* Fase (Ex: final)

### 🗄️ `bancoDb`

* Criação de tabelas
* Inserções iniciais
* Inserções permanentes
* Consultas gerais

---

## 📘 **Exemplo de Saída (Simulação)**

```
### INICIANDO O CAMPEONATO ###
✓ Conectado ao banco de dados
Criando tabelas...
✓ Categorias cadastradas
✓ Academias cadastradas
✓ Atletas cadastrados
✓ Banco de dados inicializado com sucesso!

--- LUTA CRIADA ---
Carlos Silva vs João Pereira – Final

Simulando Pontuação...
✓ Luta finalizada: Carlos Silva venceu por Pontos (6 vs 3)
```


---

## 📄 **Licença**

Este projeto é de uso livre para fins educacionais.