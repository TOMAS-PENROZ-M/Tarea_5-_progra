from typing import List
from Estudiante import Estudiante
from Asignatura import Asignatura
from Profesor import Profesor

class Grupo:
    """
    Clase que representa un grupo académico.

    Atributos:
    ----------
    _numero_grupo : int
        Número del grupo.
    _asignatura : Asignatura
        Asignatura del grupo.
    _profesor : Profesor
        Profesor asignado al grupo.
    _estudiantes : List[Estudiante]
        Lista de estudiantes en el grupo.
    """

    def __init__(self, numero_grupo: int, asignatura: Asignatura, profesor: Profesor):
        """
        Inicializa una instancia de la clase Grupo.

        Parámetros:
        -----------
        numero_grupo : int
            Número del grupo.
        asignatura : Asignatura
            Asignatura del grupo.
        profesor : Profesor
            Profesor asignado al grupo.
        """
        self._numero_grupo = numero_grupo
        self._asignatura = asignatura
        self._profesor = profesor
        self._estudiantes: List[Estudiante] = []

    # Propiedad para 'numero_grupo'
    @property
    def numero_grupo(self):
        """Devuelve el número del grupo."""
        return self._numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, valor: int):
        """Establece el número del grupo."""
        if isinstance(valor, int) and valor > 0:
            self._numero_grupo = valor
        else:
            raise ValueError("El número del grupo debe ser un número entero positivo.")

    # Propiedad para 'asignatura'
    @property
    def asignatura(self):
        """Devuelve la asignatura del grupo."""
        return self._asignatura

    @asignatura.setter
    def asignatura(self, valor: Asignatura):
        """Establece la asignatura del grupo."""
        if isinstance(valor, Asignatura):
            self._asignatura = valor
        else:
            raise ValueError("El valor debe ser una instancia de la clase Asignatura.")

    # Propiedad para 'profesor'
    @property
    def profesor(self):
        """Devuelve el profesor asignado al grupo."""
        return self._profesor

    @profesor.setter
    def profesor(self, valor: Profesor):
        """Establece el profesor asignado al grupo."""
        if isinstance(valor, Profesor):
            self._profesor = valor
        else:
            raise ValueError("El valor debe ser una instancia de la clase Profesor.")

    # Propiedad para 'estudiantes'
    @property
    def estudiantes(self):
        """Devuelve la lista de estudiantes en el grupo."""
        return self._estudiantes

    # Método para agregar estudiante
    def agregar_estudiante(self, estudiante: Estudiante):
        """Agrega un estudiante al grupo si no existe ya en la lista."""
        if not any(e.matricula == estudiante.matricula for e in self._estudiantes):
            self._estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} {estudiante.apellido} agregado al grupo {self._numero_grupo}.")
        else:
            print(f"El estudiante con matrícula {estudiante.matricula} ya está en el grupo.")

    # Método para eliminar estudiante
    def eliminar_estudiante(self, matricula: str):
        """Elimina un estudiante del grupo por su matrícula."""
        for estudiante in self._estudiantes:
            if estudiante.matricula == matricula:
                self._estudiantes.remove(estudiante)
                print(f"Estudiante {estudiante.nombre} {estudiante.apellido} eliminado del grupo {self._numero_grupo}.")
                return
        print(f"No se encontró un estudiante con matrícula {matricula} en el grupo.")

    # Método para mostrar información del grupo
    def mostrar_grupo(self):
        """Muestra la información completa del grupo."""
        print(f"Número de Grupo: {self._numero_grupo}")
        print(f"Asignatura: {self._asignatura.nombre}, Código: {self._asignatura.codigo}, Créditos: {self._asignatura.creditos}")
        print(f"Profesor: {self._profesor.nombre} {self._profesor.apellido}, Número de Empleado: {self._profesor.numero_empleado}")
        print("Estudiantes en el grupo:")
        if not self._estudiantes:
            print("No hay estudiantes en el grupo.")
        else:
            for estudiante in self._estudiantes:
                print(f"- {estudiante.nombre} {estudiante.apellido}, Matrícula: {estudiante.matricula}")

