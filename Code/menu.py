#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("../asset/MenuBg.png") # tive que mudar aqui pq o programa não estava achando a imagem, era "./asset/MenuBg.png"
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('../asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(
                    text_size=20,
                    text=MENU_OPTION[i],
                    text_color=COLOR_WHITE,
                    text_center_pos=(WIN_WIDTH / 2, 200 + 25 * i))

            pygame.display.flip()

            # for i in range(len(MENU_OPTION)):
            #     self.menu_text(text_size=20, MENU_OPTION[i], COLOR_WHITE, text_center_pos=(WIN_WIDTH / 2), 200 * 25 * i))
            # ( essa é a versão que foi apresentado na aula prática, e não está dando certo )


            # self.window.blit(source=self.surf, dest=self.rect)
            # self.menu_text(text_size= 50, text:"Mountain", COLOR_ORANGE, text_center_pos: ((WIN_WIDTH / 2 ), 70))
            # self.menu_text(text_size= 50, text:"Shooter ", COLOR_ORANGE, text_center_pos: ((WIN_WIDTH / 2), 120))
            # pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


# def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
#     text_font: Font = pygame.font.SysFont(name= "Lucida Sans Typerwriter", size=text_size)
#     text_surf: Surface = text_font.render(text, antialias= True, text_color).convert_alpha()
#     text_rect: Rect = text_surf.get_rect(center: text_center_pos)
#     self.window.blit(source=text_surf, dest=text_rect)  ( essa é a versão que foi apresentado na aula prática, e não está dando certo )


