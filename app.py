# Versão do Jogo Grécia, para desktop

# import os
# import shutil # para salvar as imagens dos cartões

from PIL import Image, ImageDraw, ImageFont, ImageTk
#from PIL import ImageWin
# import qrcode
# import sqlite3
# import json
# import webbrowser

#ctk.set_appearance_mode("dark" )  # Modo de aparência: System", "dark" ou "light"

import tkinter as tk
from tkinter import filedialog, messagebox, Label, Tk, Canvas
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from telas_iniciais import Telas
from tela_jogo import Tela_Jogo


class Interface_Jogo:
    def __init__(self, root):
        self.janela = root
        self.janela.title("BresarGames©")
        self.janela.geometry("800x600")
        
        ctk.set_appearance_mode("dark")
    
        self.janela.resizable(False, False)  # Define a janela como não redimensionável
        self.Telas_iniciais = Telas(root)
        
        # Tela de jogo agora já recebe Telas
        self.tela_jogo = self.Telas_iniciais.tela_jogo
        
        self.widgets_dinamicos = self.Telas_iniciais.widgets_dinamicos # traz de telas a Lista para armazenar widgets dinâmicos
        self.janela.configure(bg="black")

                       
        # Interface de incialização 
        #self.Telas_iniciais.tela_01()
        #self.Telas_iniciais.tela_03()
        self.tela_jogo.tela_game()
        
      
      
if __name__ == "__main__":
    root = ctk.CTk()
    app = Interface_Jogo(root)
    root.mainloop() 