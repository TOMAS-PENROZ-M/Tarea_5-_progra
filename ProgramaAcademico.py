class ProgramaAcademico:
    """
    Clase que representa un programa académico.

    Atributos:
    ----------
    _nombre : str
        Nombre del programa académico.
    _codigo : str
        Código del programa académico.
    _grupos : List[Grupo]
        Lista de grupos asociados al programa académico.
    """

    def __init__(self, nombre: str, codigo: str):
        self._nombre = nombre
        self._codigo = codigo
        self._grupos = []  # Lista protegida para almacenar objetos Grupo

    # Propiedades
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str):
        self._codigo = valor

    @property
    def grupos(self):
        return self._grupos

    def agregar_grupo(self, grupo):
        """Agrega un grupo al programa académico, evitando duplicados."""
        if grupo.numero_grupo not in [g.numero_grupo for g in self._grupos]:
            self._grupos.append(grupo)
            print(f"Grupo {grupo.numero_grupo} agregado al programa académico {self._nombre}.")
        else:
            print(f"El grupo {grupo.numero_grupo} ya existe en el programa académico {self._nombre}.")

    def eliminar_grupo(self, numero_grupo: int):
        """Elimina un grupo del programa académico por su número."""
        grupo_a_eliminar = next((g for g in self._grupos if g.numero_grupo == numero_grupo), None)
        if grupo_a_eliminar:
            self._grupos.remove(grupo_a_eliminar)
            print(f"Grupo {numero_grupo} eliminado del programa académico {self._nombre}.")
        else:
            print(f"El grupo {numero_grupo} no existe en el programa académico {self._nombre}.")

    def mostrar_programa(self):
        """Muestra la información completa del programa académico."""
        print(f"Programa Académico: {self._nombre}, Código: {self._codigo}")
        print("Grupos asociados:")
        for grupo in self._grupos:
            grupo.mostrar_grupo()  # Asegúrate de que el método mostrar_grupo esté implementado en la clase Grupo
