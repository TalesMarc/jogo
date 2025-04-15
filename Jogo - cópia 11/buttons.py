import pygame
from config import green, white

# Proporções para os botões
button_radius_ratio = 0.02
button_height_ratio = 0.08
button_width_ratio = 0.25
button_spacing_ratio = 0.06
initial_y_offset_ratio = 0.6

def create_rounded_button(text, y_offset, screen_width, screen_height, font):
    """
    Cria um botão arredondado com texto centralizado.
    """
    button_width = int(screen_width * button_width_ratio)
    button_height = int(screen_height * button_height_ratio)
    button_radius = int(min(button_width, button_height) * button_radius_ratio)
    center_x = screen_width // 2
    center_y = int(screen_height * initial_y_offset_ratio) + y_offset
    rect = pygame.Rect(center_x - button_width // 2, center_y - button_height // 2, button_width, button_height)
    text_render = font.render(text, True, white)
    text_rect = text_render.get_rect(center=rect.center)
    return rect, text_render, text_rect, button_radius

def draw_rounded_rect(surface, rect, color, radius):
    """
    Desenha um retângulo com bordas arredondadas.
    """
    x, y, w, h = rect
    pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
    pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))
    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius)