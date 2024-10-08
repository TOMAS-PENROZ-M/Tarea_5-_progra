from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

def main():
    # Crear instancias de estudiantes
    estudiante1 = Estudiante("Juan", "Pérez", "1998-05-12", "20230001", "Ingeniería", 2)
    estudiante2 = Estudiante("Ana", "Gómez", "2000-08-20", "20230002", "Ingeniería", 1)
    estudiante3 = Estudiante("Luis", "Martínez", "1999-02-15", "20230001", "Ingeniería", 3)

    # Crear instancia de un profesor
    profesor1 = Profesor("Carlos", "Fernández", "1985-04-15", "P123", "Ingeniería")

    # Crear instancia de una asignatura
    asignatura1 = Asignatura("Matemáticas", "MAT101", 5)

    # Crear instancia de un grupo
    grupo1 = Grupo(1, asignatura1, profesor1)

    # Agregar estudiantes al grupo
    grupo1.agregar_estudiante(estudiante1)
    grupo1.agregar_estudiante(estudiante2)

    # Intentar agregar un estudiante duplicado
    grupo1.agregar_estudiante(estudiante1)  # Debería mostrar un mensaje de duplicado

    # Mostrar información del grupo
    grupo1.mostrar_grupo()

    # Eliminar un estudiante del grupo
    grupo1.eliminar_estudiante("20230002")
    grupo1.eliminar_estudiante("20230002")  # Intentar eliminar un estudiante que no está en el grupo

    # Mostrar información actualizada del grupo
    grupo1.mostrar_grupo()

    # Crear instancia de un programa académico
    programa_academico = ProgramaAcademico("Ingeniería de Sistemas", "IS2023")

    # Agregar grupo al programa académico
    programa_academico.agregar_grupo(grupo1)

    # Intentar agregar un grupo duplicado
    programa_academico.agregar_grupo(grupo1)  # Debería mostrar un mensaje de duplicado

    # Mostrar información del programa académico
    programa_academico.mostrar_programa()

    # Eliminar un grupo del programa académico
    programa_academico.eliminar_grupo(1)
    programa_academico.eliminar_grupo(1)  # Intentar eliminar un grupo que no está en el programa

    # Mostrar información actualizada del programa académico
    programa_academico.mostrar_programa()

if __name__ == "__main__":
    main()
