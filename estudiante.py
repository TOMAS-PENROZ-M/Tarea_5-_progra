from persona import Persona

class Estudiante(Persona):
    def __init__(self, nom: str, ape: str, fe_na: str, matricula: str, carrera: str, semestre: str):
        super().__init__(nom, ape, fe_na)
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        
    @property
    def matricula(self):
        return self.matricula
    
    @property
    def carrera(self):
        return self.carrera
    
    @property
    def semestre(self):
        return self.semestre
    
    def estudiar(self, materia: str, horas: int):
        print(f"El estudiante a estado estudiando {materia} durante {horas} horas")