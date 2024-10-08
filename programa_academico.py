from grupo import Grupo

class Programa_academico:
    def __init__(self, nombre: str, codigo: str):
        self.__nombre = nombre
        self.__codigo = codigo
        self._grupos = []

    def agregar_grupo(self, grupo: Grupo):
        if grupo not in self._grupos:
            self._grupos.append(grupo)
        else:
            print("El grupo ya existe")

    def eliminar_grupo(self, numero_grupo:int):
        for grupo in self._grupos:
            if grupo.numero_grupo == numero_grupo:
                self._grupos.remove(grupo)
                break
        else:
            print("No se encontro al estudiante")