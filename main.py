# Interface básica com kivymd - Jogo Grécia
# Doug Bressar
# 21/07/2024 - last version

# historico aqui!
import os
import logging
import random
from random import randint
import time
import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ListProperty, ScreenManager, Screen # propriedade para o kiv "entender" as variáveis
from kivy.properties import AliasProperty, StringProperty, NumericProperty, ListProperty
# from kaki.app import App # kaki pra fazer o hot reloader
# Obs: kaki dava erro e não deixava funcionar os botões de mudança de página!! :(
from kivy.core.text import LabelBase # para definir as fontes
from kivymd.font_definitions import theme_font_styles # para criar estilos de fontes

from kivy.uix.image import Image
from kivy.clock import Clock # usar ou não??
import imageio # pra usar gifs

logging.basicConfig(level=logging.DEBUG) # Configuração de logging -> caça erros...

# Classes das telas:
class GerenciarTelas(ScreenManager):
    pass
class Tela1(Screen):
    pass
class Tela2(Screen):
    pass
class Tela3(Screen):
    pass
class Tela4(Screen):
    pass
class Tela5(Screen):
    pass


class Player:
    def __init__(self, name, about, image=None, image_pequena=None):
        self.name = name
        self.about = about
        self.image = "images/carinha_" + image
        self.image_pequena = "images/carinhas_escolha_" + image_pequena

# Players em jogo
hippolyta = Player("Hippolyta", """
Queen of the Amazons: A powerful warrior and ruler of a legendary race of female warriors.
She wants to reach Olympus to attain the status of a demigoddess.""","hipolita.png", "hipolita.png")
odysseus = Player("Odysseus", """
King of Ithaca, outsmarts monsters and gods on his epic journey home after the Trojan War.
He wants to reach Olympus to attain the status of a demigod.""", "odisseu.png", "odisseu.png")
achilles = Player("Achilles", """
The greatest Greek warrior, possesses invulnerability (except for a heel).
He wants to reach Olympus to attain the status of a demigod.""", "aquiles.png", "aquiles.png")
atalanta = Player("Atalanta", """
The Unbeatable Huntress: A Timeless Symbol of Female Strength and Independence.
He wants to reach Olympus to attain the status of a demigod.""", "atalanta.png", "atalanta.png")
theseus = Player("Theseus", """
The hero who conquered the Minotaur, united the lands of Attica, and became king.
He wants to reach Olympus to attain the status of a demigod.""", "teseu.png", "teseu.png")
# Dicionário de players
dic_players = {
    "1": odysseus,
    "2": hippolyta,
    "3": achilles,
    "4": atalanta,
    "5": theseus
}


class Cards:
    def __init__(self, nome=None, action=None, image=None, image_pequena=None):
        self.nome = nome
        self.action = action
        self.image = image
        self.image_pequena = image_pequena

    def __str__(self):
        return f"{self.nome}, {self.action}"
# Cartas em jogo
athena = Cards("Athena", "Win 1 battle, or advance 2 spaces", "images/carta_athena.jpg", "images/carta_athena_p.jpg")
ares = Cards("Ares", "Win 1 battle, or roll 1 die", "images/carta_ares.jpg", "images/carta_ares_p.jpg")
hades = Cards("Hades",  "Gain one life", "images/carta_hades.jpg", "images/carta_hades_p.jpg")
hermes = Cards("Hermes",  "Advance 5 spaces, or skip 1 space", "images/carta_hermes.jpg", "images/carta_hermes_p.jpg")
poseidon = Cards("Poseidon",  "Advance 4 spaces, or roll 1 die", "images/carta_poseidon.jpg", "images/carta_poseidon_p.jpg")
hera = Cards("Hera",  "Gain one life, or roll 1 die", "images/carta_hera.jpg", "images/carta_hera_p.jpg")
zeus = Cards("Zeus", "Advance 6 spaces, or roll 2 dice", "images/carta_zeus.jpg", "images/carta_zeus_p.jpg")
persephone = Cards("Persephone",  "Go back 1, 2, or 3 spaces", "images/carta_persephone.jpg", "images/carta_persephone_p.jpg")
hephaestus = Cards("Hephaestus", "Roll 1 die again", "images/carta_hephaestus.jpg", "images/carta_hephaestus_p.jpg")
aphrodite = Cards("Aphrodite", "Advance 6 spaces", "images/carta_aphrodite.jpg", "images/carta_aphrodite_p.jpg")
apollo = Cards("Apollo", "Roll 2 dice", "images/carta_apollo.jpg", "images/carta_apollo_p.jpg")
artemis = Cards("Artemis",  "Advance 3 spaces, or roll 1 die", "images/carta_artemis.jpg", "images/carta_artemis_p.jpg")
# Dicionário de cartas
dic_cards = {
    "1": athena,
    "2": ares,
    "3": hades,
    "4": hermes,
    "5": poseidon,
    "6": hera,
    "7": persephone,
    "8": hephaestus,
    "9": aphrodite,
    "11": apollo,
    "12": artemis
}

