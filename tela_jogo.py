# tela onde o jogo se desenrola..import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from PIL import Image, ImageDraw, ImageFont, ImageTk

from back_end import Back_End

class Tela_Jogo:
    def __init__(self, root, telas_iniciais):
        self.root = root  # Referência à janela principal
        self.widgets_dinamicos = []  # Lista para armazenar widgets dinâmicos
          
        self.back_end = Back_End()
        self.back_end.load_fonts()
        
        # Referência à instância de Telas
        self.telas_iniciais = telas_iniciais  
        
    
    
    def tela_game(self):
        self.canvas_abre = Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas_abre.place(x=0, y=0) 
        self.widgets_dinamicos.append(self.canvas_abre)
        
        # Botão de sair
        botao_avancar = ctk.CTkButton(
        self.canvas_abre,
        width=50,
        fg_color='black',
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="EXIT",
        font=("Gelio Fasolada", 18),
        command=lambda: self.telas_iniciais.tela_03() # acrescentar função de saída!!!!
        

        )
        botao_avancar.place(x=520, y=550)
        self.widgets_dinamicos.append(botao_avancar)
        
        
        
        