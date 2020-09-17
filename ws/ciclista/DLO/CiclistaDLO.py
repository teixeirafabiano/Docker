from ciclista.DTO.CiclistaDTO import CiclistaDTO
from ciclista.DAO.CiclistaDAO import CiclistaDAO

class CiclistaDLO:

    def __init__(self):
        pass

    def selectByEmail(self, column, value):
        objDao = CiclistaDAO()
        lstCiclista = []

        try:
            result = objDao.select(column, value)
            for i in range(0, len(result)):
                lstCiclista.append(CiclistaDTO(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

        except Exception as exc:
            print("Erro ao buscar ciclista pelo email!", exc)
        return lstCiclista

    def selectById(self, column, value):
        objDao = CiclistaDAO()
        lstCiclista = []

        try:
            result = objDao.select(column, value)
            for i in range(0, len(result)):
                lstCiclista.append(CiclistaDTO(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

        except Exception as exc:
            print("Erro ao buscar ciclista pelo id!", exc)
        return lstCiclista

    def deleteById(self, value):
        objDao = CiclistaDAO()
        try:
            result = objDao.delete(value)
        except Exception as exc:
            print("Erro ao deletar ciclista!", exc)
        return result

    def updateById(self, value):
        objDao = CiclistaDAO()
        try:
            result = objDao.update(value)
        except Exception as exc:
            print("Erro ao atualizar ciclista!", exc)
        return result

    def insert(self, value):
        objDao = CiclistaDAO()
        try:
            result = objDao.insert(value)
        except Exception as exc:
            print("Erro ao inserir ciclista!", exc)
        return result