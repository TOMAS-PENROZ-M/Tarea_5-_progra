class Persona:
    """
    Clase base que representa una persona.

    Atributos:
    ----------
    _nombre : str
        Nombre de la persona.
    _apellido : str
        Apellido de la persona.
    _fecha_de_nacimiento : str
        Fecha de nacimiento de la persona en formato "dd/mm/aaaa".
    """

    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str):
        """
        Inicializa una instancia de la clase Persona.

        Parámetros:
        -----------
        nombre : str
            Nombre de la persona.
        apellido : str
            Apellido de la persona.
        fecha_de_nacimiento : str
            Fecha de nacimiento de la persona en formato "dd/mm/aaaa".
        """
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento

    # Propiedad para 'nombre'
    @property
    def nombre(self):
        """Devuelve el nombre de la persona."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre de la persona."""
        if valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío.")

    # Propiedad para 'apellido'
    @property
    def apellido(self):
        """Devuelve el apellido de la persona."""
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        """Establece el apellido de la persona."""
        if valor.strip():
            self._apellido = valor
        else:
            raise ValueError("El apellido no puede estar vacío.")

    # Propiedad para 'fecha_de_nacimiento'
    @property
    def fecha_de_nacimiento(self):
        """Devuelve la fecha de nacimiento de la persona."""
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, valor):
        """Establece la fecha de nacimiento de la persona."""
        if valor.strip():
            self._fecha_de_nacimiento = valor
        else:
            raise ValueError("La fecha de nacimiento no puede estar vacía.")

    # Método para presentar a la persona
    def presentarse(self):
        """Imprime una presentación genérica de la persona."""
        print(f"Hola, soy {self._nombre} {self._apellido}. Nací el {self._fecha_de_nacimiento}.")
