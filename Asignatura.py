class Asignatura:
    """
    Clase que representa una asignatura.

    Atributos:
    ----------
    _nombre : str
        Nombre de la asignatura.
    _codigo : str
        Código de la asignatura.
    _creditos : int
        Créditos de la asignatura.
    """

    def __init__(self, nombre: str, codigo: str, creditos: int):
        """
        Inicializa una instancia de la clase Asignatura.

        Parámetros:
        -----------
        nombre : str
            Nombre de la asignatura.
        codigo : str
            Código de la asignatura.
        creditos : int
            Créditos de la asignatura.
        """
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    # Propiedad para 'nombre'
    @property
    def nombre(self):
        """Devuelve el nombre de la asignatura."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre de la asignatura."""
        if valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre de la asignatura no puede estar vacío.")

    # Propiedad para 'codigo'
    @property
    def codigo(self):
        """Devuelve el código de la asignatura."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """Establece el código de la asignatura."""
        if valor.strip():
            self._codigo = valor
        else:
            raise ValueError("El código de la asignatura no puede estar vacío.")

    # Propiedad para 'creditos'
    @property
    def creditos(self):
        """Devuelve los créditos de la asignatura."""
        return self._creditos

    @creditos.setter
    def creditos(self, valor):
        """Establece los créditos de la asignatura."""
        if isinstance(valor, int) and valor > 0:
            self._creditos = valor
        else:
            raise ValueError("Los créditos deben ser un número entero positivo.")

    # Método mostrar_informacion
    def mostrar_informacion(self):
        """Imprime la información detallada de la asignatura."""
        print(f"Asignatura: {self._nombre}, Código: {self._codigo}, Créditos: {self._creditos}")
