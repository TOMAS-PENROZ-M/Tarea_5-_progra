from persona import Persona

class Profesor(Persona):
    def __init__(self, nom: str, ape: str, fe_na: str, num_emp: str, depa: str):
        super().__init__(nom, ape, fe_na)
        self._numero_empleado = num_emp
        self._departamento = depa

    def enseñar(self, materia: str):
        print(f"El profesor esta enseñando {materia}")
    
    def presentarse(self):
        super().presentarse()
        print(f"Hola soy el profesor del departamento {self.departamento} y mi numero de empleado es {self.numero_empleado}")

    @property
    def numero_empleado(self):
        return self._numero_empleado
        
    @numero_empleado.setter
    def numero_empleado(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._numero_empleado = valor
        else:
            raise ValueError("El numero de empleado debe ser una cadena no vacia")
        
    @property
    def departamento(self):
        return self._departamento
        
    @departamento.setter
    def departamento(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._departamento = valor
        else:
            raise ValueError("El departamento debe ser una cadena no vacia")