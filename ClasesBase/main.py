import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from ClasesBase.persona import Persona
from ClasesBase.estudiante import Estudiante
from ClasesBase.profesor import Profesor
from ClasesBase.grupo import Grupo
from ClasesBase.programa_academico import Programa_academico

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x300")
root.title("Gestion Universitaria")

root.mainloop()