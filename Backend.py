#importarndo a biblioteca SQLite3
import sqlite3 as sql

class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        if TransactionObject.conn:
            TransactionObject.conn.close()
            TransactionObject.connected = False

    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

    def initDB(self):
        self.trans = TransactionObject()
        self.trans.connect()
        self.trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        self.trans.persist()
        self.trans.disconnect()

    def insert(nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def search(self, nome="", sobrenome="", email="", cpf=""):
        trans = TransactionObject()
        trans.connect()
        trans.execute("""SELECT * FROM clientes WHERE nome LIKE ? OR sobrenome LIKE ? OR email LIKE ? OR cpf LIKE ? """, (f"%{nome}%", f"%{sobrenome}%", f"%{email}%", f"%{cpf}%"))
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def delete(id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.persist()
        trans.disconnect()

    def update(id, nome, sobrenome, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()


if __name__ == "__main__":
    db = TransactionObject()
    db.initDB()