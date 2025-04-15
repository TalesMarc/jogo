import pygame
from config import grey, light_grey, white

def draw_volume_slider(screen, volume, screen_width, screen_height):
    """
    Desenha o controle de volume no menu de configurações.
    """
    # Dimensões da barra de volume
    bar_width = 200
    bar_height = 20
    bar_x = screen_width // 2 - bar_width // 2
    bar_y = screen_height // 2 - bar_height // 2

    # Desenhar a barra de volume
    bar_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
    pygame.draw.rect(screen, grey, bar_rect)

    # Desenhar o indicador (slider)
    indicator_x = int(bar_x + volume * bar_width)
    indicator_rect = pygame.Rect(indicator_x - 5, bar_y - 5, 10, bar_height + 10)
    pygame.draw.rect(screen, light_grey, indicator_rect)

    # Mostrar o valor do volume
    font = pygame.font.Font(None, 30)
    volume_text = font.render(f"{int(volume * 100)}%", True, white)
    screen.blit(volume_text, (bar_x + bar_width + 20, bar_y))

def adjust_volume(mouse_pos, screen_width):
    """
    Ajusta o volume com base na posição do mouse.
    """
    bar_width = 200
    bar_x = screen_width // 2 - bar_width // 2

    # Calcular o novo valor do volume
    relative_mouse_x = mouse_pos[0] - bar_x
    new_volume = max(0, min(1, relative_mouse_x / bar_width))  # Entre 0 e 1
    return new_volume