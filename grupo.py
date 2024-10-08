from profesor import Profesor

class Grupo:
    def __init__(self, numero_grupo: int, asignatura: Asignatura, profesor: Profesor):
        self.__numero_grupo = numero_grupo
        self.__asignatura = asignatura
        self.__profesor = profesor
        self._estudiantes = []

    def agregar_estudiante(self, estudiante: Estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)
        else:
            print("El estudiante ya esta en el grupo")

    def eliminar_estudiante(self, matricula: str):
        for estudiante in self._estudiantes:
            if estudiante.matricula == matricula:
                self._estudiantes.remove(estudiante)
                break
        else:
            print("No se encontro al estudiante")

    def mostrar_grupo(self):
        print(f"Grupo: {self.__numero_grupo}")
        self.profesor.presentarse()
        print("Lista de estudiantes")
        for estudiante in self._estudiantes:
            estudiante.presentarse()
    
    @property
    def numero_grupo(self):
        return self.__numero_grupo
    @numero_grupo.setter
    def numero_grupo(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__numero_grupo =valor
        else:
            raise ValueError("El numero de grupo de ser un entero positivo")
        
    @property
    def asignatura(self):
        return self.__asignatura
    @asignatura.setter
    def asignatura(self, valor):
        if isinstance(valor, Asignatura):
            self.__asignatura =valor
        else:
            raise ValueError("La asignatura de ser un objeto de tipo Asignatura")
        
    @property
    def profesor(self):
        return self.__profesor
    @profesor.setter
    def profesor(self, valor):
        if isinstance(valor, Profesor):
            self.__profesor =valor
        else:
            raise ValueError("El profesor de ser un objeto de tipo Profesor")
        
    @property
    def estudiantes(self):
        return self._estudiantes