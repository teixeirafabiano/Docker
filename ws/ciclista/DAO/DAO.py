import sqlite3
import os

class DAO:

    def __init__(self, database=os.getcwd()+'/ciclista/DAO/data/cyclist.db'):
        self.database = database
        self.conn = None

    def __enter__(self):
        return self._connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._connect().rollback()
        else:
            self._connect().commit()
        try:
            self.conn.close()
        except AttributeError:
            pass
        finally:
            self.conn = None

    def _connect(self):
        try:
            if self.conn is None:
                self.conn = sqlite3.connect(self.database)
        except sqlite3.Error as sqlerror:
            print("Erro ao conectar ao banco!", sqlerror)
        return self.conn

    def execute(self, sql, parameters=()):
        with self as temp:
            result = temp.execute(sql, parameters).fetchall()

        return result

    def disconnect(self):
        self.conn.close()
