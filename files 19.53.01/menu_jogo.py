# Importações necessárias
import pygame  # Importa o pygame para criação de interface gráfica

# Inicialização do Pygame
pygame.init()

# ======================== CONFIGURAÇÕES INICIAIS ========================
# Obter dimensões iniciais da tela e criar a janela do jogo
info = pygame.display.Info()
initial_width = 800
initial_height = 600
screen_width = initial_width
screen_height = initial_height
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Ceciliatas")  # Nome da janela do jogo

# Definição de cores (RGB)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
dark_green = (0, 100, 0)
red = (255, 0, 0)
grey = (50, 50, 50)
light_grey = (100, 100, 100)
light_blue = (173, 216, 230)  # Azul claro para o fundo

# ======================== BOTÃO DE TELA CHEIA ========================
fullscreen_button_size = 50
fullscreen_button_rect = pygame.Rect(screen_width - fullscreen_button_size - 10, 10, fullscreen_button_size, fullscreen_button_size)
is_fullscreen = False
fullscreen_button_down = False
button_border_color = white
button_inner_color = green

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
        pygame.draw.line(surface, color, (x + inset, y + h - inset), (x + w // 2, y + h - inset), line_thickness)
        pygame.draw.line(surface, color, (x + inset, y + h - inset), (x + inset, y + h // 2), line_thickness)
        pygame.draw.line(surface, color, (x + w - inset, y + h - inset), (x + w // 2, y + h - inset), line_thickness)
        pygame.draw.line(surface, color, (x + w - inset, y + h - inset), (x + w - inset, y + h // 2), line_thickness)
    else:  # Ícone para modo tela cheia
        inner_inset = inset + 5
        pygame.draw.line(surface, color, (x + inner_inset, y + inner_inset), (x + w // 2, y + inner_inset), line_thickness)
        pygame.draw.line(surface, color, (x + inner_inset, y + inner_inset), (x + inner_inset, y + h // 2), line_thickness)
        pygame.draw.line(surface, color, (x + w - inner_inset, y + inner_inset), (x + w // 2, y + inner_inset), line_thickness)
        pygame.draw.line(surface, color, (x + w - inner_inset, y + inner_inset), (x + w - inner_inset, y + h // 2), line_thickness)
        pygame.draw.line(surface, color, (x + inner_inset, y + h - inner_inset), (x + w // 2, y + h - inner_inset), line_thickness)
        pygame.draw.line(surface, color, (x + inner_inset, y + h - inner_inset), (x + inner_inset, y + h // 2), line_thickness)
        pygame.draw.line(surface, color, (x + w - inner_inset, y + h - inner_inset), (x + w // 2, y + h - inner_inset), line_thickness)
        pygame.draw.line(surface, color, (x + w - inner_inset, y + h - inner_inset), (x + w - inner_inset, y + h // 2), line_thickness)

# ======================== CONFIGURAÇÕES DE TEXTO ========================
# Fonte para textos
font = pygame.font.Font(None, 30)

# ======================== ESTADOS DO MENU ========================
# Estados possíveis para o menu
MENU_PRINCIPAL = 0
MENU_JOGAR = 1
MENU_CONFIGURACOES = 2
MENU_SOLO = 3

current_menu = MENU_PRINCIPAL  # Menu atual
sub_buttons = []  # Botões do submenu

# ======================== PROPRIEDADES DOS BOTÕES ========================
# Proporções para os botões (ajustáveis)
button_radius_ratio = 0.02
button_height_ratio = 0.08
button_width_ratio = 0.25
button_spacing_ratio = 0.06
initial_y_offset_ratio = 0.6  # Posição inicial dos botões

def create_rounded_button(text, y_offset):
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

# ======================== CÁLCULO DOS BOTÕES ========================
def calculate_main_menu_buttons():
    """
    Calcula as propriedades dos botões do menu principal.
    """
    buttons = []
    y_offset = 0
    spacing = int(screen_height * button_spacing_ratio)
    button_height = int(screen_height * button_height_ratio)

    # Botões principais
    rect_jogar, text_jogar, rect_text_jogar, radius_jogar = create_rounded_button("Jogar", y_offset)
    buttons.append(("jogar", rect_jogar, text_jogar, rect_text_jogar, radius_jogar))
    y_offset += button_height + spacing

    rect_config, text_config, rect_text_config, radius_config = create_rounded_button("Configurações", y_offset)
    buttons.append(("configuracoes", rect_config, text_config, rect_text_config, radius_config))
    y_offset += button_height + spacing

    rect_atualizar, text_atualizar, rect_text_atualizar, radius_atualizar = create_rounded_button("Atualizações", y_offset)
    buttons.append(("atualizacoes", rect_atualizar, text_atualizar, rect_text_atualizar, radius_atualizar))

    return buttons

# Função para desenhar os botões
def draw_menu(buttons):
    """
    Desenha os botões na tela.
    """
    for _, rect, text_render, text_rect, radius in buttons:
        draw_rounded_rect(screen, rect, green, radius)
        screen.blit(text_render, text_rect)

# Botões do menu principal
main_menu_buttons = calculate_main_menu_buttons()

# ======================== LOOP PRINCIPAL ========================
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Atualização da tela
    screen.fill(light_blue)

    # Verifica qual menu está ativo e renderiza os botões
    if current_menu == MENU_PRINCIPAL:
        draw_menu(main_menu_buttons)

    pygame.display.flip()

pygame.quit()