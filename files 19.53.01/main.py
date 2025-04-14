import pygame
from config import (
    initial_width,
    initial_height,
    light_blue,
    MENU_PRINCIPAL,
    MENU_JOGAR,
    MENU_CONFIGURACOES,
    MENU_LANGUAGE,
)
from fullscreen import create_fullscreen_button, draw_fullscreen_icon
from buttons import draw_rounded_rect
from menus import (
    calculate_main_menu_buttons,
    calculate_jogar_menu_buttons,
    calculate_config_menu_buttons,
    calculate_language_menu_buttons,
)
from volume import draw_volume_slider, adjust_volume
from language import LanguageManager

# Inicialização do Pygame
pygame.init()

# Configurações iniciais
screen_width = initial_width
screen_height = initial_height
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Ceciliatas")

# Fonte para textos
font = pygame.font.Font(None, 30)

# Gerenciador de idiomas
lang_manager = LanguageManager()

# Botões e menus
fullscreen_button_rect = create_fullscreen_button(screen_width)
main_menu_buttons = calculate_main_menu_buttons(screen_width, screen_height, font)
jogar_menu_buttons = calculate_jogar_menu_buttons(screen_width, screen_height, font)
config_menu_buttons = calculate_config_menu_buttons(screen_width, screen_height, font)
language_menu_buttons = calculate_language_menu_buttons(screen_width, screen_height, font)

# Estado do menu atual
current_menu = MENU_PRINCIPAL

# Variável de volume global
volume = 0.5
is_dragging_volume = False

# Loop principal do jogo
running = True
while running:
    screen.fill(light_blue)

    # Eventos do Pygame
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Detectar cliques nos botões
            if current_menu == MENU_PRINCIPAL:
                for action, rect, _, _, _ in main_menu_buttons:
                    if rect.collidepoint(event.pos):
                        if action == "jogar":
                            current_menu = MENU_JOGAR
                        elif action == "configuracoes":
                            current_menu = MENU_CONFIGURACOES
                        elif action == "language":
                            current_menu = MENU_LANGUAGE
            elif current_menu == MENU_JOGAR:
                for action, rect, _, _, _ in jogar_menu_buttons:
                    if rect.collidepoint(event.pos):
                        if action == "voltar":
                            current_menu = MENU_PRINCIPAL
            elif current_menu == MENU_CONFIGURACOES:
                for action, rect, _, _, _ in config_menu_buttons:
                    if rect.collidepoint(event.pos):
                        if action == "voltar":
                            current_menu = MENU_PRINCIPAL
                        elif action == "volume":
                            # Inicia o ajuste de volume
                            volume_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 10, 200, 20)
                            if volume_rect.collidepoint(event.pos):
                                is_dragging_volume = True
            elif current_menu == MENU_LANGUAGE:
                for lang_code, rect, _, _, _ in language_menu_buttons:
                    if rect.collidepoint(event.pos):
                        if lang_code == "back":
                            current_menu = MENU_CONFIGURACOES
                        else:
                            lang_manager.set_language(lang_code)
        elif event.type == pygame.MOUSEBUTTONUP:
            is_dragging_volume = False
        elif event.type == pygame.MOUSEMOTION:
            if is_dragging_volume:
                volume = adjust_volume(mouse_pos, screen_width)

    # Renderizar elementos na tela
    if current_menu == MENU_PRINCIPAL:
        for _, rect, text_render, text_rect, radius in main_menu_buttons:
            draw_rounded_rect(screen, rect, (0, 128, 0), radius)
            screen.blit(text_render, text_rect)
    elif current_menu == MENU_JOGAR:
        for _, rect, text_render, text_rect, radius in jogar_menu_buttons:
            draw_rounded_rect(screen, rect, (0, 128, 0), radius)
            screen.blit(text_render, text_rect)
    elif current_menu == MENU_CONFIGURACOES:
        for _, rect, text_render, text_rect, radius in config_menu_buttons:
            draw_rounded_rect(screen, rect, (0, 128, 0), radius)
            screen.blit(text_render, text_rect)

        # Desenhar controle de volume
        draw_volume_slider(screen, volume, screen_width, screen_height)
    elif current_menu == MENU_LANGUAGE:
        for _, rect, text_render, text_rect, radius in language_menu_buttons:
            draw_rounded_rect(screen, rect, (0, 128, 0), radius)
            screen.blit(text_render, text_rect)

    # Desenhar botão de tela cheia
    draw_fullscreen_icon(screen, fullscreen_button_rect, False, (255, 255, 255))

    pygame.display.flip()

pygame.quit()