class Casas:
    def __init__(self, nome=None, image_pequena=None, image_grande=None, carta=False, texto=None, ):
        self.nome = nome
        self.image_pequena = image_pequena
        self.image_grande = image_grande
        self.texto = texto
        self.carta = carta

    def __str__(self):
        return (f"{self.nome}, {self.image_pequena}, {self.image_grande}, {self.texto}")

# todos os 'objeto casa'...
casa_1 = Casas("Hermes", "casas/casa_1.jpg", "casas_img_grande/casa_001_hermes.jpg",
               True,"Draw a card or move forward 2 spaces" )
casa_2 = Casas(None, "casas/casa_2.jpg", None,
               False,None)
casa_3 = Casas(None, "casas/casa_3.jpg", None,
               False,None)
casa_4 = Casas(None, "casas/casa_4.jpg", None,
               False,None)
casa_5 = Casas("Sphinx", "casas/casa_5.jpg", "casas_img_grande/casa_005_esfinge.jpg",
               False,"""She asked you a question.
Solve the riddle and roll a die.
If you get 3 or more, move forward 2 spaces.
If you get 2 or less, move back 2 spaces.""")
casa_6= Casas(None, "casas/casa_6.jpg", None,
               False,None)
casa_7= Casas(None, "casas/casa_7.jpg", None,
               False,None)
casa_8 = Casas("Prometheus", "casas/casa_8.jpg", "casas_img_grande/casa_008_prometeu.jpg",
               False,"""Watch the condemned Titan in his punishment and return 2 spaces.""")
casa_9= Casas(None, "casas/casa_9.jpg", None,
               False,None)
casa_10 = Casas("Sparta", "casas/casa_10.jpg", "casas_img_grande/casa_010_esparta.jpg",
               False,"""The Spartans don't like strangers!
Fight for your life.
Use a card or roll a die.
If you win, advance 2 spaces.
If you lose, lose 1 life.""")
casa_11 = Casas(None, "casas/casa_11.jpg", None,
               False,None)
casa_12 = Casas(None, "casas/casa_12.jpg", None,
               False,None)
casa_13 = Casas("Hestia", "casas/casa_13.jpg", "casas_img_grande/casa_013_hestia.jpg",
               False,"""Back 1 space and assist the Goddess with her hearth.""")
casa_14= Casas(None, "casas/casa_14.jpg", None,
               False,None)
casa_15= Casas(None, "casas/casa_15.jpg", None,
               False,None)
casa_16= Casas(None, "casas/casa_16.jpg", None,
               False,None)
casa_17 = Casas("Chimera", "casas/casa_17.jpg", "casas_img_grande/casa_017_quimera.jpg",
               False,"""Roll 1 die and fight against the monster.
If you lose, move back 3 spaces.
If you win, move forward 3 spaces.""")
casa_18= Casas(None, "casas/casa_18.jpg", None,
               False,None)
casa_19= Casas(None, "casas/casa_19.jpg", None,
               False,None)
casa_20= Casas(None, "casas/casa_20.jpg", None,
               False,None)
casa_21 = Casas("Poseidon", "casas/casa_21.jpg", "casas_img_grande/casa_021_poseidon.jpg",
               True,"""Draw 1 card or move forward 2 spaces""")
casa_22= Casas(None, "casas/casa_22.jpg", None,
               False,None)
casa_23= Casas(None, "casas/casa_23.jpg", None,
               False,None)
casa_24 = Casas("Ciclops", "casas/casa_24.jpg", "casas_img_grande/casa_024_ciclope.jpg",
               False,"""Engage in battle against the Cyclops and roll a die.
If you win, move forward 1 space.""")
casa_25= Casas(None, "casas/casa_25.jpg", None,
               False,None)
casa_26= Casas(None, "casas/casa_26.jpg", None,
               False,None)
casa_27= Casas(None, "casas/casa_27.jpg", None,
               False,None)
casa_28 = Casas("Harpies", "casas/casa_28.jpg", "casas_img_grande/casa_028_harpias.jpg",
               False,"""Face the bronze-feathered monsters and roll 1 die.
If you win, move forward 1 space.""")
casa_29= Casas(None, "casas/casa_29.jpg", None,
               False,None)
casa_30 = Casas("Athena", "casas/casa_30.jpg", "casas_img_grande/casa_030_atena.jpg",
               True, """Receive Athena's blessings:
Draw a card, or move forward 1 space.""")
casa_31 = Casas(None, "casas/casa_31.jpg", None,
               False, None)
casa_32 = Casas("Thanatos", "casas/casa_32.jpg", None,
               False, None)
casa_33= Casas(None, "casas/casa_33.jpg", None,
               False,None)
