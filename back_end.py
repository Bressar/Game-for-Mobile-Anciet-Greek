# Funcionalidades do jogo
# criado:  18/12/24
# atualizado: 18/12/24

import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage

class Back_End:
    def __init__(self):
        self.personagem_escolhido = None
        self.cartas_player = [] # cartas do jogador na partida
        self.cartas_deuses = [] # todas as cartas
        
        
    def load_font(self, font_path):  # Método para carregar fontes personalizadas
        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20
        pathbuf = ctypes.create_unicode_buffer(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(pathbuf, FR_PRIVATE | FR_NOT_ENUM, 0)


    def load_fonts(self):  # Método para inicializar e verificar fontes
        self.load_font("fonts/Gelio Fasolada.ttf")
        self.load_font("fonts/OlympusBold.ttf")        
        # Verifica as fontes carregadas
        #print("Fontes disponíveis:", font.families())  # Opcional: listar todas as fontes disponíveis 
        
  
  
  
        
    def escolher_personagem(self, personagem=None):
        self.personagem_escolhido = personagem
        print(f"Personagem escolhido foi {self.personagem_escolhido}")
        
        
    def escolher_carta(self, carta=None): # implementar
        pass
        # self.cartas_player.append(carta)
        # print(f"Personagem escolhido foi {self.personagem_escolhido}")
        
    