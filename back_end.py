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
        self.cores_layout = {
            'branco': "#FFFFFF", # branco
            'azul': "#4DC2F5",   # (0.3, 0.76, 0.96, 1)
            'verde': "#2DCD70",  # (0.18, 0.8, 0.44)
            'amarelo': "#F1C20D",  # (0.94, 0.76, 0.05)
            'laranja': "#FF8A65",  # (255/255, 138/255, 101/255)
            'vermelho': "#D32F2F",  # (211/255, 47/255, 47/255)
            'rosa': "#F48FB1",  # (244/255, 143/255, 177/255)
            'roxo': "#9575CD"   # (149/255, 117/255, 205/255)
        }
        # deixar no default quando terminar o layout
        self.cor_layout_atual = self.cores_layout['branco'] #"default de layout texto branco
        
        
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
        
    
        
    