casa_34 = Casas("Minotaur", "casas/casa_34.jpg", None,
               False, None)
casa_35 = Casas(None, "casas/casa_35.jpg", None,
               False, None)
casa_36 = Casas("Labyrinth", "casas/casa_36.jpg", None,
               False, None)
casa_37 = Casas(None, "casas/casa_37.jpg", None,
               False, None)
casa_38 = Casas("Hades", "casas/casa_38.jpg", None,
               True, None)
casa_39 = Casas("Charon", "casas/casa_39.jpg", None,
               False, None)
casa_40 = Casas(None, "casas/casa_40.jpg", None,
               False, None)
casa_41 = Casas(None, "casas/casa_41.jpg", None,
               False, None)
casa_42 = Casas("Judgment", "casas/casa_42.jpg", None,
               False, None)
casa_43 = Casas(None, "casas/casa_43.jpg", None,
               False, None)
casa_44 = Casas("Orpheus", "casas/casa_44.jpg", None,
               False, None)
casa_45 = Casas(None, "casas/casa_45.jpg", None,
               False, None)
casa_46 = Casas(None, "casas/casa_46.jpg", None,
               False, None)
casa_47 = Casas(None, "casas/casa_47.jpg", None,
               False, None)
casa_48 = Casas(None, "casas/casa_48.jpg", None,
               False, None)
casa_49 = Casas("Hephaestus", "casas/casa_49.jpg", None,
               True, None)
casa_50 = Casas(None, "casas/casa_50.jpg", None,
               False, None)
casa_51 = Casas(None, "casas/casa_51.jpg", None,
               False, None)
casa_52= Casas("Erinyes", "casas/casa_52.jpg", None,
               False, None)
casa_53 = Casas(None, "casas/casa_53.jpg", None,
               False, None)
casa_54 = Casas(None, "casas/casa_54.jpg", None,
               False, None)
casa_55= Casas("Demeter", "casas/casa_55.jpg", None,
               False, None)
casa_56 = Casas("", "casas/casa_56.jpg", None,
               False, None)
casa_57 = Casas("", "casas/casa_57.jpg", None,
               False, None)
casa_58 = Casas("", "casas/casa_58.jpg", None, False, None)
casa_59 = Casas("", "casas/casa_59.jpg", None, False, None)
casa_60 = Casas("", "casas/casa_60.jpg", None, False, None)
casa_61 = Casas("", "casas/casa_61.jpg", None, False, None)
casa_62 = Casas("", "casas/casa_62.jpg", None, False, None)
casa_63 = Casas("", "casas/casa_63.jpg", None, False, None)
casa_64 = Casas("", "casas/casa_64.jpg", None, False, None)
casa_65 = Casas("", "casas/casa_65.jpg", None, False, None)
casa_66 = Casas("", "casas/casa_66.jpg", None, False, None)
casa_67 = Casas("", "casas/casa_67.jpg", None, False, None)
casa_68 = Casas("", "casas/casa_68.jpg", None, False, None)
casa_69 = Casas("", "casas/casa_69.jpg", None, False, None)
casa_70 = Casas("", "casas/casa_70.jpg", None, False, None)
casa_71 = Casas("", "casas/casa_71.jpg", None, False, None)
casa_72 = Casas("", "casas/casa_72.jpg", None, False, None)
casa_73 = Casas("", "casas/casa_73.jpg", None, False, None)
casa_74 = Casas("", "casas/casa_74.jpg", None, False, None)
casa_75 = Casas("", "casas/casa_75.jpg", None, False, None)
casa_76 = Casas("", "casas/casa_76.jpg", None, False, None)
casa_77 = Casas("", "casas/casa_77.jpg", None, False, None)
casa_78 = Casas("", "casas/casa_78.jpg", None, False, None)
casa_79 = Casas("", "casas/casa_79.jpg", None, False, None)
casa_80 = Casas("", "casas/casa_80.jpg", None, False, None)
casa_81 = Casas("", "casas/casa_81.jpg", None, False, None)
casa_82 = Casas("", "casas/casa_82.jpg", None, False, None)
casa_83 = Casas("", "casas/casa_83.jpg", None, False, None)
casa_84 = Casas("", "casas/casa_84.jpg", None, False, None)
casa_85 = Casas("", "casas/casa_85.jpg", None, False, None)
casa_86 = Casas("", "casas/casa_86.jpg", None, False, None)
casa_87 = Casas("", "casas/casa_87.jpg", None, False, None)
casa_88 = Casas("", "casas/casa_88.jpg", None, False, None)
casa_89 = Casas("", "casas/casa_89.jpg", None, False, None)
casa_90 = Casas("", "casas/casa_90.jpg", None, False, None)
casa_91 = Casas("", "casas/casa_91.jpg", None, False, None)
casa_92 = Casas("", "casas/casa_92.jpg", None, False, None)
casa_93 = Casas("", "casas/casa_93.jpg", None, False, None)
casa_94 = Casas("", "casas/casa_94.jpg", None, False, None)
casa_95 = Casas("", "casas/casa_95.jpg", None, False, None)
casa_96 = Casas("", "casas/casa_96.jpg", None, False, None)
casa_97 = Casas("", "casas/casa_97.jpg", None, False, None)
casa_98 = Casas("", "casas/casa_98.jpg", None, False, None)
casa_99 = Casas("", "casas/casa_99.jpg", None, False, None)
casa_100 = Casas("", "casas/casa_100.jpg", None, False, None)
casa_101 = Casas("", "casas/casa_101.jpg", None, False, None)
casa_102 = Casas("", "casas/casa_102.jpg", None, False, None)
casa_103 = Casas("", "casas/casa_103.jpg", None, False, None)
casa_104 = Casas("", "casas/casa_104.jpg", None, False, None)
casa_105 = Casas("", "casas/casa_105.jpg", None, False, None)
casa_106 = Casas("", "casas/casa_106.jpg", None, False, None)
casa_107 = Casas("", "casas/casa_107.jpg", None, False, None)
casa_108 = Casas("", "casas/casa_108.jpg", None, False, None)
casa_109 = Casas("", "casas/casa_109.jpg", None, False, None)
casa_110 = Casas("", "casas/casa_110.jpg", None, False, None)
casa_111 = Casas("", "casas/casa_111.jpg", None, False, None)
casa_112 = Casas("", "casas/casa_112.jpg", None, False, None)
casa_113 = Casas("", "casas/casa_113.jpg", None, False, None)
casa_114 = Casas("", "casas/casa_114.jpg", None, False, None)
casa_115 = Casas("", "casas/casa_115.jpg", None, False, None)
casa_116 = Casas("", "casas/casa_116.jpg", None, False, None)
casa_117 = Casas("", "casas/casa_117.jpg", None, False, None)
casa_118 = Casas("", "casas/casa_118.jpg", None, False, None)
casa_119 = Casas("", "casas/casa_119.jpg", None, False, None)
casa_120 = Casas("", "casas/casa_120.jpg", None, False, None)


