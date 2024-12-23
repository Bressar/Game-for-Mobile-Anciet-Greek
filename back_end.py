# Funcionalidades do jogo
# criado:  18/12/24
# atualizado: 22/12/24

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
        
        self.player_xp = 3
        self.player_pontos = 0    
        self.casa_atual = 1 # Inicializando com a casa 1
        
        self.observadores = []  # Lista de observadores
        
        self.carta_inicial = [{
            "nome": "No name",
            "action": "Return and select a card to start",
            "action_p": """Return and select
a card to start""",
            "imagem": "images/carta_default.png",
            "imagem_pequena": "images/carta_menu.png"
        }]
        
        self.carta_casa_deus = [ {
            "nome": "Persephone",
            "action": "Go back 1, 2, or 3 spaces",
            "action_p": """Return and select
a card to start""",
            "imagem": "images/carta_persephone.png",
            "imagem_pequena": "images/carta_persephone_p.png"
        }]
        # Só pode ter 1 carta no inicio
        self.cartas_player = [  ] # cartas do jogador na partida, máximo 3 cartas
                
        self.cores_layout = {
            'branco': "#FFFFFF", # branco
            'azul': "#4DC2F5",   # (0.3, 0.76, 0.96, 1)
            'verde': "#2DCD70",  # (0.18, 0.8, 0.44)
            'amarelo': "#F1C20D",  # (0.94, 0.76, 0.05)
            'laranja': "#FF8A65",  # (255/255, 138/255, 101/255)
            'vermelho': "#D32F2F",  # (211/255, 47/255, 47/255)
            'rosa': "#F48FB1",  # (244/255, 143/255, 177/255)
            'roxo': "#9575CD",   # (149/255, 117/255, 205/255)
            'agua': "#5FD3C1",
        }
        # deixar no default quando terminar o layout
        
        self.cor_layout_atual = self.cores_layout['azul'] #"default de layout texto azul
        
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
            "action_p": """Advance
6 spaces""",
            "imagem": "images/carta_aphrodite.png",
            "imagem_pequena": "images/carta_aphrodite_p.png"
        },
        {
            "nome": "Apollo",
            "action": "Roll 2 dice",
            "action_p": """Roll
2 dice""",
            "imagem": "images/carta_apollo.png",
            "imagem_pequena": "images/carta_apollo_p.png"
        },
        {
            "nome": "Artemis",
            "action": "Advance 3 spaces, or roll 1 die",
            "action_p": """Advance
3 spaces,
or roll
1 die""",
            "imagem": "images/carta_artemis.png",
            "imagem_pequena": "images/carta_artemis_p.png"
        },
        {
            "nome": "Ares",
            "action": "Win 1 battle, or roll 1 die",
            "action_p": """Win
1 battle,
or roll
1 die""",
            "imagem": "images/carta_ares.png",
            "imagem_pequena": "images/carta_ares_p.png"
        },
        {
            "nome": "Hades",
            "action": "Gain one life",
            "action_p": """Gain
1 life""",
            "imagem": "images/carta_hades.png",
            "imagem_pequena": "images/carta_hades_p.png"
        },
        {
            "nome": "Hephaestus",
            "action": "Roll 1 die again",
            "action_p": """Roll
1 die
again""",
            "imagem": "images/carta_hephaestus.png",
            "imagem_pequena": "images/carta_hephaestus_p.png"
        },
        {
            "nome": "Hera",
            "action": "Gain one life, or roll 1 die",
            "action_p": """Gain
1 life,
or roll 
1 die""",
            "imagem": "images/carta_hera.png",
            "imagem_pequena": "images/carta_hera_p.png"
        },
        {
            "nome": "Hermes",
            "action": "Advance 5 spaces, or skip 1 space",
            "action_p": """Advance 
5 spaces,
or skip
1 space""",
            "imagem": "images/carta_hermes.png",
            "imagem_pequena": "images/carta_hermes_p.png"
        },
        {
            "nome": "Persephone",
            "action": "Go back 1, 2, or 3 spaces",
            "action_p": """Go back
1, 2, or
3 spaces""",
            "imagem": "images/carta_persephone.png",
            "imagem_pequena": "images/carta_persephone_p.png"
        },
        {
            "nome": "Poseidon",
            "action": "Advance 4 spaces, or roll 1 die",
            "action_p": """Advance
4 spaces,
or roll
1 die""",
            "imagem": "images/carta_poseidon.png",
            "imagem_pequena": "images/carta_poseidon_p.png"
        },
        {
            "nome": "Zeus",
            "action": "Advance 6 spaces, or roll 2 dice",
            "action_p": """Advance
6 spaces,
or roll
2 dice""",
            "imagem": "images/carta_zeus.png",
            "imagem_pequena": "images/carta_zeus_p.png"
        },
         {
            "nome": "Athena",
            "action": "Win 1 battle, or advance 2 spaces",
            "action_p": """Win
1 battle, or
advance 2 spaces""",
            "imagem": "images/carta_athena.png",
            "imagem_pequena": "images/carta_athena_p.png"
        }
    ]
      
        self.tijolos_cor = {
            "azul": "images/tijolos_azuis.png",
            "verde": "images/tijolos_verde.png",
            "amarelo": "images/tijolos_amarelo.png",
            "laranja": "images/tijolos_laranja.png",
            "vermelho": "images/tijolos_vermelho.png",
            "rosa": "images/tijolos_rosa.png",
            "roxo": "images/tijolos_roxo.png",
            "agua": "images/tijolos_agua.png",
        }
        
        self.tijolos_cor_atual = "images/tijolos_azuis.png" # default
        
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
        
        self.casas = [
    {"numero": 1, "texto": "Hermes", "imagem": "imagens_casas/casa_001.png"},
    {"numero": 2, "texto": "", "imagem": "imagens_casas/casa_002.png"},
    {"numero": 3, "texto": "", "imagem": "imagens_casas/casa_003.png"},
    {"numero": 4, "texto": "", "imagem": "imagens_casas/casa_004.png"},
    {"numero": 5, "texto": "Sphinx", "imagem": "imagens_casas/casa_005.png"},
    {"numero": 6, "texto": "", "imagem": "imagens_casas/casa_006.png"},
    {"numero": 7, "texto": "", "imagem": "imagens_casas/casa_007.png"},
    {"numero": 8, "texto": "Prometheus", "imagem": "imagens_casas/casa_008.png"},
    {"numero": 9, "texto": "", "imagem": "imagens_casas/casa_009.png"},
    {"numero": 10, "texto": "Sparta", "imagem": "imagens_casas/casa_010.png"},
    {"numero": 11, "texto": "", "imagem": "imagens_casas/casa_011.png"},
    {"numero": 12, "texto": "", "imagem": "imagens_casas/casa_012.png"},
    {"numero": 13, "texto": "Hestia", "imagem": "imagens_casas/casa_013.png"},
    {"numero": 14, "texto": "", "imagem": "imagens_casas/casa_014.png"},
    {"numero": 15, "texto": "", "imagem": "imagens_casas/casa_015.png"},
    {"numero": 16, "texto": "", "imagem": "imagens_casas/casa_016.png"},
    {"numero": 17, "texto": "Chimera", "imagem": "imagens_casas/casa_017.png"},
    {"numero": 18, "texto": "", "imagem": "imagens_casas/casa_018.png"},
    {"numero": 19, "texto": "", "imagem": "imagens_casas/casa_019.png"},
    {"numero": 20, "texto": "", "imagem": "imagens_casas/casa_020.png"},
    {"numero": 21, "texto": "Poseidon", "imagem": "imagens_casas/casa_021.png"},
    {"numero": 22, "texto": "", "imagem": "imagens_casas/casa_022.png"},
    {"numero": 23, "texto": "", "imagem": "imagens_casas/casa_023.png"},
    {"numero": 24, "texto": "Ciclops", "imagem": "imagens_casas/casa_024.png"},
    {"numero": 25, "texto": "", "imagem": "imagens_casas/casa_025.png"},
    {"numero": 26, "texto": "", "imagem": "imagens_casas/casa_026.png"},
    {"numero": 27, "texto": "", "imagem": "imagens_casas/casa_027.png"},
    {"numero": 28, "texto": "Harpies", "imagem": "imagens_casas/casa_028.png"},
    {"numero": 29, "texto": "", "imagem": "imagens_casas/casa_029.png"},
    {"numero": 30, "texto": "Athena", "imagem": "imagens_casas/casa_030.png"},
    {"numero": 31, "texto": "", "imagem": "imagens_casas/casa_031.png"},
    {"numero": 32, "texto": "Thanatos", "imagem": "imagens_casas/casa_032.png"},
    {"numero": 33, "texto": "", "imagem": "imagens_casas/casa_033.png"},
    {"numero": 34, "texto": "Minotaur", "imagem": "imagens_casas/casa_034.png"},
    {"numero": 35, "texto": "", "imagem": "imagens_casas/casa_035.png"},
    {"numero": 36, "texto": "Labyrinth", "imagem": "imagens_casas/casa_036.png"},
    {"numero": 37, "texto": "", "imagem": "imagens_casas/casa_037.png"},
    {"numero": 38, "texto": "Hades", "imagem": "imagens_casas/casa_038.png"},
    {"numero": 39, "texto": "Charon", "imagem": "imagens_casas/casa_039.png"},
    {"numero": 40, "texto": "", "imagem": "imagens_casas/casa_040.png"},
    {"numero": 41, "texto": "", "imagem": "imagens_casas/casa_041.png"},
    {"numero": 42, "texto": "Judgment", "imagem": "imagens_casas/casa_042.png"},
    {"numero": 43, "texto": "", "imagem": "imagens_casas/casa_043.png"},
    {"numero": 44, "texto": "Orpheus", "imagem": "imagens_casas/casa_044.png"},
    {"numero": 45, "texto": "", "imagem": "imagens_casas/casa_045.png"},
    {"numero": 46, "texto": "", "imagem": "imagens_casas/casa_046.png"},
    {"numero": 47, "texto": "", "imagem": "imagens_casas/casa_047.png"},
    {"numero": 48, "texto": "", "imagem": "imagens_casas/casa_048.png"},
    {"numero": 49, "texto": "Hephaestus", "imagem": "imagens_casas/casa_049.png"},
    {"numero": 50, "texto": "", "imagem": "imagens_casas/casa_050.png"},
    {"numero": 51, "texto": "", "imagem": "imagens_casas/casa_051.png"},
    {"numero": 52, "texto": "Erinyes", "imagem": "imagens_casas/casa_052.png"},
    {"numero": 53, "texto": "", "imagem": "imagens_casas/casa_053.png"},
    {"numero": 54, "texto": "", "imagem": "imagens_casas/casa_054.png"},
    {"numero": 55, "texto": "Persephone", "imagem": "imagens_casas/casa_055.png"},
    {"numero": 56, "texto": "", "imagem": "imagens_casas/casa_056.png"},
    {"numero": 57, "texto": "", "imagem": "imagens_casas/casa_057.png"},
    {"numero": 58, "texto": "", "imagem": "imagens_casas/casa_058.png"},
    {"numero": 59, "texto": "", "imagem": "imagens_casas/casa_059.png"},
    {"numero": 60, "texto": "", "imagem": "imagens_casas/casa_060.png"},
    {"numero": 61, "texto": "Hydra", "imagem": "imagens_casas/casa_061.png"},
    {"numero": 62, "texto": "", "imagem": "imagens_casas/casa_062.png"},
    {"numero": 63, "texto": "", "imagem": "imagens_casas/casa_063.png"},
    {"numero": 64, "texto": "Apollo", "imagem": "imagens_casas/casa_064.png"},
    {"numero": 65, "texto": "", "imagem": "imagens_casas/casa_065.png"},
    {"numero": 66, "texto": "Sisyphus", "imagem": "imagens_casas/casa_066.png"},
    {"numero": 67, "texto": "", "imagem": "imagens_casas/casa_067.png"},
    {"numero": 68, "texto": "", "imagem": "imagens_casas/casa_068.png"},
    {"numero": 69, "texto": "Centaurs", "imagem": "imagens_casas/casa_069.png"},
    {"numero": 70, "texto": "", "imagem": "imagens_casas/casa_070.png"},
    {"numero": 71, "texto": "Satyrs", "imagem": "imagens_casas/casa_071.png"},
    {"numero": 72, "texto": "", "imagem": "imagens_casas/casa_072.png"},
    {"numero": 73, "texto": "Hera", "imagem": "imagens_casas/casa_073.png"},
    {"numero": 74, "texto": "", "imagem": "imagens_casas/casa_074.png"},
    {"numero": 75, "texto": "Sirens", "imagem": "imagens_casas/casa_075.png"},
    {"numero": 76, "texto": "", "imagem": "imagens_casas/casa_076.png"},
    {"numero": 77, "texto": "", "imagem": "imagens_casas/casa_077.png"},
    {"numero": 78, "texto": "", "imagem": "imagens_casas/casa_078.png"},
    {"numero": 79, "texto": "Ares", "imagem": "imagens_casas/casa_079.png"},
    {"numero": 80, "texto": "", "imagem": "imagens_casas/casa_080.png"},
    {"numero": 81, "texto": "", "imagem": "imagens_casas/casa_081.png"},
    {"numero": 82, "texto": "Nymphs", "imagem": "imagens_casas/casa_082.png"},
    {"numero": 83, "texto": "", "imagem": "imagens_casas/casa_083.png"},
    {"numero": 84, "texto": "", "imagem": "imagens_casas/casa_084.png"},
    {"numero": 85, "texto": "Troy", "imagem": "imagens_casas/casa_085.png"},
    {"numero": 86, "texto": "", "imagem": "imagens_casas/casa_086.png"},
    {"numero": 87, "texto": "", "imagem": "imagens_casas/casa_087.png"},
    {"numero": 88, "texto": "Aphrodite", "imagem": "imagens_casas/casa_088.png"},
    {"numero": 89, "texto": "", "imagem": "imagens_casas/casa_089.png"},
    {"numero": 90, "texto": "Eros", "imagem": "imagens_casas/casa_090.png"},
    {"numero": 91, "texto": "", "imagem": "imagens_casas/casa_091.png"},
    {"numero": 92, "texto": "", "imagem": "imagens_casas/casa_092.png"},
    {"numero": 93, "texto": "Pegasus", "imagem": "imagens_casas/casa_093.png"},
    {"numero": 94, "texto": "", "imagem": "imagens_casas/casa_094.png"},
    {"numero": 95, "texto": "", "imagem": "imagens_casas/casa_095.png"},
    {"numero": 96, "texto": "Dionisius", "imagem": "imagens_casas/casa_096.png"},
    {"numero": 97, "texto": "", "imagem": "imagens_casas/casa_097.png"},
    {"numero": 98, "texto": "Bacchaes", "imagem": "imagens_casas/casa_098.png"},
    {"numero": 99, "texto": "", "imagem": "imagens_casas/casa_099.png"},
    {"numero": 100, "texto": "Pan", "imagem": "imagens_casas/casa_100.png"},
    {"numero": 101, "texto": "", "imagem": "imagens_casas/casa_101.png"},
    {"numero": 102, "texto": "", "imagem": "imagens_casas/casa_102.png"},
    {"numero": 103, "texto": "", "imagem": "imagens_casas/casa_103.png"},
    {"numero": 104, "texto": "Artemis", "imagem": "imagens_casas/casa_104.png"},
    {"numero": 105, "texto": "", "imagem": "imagens_casas/casa_105.png"},
    {"numero": 106, "texto": "", "imagem": "imagens_casas/casa_106.png"},
    {"numero": 107, "texto": "Orion", "imagem": "imagens_casas/casa_107.png"},
    {"numero": 108, "texto": "", "imagem": "imagens_casas/casa_108.png"},
    {"numero": 109, "texto": "", "imagem": "imagens_casas/casa_109.png"},
    {"numero": 110, "texto": "Midas", "imagem": "imagens_casas/casa_110.png"},
    {"numero": 111, "texto": "", "imagem": "imagens_casas/casa_111.png"},
    {"numero": 112, "texto": "Zeus", "imagem": "imagens_casas/casa_112.png"},
    {"numero": 113, "texto": "", "imagem": "imagens_casas/casa_113.png"},
    {"numero": 114, "texto": "", "imagem": "imagens_casas/casa_114.png"},
    {"numero": 115, "texto": "", "imagem": "imagens_casas/casa_115.png"},
    {"numero": 116, "texto": "Chronos", "imagem": "imagens_casas/casa_116.png"},
    {"numero": 117, "texto": "", "imagem": "imagens_casas/casa_117.png"},
    {"numero": 118, "texto": "", "imagem": "imagens_casas/casa_118.png"},
    {"numero": 119, "texto": "Griffins", "imagem": "imagens_casas/casa_119.png"},
    {"numero": 120, "texto": "", "imagem": "imagens_casas/casa_120.png"}
]
       
    # escolha a carta inicial
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

    # Em construção!!!!
    def adicionar_carta_player(self):
        if self.casa_atual == 1:
            self.carta_casa_deus = self.carta_casa_deus[7] #hermes
        elif self.casa_atual == 21:
            self.carta_casa_deus = self.carta_casa_deus[9] #poseidon
        elif self.casa_atual == 30:
            self.carta_casa_deus = self.carta_casa_deus[11] #atena
        elif self.casa_atual == 38:
            self.carta_casa_deus = self.carta_casa_deus[4] #hades
        elif self.casa_atual == 49:
            self.carta_casa_deus = self.carta_casa_deus[5] #hefesto
        elif self.casa_atual == 55:
            self.carta_casa_deus = self.carta_casa_deus[8] #persefone
        elif self.casa_atual == 64:
            self.carta_casa_deus = self.carta_casa_deus[1] #apolo
        elif self.casa_atual == 73:
            self.carta_casa_deus = self.carta_casa_deus[6] #hera
        elif self.casa_atual == 79:
            self.carta_casa_deus = self.carta_casa_deus[3] #ares
        elif self.casa_atual == 88:
            self.carta_casa_deus = self.carta_casa_deus[0] #afrodite
        elif self.casa_atual == 104:
            self.carta_casa_deus = self.carta_casa_deus[2] #artemis
        elif self.casa_atual == 112:
            self.carta_casa_deus = self.carta_casa_deus[10] #zeus
            
        self.cartas_player.add(self.carta_casa_deus)
        
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
         

    def exibir_casas_BE(self, lista_maior):
        # O número sorteado define de onde os 8 itens devem começar
        # Vamos garantir que o número esteja entre 1 e 120
        if self.casa_atual < 1 or self.casa_atual> 120:
            raise ValueError("O número deve estar entre 1 e 120.")
        
        # Calcular o índice de início para a exibição de 8 itens
        inicio = self.casa_atual - 1  # O índice começa de 0, então subtrai 1
        
        # Garantir que o início não ultrapasse o limite de 120 elementos
        fim = inicio + 8
        
        # Se o fim ultrapassar 120, ajustamos para pegar até o fim da lista
        if fim > len(lista_maior):
            fim = len(lista_maior)
            
         # Calcular o início para garantir que sempre mostremos 8 elementos (se possível)
        if fim - inicio < 8:  # Se o número de elementos a ser exibido for menor que 8
            inicio = max(fim - 8, 0)  # Ajusta o início para que tenha 8 itens (ou menos no final)
        
        
        # Pega os 8 itens ou até o fim da lista
        lista_exibida = lista_maior[inicio:fim]
        
        # Retorna os 8 itens para serem exibidos
        return lista_exibida
    
       
    def atualizar_tijolos_BE(self):
        if self.casa_atual <= 16:
            self.tijolos_cor_atual = self.tijolos_cor["azul"]
        elif self.casa_atual <= 32:
            self.tijolos_cor_atual = self.tijolos_cor["verde"]
        elif self.casa_atual <= 48:
            self.tijolos_cor_atual = self.tijolos_cor["amarelo"]
        elif self.casa_atual <= 64:
            self.tijolos_cor_atual = self.tijolos_cor["laranja"]
        elif self.casa_atual <= 80:
            self.tijolos_cor_atual = self.tijolos_cor["vermelho"]
        elif self.casa_atual <= 96:
            self.tijolos_cor_atual = self.tijolos_cor["rosa"]
        elif self.casa_atual <= 112:
            self.tijolos_cor_atual = self.tijolos_cor["roxo"]
        elif self.casa_atual <= 120:
            self.tijolos_cor_atual = self.tijolos_cor["agua"]
            
            
    def atualizar_cor_layout_BE(self):
        if self.casa_atual <= 16:
            self.cor_layout_atual = self.cores_layout["azul"]
        elif self.casa_atual <= 32:
            self.cor_layout_atual = self.cores_layout["verde"]
        elif self.casa_atual <= 48:
            self.cor_layout_atual = self.cores_layout["amarelo"]
        elif self.casa_atual <= 64:
            self.cor_layout_atual = self.cores_layout["laranja"]
        elif self.casa_atual <= 80:
            self.cor_layout_atual = self.cores_layout["vermelho"]
        elif self.casa_atual <= 96:
            self.cor_layout_atual = self.cores_layout["rosa"]
        elif self.casa_atual <= 112:
            self.cor_layout_atual = self.cores_layout["roxo"]
        elif self.casa_atual <= 120:
            self.cor_layout_atual = self.cores_layout["agua"]

     
    def rolar_dado_BE(self):
        # sorteia um número entre 1 e 6
        # Atualiza a posição od jogador
        # + 15 pontos para cada casa avançada
        numero_sorteado = random.randint(1, 6)
        print(f'Número sorteado: {numero_sorteado}')
        self.casa_atual += numero_sorteado
        print(f'Casa atual {self.casa_atual}')
        self.atualizar_tijolos()
        self.atualizar_cor_layout()
        self.atualizar_tijolos()
        
        
       # self.notificar_observadores()  # Notifica as mudanças
        
        
        
        #self.pontos += (numero_sorteado * 15)
        #self.atualizar_numeros_tabuleiro()

        # if numero_sorteado == 1:
        #     self.imagem_dado = "images/dado1.png"
        # elif numero_sorteado == 2:
        #     self.imagem_dado = "images/dado2.png"
        # elif numero_sorteado == 3:
        #     self.imagem_dado = "images/dado3.png"
        # elif numero_sorteado == 4:
        #     self.imagem_dado = "images/dado4.png"
        # elif numero_sorteado == 5:
        #     self.imagem_dado = "images/dado5.png"
        # else:
        #     self.imagem_dado = "images/dado6.png"

        # # Atualiza a lista de posições exibidas
        # self.obter_numeros_exibidos()   