import sqlite3

class database: 
    
    def __init__(self, dbPath: str = "exemplo.bd"):
        self.dbPath = dbPath
        self.conn = None

    def conectar(self):
        self.conn = sqlite3.connect(self.dbPath)
        isolation_level=None
        self.conn.row_factory = sqlite3.row_factory
        self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn

    def fechar(self):
        self.conn.close()

    def myCursor(self):
        return self.conn.cursor()
    
    def criarTabelas(self):
        cur = self.cursor
        cur.execute()
        cur.execute()

    def limparTabelas(self):
        cur = self.myCursor()
