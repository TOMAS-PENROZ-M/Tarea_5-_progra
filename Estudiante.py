from Persona import Persona

class Estudiante(Persona):
    """
    Clase que representa a un estudiante, hereda de la clase Persona.

    Atributos:
    ----------
    _matricula : str
        Matrícula del estudiante.
    _carrera : str
        Carrera que cursa el estudiante.
    _semestre : int
        Semestre actual del estudiante.
    """

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, matricula: str, carrera: str, semestre: int):
        """
        Inicializa una instancia de la clase Estudiante.

        Parámetros:
        -----------
        nombre : str
            Nombre del estudiante.
        apellido : str
            Apellido del estudiante.
        fecha_de_nacimiento : str
            Fecha de nacimiento del estudiante.
        matricula : str
            Matrícula del estudiante.
        carrera : str
            Carrera que cursa el estudiante.
        semestre : int
            Semestre actual del estudiante.
        """
        # Llamar al constructor de la clase base Persona
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre

    # Propiedad para 'matricula'
    @property
    def matricula(self):
        """Devuelve la matrícula del estudiante."""
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        """Establece la matrícula del estudiante."""
        if valor.strip():
            self._matricula = valor
        else:
            raise ValueError("La matrícula no puede estar vacía.")

    # Propiedad para 'carrera'
    @property
    def carrera(self):
        """Devuelve la carrera que cursa el estudiante."""
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        """Establece la carrera que cursa el estudiante."""
        if valor.strip():
            self._carrera = valor
        else:
            raise ValueError("La carrera no puede estar vacía.")

    # Propiedad para 'semestre'
    @property
    def semestre(self):
        """Devuelve el semestre del estudiante."""
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        """Establece el semestre del estudiante."""
        if isinstance(valor, int) and valor > 0:
            self._semestre = valor
        else:
            raise ValueError("El semestre debe ser un número entero positivo.")

    # Método estudiar
    def estudiar(self, materia: str, horas: int):
        """
        Imprime un mensaje indicando que el estudiante ha estudiado una materia durante cierta cantidad de horas.

        Parámetros:
        -----------
        materia : str
            La materia que el estudiante ha estudiado.
        horas : int
            La cantidad de horas que el estudiante ha dedicado a estudiar.
        """
        if materia.strip() and isinstance(horas, int) and horas > 0:
            print(f"{self._nombre} ha estudiado {materia} durante {horas} horas.")
        else:
            raise ValueError("Los datos de la materia o las horas de estudio no son válidos.")

    # Sobrescribir el método presentarse
    def presentarse(self):
        """Sobrescribe el método presentarse para incluir la información del estudiante."""
        print(f"Hola, soy {self._nombre} {self._apellido}, estudiante de {self._carrera}, actualmente en el semestre {self._semestre}. Mi matrícula es {self._matricula}.")
