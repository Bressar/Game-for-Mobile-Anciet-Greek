# Versão do Jogo Grécia, para desktop

# import os
# import shutil # para salvar as imagens dos cartões

from PIL import Image, ImageDraw, ImageFont, ImageTk
#from PIL import ImageWin
# import qrcode
# import sqlite3
# import json
# import webbrowser

import tkinter as tk
from tkinter import filedialog, messagebox, Label, Tk, Canvas
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from telas import Telas

#ctk.set_appearance_mode("dark" )  # Modo de aparência: System", "dark" ou "light"


class Interface_Jogo:
    def __init__(self, root):
        self.janela = root
        self.janela.title("Ascent To Olympus")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)  # Define a janela como não redimensionável
        self.Telas = Telas(root)
        self.widgets_dinamicos = self.Telas.widgets_dinamicos # traz de telas a Lista para armazenar widgets dinâmicos
        self.janela.configure(bg="black")

        
                       
        # Interface de incialização 
        #self.Telas.tela_01()
        self.Telas.tela_02()
      
      
if __name__ == "__main__":
    root = ctk.CTk()
    app = Interface_Jogo(root)
    root.mainloop() 