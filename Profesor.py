from Persona import Persona

class Profesor(Persona):
    """
    Clase que representa a un profesor, hereda de la clase Persona.

    Atributos:
    ----------
    _numero_empleado : str
        Número de empleado del profesor.
    _departamento : str
        Departamento en el que trabaja el profesor.
    """

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, numero_empleado: str, departamento: str):
        """
        Inicializa una instancia de la clase Profesor.

        Parámetros:
        -----------
        nombre : str
            Nombre del profesor.
        apellido : str
            Apellido del profesor.
        fecha_de_nacimiento : str
            Fecha de nacimiento del profesor.
        numero_empleado : str
            Número de empleado del profesor.
        departamento : str
            Departamento en el que trabaja el profesor.
        """
        # Llamar al constructor de la clase base Persona
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento

    # Propiedad para 'numero_empleado'
    @property
    def numero_empleado(self):
        """Devuelve el número de empleado del profesor."""
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, valor):
        """Establece el número de empleado del profesor."""
        if valor.strip():
            self._numero_empleado = valor
        else:
            raise ValueError("El número de empleado no puede estar vacío.")

    # Propiedad para 'departamento'
    @property
    def departamento(self):
        """Devuelve el departamento del profesor."""
        return self._departamento

    @departamento.setter
    def departamento(self, valor):
        """Establece el departamento del profesor."""
        if valor.strip():
            self._departamento = valor
        else:
            raise ValueError("El departamento no puede estar vacío.")

    # Método enseñar
    def enseñar(self, materia: str):
        """
        Imprime un mensaje indicando que el profesor está enseñando una materia.

        Parámetros:
        -----------
        materia : str
            La materia que el profesor está enseñando.
        """
        if materia.strip():
            print(f"{self._nombre} está enseñando {materia}.")
        else:
            raise ValueError("El nombre de la materia no puede estar vacío.")

    # Sobrescribir el método presentarse
    def presentarse(self):
        """Sobrescribe el método presentarse para incluir la información del profesor."""
        print(f"Hola, soy {self._nombre} {self._apellido}, profesor del departamento de {self._departamento}. Mi número de empleado es {self._numero_empleado}.")
