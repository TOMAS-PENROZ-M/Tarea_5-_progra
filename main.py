import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from persona import Persona
from estudiante import Estudiante
from profesor import Profesor
from grupo import Grupo
from programa_academico import Programa_academico

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x300")
root.title("Gestion Universitaria")

root.mainloop()