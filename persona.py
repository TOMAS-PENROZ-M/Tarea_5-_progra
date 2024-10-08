class Persona:
    def __init__(self, nom:str, ape:str, fe_na:str):
        self.__nombre = nom
        self.__apellido = ape
        self.__fecha_nac = fe_na

    def presentarse(self):
            print(f"Hola mi nombre es {self.nombre} {self.apellido} y naci el {self.fecha_de_nacimiento}")

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
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__apellido = valor
        else:
            raise ValueError("El apellido debe ser una cadena no vacia")
        
    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_nac
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__fecha_nac = valor
        else:
            raise ValueError("La fecha de nacimiento debe ser una cadena no vacia")
