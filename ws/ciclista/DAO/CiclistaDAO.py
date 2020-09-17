from ciclista.DAO.DAO import DAO

class CiclistaDAO(DAO):

    def __init__(self):
        super().__init__()

    def select(self, column, value):
        query = "select * from cyclist where " + column + " = ?"
        try:
            self._connect()
            result = self.execute(query, value)
        except Exception as exc:
            print("Erro ao selecionar ciclista!", exc)
        return result

    def update(self, value):
        query = "update cyclist set name = ?, email = ?, bike = ?, kind = ? where id = ?"
        try:
            self._connect()
            result = self.execute(query, value)
        except Exception as exc:
            print("Erro ao atualizar ciclista!", exc)
        return result

    def delete(self, value):
        query = "delete from cyclist where id = ?"
        try:
            self._connect()
            result = self.execute(query, value)
        except Exception as exc:
            print("Erro ao deletar ciclista!", exc)
        return result

    def insert(self, value):
        query = "insert into cyclist values ( ?, ?, ?, ?, ? )"
        try:
            self._connect()
            result = self.execute(query, value)
        except Exception as exc:
            print("Erro ao inserir ciclista!", exc)
        return result


