# 🥋 Jiu-Manager - Sistema Completo de Gestão para Jiu-Jitsu

Sistema para gerenciamento de academias, atletas, categorias e competições de Jiu-Jitsu. Desenvolvido em Python com banco de dados SQLite e interface interativa.
---

## **Funcionalidades**

### **Gestão de Atletas**
- 📝 Cadastro com validação de CPF
- 👀 Listagem completa
- ✏️ Atualização de dados
- 🗑️ Remoção segura

### **Gestão de Academias**
- 🏢 Listagem de academias cadastradas
- 🔗 Associação automática de atletas

### **Gestão de Categorias**
-  Categorias por peso e sexo
   Consulta de limites e regras

### **Segurança**
- 🔐 Login com usuário e senha
- 👤 Usuário padrão: `admin` / `admin`

---

## 🏗️ **Estrutura do Projeto**

```
jiuManager/
├── main.py                      # Sistema principal interativo
├── models/
│   ├── bancoDeDados.py          # Gerenciamento do banco SQLite
│   ├── atleta.py               # Modelo com properties
│   ├── categoria.py            # Modelo com validações
│   └── luta.py                 # Sistema de lutas (próxima versão)
└── README.md                   
```

---

## **Instalação e Execução**

### **Pré-requisitos**
```bash
Python 3.8+
SQLite (incluído no Python)
```

### **Primeira Execução**
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd jiu-manager-pro

# Execute o sistema
python main.py

# Credenciais iniciais
Usuário: admin
Senha: admin
```

---

## 🎯 **Como Usar**

### **1. Login no Sistema**
- Execute `python main.py`
- Digite usuário e senha

### **2. Menu Principal**
```
=== Menu ===
1 - Cadastrar Atleta
2 - Listar Atletas  
3 - Atualizar Atleta
4 - Remover Atleta
5 - Listar Categorias
6 - Listar Academias
0 - Sair
```

### **3. Cadastro de Atleta**
- Nome completo
- CPF (com validação automática)
- Data de nascimento (dd/mm/aaaa)
- Equipe
- Faixa
- Peso (kg)
- Academia (seleção da lista)

---

## **Banco de Dados**

### **Tabelas Principais**
```sql
Atleta (id_atleta, nome, cpf, data_nascimento, equipe, faixa, peso, id_academia)
Categoria (id_peso, categoria_peso, limite_peso, sexo) 
Academia (id_academia, nome_academia, CNPJ, telefone)
Usuario (id_user, username, senha_hash, salt)
```

### **Dados Iniciais**
- **12 academias** pré-cadastradas
- **9 categorias** de peso (masculino/feminino)
- **Usuário admin** criado automaticamente

---

## **Desenvolvimento**

### **Validações Implementadas**
```python
# CPF válido (algoritmo oficial)
def cpf_valido(cpf)

# Campos não vazios  
def solicitar_nao_vazio(msg)

# Números positivos
def solicitar_float_positivo(msg)

# Opções válidas no menu
def solicitar_int_opcao(msg, opcoes)
```

### **Models com Properties**
```python
class Atleta:
    @property
    def nome(self):
        return self._nome
        
    @nome.setter 
    def nome(self, value):
        self._nome = value.strip()  # Auto-trim
```

---

##  **Solução de Problemas**

### **Problemas Comuns**
```bash
# "Credenciais inválidas"
Verifique se digitou admin/admin

# Erro de banco de dados
Delete jj2.db e execute novamente

# CPF não aceito
Digite com ou sem pontuação, o sistema valida
```

### **Comandos Úteis**
```python
# Reset completo
from models.bancoDeDados import bancoDb
db = bancoDb('jj2.db')
db.conectar()
db.limparDados()
```

---

## 👥 **Contribuição**

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'Add nova funcionalidade'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

---

## 📄 **Licença**

Este projeto é livre para uso educacional e acadêmico.

---

## 🆘 **Suporte**

Encontrou um problema? Abra uma issue no repositório com:
- Descrição do erro
- Passos para reproduzir
- Screenshots (se aplicável)

**Commit sugerido:** `feat: implementar sistema completo CRUD com autenticação e validações`

