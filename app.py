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
        self.janela.title("Hermes&BresarGames©")
        self.janela.geometry("800x600")
        
        ctk.set_appearance_mode("dark")    
        self.janela.resizable(False, False)  # Define a janela como não redimensionável
        self.janela.configure(bg="black")
        
        # Passa a referência da própria instância para Telas        
        self.Telas_iniciais = Telas(root, self)
        self.tela_jogo = self.Telas_iniciais.tela_jogo # Tela de jogo agora já recebe Telas
        
        self.widgets_dinamicos = self.Telas_iniciais.widgets_dinamicos # traz de telas a Lista para armazenar widgets dinâmicos
        
        self.janelas_abertas = [] # para a função sair(main)


                       
        # Interface de incialização 
        self.Telas_iniciais.tela_01()
        #self.Telas_iniciais.tela_02()
        #self.Telas_iniciais.tela_03()
        #self.tela_jogo.tela_game()
        


    def sair_jogo(self):
        print("Função sair_jogo chamada")  # Verificação
        janela_confirmacao = ctk.CTkToplevel(self.janela)
        janela_confirmacao.title("EXIT")
        janela_confirmacao.geometry("200x150")
        janela_confirmacao.configure(bg="black")  
        janela_confirmacao.wm_attributes("-topmost", True)    
        self.janelas_abertas.append(janela_confirmacao) # Armazenar a janela Toplevel em uma lista
        
        # Texto de confirmação
        texto = ctk.CTkLabel(
            janela_confirmacao, 
            text="Exit Game?", 
            fg_color=None,  # Transparente
            text_color="white",  # Texto branco
            font=("Gelio Fasolada", 24)
        )
        texto.place(relx=0.5, rely=0.3, anchor="center")  # Centraliza o texto na janela

        # Botões de Sim e Não
        botao_sim = ctk.CTkButton(
            janela_confirmacao,
            width= 50,
            text="Yes",
            font=("Gelio Fasolada", 18),
            fg_color="green", 
            text_color="white",
            hover_color="darkgreen",
            command=lambda: self.confirmar_saida(janela_confirmacao)
        )
        botao_sim.place(relx=0.3, rely=0.7, anchor="center")  # Posiciona o botão Sim

        botao_nao = ctk.CTkButton(
            janela_confirmacao,
            width= 50,
            text="No",
            font=("Gelio Fasolada", 18),
            fg_color="red", 
            text_color="white",
            hover_color="darkred",
            command=janela_confirmacao.destroy
        )
        botao_nao.place(relx=0.7, rely=0.7, anchor="center")  # Posiciona o botão Não

    
    def confirmar_saida(self, janela_confirmacao):# Função auxiliar para confirmar saída
        print("Encerrando o programa...")
        janela_confirmacao.destroy()
        self.janela.destroy()  # Fecha a janela principal e encerra o programa

        
# def sair_jogo(self): # versão com janela de sistema - SIMPLES!
#     resposta = messagebox.askyesno("Confirmação", "Tem certeza de que deseja sair do jogo?")
#     if resposta:
#         print("Encerrando programa...")
#         self.janela.destroy()  # Fecha a janela principal e encerra o programa 
    
            
if __name__ == "__main__":
    root = ctk.CTk()
    app = Interface_Jogo(root)
    root.mainloop() 