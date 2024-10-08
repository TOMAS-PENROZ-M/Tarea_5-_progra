import tkinter as tk
from tkinter import messagebox
from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión Académica")
        self.geometry("600x600")

        # Crear un programa académico para la gestión
        self.programa_academico = ProgramaAcademico("Ingeniería de Sistemas", "IS2023")

        # Configurar los elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Sección para agregar estudiantes
        tk.Label(self, text="Agregar Estudiante").grid(row=0, column=0, pady=10)
        tk.Label(self, text="Nombre:").grid(row=1, column=0)
        tk.Label(self, text="Apellido:").grid(row=2, column=0)
        tk.Label(self, text="Matrícula:").grid(row=3, column=0)
        tk.Label(self, text="Carrera:").grid(row=4, column=0)
        tk.Label(self, text="Semestre:").grid(row=5, column=0)

        self.entry_nombre = tk.Entry(self)
        self.entry_apellido = tk.Entry(self)
        self.entry_matricula = tk.Entry(self)
        self.entry_carrera = tk.Entry(self)
        self.entry_semestre = tk.Entry(self)

        self.entry_nombre.grid(row=1, column=1)
        self.entry_apellido.grid(row=2, column=1)
        self.entry_matricula.grid(row=3, column=1)
        self.entry_carrera.grid(row=4, column=1)
        self.entry_semestre.grid(row=5, column=1)

        tk.Button(self, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=6, column=0, columnspan=2, pady=10)

        # Sección para agregar grupos
        tk.Label(self, text="Agregar Grupo").grid(row=7, column=0, pady=10)
        tk.Label(self, text="Número de Grupo:").grid(row=8, column=0)
        tk.Label(self, text="Asignatura:").grid(row=9, column=0)
        tk.Label(self, text="Profesor:").grid(row=10, column=0)

        self.entry_numero_grupo = tk.Entry(self)
        self.entry_asignatura = tk.Entry(self)
        self.entry_profesor = tk.Entry(self)

        self.entry_numero_grupo.grid(row=8, column=1)
        self.entry_asignatura.grid(row=9, column=1)
        self.entry_profesor.grid(row=10, column=1)

        tk.Button(self, text="Agregar Grupo", command=self.agregar_grupo).grid(row=11, column=0, columnspan=2, pady=10)

        # Sección para inscribir estudiantes a grupos
        tk.Label(self, text="Inscribir Estudiante a Grupo").grid(row=12, column=0, pady=10)
        tk.Label(self, text="Matrícula del Estudiante:").grid(row=13, column=0)
        tk.Label(self, text="Número de Grupo:").grid(row=14, column=0)

        self.entry_matricula_inscripcion = tk.Entry(self)
        self.entry_numero_grupo_inscripcion = tk.Entry(self)

        self.entry_matricula_inscripcion.grid(row=13, column=1)
        self.entry_numero_grupo_inscripcion.grid(row=14, column=1)

        tk.Button(self, text="Inscribir Estudiante", command=self.inscribir_estudiante).grid(row=15, column=0, columnspan=2, pady=10)

        # Sección para mostrar información
        tk.Button(self, text="Mostrar Información", command=self.mostrar_informacion).grid(row=16, column=0, columnspan=2, pady=20)

    def agregar_estudiante(self):
        """Agregar un estudiante al programa académico."""
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        matricula = self.entry_matricula.get()
        carrera = self.entry_carrera.get()
        semestre = self.entry_semestre.get()

        try:
            semestre = int(semestre)  # Convertir semestre a entero
            estudiante = Estudiante(nombre, apellido, "2000-01-01", matricula, carrera, semestre)  # Se puede ajustar la fecha
            self.programa_academico.agregar_grupo(estudiante)  # Esto debería ser a la lista de grupos
            messagebox.showinfo("Éxito", f"Estudiante {nombre} agregado.")
        except ValueError:
            messagebox.showerror("Error", "Semestre debe ser un número entero.")

    def agregar_grupo(self):
        """Agregar un grupo al programa académico."""
        numero_grupo = self.entry_numero_grupo.get()
        asignatura = self.entry_asignatura.get()
        profesor = self.entry_profesor.get()

        grupo = Grupo(int(numero_grupo), Asignatura(asignatura, "AS101", 5), Profesor(profesor, "Apellido", "1990-01-01", "P123", "Ingeniería"))
        self.programa_academico.agregar_grupo(grupo)

    def inscribir_estudiante(self):
        """Inscribir un estudiante a un grupo."""
        matricula = self.entry_matricula_inscripcion.get()
        numero_grupo = self.entry_numero_grupo_inscripcion.get()

        # Aquí deberías buscar el estudiante y el grupo correspondiente
        grupo = next((g for g in self.programa_academico.grupos if g.numero_grupo == int(numero_grupo)), None)
        if grupo:
            estudiante = next((e for e in self.programa_academico.grupos if e.matricula == matricula), None)
            if estudiante:
                grupo.agregar_estudiante(estudiante)
                messagebox.showinfo("Éxito", f"Estudiante {matricula} inscrito en el grupo {numero_grupo}.")
            else:
                messagebox.showerror("Error", f"Estudiante con matrícula {matricula} no encontrado.")
        else:
            messagebox.showerror("Error", f"Grupo {numero_grupo} no encontrado.")

    def mostrar_informacion(self):
        """Mostrar información de programas académicos y sus componentes."""
        info = f"Programa Académico: {self.programa_academico.nombre}\nGrupos:\n"
        for grupo in self.programa_academico.grupos:
            info += f"Grupo {grupo.numero_grupo}, Asignatura: {grupo.asignatura.nombre}\n"
            info += "Estudiantes:\n"
            for estudiante in grupo.estudiantes:
                info += f"  - {estudiante.nombre} {estudiante.apellido}\n"
        messagebox.showinfo("Información", info)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
