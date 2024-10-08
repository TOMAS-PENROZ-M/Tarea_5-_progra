from persona import Persona

class Estudiante(Persona):
    def __init__(self, nom: str, ape: str, fe_na: str, matricula: str, carrera: str, semestre: str):
        super().__init__(nom, ape, fe_na)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        
    @property
    def matricula(self):
        return self._matricula
    
    @property
    def carrera(self):
        return self._carrera
    
    @property
    def semestre(self):
        return self._semestre
    
    def estudiar(self, materia: str, horas: int):
        print(f"El estudiante a estado estudiando {materia} durante {horas} horas")

    def presentarse(self):
        super().presentarse()
        print(f"Soy estudiante de {self.carrera}, estoy en el semestre {self.semestre}, y mi matrícula es {self.matricula}")