import pygame
from config import white, green  # Importa as cores necessárias

# Botão de tela cheia
fullscreen_button_size = 50
is_fullscreen = False

def create_fullscreen_button(screen_width):
    """
    Cria o botão de tela cheia com base na largura da tela.
    """
    return pygame.Rect(screen_width - fullscreen_button_size - 10, 10, fullscreen_button_size, fullscreen_button_size)

def draw_fullscreen_icon(surface, rect, is_fullscreen, color):
    """
    Desenha o ícone do botão de tela cheia.
    """
    x, y, w, h = rect
    line_thickness = 3
    inset = 12

    if not is_fullscreen:  # Ícone para modo janela
        pygame.draw.line(surface, color, (x + inset, y + inset), (x + w // 2, y + inset), line_thickness)
        pygame.draw.line(surface, color, (x + inset, y + inset), (x + inset, y + h // 2), line_thickness)
        pygame.draw.line(surface, color, (x + w - inset, y + inset), (x + w // 2, y + inset), line_thickness)
        pygame.draw.line(surface, color, (x + w - inset, y + inset), (x + w - inset, y + h // 2), line_thickness)
    else:  # Ícone para modo tela cheia
        inner_inset = inset + 5
        pygame.draw.line(surface, color, (x + inner_inset, y + inner_inset), (x + w // 2, y + inner_inset), line_thickness)
        pygame.draw.line(surface, color, (x + inner_inset, y + inner_inset), (x + inner_inset, y + h // 2), line_thickness)
        pygame.draw.line(surface, color, (x + w - inner_inset, y + inner_inset), (x + w // 2, y + inner_inset), line_thickness)
        pygame.draw.line(surface, color, (x + w - inner_inset, y + inner_inset), (x + w - inner_inset, y + h // 2), line_thickness)