from buttons import create_rounded_button
from language import LanguageManager

lang_manager = LanguageManager()

def calculate_main_menu_buttons(screen_width, screen_height, font):
    """
    Calcula as propriedades dos botões do menu principal.
    """
    buttons = []
    y_offset = 0
    spacing = int(screen_height * 0.06)  # Espaçamento entre botões
    button_height = int(screen_height * 0.08)

    # Botões principais
    rect_play, text_play, rect_text_play, radius_play = create_rounded_button(
        lang_manager.translate("play"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("jogar", rect_play, text_play, rect_text_play, radius_play))
    y_offset += button_height + spacing

    rect_settings, text_settings, rect_text_settings, radius_settings = create_rounded_button(
        lang_manager.translate("settings"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("configuracoes", rect_settings, text_settings, rect_text_settings, radius_settings))
    y_offset += button_height + spacing

    rect_language, text_language, rect_text_language, radius_language = create_rounded_button(
        lang_manager.translate("language"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("language", rect_language, text_language, rect_text_language, radius_language))
    y_offset += button_height + spacing

    rect_quit, text_quit, rect_text_quit, radius_quit = create_rounded_button(
        lang_manager.translate("quit"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("sair", rect_quit, text_quit, rect_text_quit, radius_quit))

    return buttons


def calculate_jogar_menu_buttons(screen_width, screen_height, font):
    """
    Calcula os botões do submenu "Jogar".
    """
    buttons = []
    y_offset = 0
    spacing = int(screen_height * 0.06)  # Espaçamento entre botões
    button_height = int(screen_height * 0.08)

    # Botões do submenu Jogar
    rect_solo, text_solo, rect_text_solo, radius_solo = create_rounded_button(
        lang_manager.translate("solo"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("solo", rect_solo, text_solo, rect_text_solo, radius_solo))
    y_offset += button_height + spacing

    rect_multiplayer, text_multiplayer, rect_text_multiplayer, radius_multiplayer = create_rounded_button(
        lang_manager.translate("multiplayer"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("multiplayer", rect_multiplayer, text_multiplayer, rect_text_multiplayer, radius_multiplayer))
    y_offset += button_height + spacing

    rect_back, text_back, rect_text_back, radius_back = create_rounded_button(
        lang_manager.translate("back"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("voltar", rect_back, text_back, rect_text_back, radius_back))

    return buttons


def calculate_config_menu_buttons(screen_width, screen_height, font):
    """
    Calcula os botões do submenu "Configurações".
    """
    buttons = []
    y_offset = 0
    spacing = int(screen_height * 0.06)  # Espaçamento entre botões
    button_height = int(screen_height * 0.08)

    # Botões do submenu Configurações
    rect_volume, text_volume, rect_text_volume, radius_volume = create_rounded_button(
        lang_manager.translate("volume"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("volume", rect_volume, text_volume, rect_text_volume, radius_volume))
    y_offset += button_height + spacing

    rect_language, text_language, rect_text_language, radius_language = create_rounded_button(
        lang_manager.translate("language"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("language", rect_language, text_language, rect_text_language, radius_language))
    y_offset += button_height + spacing

    rect_back, text_back, rect_text_back, radius_back = create_rounded_button(
        lang_manager.translate("back"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("voltar", rect_back, text_back, rect_text_back, radius_back))

    return buttons


def calculate_language_menu_buttons(screen_width, screen_height, font):
    """
    Calcula os botões do menu de seleção de idiomas.
    """
    buttons = []
    y_offset = 0
    spacing = int(screen_height * 0.04)

    for lang_code, lang_name in lang_manager.languages.items():
        rect, text, rect_text, radius = create_rounded_button(
            lang_name, y_offset, screen_width, screen_height, font
        )
        buttons.append((lang_code, rect, text, rect_text, radius))
        y_offset += spacing + 30

    rect_back, text_back, rect_text_back, radius_back = create_rounded_button(
        lang_manager.translate("back"), y_offset, screen_width, screen_height, font
    )
    buttons.append(("back", rect_back, text_back, rect_text_back, radius_back))

    return buttons