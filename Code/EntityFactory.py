#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Background import Background
from Code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # ESSA AQUI PASSA AS 7 PRIMEIRAS IMGAENS
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))   # ESSA PASSA MAIS 7 E O CICLO CONTINUA, PARA RODAR O JOGO NORMALMENTE
                return list_bg