dic_casas = {
    "1": casa_1, "2": casa_2, "3": casa_3, "4": casa_4, "5": casa_5, "6": casa_6, "7": casa_7, "8": casa_8, "9": casa_9, "10": casa_10,
    "11": casa_11, "12": casa_12, "13": casa_13, "14": casa_14, "15": casa_15, "16": casa_16, "17": casa_17, "18": casa_18, "19": casa_19, "20": casa_20,
    "21": casa_21, "22": casa_22, "23": casa_23, "24": casa_24, "25": casa_25, "26": casa_26, "27": casa_27, "28": casa_28, "29": casa_29, "30": casa_30,
    "31": casa_31, "32": casa_32, "33": casa_33, "34": casa_34, "35": casa_35, "36": casa_36, "37": casa_37, "38": casa_38, "39": casa_39, "40": casa_40,
    "41": casa_41, "42": casa_42, "43": casa_43, "44": casa_44, "45": casa_45, "46": casa_46, "47": casa_47, "48": casa_48, "49": casa_49, "50": casa_50,
    "51": casa_51, "52": casa_52, "53": casa_53, "54": casa_54, "55": casa_55, "56": casa_56, "57": casa_57, "58": casa_58, "59": casa_59, "60": casa_60,
    "61": casa_61, "62": casa_62, "63": casa_63, "64": casa_64, "65": casa_65, "66": casa_66, "67": casa_67, "68": casa_68, "69": casa_69, "70": casa_70,
    "71": casa_71, "72": casa_72, "73": casa_73, "74": casa_74, "75": casa_75, "76": casa_76, "77": casa_77, "78": casa_78, "79": casa_79, "80": casa_80,
    "81": casa_81, "82": casa_82, "83": casa_83, "84": casa_84, "85": casa_85, "86": casa_86, "87": casa_87, "88": casa_88, "89": casa_89, "90": casa_90,
    "91": casa_91, "92": casa_92, "93": casa_93, "94": casa_94, "95": casa_95, "96": casa_96, "97": casa_97, "98": casa_98, "99": casa_99, "100": casa_100,
    "101": casa_101, "102": casa_102, "103": casa_103, "104": casa_104, "105": casa_105, "106": casa_106, "107": casa_107, "108": casa_108, "109": casa_109,
    "110": casa_110, "111": casa_111, "112": casa_112, "113": casa_113, "114": casa_114, "115": casa_115, "116": casa_116, "117": casa_117, "118": casa_118,
    "119": casa_119, "120": casa_120,
}
dic_nomes_casas = {
    "1": "Hermes", "2": "", "3": "", "4": "", "5": "Sphinx", "6": "", "7": "", "8": "Prometheus", "9": "", "10": "Sparta",
    "11": "", "12": "", "13": "Hestia", "14": "", "15": "", "16": "", "17": "Chimera", "18": "", "19": "", "20": "",
    "21": "Poseidon", "22": "", "23": "", "24": "Ciclops", "25": "", "26": "", "27": "", "28": "Harpies", "29": "", "30": "Athena",
    "31": "", "32": "Thanatos", "33": "", "34": "Minotaur", "35": "", "36": "Labyrinth", "37": "", "38": "Hades", "39": "Charon", "40": "",
    "41": "", "42": "Judgment", "43": "", "44": "Orpheus", "45": "", "46": "", "47": "", "48": "", "49": "Hephaestus", "50": "",
    "51": "", "52": "Erinyes", "53": "", "54": "", "55": "Demeter", "56": "", "57": "", "58": "", "59": "", "60": "",
    "61": "Hydra", "62": "", "63": "", "64": "Apollo", "65": "", "66": "Sisyphus", "67": "", "68": "", "69": "Centaurs", "70": "",
    "71": "Satyrs", "72": "", "73": "Hera", "74": "", "75": "Sirens", "76": "", "77": "", "78": "", "79": "Ares", "80": "",
    "81": "", "82": "Nymphs", "83": "", "84": "", "85": "Troy", "86": "", "87": "", "88": "Aphrodite", "89": "", "90": "Eros",
    "91": "", "92": "", "93": "Pegasus", "94": "", "95": "", "96": "Dionisius", "97": "", "98": "Bacchaes", "99": "", "100": "Pan",
    "101": "", "102": "", "103": "", "104": "Artemis", "105": "", "106": "", "107": "Orion", "108": "", "109": "", "110": "Midas",
    "111": "", "112": "Zeus", "113": "", "114": "", "115": "", "116": "Chronos", "117": "", "118": "", "119": "Griffins", "120": "Olympus"
}


