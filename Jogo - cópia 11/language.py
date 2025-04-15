# Language management module
class LanguageManager:
    def __init__(self):
        self.languages = {
            "en": "English",
            "zh": "Mandarin Chinese",
            "hi": "Hindi",
            "es": "Spanish",
            "fr": "French",
            "ar": "Standard Arabic",
            "bn": "Bengali",
            "ru": "Russian",
            "ja": "Japanese",
            "de": "German",
            "pt": "Portuguese",
        }
        self.current_language = "en"  # Default language is English
        self.translations = self.load_translations()

    def load_translations(self):
        """
        Load translations for all supported languages.
        """
        return {
            "en": {
                "play": "Play",
                "settings": "Settings",
                "quit": "Quit",
                "volume": "Volume",
                "language": "Language",
                "back": "Back",
            },
            "pt": {
                "play": "Jogar",
                "settings": "Configurações",
                "quit": "Sair",
                "volume": "Volume",
                "language": "Idioma",
                "back": "Voltar",
            },
            # Add translations for other languages (Example for Mandarin Chinese)
            "zh": {
                "play": "玩",
                "settings": "设置",
                "quit": "退出",
                "volume": "音量",
                "language": "语言",
                "back": "返回",
            },
            # Other languages follow the same structure...
        }

    def set_language(self, lang_code):
        if lang_code in self.languages:
            self.current_language = lang_code

    def translate(self, key):
        """
        Translate a given key based on the current language.
        """
        return self.translations.get(self.current_language, {}).get(key, key)