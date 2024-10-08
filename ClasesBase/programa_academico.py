from ClasesBase.grupo import Grupo

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

    def mostrar_programa(self):
        print(f"Programa academico {self.__nombre} {self.__codigo}")
        if not self._grupos:
            print("No se encuentran grupos en este programa")
        else:
            for grupo in self._grupos:
                grupo.mostrar_grupo()
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")
        
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__codigo = valor
        else:
            raise ValueError("El codigo debe ser una cadena no vacia")

    @property   
    def grupos(self):
        return self._grupos