class Tabuleiro:
    # def __init__(self):
    #     self.numeros_tabuleiro = list(range(126)) ### já copiei
    #     self.posicao_atual = 0
    #     self.pontos = 0
    #     self.vida = 9
    #     self.nome = None
    #     self.casa = 0
    #     self.texto = None
    #     self.image = None
    #     self.cartas_player = []
    #     self.cartas_usadas = []
    pass


class Aplicativo(MDApp):
    #numeros_tabuleiro = ListProperty([range(121)]) #list(range(126?))
    posicao_atual = NumericProperty(0)
    pontos = NumericProperty(0)
    vida = NumericProperty(3)
    imagem_dado = StringProperty("images/dado_grego.gif")
    nome_player = StringProperty("")
    image_player = StringProperty("")
    about_player = StringProperty("")
    image_carta = StringProperty("")
    action_carta = StringProperty("")
    cartas_player = ListProperty([])
    cartas_usadas = ListProperty([])
    #tijolo_atual = StringProperty("images/tijolinhos_azul_1.png") # tijolo inicial
    # daqui pra baixo é gambiarra!!! O .KV NÃO RECONHCE O OBJETO Da LISTA cartas_player = ListProperty([])
    image_pequena_1 = StringProperty("images/cartinha_vazia_cinza.jpg")
    image_pequena_2 = StringProperty("images/cartinha_vazia_cinza.jpg")
    image_pequena_3 = StringProperty("images/cartinha_vazia_cinza.jpg")
    tema_botoes = StringProperty("Red")
    #numeros_tabuleiro = ListProperty([0, 1, 2, 3, 4, 5])
    numeros_tabuleiro = ListProperty([1, 2, 3, 4, 5, 6])
    #numeros_tabuleiro = ListProperty([10, 11, 12, 13, 14, 15])
    numeros_tabuleiro_total = ListProperty(range(126))


    # ATRIBUINDO PRA outra VARIAVEL NA FORÇA!!!
    cores_tabuleiro = {
        'azul': (0.3, 0.76, 0.96, 1), #(0, 0, 1, 1)
        'verde': (0.18, 0.8, 0.44), #(0, 1, 0, 1)
        'amarelo': (0.94, 0.76, 0.05), #(1, 1, 0, 1)
        'laranja': (255/255, 138/255, 101/255), #(1, 0.65, 0, 1)
        'vermelho': (211/255, 47/255, 47/255),#(1, 0, 0, 1)
        'rosa': (244/255, 143/255, 177/255), #(1, 0.75, 0.8, 1)
        'roxo': (149/255, 117/255, 205/255) # (0.5, 0, 0.5, 1)
    }
    tijolos_tabuleiro = {
        'azul': "images/tijolinhos_azul_1.png",
        'verde': "images/tijolinhos_verde_2.png",
        'amarelo': "images/tijolinhos_amarelo_3.png",
        'laranja': "images/tijolinhos_laranja_4.png",
        'vermelho': "images/tijolinhos_vermelho_5.png",
        'rosa':"images/tijolinhos_rosa_6.png",
        'roxo': "images/tijolinhos_roxo_7.png"
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tabuleiro = Tabuleiro()
        self.cards = Cards()
        self.casas = Casas(self.tabuleiro, self.cartas_player)  # Passa cartas_player - Gambiarra!

    def _get_posicao_tijolos(self):
        if self.posicao_atual <= 20:
            return self.tijolos_tabuleiro['azul']
        elif self.posicao_atual <= 40:
            return self.tijolos_tabuleiro['verde']
        elif self.posicao_atual <= 60:
            return self.tijolos_tabuleiro['amarelo']
        elif self.posicao_atual <= 80:
            return self.tijolos_tabuleiro['laranja']
        elif self.posicao_atual <= 100:
            return self.tijolos_tabuleiro['vermelho']
        elif self.posicao_atual <= 120:
            return self.tijolos_tabuleiro['rosa']
        else:
            return self.tijolos_tabuleiro['roxo']

    def _get_cortabuleiro(self):
        if self.posicao_atual <= 20:
            return self.cores_tabuleiro['azul']
        elif self.posicao_atual <= 40:
            return self.cores_tabuleiro['verde']
        elif self.posicao_atual <= 60:
            return self.cores_tabuleiro['amarelo']
        elif self.posicao_atual <= 80:
            return self.cores_tabuleiro['laranja']
        elif self.posicao_atual <= 100:
            return self.cores_tabuleiro['vermelho']
        elif self.posicao_atual <= 120:
            return self.cores_tabuleiro['rosa']
        else:
            return self.cores_tabuleiro['roxo']

    posicao_tijolos = AliasProperty(_get_posicao_tijolos, None, bind=['posicao_atual'])
    cortabuleiro = AliasProperty(_get_cortabuleiro, None, bind=['posicao_atual'])


    def sair_jogo(self):
        print("Encerrando programa...")
        self.stop()

    def obter_numeros_exibidos(self):
        if self.posicao_atual > 2:
            inicio = self.posicao_atual - 2
        else:
            inicio = 0
        fim = inicio + 6
        self.numeros_tabuleiro = list(range(inicio + 1, fim + 1))

    # nova versão -- Bressar Version
    def _get_exibir_nome_casa(self, index):
        if index < len(self.numeros_tabuleiro):
            casa_numero = str(self.numeros_tabuleiro[index])
            return dic_nomes_casas.get(casa_numero, "")
        return ""

    exibir_nome_casa_0 = AliasProperty(lambda self: self._get_exibir_nome_casa(0), None, bind=['numeros_tabuleiro'])
    exibir_nome_casa_1 = AliasProperty(lambda self: self._get_exibir_nome_casa(1), None, bind=['numeros_tabuleiro'])
    exibir_nome_casa_2 = AliasProperty(lambda self: self._get_exibir_nome_casa(2), None, bind=['numeros_tabuleiro'])
    exibir_nome_casa_3 = AliasProperty(lambda self: self._get_exibir_nome_casa(3), None, bind=['numeros_tabuleiro'])
    exibir_nome_casa_4 = AliasProperty(lambda self: self._get_exibir_nome_casa(4), None, bind=['numeros_tabuleiro'])
    exibir_nome_casa_5 = AliasProperty(lambda self: self._get_exibir_nome_casa(5), None, bind=['numeros_tabuleiro'])

    def _get_mostra_casa_gambirra1(self):
        if self.posicao_atual > 0:
            casa_numero = str(self.posicao_atual - 1)
            return f"casas/casa_{casa_numero}.jpg"
        else:
            return "casas/casa_1.jpg"
    mostra_casa_gambirra1 = AliasProperty(_get_mostra_casa_gambirra1, None, bind=['posicao_atual'])

    def _get_mostra_casa_gambirra2(self):
        if self.posicao_atual > 0:
            casa_numero = str(self.posicao_atual)
            return f"casas/casa_{casa_numero}.jpg"
        else:
            return "casas/casa_2.jpg"
    mostra_casa_gambirra2 = AliasProperty(_get_mostra_casa_gambirra2, None, bind=['posicao_atual'])

    def _get_mostra_casa_gambirra3(self):
        if self.posicao_atual > 0:
            casa_numero = str(self.posicao_atual + 1)
            return f"casas/casa_{casa_numero}.jpg"
        else:
            return "casas/casa_3.jpg"
    mostra_casa_gambirra3 = AliasProperty(_get_mostra_casa_gambirra3, None, bind=['posicao_atual'])

    def _get_mostra_casa_gambirra4(self):
        if self.posicao_atual > 0:
            casa_numero = str(self.posicao_atual + 2)
            return f"casas/casa_{casa_numero}.jpg"
        else:
            return "casas/casa_4.jpg"
    mostra_casa_gambirra4 = AliasProperty(_get_mostra_casa_gambirra4, None, bind=['posicao_atual'])

    def _get_mostra_casa_gambirra5(self):
        if self.posicao_atual > 0:
            casa_numero = str(self.posicao_atual + 3)
            return f"casas/casa_{casa_numero}.jpg"
        else:
            return "casas/casa_5.jpg"
    mostra_casa_gambirra5 = AliasProperty(_get_mostra_casa_gambirra5, None, bind=['posicao_atual'])

    def _get_mostra_casa_gambirra6(self):
        if self.posicao_atual > 0:
            casa_numero = str(self.posicao_atual + 4)
            return f"casas/casa_{casa_numero}.jpg"
        else:
            return "casas/casa_6.jpg"
    mostra_casa_gambirra6 = AliasProperty(_get_mostra_casa_gambirra6, None, bind=['posicao_atual'])


    def _get_exibir_texto_casa(self, index): # Usar essa função mais pra frente...
        if index < len(self.numeros_tabuleiro):
            casa_numero = str(self.numeros_tabuleiro[index])
            casa = dic_casas.get(casa_numero)
            if casa:
                return casa.texto if casa.texto else ""
        return ""

    exibir_texto_casa_0 = AliasProperty(lambda self: self._get_exibir_texto_casa(0), None, bind=['posicao_atual'])
    exibir_texto_casa_1 = AliasProperty(lambda self: self._get_exibir_texto_casa(1), None, bind=['posicao_atual'])
    exibir_texto_casa_2 = AliasProperty(lambda self: self._get_exibir_texto_casa(2), None, bind=['posicao_atual'])
    exibir_texto_casa_3 = AliasProperty(lambda self: self._get_exibir_texto_casa(3), None, bind=['posicao_atual'])
    exibir_texto_casa_4 = AliasProperty(lambda self: self._get_exibir_texto_casa(4), None, bind=['posicao_atual'])
    exibir_texto_casa_5 = AliasProperty(lambda self: self._get_exibir_texto_casa(5), None, bind=['posicao_atual'])

    def _get_voce_esta_aqui(self, index):
        if index < len(self.numeros_tabuleiro):
            if self.numeros_tabuleiro[index] == self.posicao_atual:
                return "You are Here!"
        return ""

    voce_esta_aqui_0 = AliasProperty(lambda self: self._get_voce_esta_aqui(0), None, bind=['posicao_atual'])
    voce_esta_aqui_1 = AliasProperty(lambda self: self._get_voce_esta_aqui(1), None, bind=['posicao_atual'])
    voce_esta_aqui_2 = AliasProperty(lambda self: self._get_voce_esta_aqui(2), None, bind=['posicao_atual'])
    voce_esta_aqui_3 = AliasProperty(lambda self: self._get_voce_esta_aqui(3), None, bind=['posicao_atual'])
    voce_esta_aqui_4 = AliasProperty(lambda self: self._get_voce_esta_aqui(4), None, bind=['posicao_atual'])
    voce_esta_aqui_5 = AliasProperty(lambda self: self._get_voce_esta_aqui(5), None, bind=['posicao_atual'])

    def _get_you_are_here(self):
        if self.posicao_atual > 6:
            return "You are Here!"
        else:
            return ""

    you_are_here = AliasProperty(_get_you_are_here, None, bind=['posicao_atual'])
    # you_are_here = AliasProperty(lambda self: self._get_you_are_here, None, bind=['posicao_atual'])

    def atualizar_numeros_tabuleiro(self):
        # Define o início da lista para manter a posicao_atual no meio (index 2)
        if self.posicao_atual <= 2:
            inicio = 0
        else:
            inicio = self.posicao_atual - 2
        fim = inicio + 6
        self.numeros_tabuleiro = list(range(inicio + 1, fim + 1))# Garante que sempre teremos 6 itens na lista

    def rolar_dado(self):
        # sorteia um número entre 1 e 6
        # Atualiza a posição od jogador
        # + 15 pontos para cada casa avançada
        numero_sorteado = random.randint(1, 6)
        self.posicao_atual += numero_sorteado
        self.pontos += (numero_sorteado * 15)
        self.atualizar_numeros_tabuleiro()

        if numero_sorteado == 1:
            self.imagem_dado = "images/dado1.png"
        elif numero_sorteado == 2:
            self.imagem_dado = "images/dado2.png"
        elif numero_sorteado == 3:
            self.imagem_dado = "images/dado3.png"
        elif numero_sorteado == 4:
            self.imagem_dado = "images/dado4.png"
        elif numero_sorteado == 5:
            self.imagem_dado = "images/dado5.png"
        else:
            self.imagem_dado = "images/dado6.png"

        # Atualiza a lista de posições exibidas
        self.obter_numeros_exibidos()

        #for debug
        print(f"número sorteado: {numero_sorteado}")
        print(f"posição atual: {self.posicao_atual}")
        print(f"pontos: {self.pontos}")
        print(f"lista de posições: {self.numeros_tabuleiro}")
        # encerrando o jogo, mudar para uma página de encerrameneto... e não break!
        # Encerra o jogo se a posição atual for maior ou igual a 130
        if self.posicao_atual >= 130:
            print('Encerrando jogo!!')
            self.sair_jogo()

    def escolher_jogador(self, numero_escolha):
        # função para escolher o jogador e exibir os seus dados
        escolha = str(numero_escolha)
        player = dic_players.get(escolha)
        if player:
            self.nome_player = player.name
            self.about_player = player.about
            self.image_player = player.image

            # print for debug
            print(f"nome do Jogador escolhido: {self.nome_player}\n"
                  f"ABOUT: {self.about_player}\n"
                  f"nome/path da Imagem: {self.image_player}\n")
        else:
            print("Jogador desconhecido, escolha novamente!")

    def escolher_carta(self):
        # função para escolher a carta acrescentá-la na lista de cartas do jogador
        # Em um total de no máximo 3 cartas
        # E exibir os atributos  da carta no layout
        carta_escolhida = random.choice(list(dic_cards.keys()))
        carta_inicial = dic_cards[carta_escolhida]
        if carta_inicial not in self.cartas_player and carta_inicial not in self.cartas_usadas:
            self.image_carta = carta_inicial.image  # trecho teste
            self.action_carta = carta_inicial.action # trecho teste

            if len(self.cartas_player) >= 3:
                self.cartas_player.pop(0)  # Remove o primeiro item se a lista já tiver 3 itens
            self.cartas_player.append(carta_inicial)
            self.cartas_player = self.cartas_player[:]  # Trigger update
            self.update_cartinhas_images()
            # Trecho print for Debug
            print(f"Your starting card is: {carta_inicial.nome}\n"
                  f"And your power is: {carta_inicial.action}")
            # Print mostrando as listas cartas_player e cartas_usadas
            print("**Cartas do Jogador:**")
            for carta in self.cartas_player:
                print(f"- {carta.nome}: {carta.action}")
                print(f"- {carta.nome}: {carta.image_pequena}")
            print("\n**Cartas Usadas:**")
            for carta in self.cartas_usadas:
                print(f"- {carta.nome}: {carta.action}")

    # GAMBIARRA! atualizar na marra,
    # faz a atualização da lista de cartas paras
    # as variaveis que recebem as cartinhas a serem exibidas no layout:
    def update_cartinhas_images(self): # cartinhas para exibição somente
        # função para exibir as cartinhas do jogador na página do game
        self.image_pequena_1 = self.cartas_player[0].image_pequena if len(
            self.cartas_player) > 0 else 'images/cartinha_vazia.jpg'
        self.image_pequena_2 = self.cartas_player[1].image_pequena if len(
            self.cartas_player) > 1 else 'images/cartinha_vazia.jpg'
        self.image_pequena_3 = self.cartas_player[2].image_pequena if len(
            self.cartas_player) > 2 else 'images/cartinha_vazia.jpg'
    # fim da gambirra


    def build(self): # Alterado de  build_app para build, sem **kwargs
        self.theme_cls.primary_palette = self.tema_botoes
        fonts_path = "fonts"
        fonts = {
            "Gelio Fasolada": "Gelio Fasolada.ttf",
            "Gelio Greek Diner": "Gelio Greek Diner.ttf",
            "Olympus": "Olympus-nD6Y.ttf",
            "Olympus Bold": "OlympusBold.ttf"
        }
        for font_name, font_file in fonts.items():
            font_path = os.path.join(fonts_path, font_file)
            if os.path.exists(font_path):
                LabelBase.register(name=font_name, fn_regular=font_path)
                logging.debug(f"Fonte registrada: {font_name} - {font_path}")
            else:
                logging.error(f"Fonte não encontrada: {font_path}")
        for font in LabelBase._fonts.keys(): # Debug fontes!!!!!!!!!!!!!!!!!!
            logging.debug(f"Fonte registrada: {font}")
        theme_font_styles.append('Gelio Fasolada')
        self.theme_cls.font_styles["Gelio Fasolada"] = [
            "Gelio Fasolada", 10, False, 1.0
        ]
        theme_font_styles.append('Gelio Greek Diner')
        self.theme_cls.font_styles["Gelio Greek Diner"] = [
            "Gelio Greek Diner", 10, False, 1.0
        ]
        logging.debug("Construindo a aplicação e retornando ScreenManager")# conferindo se fez o build
        return Builder.load_file('aplicativo.kv')


if __name__ == "__main__": # Rodar a aplicação
    Aplicativo().run()
