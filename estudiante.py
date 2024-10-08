from persona import Persona

class Estudiante(Persona):
    def __init__(self, nom: str, ape: str, fe_na: str, matricula: str, carrera: str, semestre: str):
        super().__init__(nom, ape, fe_na)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre

    def estudiar(self, materia: str, horas: int):
        print(f"{self.nombre} a estado estudiando {materia} durante {horas} horas")

    def presentarse(self):
        super().presentarse()
        print(f"Hola soy {self.nombre} {self.apellido} estudiante de {self.carrera}, estoy en el semestre {self.semestre}, y mi matrícula es {self.matricula}")
        
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @property
    def carrera(self):
        return self.__carrera
    @carrera.setter
    def carrera(self, valor):
        self.__carrera = valor
    
    @property
    def semestre(self):
        return self.__semestre
    @semestre.setter
    def semestre(self, valor):
        self.__semestre = valor