# Funcionalidades do jogo
# criado:  18/12/24
# atualizado: 18/12/24

import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import random
from random import randint

class Back_End:
    def __init__(self):
        print(f"Instância de Back_End criada: {id(self)}") # for debug
        self.personagem_escolhido_nome = "No Name"
        self.personagem_escolhido_about = "Return and select a player\nto start"
        self.personagem_escolhido_imagem = None
        
        self.carta_inicial = [{
            "nome": "No name",
            "action": "Return and select a card to start",
            "imagem": "images/carta_default.png",
            "imagem_pequena": "images/carta_menu.png"
        }]
        # Só pode ter 1 carta
        self.cartas_player = [{
        "nome": "cartinha 1",
        "action": "Return and select a card to start",
        "imagem": "images/carta_default.png",
        "imagem_pequena": "images/carta_menu.png"
         },
         {
        "nome": "cartinha 2",
        "action": "Return and select a card to start",
        "imagem": "images/carta_default.png",
        "imagem_pequena": "images/carta_menu.png"
         },
         {
        "nome": "cartinha 3",
        "action": "Return and select a card to start",
        "imagem": "images/carta_default.png",
        "imagem_pequena": "images/carta_menu.png"
         }] # cartas do jogador na partida, máximo 3 cartas
        
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
        
        # dicionário dos personagens em jogo
        self.personagens_jogo = [
            {
            "nome" : "Hippolyta",
            "about":  """Queen of the Amazons: A powerful warrior 
and ruler of a legendary race of female warriors.
She wants to reach Olympus to attain 
the status of a demigoddess.""",
            "imagem": "images/hipolita.png"},
            
            {"nome" : "Odysseus",
             "about":  """King of Ithaca, outsmarts monsters and gods
on his epic journey home after the Trojan War.
He wants to reach Olympus to attain
the status of a demigod.""",
             "imagem": "images/odisseu.png"},
            
            {"nome" : "Achilles",
             "about": """The greatest Greek warrior,
possesses invulnerability (except for a heel).
He wants to reach Olympus to attain
the status of a demigod.""",
             "imagem": "images/aquiles.png"},
            
            {"nome" : "Atalanta",
             "about": """The Unbeatable Huntress: A Timeless 
Symbol of Female Strength and Independence.
He wants to reach Olympus to attain
the status of a demigod.""",
             "imagem": "images/atalanta.png"},
            
            {"nome" : "Theseus",
             "about": """The hero who conquered the Minotaur,
united the lands of Attica, and became king.
He wants to reach Olympus to attain
the status of a demigod.""",
             "imagem": "images/teseu.png"}
        ]
            
        # Todas as cartas do jogo
        self.cartas_deuses = [
        {
            "nome": "Aphrodite",
            "action": "Advance 6 spaces",
            "imagem": "images/carta_aphrodite.png",
            "imagem_pequena": "images/carta_aphrodite_p.png"
        },
        {
            "nome": "Apollo",
            "action": "Roll 2 dice",
            "imagem": "images/carta_apollo.png",
            "imagem_pequena": "images/carta_apollo_p.png"
        },
        {
            "nome": "Artemis",
            "action": "Advance 3 spaces, or roll 1 die",
            "imagem": "images/carta_artemis.png",
            "imagem_pequena": "images/carta_artemis_p.png"
        },
        {
            "nome": "Ares",
            "action": "Win 1 battle, or roll 1 die",
            "imagem": "images/carta_ares.png",
            "imagem_pequena": "images/carta_ares_p.png"
        },
        {
            "nome": "Hades",
            "action": "Gain one life",
            "imagem": "images/carta_hades.png",
            "imagem_pequena": "images/carta_hades_p.png"
        },
        {
            "nome": "Hephaestus",
            "action": "Roll 1 die again",
            "imagem": "images/carta_hephaestus.png",
            "imagem_pequena": "images/carta_hephaestus_p.png"
        },
        {
            "nome": "Hera",
            "action": "Gain one life, or roll 1 die",
            "imagem": "images/carta_hera.png",
            "imagem_pequena": "images/carta_hera_p.png"
        },
        {
            "nome": "Hermes",
            "action": "Advance 5 spaces, or skip 1 space",
            "imagem": "images/carta_hermes.png",
            "imagem_pequena": "images/carta_hermes_p.png"
        },
        {
            "nome": "Persephone",
            "action": "Go back 1, 2, or 3 spaces",
            "imagem": "images/carta_persephone.png",
            "imagem_pequena": "images/carta_persephone_p.png"
        },
        {
            "nome": "Poseidon",
            "action": "Advance 4 spaces, or roll 1 die",
            "imagem": "images/carta_poseidon.png",
            "imagem_pequena": "images/carta_poseidon_p.png"
        },
        {
            "nome": "Zeus",
            "action": "Advance 6 spaces, or roll 2 dice",
            "imagem": "images/carta_zeus.png",
            "imagem_pequena": "images/carta_zeus_p.png"
        },
         {
            "nome": "Athena",
            "action": "Win 1 battle, or advance 2 spaces",
            "imagem": "images/carta_athena.png",
            "imagem_pequena": "images/carta_athena_p.png"
        }
    ]
      
        self.dic_cards = {
            "1": self.cartas_deuses[0],   # Aphrodite
            "2": self.cartas_deuses[1],   # Apollo
            "3": self.cartas_deuses[2],   # Artemis
            "4": self.cartas_deuses[3],   # Ares
            "5": self.cartas_deuses[4],   # Hades
            "6": self.cartas_deuses[5],   # Hephaestus
            "7": self.cartas_deuses[6],   # Hera
            "8": self.cartas_deuses[7],   # Hermes
            "9": self.cartas_deuses[8],   # Persephone
            "10": self.cartas_deuses[9],  # Poseidon
            "11": self.cartas_deuses[10],  # Zeus
            "12": self.cartas_deuses[11]  # Atena
        }


    def escolher_carta(self):
        # Sorteia um número aleatório entre 1 e 12
        numero_sorteado = str(random.randint(1, 12))  # Convertido para string, pois as chaves no dic_cards são strings

        # Atualiza a carta inicial com a carta sorteada
        self.carta_inicial[0] = self.dic_cards[numero_sorteado]

        # Substitui a carta que está no índice 0 da lista cartas_player
        if not self.cartas_player:
            # Se a lista estiver vazia, inicializa com a carta sorteada
            self.cartas_player.append(self.carta_inicial[0])
        else:
            # Se já existir uma carta no índice 0, substitui a carta
            self.cartas_player[0] = self.carta_inicial[0]

        # Garante que a lista de cartas do jogador não exceda o limite de 3
        if len(self.cartas_player) > 3:
            self.cartas_player = self.cartas_player[:3]  # Mantém apenas os primeiros 3 elementos

        # Exibe as informações da carta sorteada
        carta_sorteada = self.carta_inicial[0]
        print(f"**Carta Sorteada:** {carta_sorteada['nome']}")
        print(f"Ação: {carta_sorteada['action']}")
        print(f"Imagem: {carta_sorteada['imagem']}")

        # Debug: Exibe todas as cartas do jogador
        print("**Cartas do Jogador:**")
        for carta in self.cartas_player:
            print(f"- {carta['nome']}: {carta['action']}")
            print(f"- {carta['imagem']}: {carta['imagem_pequena']}")
      
        
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
        

    def escolher_personagem(self, nome_personagem):
        # Busca os dados do personagem no dicionário
        personagem = next(
            (p for p in self.personagens_jogo if p["nome"].lower() == nome_personagem.lower()), None
        )
        if personagem:
            self.personagem_escolhido_nome = personagem["nome"]
            self.personagem_escolhido_about = personagem["about"]
            self.personagem_escolhido_imagem = personagem["imagem"]
            print(f"Personagem escolhido foi {self.personagem_escolhido_nome}\n"
                  f"Texto personagem: {self.personagem_escolhido_about}\n"
                  f"Imagem do personagem: {self.personagem_escolhido_imagem}")
        else:
            print(f"Personagem {nome_personagem} não encontrado!")
            
        
